import os
from dataclasses import dataclass
import numpy as np
from src.logger import logging
from src.exception import custom_exception
from sklearn.preprocessing import StandardScaler,OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from src.utils import save_obj
import sys
import pandas as pd

@dataclass
class data_transformation:
    preprocessor_file_path=os.path.join("artifacts", "preprocessor.pkl")

class DataTransformationconfig:
    def __init__(self):
        self.datatransformation=data_transformation()

    def get_preprocessor_pickle_file(self):
        try:
            num_col=['reading_score', 'writing_score']
            cat_col=['gender','race_ethnicity','parental_level_of_education','lunch','test_preparation_course']


            num_pipeline=Pipeline([
                ("Imputer",SimpleImputer(strategy="median")),
                ("scaling",StandardScaler())
            ])
            cat_pipeline=Pipeline([
                ("imputer",SimpleImputer(strategy="most_frequent")),
                ("encoder",OneHotEncoder()),
                ("scaling",StandardScaler(with_mean=False))
            ])

            preprocessor=ColumnTransformer([
                ("num_col",num_pipeline,num_col),
                ("cat_col",cat_pipeline,cat_col)
            ])

            return preprocessor
        
        except Exception as e:
            raise custom_exception(e,sys)


    def initiate_data_transformation(self,train_path,test_path):
        try:
            logging.info("Data transformation started")
            preprocessor_obj=self.get_preprocessor_pickle_file()
            train_data=pd.read_csv(train_path)
            test_data=pd.read_csv(test_path)

            target_col="math_score"
            

            train_data_input_col=train_data.drop(columns=[target_col],axis=1)
            train_data_ouput_col=train_data[target_col]

            test_data_input_col=test_data.drop(columns=[target_col],axis=1)
            test_data_output_col=test_data[target_col]

            

            train_fir_array=preprocessor_obj.fit_transform(train_data_input_col)
            test_fir_array=preprocessor_obj.transform(test_data_input_col)

            train_arr=np.c_[train_fir_array,np.array(train_data_ouput_col)]
            test_arr=np.c_[test_fir_array,np.array(test_data_output_col)]

            save_obj(

                file_path=self.datatransformation.preprocessor_file_path,
                obj=preprocessor_obj

            )

            return train_arr,test_arr, self.datatransformation.preprocessor_file_path
            

        except Exception as e:
            raise custom_exception(e,sys)



