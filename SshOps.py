#!/usr/bin/python
# -*- coding: UTF-8 -*-
#SshOps.py

from paramiko.client import SSHClient
import paramiko
import ConfigParser

class SshOps:
	def __init__(self):
		self.ssh = SSHClient()
		self.ssh.load_system_host_keys()
		self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		self.ssh.connect(hostname='127.0.0.1',username='vitor',password='100567')

	def runCommand(self,command):
		stdin,stdout,stderr = self.ssh.exec_command(command)
		if stderr.channel.recv_exit_status() != 0:
			return {"status":1,"message":stderr.read()}
		else:
			return {"status":0,"message":stdout.read()}











