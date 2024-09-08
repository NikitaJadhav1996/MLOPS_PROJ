# ingest data from API, SQL DB, S3, GCS

import pandas as pd
# from sqlalchemy import create_engine
# import boto3
# from google.cloud import storage
# import requests
import logging
import os



class Data_Ingestion:

     def __init__(self,data_path):
         logging.basicConfig(level=logging.INFO)
         self.data_path=data_path
    #     self.url=url
    #     self.db_conn_string=db_conn_string

    

     def sleep_data_ingest(self):
         try:
            logging.info('Data ingestion started')
            data=pd.read_csv(self.data_path,sep='',encoding='utf-8')   
            return data
         except Exception as e:
            logging.error(f'Error occured {e}')
            return None


    # def __init__(self,url,db_conn_string):
    #     self.url=url
    #     self.db_conn_string=db_conn_string
    
    # def ingest_api(self):
    #     try:
    #         logging.info("Initiated ingestion from API Endpoints")
    #         response=requests.get(self.url)
    #         response.raise_for_status()
    #         data=response.json()
    #         df=pd.DataFrame(data)
    #         logging.info("Converted data from API Endpoints to df")
    #         return df
    #     except Exception as e:
    #         logging.error(f'Error occured ingest_api {e}')

    # def ingest_db(self):
    #     try:
    #         logging.info("Data ingestion from DB initiated")
    #         engine=create_engine(self.db_conn_string)
    #         query="SELECT * FROM my_table"
    #         data=pd.read_sql(query,engine)
    #         df=pd.DataFrame(data)
    #         logging.info('Returned data from DB in DataFrame')
    #         return df
    #     except Exception as e:
    #         logging.error(f'Error occured ingest_db {e}')

###
# /**                   
#     def ingest_s3(bucket,key):
#         try:
#             logging.info("Initiated data from AWS s3")

#             client=boto3.client('s3')
#             response=client.get_object(Bucket=bucket,Key=key)
#             data=response['Body'].read().decode('utf-8')
#             df=pd.DataFrame(data)

#             logging.info("Data ingestion from S3 is done")
#             return df
#         except Exception as e:
#             logging.error(f'Error occured {e}')

#     def ingest_gcs(bucket,file_name):
#         try:
#             logging.info("Ingestion data_gcs initiated")

#             client=storage.Client() 
#             bucket=client.get_bucket(bucket)
#             blob=bucket.blob(file_name)
#             data=blob.download_as_text()
#             df=pd.DataFrame(data)

#             logging.info("Data ingestion from GCS is done")
#             return df
#         except Exception as e:
#             logging.error(f'Error occured {e}')
# ###
# **/
            
    # def data_ingest(self,data_list):
    #     try:
    #         logging.info("Initiated Data Combining")

    #         dataframe=pd.concat(data_list,ignore_index=True)

    #         logging.info(f'Final DataFrame length {len(dataframe)}')
    #         return dataframe
    #     except Exception as e:
    #         logging.errror(f'Error occured {e}')

    # def data_combine(self):
    #     api_data=self.ingest_api()
    #     db_data=self.ingest_db()
    #     combined_data=self.data_ingest([api_data,db_data])
    #     return combined_data
        
    
    # def upload_gcs(self,data,dest_folder,filename):
    #     try:
    #         logging.info("Uploading the combined data to gcs")
    #         client=storage.client()
    #         bucket=client.get_bucket(bucket)
    #         blob=bucket.blob(os.path.join(dest_folder,filename))
    #         blob.upload_from_string(data)
    #         logging.info('Upload finish')
    #         return dest_folder
    #     except Exception as e:
    #         logging.error(f'Error {e}')
            

    
            

