# coding=UTF-8
import requests
import json
import time
import re
import ast
import logging
import os
import math
import time
import ctypes 
import threading
import callApiUtils
from datetime import datetime
from datetime import datetime
from flask import Flask, Response, render_template, request, redirect, jsonify
from threading import Timer,Thread,Event
from flask_restful import Resource
import const
import log as logpy
import utils
from pymessenger import Bot

log = logpy.logging.getLogger(__name__)

def setup_route(api):
    api.add_resource(Default, '/')
    api.add_resource(HealthCheck, '/healthCheck')
    api.add_resource(Webhook, '/fb/webhook')

class Default(Resource):
    log.debug('check health')
    def get(self):
        return {
            'status': 0,
            'message': 'success'
        }, 200

class HealthCheck(Resource):
    log.debug('check health')
    def get(self):
        return {
            'status': 0,
            'message': 'success'
        }, 200

class Webhook(Resource):
    def get(self):
        log.info(request.args.get('hub.verify_token'))
        log.info(const.VERIFY_TOKEN)
        if request.args.get('hub.verify_token') == const.VERIFY_TOKEN:
            log.info(request.args.get('hub.challenge'))
            return int(request.args.get('hub.challenge'))
        log.info('Wrong Verify Token')
        return "Wrong Verify Token"
    def post(self):
        try:
            log.debug(const.ACCESS_TOKEN)
            access_token_disc = const.ACCESS_TOKEN
            data = json.loads(request.data)
            log.info(data)
            log.info(data['entry'][0]['id'])
            token = access_token_disc.get(data['entry'][0]['id'])
            log.debug(token)
            sender = data['entry'][0]['messaging'][0]['sender']['id'] # Sender ID
            payload = {}
            # {'object': 'page', 'entry': [{'id': '105566678411846', 'time': 1622748029330, 'messaging': [{'sender': {'id': '3638090612961775'}, 'recipient': {'id': '105566678410846'}, 'timestamp': 1622748028944, 'postback': {'title': 'Get Started', 'payload': 'GET_START'}}]}]}
            if data['entry'][0]['messaging'][0].get('postback'):
                log.info(data['entry'][0]['messaging'][0]['postback'])
                log.info(sender)
                if const.GET_START_WELCOME:
                    welcomeMessage(sender, token)
                for message in const.PAYLOAD:
                    payload = {'recipient': {'id': sender}, 'message': message}
                    r = requests.post('https://graph.facebook.com/v2.6/me/messages/?access_token=' + token, json=payload)
            elif data['entry'][0]['messaging'][0].get('message'):
                text = data['entry'][0]['messaging'][0]['message']['text'] 
                log.info(text)
                log.info(sender)
                if const.MESSAGE_WELCOME:
                    welcomeMessage(sender, token)
                for message in const.PAYLOAD:
                    payload = {'recipient': {'id': sender}, 'message': message}
                    r = requests.post('https://graph.facebook.com/v2.6/me/messages/?access_token=' + token, json=payload)
        except Exception as e:
            log.error("post webhook error: "+utils.except_raise(e))


def welcomeMessage(sender, token):
    username=''
    try:
        # 'https://graph.facebook.com/v2.6/2357988760980771?fields=name&access_token=EAAGJwZCK6hFUBANZCXTgn9pc6YnvBZBwKFGYHUjVEop2ZBT1CDBpg40G6WDyt8nIjiUe2nKZCr3fZBVAi29QoDL6SeZCDtOoGQXjb4hoTsf0sp1MZCZBOWjXVw420V7QSEUGFlF2ZCTFIvVD3aeapAkiSCmnz7HJGRHLuLMSwrIiTmS90RgCqSSi4V'
        reqUrl = "https://graph.facebook.com/v2.6/{USER_ID}?fields=name&access_token={PAGE_ACCESS_TOKEN}".format(USER_ID=sender, PAGE_ACCESS_TOKEN=token)
        log.info(reqUrl)
        headers = { "Content-Type": "application/json" }
        r = callApiUtils.CallApi().get_request( reqUrl, headers)
        jsonResponse = json.loads(r.text)
        username = jsonResponse.get("name")
        log.info(username)
    except Exception as e:
        log.error("post webhook error: "+utils.except_raise(e))
    log.info(const.WELCOME_MESSAGE)
    payload = {'recipient': {'id': sender}, 'message': {'text': username + const.WELCOME_MESSAGE.get("data")}}
    r = requests.post('https://graph.facebook.com/v2.6/me/messages/?access_token=' + token, json=payload)
