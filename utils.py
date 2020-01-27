from ntc_templates.parse import parse_output
from netmiko import ConnectHandler
from device_info import ios_info
import time
import sheetnames
import re


def ios_connection(host, device_type, command):


    ios_device = {
        'device_type': device_type,
        'host': host,
        'username': ios_info['username'],
        'password': ios_info['password'],
        'secret': ios_info['secret']
    }
    try:
        net_connect = ConnectHandler(**ios_device)
        net_connect.enable()
        output = net_connect.send_command(command)
        info = parse_output(platform=device_type, command=command, data=output)
        net_connect.disconnect()

    except ValueError:
        reason = e
        raise ValueError(f"SCOTT Failed to execute cli on {host} due to {reason}")



    if not net_connect:
        net_connect.disconnect()
    return(info)


def timestamp():
    timestamp = time.strftime('%Y-%m-%d')
    return timestamp

def sheet(command_input):
    commands = [
        "^(show\sinterface)",
        #"^(show\sip\seigrp\sneighbor)(?:\svrf\s[\w]+|)",
        "^(show\sip\seigrp\sneighbor)",
        "^(show\sip\sospf\sneighbor)(?:\svrf\s[\w]+|)",
        "^(show\scdp\sneighbor\sdetail)",
        "^(show\scdp\sneighbor)",
        "^(show\sversion)"
    ]

    for command in commands:
        pattern = re.compile(command)
        matches = pattern.finditer(command_input)
        for match in matches:
            return(sheetnames.sheetnames[match.group(0)])

