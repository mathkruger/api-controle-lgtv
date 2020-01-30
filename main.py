from bottle import route, run
from pylgtv import WebOsClient
import json
from configs import tv_ip

webos_client = None

@route('/init')
def index():
    try:
        webos_client = WebOsClient(tv_ip)
        return json.dumps("Sua TV foi conectada")
    except:
        return json.dumps("Ocorreu um erro a se conectar com sua TV")


@route('/volume/<vol>')
def volume(vol):
    # webos_client.set_volume(int(vol))
    return json.dumps("Volume aumentado para: " + vol)


@route('/apps')
def get_apps():
    apps = []
    # for app in webos_client.get_apps():
    #     apps.append(app)
    return json.dumps(apps)


@route('/apps/<app>')
def get_apps(app):
    # webos_client.launch_app(app)
    return json.dumps("Aplicativo " + app + " iniciado")


run(host='localhost', port=8080)
