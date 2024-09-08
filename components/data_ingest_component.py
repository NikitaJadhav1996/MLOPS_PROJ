import kfp

from kfp.v2.dsl import(
    Input,
    Output,
    Dataset,
    Artifact,
    Metrics,
    component
)

import warnings
warnings.filterwarnings('ignore')

from data.data_ingest import Data_Ingestion 

@component(
    output_component_file='data_ingestion.yaml',
    base_image='python:3.9-slim',
    packages_to_install=['pandas','google-cloud-storage','requests','boto3']
)
def ingest_data_component(data_path:str, output_artifact:Output[Artifact]):#url:str,db_conn_string:str,csv_file_name:str, 
    DI=Data_Ingestion(data_path)
    data=DI.sleep_data_ingest()
    output_artifact.metadata['csv_data']=data_path
    if data is not None:
        output_artifact.metadata['ingested_rows']=len(data)
    else:
        output_artifact.metadata['ingested_rows']=0
        
    # 
    # DI=Data_Ingestion(url,db_conn_string)
    # data=DI.data_combine()
    # data.to_csv(csv_file_name)
    # output_artifact.metadata['csv_file_name']=csv_file_name
    
