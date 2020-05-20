# -*- coding: utf-8 -*-

import requests, json
from requests.auth import HTTPBasicAuth

import eventlet
from eventlet.green import urllib2

# baseUrl = "http://172.20.10.171:3333/ins"
#
# payload = \
#     {
#         "ins_api":
#         {
#             "version": "0.1",
# 		    "type": "cli_conf",
# 		    "chunk": "0",
# 		    "sid": "session1",
# 		    "input": "interface Ethernet1/10 ; shutdown",
# 		    "output_format": "json"
#         }
#     }
#
# data = json.dumps(payload)
#
# r = requests.post(baseUrl, auth = HTTPBasicAuth('admin', 'inspur@123'), json = payload)
#
# print r.status_code
# print r.content
# result =  json.loads(r.content)
# print result["ins_api"]["outputs"]["output"][0]["code"]


def sw_config(ip, port, usr, pwd, cmds):
    """
    payload = \
    {
        "ins_api":
            {
                "version": "0.1",
                "type": "cli_conf",
                "chunk": "0",
                "sid": "session1",
                "input": "interface Ethernet1/12 ; shutdown",
                "output_format": "json"
            }
    }
    """
    url = 'http://%s:%d/ins' %(ip, port)

    payload = body_cmds(" ; ".join(cmds))
    print payload
    code = 404

    try:
        r = requests.post(url, auth=HTTPBasicAuth(usr, pwd), json=payload)
        code = r.status_code
    except Exception:
        print Exception

    print code

    return code

def body(version, cli_type, chunk, sid, cmds, format):
    ins_api = dict(
        zip(('version', 'type', 'chunk', 'sid', 'input', 'output_format'), (version, cli_type, chunk, sid, cmds, format)))
    return {'ins_api' : ins_api}

def body_cmds(cmds):
    return body('0.1', "cli_conf", '0', "session1", cmds, "json")

# print sw_config('172.20.10.171', 3333, "admin", "inspur@123", ("interface Ethernet1/12", "shutdown"))

# pool = eventlet.GreenPool()
# for body in pool.imap(sw_config, '172.20.10.171', 3333, "admin", "inspur@123", ("interface Ethernet1/12", "shutdown")):
#     print("got body", len(body))

x = eventlet.spawn(sw_config, '172.20.10.191', 3333, "admin", "inspur@123", ("interface Ethernet1/13", "shutdown"))

x.wait()

def test(x):
    while True:
        print('Greenthread test Num:%d' %x)
        x += 1
        eventlet.greenthread.sleep(1)
    return x

def test1(y):
    print('Greenthread test1 Num:%d' %y)
    eventlet.greenthread.sleep(10)
    return y

x = eventlet.spawn(test, 1)
y = eventlet.spawn(test1, 2)
x.wait()
