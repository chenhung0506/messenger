# -*- coding: utf-8 -*-
import os
import json
from dotenv import load_dotenv

APP_ROOT = os.path.join(os.path.dirname(__file__), '.')  
dotenv_path = os.path.join(APP_ROOT, '../docker/dev.env')
load_dotenv(dotenv_path)
print( os.getenv('IS_LOADED') + ", .env file path: " + dotenv_path )
PORT=os.environ.get('PORT', os.getenv('PORT'))
LOG_LEVEL=os.environ.get('LOG_LEVEL', os.getenv('LOG_LEVEL'))
LOG_FOLDER_PATH=os.environ.get('LOG_FOLDER_PATH', os.getenv('LOG_FOLDER_PATH'))

WELCOME_MESSAGE=json.loads(os.environ.get('WELCOME_MESSAGE', os.getenv('WELCOME_MESSAGE')).replace("'", ""))
GET_START_WELCOME=json.loads(os.environ.get('GET_START_WELCOME', os.getenv('GET_START_WELCOME')).replace("'", ""))
MESSAGE_WELCOME=json.loads(os.environ.get('MESSAGE_WELCOME', os.getenv('MESSAGE_WELCOME')).replace("'", ""))
ACCESS_TOKEN=json.loads(os.environ.get('ACCESS_TOKEN', os.getenv('ACCESS_TOKEN')).replace("'", ""))
VERIFY_TOKEN=os.environ.get('VERIFY_TOKEN', os.getenv('VERIFY_TOKEN')).replace("'", "")
PAYLOAD=json.loads(os.environ.get('PAYLOAD', os.getenv('PAYLOAD')).replace("'", ""))
