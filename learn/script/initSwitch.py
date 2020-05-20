#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys,urllib2,json,uuid,time

leaf = [
    'no vlan 11-99', 'no vlan 111-1000', 'no vlan 1001-2000', 'no vlan 2001-3000',
    'no vlan 3001-3863', 'no int vlan 11-99', 'no int vlan 111-1000', 'no int vlan  1001-2000',
    'no int vlan  2001-3000', 'no int vlan  3001-3863',
    'no interface loopback 91', 'no interface loopback 95', 'no feature bgp',
    'no feature vpc', 'no int nve 1'
]

border = [
    'no vlan 2-1000', 'no vlan 1001-2000', 'no vlan 2001-3000',
    'no vlan 3001-3863', 'no int vlan  2-1000', 'no int vlan  1001-2000',
    'no int vlan  2001-3000', 'no int vlan  3001-3863',
    'no interface loopback 91', 'no interface loopback 95', 'no feature bgp',
    'no feature vpc', 'no int nve 1'
]

spine = [
    'no interface loopback 91', 'no interface loopback 95', 'no feature bgp'
]

def basic_authorization(user, password):
    s = user + ":" + password
    return "Basic " + s.encode("base64").rstrip()

def send_request_post(url, params):
    req = urllib2.Request(
        url,
        headers={
            "Authorization": basic_authorization("admin", "ICnt@258!"),
            "Content-Type": "application/json",
            "Accept": "*/*",
        },
        data=json.dumps(params))
    f = urllib2.urlopen(req)
    return f.read()

def getParams(command, version):
    com = {
        "ins_api": {
            "version": version,
            "type": "cli_conf",
            "chunk": "0",
            "sid": "1",
            "input": "conf t ;" + command,
            "output_format": "json"
        }
    }
    return com

def sendCommand(command, ip, version="1.2"):
    nxapi = "http://" + ip + ":3333/ins"
    send_request_post(nxapi, getParams(command,version))
    print ip + "; " + command
    return

def del_command(command, ip, version="1.2"):
    nxapi = "http://" + ip + ":3333/ins"
    returnInfo=json.loads(send_request_post(nxapi, getParams(command,version)))
    code = returnInfo['ins_api']['outputs']['output'][1]['code']
    if code == "200":
        info = returnInfo['ins_api']['outputs']['output'][1]['body']
        if len(info) < 1:
            print ip +"; return is null"
            return
        else:
            infos=info.split("\n")
            for i in range(0,len(infos)-1):
                print ip + "; no "+ infos[i]
                send_request_post(nxapi, getParams("no "+ infos[i],version))
            return
    else:
        print ip +"; return is error"

def del_portchannel(command, ip, version="1.2"):
    nxapi = "http://" + ip + ":3333/ins"
    returnInfo=json.loads(send_request_post(nxapi, getParams(command,version)))
    info = returnInfo['ins_api']['outputs']['output'][1]['body']
    if len(info) < 1:
        print ip + "; return is null"
        return
    else:
        infos=info.split("\n")
        for i in range(0,len(infos)-1):
            portNumber=infos[i].split(" ")[0]
            print ip + "; no int port-channel "+portNumber 
            send_request_post(nxapi, getParams("no int port-channel  "+ portNumber,version))
        return

def del_Ethernet_IP(command, ip, version="1.2"):
    nxapi = "http://" + ip + ":3333/ins"
    returnInfo=json.loads(send_request_post(nxapi, getParams(command,version)))
    info = returnInfo['ins_api']['outputs']['output'][1]['body']
    if len(info) < 1:
        print "return is null"
        return
    else:
        infos=info.split("\n")
        for i in range(0,len(infos)-1):
            ethernet=infos[i].split(" ")[0]
            print ip + "; interface "+ethernet +" ;no ip address" 
            send_request_post(nxapi, getParams("interface "+ethernet +" ;no ip address",version))
        return

def del_other( ip, version="1.2"):
    """
    delete vrf,pim,route-map,access-list,policy-map,class-map,port-channel,ip
    """
    del_command("show run | in vrf | in context | exclude  VPC-KPL | exclude management",ip,version)
    del_command("show run pim | in rp",ip,version)
    del_command("show run | in route-map | exclude evpnpermitall",ip,version)
    del_command("show run | in access-list",ip,version)
    del_command("show run | in policy-map",ip,version)
    del_command("show run | in class-map",ip,version)
    del_portchannel("show port-channel summary  | include Eth",ip,version)
    del_Ethernet_IP("show ip int brief vrf all  | include protocol | exclude mgmt0 | exclude Vlan",ip,version)
    return

#file_path = sys.path[0]+'/topology.properties'
#props = properties.parse(file_path)
#serverLeafs = properties._list(props.get('serverLeaf'))
#borderLeafs = properties._list(props.get('borderLeaf'))
#spines = properties._list(props.get('spine'))
#spine6ks = properties._list(props.get('spine_6k'))
serverLeafs = {'10.49.8.153'}
borderLeafs = {}
spines = {}
spine6ks = {}

for i in serverLeafs:
    print "clear switch "+ i
    for j in leaf:
        sendCommand(j, i, "1.0")
    del_other(i,"1.0")

for i in borderLeafs:
    print "clear switch "+ i
    for j in border:
        sendCommand(j, i)
    del_other(i)

for i in spines:
    print "clear switch "+ i
    for j in spine:
        sendCommand(j, i)
    del_other(i)
for i in spine6ks:
    print "clear switch "+ i
    for j in spine:
        sendCommand(j, i, "1.0")
    del_other(i, "1.0")
print "run end...."
