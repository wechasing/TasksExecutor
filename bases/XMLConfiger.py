#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    read the configuration information from the configuration file such as conf.xml
"""
import Configer
import xml.etree.cElementTree as ET
from fabric.api import env

class XMLConfiger(Configer):

    def config(self):
        file_path = "../conf/conf.xml"
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

        user = root.find('user')

        # if user is defined in the conf.xml settle it to the env.user else do nothing
        if user is not None:
            env.user = user.text
