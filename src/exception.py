from src.logger import logging
import os
import sys


def error_messge_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message= f"Error occurred in file name {file_name} and the line no is {exc_tb.tb_lineno} and the error is {error}"
    return error_message

class custom_exception(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_messge_detail(error=error_message,error_detail=error_detail)

    def __str__(self) -> str:
        return (self.error_message) 


if __name__=="__main__":
    try:
        a=1/0
        logging.info("logging sytaryted")
    except Exception as e:
        raise custom_exception(e,sys)