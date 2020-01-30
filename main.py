#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bottle import route, run, response
from pylgtv import WebOsClient
import json
from configs import tv_ip

@route('/volume/<vol>')
def volume(vol):
    response.content_type = 'application/json'
    
    try:
        webos_client = WebOsClient(tv_ip)

        webos_client.set_volume(int(vol))
        return json.dumps("Volume aumentado para: " + vol)
    except:
        return json.dumps("Ocorreu um erro ao se conectar com sua TV")


@route('/apps')
def get_apps():
    response.content_type = 'application/json'

    try:
        # webos_client = WebOsClient(tv_ip)

        apps = []
        apps.append('netflix')
        apps.append('prime')

        # for app in webos_client.get_apps():
        #     apps.append(app)

        return json.dumps(apps)
    except:
        return json.dumps("Ocorreu um erro ao se conectar com sua TV")


@route('/apps/<app>')
def set_app(app):
    response.content_type = 'application/json'

    try:
        webos_client = WebOsClient(tv_ip)

        webos_client.launch_app(app)
        return json.dumps("Aplicativo " + app + " iniciado")
    except:
        return json.dumps("Ocorreu um erro ao se conectar com sua TV")


run(host='localhost', port=8080)
