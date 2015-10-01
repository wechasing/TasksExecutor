#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
    The entrance of the framework
"""
from fabric.api import task

from bases import XMLConfiger

def initEnv(configer):
    """
        init the environment
    """
    configer.config()


@task
def executor():
    configer = XMLConfiger()
    initEnv(configer)

if __name__ == '__main__':
    executor()