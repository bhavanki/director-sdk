
# DiagnosticDataSummary

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clouderaManagerLogsDownloaded** | **Boolean** | Whether Cloudera Manager logs were also downloaded from Cloudera Manager |  [optional]
**collectionTime** | **Long** | Time of collection | 
**details** | **List&lt;String&gt;** | Details on the collection effort |  [optional]
**diagnosticDataCollected** | **Boolean** | Whether diagnostic data was collected successfully by Cloudera Manager |  [optional]
**diagnosticDataDownloaded** | **Boolean** | Whether diagnostic data was downloaded successfully from Cloudera Manager |  [optional]
**localFilePath** | **String** | Local path to the diagnostic data file |  [optional]
**status** | [**StatusEnum**](#StatusEnum) | Status of the collection effort | 


<a name="StatusEnum"></a>
## Enum: StatusEnum
Name | Value
---- | -----
COLLECTING | &quot;COLLECTING&quot;
READY | &quot;READY&quot;
FAILED | &quot;FAILED&quot;



