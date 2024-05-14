import os
from dataclasses import dataclass
from src.utils import evlaute_model
import sys
from src.exception import custom_exception
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestRegressor,AdaBoostRegressor,GradientBoostingRegressor
from sklearn.svm import SVR
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import Ridge,Lasso
from sklearn.linear_model import ElasticNet
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import r2_score
from src.utils import save_obj

@dataclass
class model_trainer_config:
    model_pcikle_file_path=os.path.join("artifacts","model.pkl")

class model_trainer:
    def __init__(self):
        self.model_trainer=model_trainer_config()

    def initiate_model_training(self,train_ar,test_ar):
        try:
            X_train,Y_train,X_test,Y_test=(train_ar[:,:-1],train_ar[:,-1],test_ar[:,:-1],test_ar[:,-1])
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

            best_modl=evlaute_model(x_train=X_train,y_train=Y_train,x_test=X_test,y_test=Y_test)
            best_model=(max(best_modl.values()))
            model=([i[0] for i in best_modl.items() if i[1]==best_model])
            best_model=models[model[0]]
            mod=best_model.fit(X_train,Y_train)
            predicts=best_model.predict(X_test)

            save_obj(obj=best_model,file_path=self.model_trainer.model_pcikle_file_path)



            return (r2_score(Y_test,predicts))

       
        except Exception as e:
            raise custom_exception(e,sys)




