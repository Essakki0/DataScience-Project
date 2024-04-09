# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 18:16:55 2024

@author: 30083304
"""

import logging
import os
from datetime import datetime

#format for log file name
LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

#getting current path and adding log file name
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)

#create log file
os.makedirs(logs_path,exist_ok=True)

LOGS_FILE_PATH=os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOGS_FILE_PATH,
    format="[%(asctime)s]%(lineno)d %(name)s-%(levelname)s-%(message)s",
    level=logging.INFO,
    )

if __name__ == '__main__':
    logging.info("logging has started")