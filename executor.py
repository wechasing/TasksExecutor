#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
    The entrance of the framework
"""

import os
import xml.etree.cElementTree as ET
from fabric.api import run, env, task

def initEnv():
    """
        init the environment
    """
    file_path = "./conf/conf.xml"
    tree = ET.ElementTree(file=file_path)
    root = tree.getroot()
    roles_root = root.find('roles')
    roles = roles_root.findall('role')

    for role in roles:
        role_name = role.attrib['name']
        hosts = role.find('hosts')
        env.roledefs[role_name] = []
        for host in hosts.findall('host'):
            host_name = host.text
            #add the each host to the env.hosts and env.roledefs
            env.roledefs[role_name].append(host_name)
            env.hosts.append(host_name)


@task
def executor():
    initEnv()

if __name__ == '__main__':
    executor()