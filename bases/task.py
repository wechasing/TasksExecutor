#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'weixiang'

from fabric.api import task, settings, sudo
class task():
    """
        the abstract class of the tasks
    """

    def __init__(self, commands):
        """
            :param commands: commands to execute
            :return: None
        """
        if commands is None or not (isinstance(commands, str) or isinstance(commands, list)):
            raise Exception()
        self.commands = commands

    def execute(self):
        """
            the method to execute the commands
            :return: None
        """
        # if there only one command to execute
        if isinstance(self.commands, str):
            with(settings(warn_only = True)):
                sudo(self.commands, shell=False)

        # if there some commands  to execute
        elif isinstance(self.commands, list):
            with(settings(warn_only = True)):
                for cmd in self.commands:
                    sudo(cmd, shell=False)
        # do nothing
        else:
            pass

