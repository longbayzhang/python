# -*- coding: utf-8 -*-

from pysnmp.hlapi import *

systemDesc = '1.3.6.1.2.1.1.1.0'
ifEntry = '1.3.6.1.2.1.2.2.1.2'

errorIndication, errorStatus, errorIndex, varBinds = next(
    getCmd(SnmpEngine(),
           CommunityData('public', mpModel=0),
           UdpTransportTarget(('172.20.10.171', 161)),
           ContextData(),
           ObjectType(ObjectIdentity(ifEntry)))
)

if errorIndication:
    print(errorIndication)
elif errorStatus:
    print('%s at %s' % (errorStatus.prettyPrint(),
                        errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
else:
    for varBind in varBinds:
        print(' = '.join([x.prettyPrint() for x in varBind]))
