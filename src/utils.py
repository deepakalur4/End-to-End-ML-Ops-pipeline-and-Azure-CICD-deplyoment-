import os
import pickle
import sys
from src.logger import logging
from src.exception import custom_exception
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestRegressor,AdaBoostRegressor,GradientBoostingRegressor
from sklearn.svm import SVR
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import Ridge,Lasso
from sklearn.linear_model import ElasticNet
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import r2_score

def save_obj(file_path,obj):
    try:
        dir_path = os.path.dirname(file_path)        
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path,"wb") as file_obj:
            pickle.dump(obj,file_obj)
    except Exception as e:
        raise custom_exception(e,sys)


def evlaute_model(x_train,x_test,y_train,y_test):
                models={"logistic_reg":LogisticRegression(),
                    "decision_tree":DecisionTreeRegressor(),
                    "svr":SVR(),
                    "laso":Lasso(),
                    "ridge":Ridge(),
                    "elastic_net":ElasticNet(),
                    "neibour":KNeighborsRegressor(),
                    "rabdim_forst":RandomForestRegressor(),
                    "ada":AdaBoostRegressor(),
                    "gradinet":GradientBoostingRegressor()
                    }
                score_dic=dict()
                for model_name,model in models.items():
                      mod=model.fit(x_train,y_train)
                      y_pred=mod.predict(x_test)
                      socre=r2_score(y_test,y_pred)
                      score_dic[model_name]=socre
                return score_dic



      

def load_model(model_path):
      with open(model_path,"rb") as model_obj:
            return pickle.load(model_obj)