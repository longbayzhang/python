# -*- coding: utf-8 -*-

import requests, json
from requests.auth import HTTPBasicAuth

switchIp = "172.20.10.191"

baseUrl = "http://172.20.10.125:8181/"

loginUrl = "auth/login/login"

params = {"username": "admin",
          "password": "admin"}
r = requests.get(baseUrl + loginUrl, params = params)

print r.status_code

switchsUrl = "api/underlay/v1/switch/switches"

r = requests.get(baseUrl + switchsUrl, auth = HTTPBasicAuth('admin', 'admin'))

print r.status_code

payload = {"mirrorId": "1",
           "mirrorDesc": "",
           "mirrorSrc": "interface ethernet 1/5",
           "mirrorDst": "interface ethernet 1/6",
           "mirrorDir": "rx"}

mirrorUrl = "api/underlay/v1/mirrors/" + switchIp

data = json.dumps(payload)

r = requests.post(baseUrl + mirrorUrl, auth = HTTPBasicAuth('admin', 'admin'), json = payload)

print r.status_code

r = requests.get(baseUrl + mirrorUrl, auth = ('admin', 'admin'))

print r.status_code
