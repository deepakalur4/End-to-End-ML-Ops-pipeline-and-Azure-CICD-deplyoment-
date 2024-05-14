import pandas as pd
from dataclasses import dataclass
import os
from sklearn.model_selection import train_test_split
from src.logger import logging
from src.exception import custom_exception
import sys
from src.components.data_transforamation import * 
from src.components.model_trainer import *

@dataclass
class dataingestion:
    raw_data_path=os.path.join("artifacts","rawdata.csv")
    train_data_path=os.path.join("artifacts","train.csv")
    test_data_path=os.path.join("artifacts","test.csv")

class data_ingestion_config:
    def __init__(self) -> None:
        self.data_ingestion=dataingestion()
    
    def initiate_data_ingestion(self):
        try:
            df=pd.read_csv(r"src\notebooks\data\stud.csv")
            train_data,test_data=train_test_split(df,test_size=0.2,random_state=42)

            os.makedirs(os.path.dirname(self.data_ingestion.raw_data_path),exist_ok=True)
            df.to_csv(self.data_ingestion.raw_data_path,header=True,index=False)

            os.makedirs(os.path.dirname(self.data_ingestion.train_data_path),exist_ok=True)
            train_data.to_csv(self.data_ingestion.train_data_path,header=True,index=False)        

            os.makedirs(os.path.dirname(self.data_ingestion.test_data_path),exist_ok=True)
            test_data.to_csv(self.data_ingestion.test_data_path,header=True,index=False)

            return (self.data_ingestion.train_data_path,self.data_ingestion.test_data_path)
        
        except Exception as e:
            raise custom_exception(e,sys)

if __name__=="__main__":
    data_ingestion_obj=data_ingestion_config()
    train_path_1,test_path_1=data_ingestion_obj.initiate_data_ingestion()
    data_transformation_obj=DataTransformationconfig()
    train_arr,test_arr,_=data_transformation_obj.initiate_data_transformation(train_path_1,test_path_1)
    model_train_obj=model_trainer()
    model_train_obj.initiate_model_training(train_arr,test_arr)

