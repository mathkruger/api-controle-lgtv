#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bottle import route, run, response
from pylgtv import WebOsClient
import json
from configs import tv_ip

@route('/volume')
def get_volume():
    response.content_type = 'application/json'
    
    try:
        webos_client = WebOsClient(tv_ip)

        vol = webos_client.get_volume()
        return json.dumps(vol)
    except:
        return json.dumps("Ocorreu um erro ao se conectar com sua TV")

@route('/volume/<vol>')
def set_volume(vol):
    response.content_type = 'application/json'
    
    try:
        webos_client = WebOsClient(tv_ip)

        webos_client.set_volume(int(vol))
        return json.dumps("Volume setado para " + vol)
    except:
        return json.dumps("Ocorreu um erro ao se conectar com sua TV")

@route('/input/<id>')
def set_entrada(id):
    response.content_type = 'application/json'
    
    try:
        webos_client = WebOsClient(tv_ip)

        webos_client.set_input(id)
        return json.dumps("Entrada mudada para: " + id)
    except:
        return json.dumps("Ocorreu um erro ao se conectar com sua TV")

@route('/input')
def get_entradas():
    response.content_type = 'application/json'
    
    try:
        webos_client = WebOsClient(tv_ip)
        entradas = webos_client.get_inputs()

        return json.dumps(entradas)
    except:
        return json.dumps("Ocorreu um erro ao se conectar com sua TV")

@route('/apps')
def get_apps():
    response.content_type = 'application/json'

    try:
        webos_client = WebOsClient(tv_ip)
        apps = webos_client.get_apps()
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
