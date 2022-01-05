import os
from azure.storage.blob import BlobServiceClient,BlobClient

try:
    connect_str = "DefaultEndpointsProtocol=https;AccountName=mcontainer;AccountKey=KKv4w/8ZCAU36CSm9m9K0+wkAs17N57nV7K+RxZx8EB/k78kibfgBgvqRUN2NYMCRkneLkB4+TnB/sjN4TrEKg==;EndpointSuffix=core.windows.net"
    #os.getenv('AZURE_STORAGE_CONNECTION_STRING')
    #print(connect_str)
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)
    container_name = "unload"
    container_client = blob_service_client.get_container_client(container_name)
    blob_list = container_client.list_blobs()
    blob_cnt=[]
    for blob in blob_list:
        blob_cnt.append(blob)
    if(len(blob_cnt)>0):
        stream_downloader=container_client.download_blob("load.csv")
        file_reader=stream_downloader.readall()
        print(file_reader)
        container_client.delete_blob(blob="load.csv")
        print("deleted Successfully")
    else:
        print("Container has no files")


except Exception as ex:
    print('Exception:')
    print(ex)

