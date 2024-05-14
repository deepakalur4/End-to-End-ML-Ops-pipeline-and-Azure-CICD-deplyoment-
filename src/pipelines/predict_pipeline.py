import os
from dataclasses import dataclass
from src.utils import load_model
import pandas as pd
from src.exception import custom_exception
import sys

class pipeline_1:
    def __init__(self):
        pass

    def predict_pipeling(self,features):
        model_path=os.path.join("artifacts","model.pkl")
        preprocessor_path=os.path.join("artifacts","preprocessor.pkl")
        loaded_model=load_model(model_path)
        loaded_preprocessor=load_model(preprocessor_path)
        scaled_Data=loaded_preprocessor.transform(features)
        preds=loaded_model.predict(scaled_Data)
        return preds

class custom_data:
    def __init__(self,gender,race_ethnicity,parental_level_of_education,lunch,test_preparation_course,reading_score,writing_score):
        self.gender=gender
        self.race_ethnicity=race_ethnicity
        self.parental_level_of_education=parental_level_of_education
        self.lunch=lunch
        self.test_preparation_course=test_preparation_course
        self.reading_score=reading_score
        self.writing_score=writing_score

    def get_data_As_dataframe(self):
        try:
            dataframe_data={"gender":[self.gender],
                            "race_ethnicity":[self.race_ethnicity],
                            "parental_level_of_education":[self.parental_level_of_education],
                            "lunch":[self.lunch],
                            "test_preparation_course":[self.test_preparation_course],
                            "reading_score":[self.reading_score],
                            "writing_score":[self.writing_score]
                            }
            return pd.DataFrame(dataframe_data)
            

        except Exception as e:
            raise custom_exception(e,sys)
            

    
