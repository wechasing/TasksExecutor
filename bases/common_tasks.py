#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    some basic tasks in our common operations
"""


from fabric.api import task

@task
def copy_file(path):
    """
    copying the file (file and folder)
    :param path: the path of the file or folder
    :return:
    """

    pass

@task
def execute_command(command):
    """
    executing the specify command
    :param command: the command to execute
    :return:
    """

    if type(command) == list:
        pass
    elif isinstance(command,basestring):
        pass
    else:
        pass



