import logging
import os
from datetime import datetime

log_file_path=f"{datetime.now().strftime("%d_%m_%y_%H_%M_%S")}.log"
log_dir=os.path.join(os.getcwd(),"logs",log_file_path)

os.makedirs(log_dir,exist_ok=True)

log_file_path=os.path.join(log_dir,log_file_path)


logging.basicConfig(filename=log_file_path,level=logging.INFO)