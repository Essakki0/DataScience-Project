# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 18:16:50 2024

@author: 30083304
"""

import sys

def error_message_detail(error,error_detail:sys):
    #.exc_info returns 3 values.
    _,_,exc_tb=error_detail.exc_info()
    
    #Error message formatting
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="Error occured in python script name  [{0}] line number [{1}] \
        error message [{2}]".format(file_name,exc_tb.tb_lineno,str(error))

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error, error_detail)
    
    def __str(self):
        return self.error_message