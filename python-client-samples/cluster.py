#! /usr/bin/env python

# Copyright (c) 2015 Cloudera, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Simple script that shows how to use the Cloudera Altus Director API to start a
cluster on AWS.
"""

import ConfigParser
import argparse
from os.path import isfile
import sys
import time
import uuid
from cloudera.director.common.client import ApiClient, Configuration
from cloudera.director.common.rest import ApiException
from cloudera.director.latest import (EnvironmentsApi, DeploymentsApi, ClustersApi)
from cloudera.director.latest.models import (SshCredentials, InstanceProviderConfig, Environment,
                                             InstanceTemplate, VirtualInstance, DeploymentTemplate,
                                             ClusterTemplate, VirtualInstanceGroup)

def get_authenticated_client(args):
    """
    Create a new API client and authenticate against a server as admin

    @param args: dict of parsed command line arguments that
                 include server host and admin credentials
    @rtype:      ApiClient
    @return:     authenticated API client
    """

    configuration = Configuration()
    configuration.host = args.server
    configuration.username = args.admin_username
    configuration.password = args.admin_password

    if args.server.startswith('https'):
        configuration.verify_ssl = True
        if args.cafile:
            configuration.ssl_ca_cert = args.cafile

    client = ApiClient(configuration=configuration)
    return client


def create_environment(client, config):
    """
    Create a new environment with data from the configuration file

    @param client: authenticated API client
    @param config: parsed configuration file
    """

    # Start by defining your credentials for this environment

    credentials = SshCredentials(username=config.get("ssh", "username"),
                                 port=22,
                                 private_key=file(config.get("ssh", "privateKey")).read())

    # Retrieve your AWS credentials

    provider_config = {
        'accessKeyId': config.get("provider", "accessKeyId"),
        'secretAccessKey': config.get("provider", "secretAccessKey"),
        'region': config.get("provider", "region")
    }
    provider = InstanceProviderConfig(type=config.get("provider", "type"),
                                      config=provider_config)

    # Create a new environment object using the credentials and provider

    env = Environment(name="%s Environment" % config.get("cluster", "name"),
                      credentials=credentials,
                      provider=provider)

    # Post this information to Cloudera Altus Director (to be validated and stored)

    api = EnvironmentsApi(client)
    try:
        api.create(env)

    except ApiException as exc:
        if exc.status == 409:
            print 'Warning: an environment with the same name already exists'
        else:
            raise exc

    print "Environments: %s" % api.list()
    return env.name


def create_deployment(client, environment_name, config):
    """
    Create a new deployment (Cloudera Manager) with data from the configuration file

    @param client: authenticated API client
    @param environment_name: the name of the parent environment
    @param config: parsed configuration file
    """
    template = DeploymentTemplate(
        name="%s Deployment" % config.get('cluster', 'name'),
        manager_virtual_instance=create_virtual_instance(config, 'manager'),
        port=7180,
        enable_enterprise_trial=True,
        configs={
            'CLOUDERA_MANAGER': {
                'enable_api_debug': 'true'
            }
        }
    )

    api = DeploymentsApi(client)
    try:
        api.create(environment_name, template)

    except ApiException as exc:
        if exc.status == 409:
            print 'Warning: a deployment with the same name already exists'
        else:
            raise exc

    print "Deployments: %s" % api.list(environment_name)
    return template.name


def create_cluster(client, environment_name, deployment_name, config):
    """
    Create a new CDH cluster with data from the configuration file

    @param client: authenticated API client
    @param environment_name: the name of the parent environment
    @param deployment_name: the name of the parent deployment
    @param config: parsed configuration file
    """
    num_workers = config.getint("cluster", "num_workers")
    template = ClusterTemplate(
        name=config.get('cluster', 'name'),
        product_versions={
            'CDH': config.get('cluster', 'cdh_version')
        },
        services=['HDFS', 'YARN'],
        services_configs={
        },
        virtual_instance_groups={
            'masters': VirtualInstanceGroup(
                name='masters',
                min_count=1,
                service_type_to_role_types={
                    'HDFS': ['NAMENODE', 'SECONDARYNAMENODE'],
                    'YARN': ['RESOURCEMANAGER', 'JOBHISTORY']
                },
                role_types_configs={
                },
                virtual_instances=[create_virtual_instance(config, 'master')]
            ),
            'workers': VirtualInstanceGroup(
                name='workers',
                min_count=num_workers,
                service_type_to_role_types={
                    'HDFS': ['DATANODE'],
                    'YARN': ['NODEMANAGER']
                },
                # optional role configurations, if desired or needed
                role_types_configs={
                    #'HDFS': {
                    #    'DATANODE': {
                    #        'dfs_datanode_handler_count': '10'
                    #    },
                    #    'NODEMANAGER': {
                    #        'nodemanager_webserver_port': '8047'
                    #    }
                    #}
                },
                virtual_instances=[create_virtual_instance(config, 'worker')
                                   for _ in range(0, num_workers)]
            )
        }
    )

    api = ClustersApi(client)
    try:
        api.create(environment_name, deployment_name, template)

    except ApiException as exc:
        if exc.status == 409:
            print 'Warning: a cluster with the same name already exists'
        else:
            raise exc

    print "Clusters: %s" % api.list(environment_name, deployment_name)
    return template.name


def create_instance_template(config, name):
    """
    Create an instance template with data from the configuration file

    @param config: parsed configuration file
    @param name: the name of the new template
    @rtype: InstanceTemplate
    """
    template_config = {
        'subnetId': config.get('instance', 'subnetId'),
        'securityGroupsIds': config.get('instance', 'securityGroupId'),
        'instanceNamePrefix': config.get('instance', 'namePrefix')
    }
    template = InstanceTemplate(name=name,
                                image=config.get('instance', 'image'),
                                type=config.get('instance', 'type'),
                                config=template_config)

    return template


def create_virtual_instance(config, instance_template_name):
    """
    Create a new virtual instance object with a random ID

    @param config: parsed configuration file
    @param instance_template_name: the name of the instance template
    @rtype: VirtualInstance
    """
    return VirtualInstance(
        id=str(uuid.uuid4()),
        template=create_instance_template(config, instance_template_name)
    )


def wait_for_deployment(client, environment_name, deployment_name):
    """
    Wait for the deployment bootstrap process to complete

    @param client: authenticated API client
    """
    api = DeploymentsApi(client)
    stage = None
    while stage not in ['READY', 'BOOTSTRAP_FAILED']:
        sys.stdout.write(".")
        sys.stdout.flush()

        time.sleep(0.5)
        stage = api.get_status(environment_name, deployment_name).stage

    print "\nDeployment '%s' current stage is '%s'" % (deployment_name, stage)


def wait_for_cluster(client, environment_name, deployment_name, cluster_name):
    """
    Wait for the cluster bootstrap process to complete

    @param client: authenticated API client
    """
    api = ClustersApi(client)
    stage = None
    while stage not in ['READY', 'BOOTSTRAP_FAILED']:
        sys.stdout.write(".")
        sys.stdout.flush()

        time.sleep(0.5)
        stage = api.get_status(environment_name, deployment_name, cluster_name).stage

    print "\nCluster '%s' current stage is '%s'" % (cluster_name, stage)


def main():
    """
    Main function

    @return: 0 when successful
    """
    parser = argparse.ArgumentParser(prog='cluster.py')

    parser.add_argument('--admin-username', default="admin",
                        help='Name of an user with administrative access (defaults to %(default)s)')
    parser.add_argument('--admin-password', default="admin",
                        help='Password for the administrative user (defaults to %(default)s)')
    parser.add_argument('--server', default="http://localhost:7189",
                        help="Cloudera Altus Director server URL (defaults to %(default)s)")
    parser.add_argument('--cafile', default=None,
                        help='Path to file containing trusted certificate(s) ' +
                        '(defaults to %(default)s)')

    parser.add_argument('ini_file', help="Cluster configuration file (.ini)")

    args = parser.parse_args()

    if not isfile(args.ini_file):
        print 'Error: "%s" not found or not a file' % args.ini_file
        return -1

    config = ConfigParser.SafeConfigParser()
    config.read(args.ini_file)

    client = get_authenticated_client(args)

    print 'Creating a new environment ...'
    environment_name = create_environment(client, config)

    print 'Creating a new Cloudera Manager instance ...'
    deployment_name = create_deployment(client, environment_name, config)

    print 'Creating a new CDH cluster ...'
    cluster_name = create_cluster(client, environment_name, deployment_name, config)

    print 'Waiting for deployment to be ready. Check the web interface for details.'
    wait_for_deployment(client, environment_name, deployment_name)

    print 'Waiting for the cluster to be ready. Check the web interface for details.'
    wait_for_cluster(client, environment_name, deployment_name, cluster_name)

    return 0


if __name__ == '__main__':
    try:
        sys.exit(main())

    except ApiException as exc:
        print str(exc)
        raise exc
