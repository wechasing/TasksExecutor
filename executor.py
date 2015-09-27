#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
    The entrance of the framework
"""

import os
import xml.etree.cElementTree as ET
import fabric

def initEnv():
    """
        init the environment
    """
    filePath = "./conf/conf.xml"
    tree = ET.ElementTree(file=filePath)
    root = tree.getroot()
    configuration = root.find('configuration')
    roles = configuration.find('roles')
    pass


def executor():
    initEnv()

    pass



if __name__ == '__main__':
    executor()