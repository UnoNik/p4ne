#!/usr/bin/python3
from pysnmp.hlapi import *

snmp_object = ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0)

result = getCmd(SnmpEngine(), CommunityData("public", mpModel=0), UdpTransportTarget(("10.31.70.107", 161)), ContextData(), ObjectType(snmp_object))

for i in result:
    varBinds = list(i[3])
    for s in varBinds:
        print(s)

