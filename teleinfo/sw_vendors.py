#!/usr/bin/env python

import socket
import time
from abc import ABCMeta, abstractmethod
from .base_vendor import BASE_vendor

class SW_tcp_based(BASE_vendor):
	__metaclass__ = ABCMeta
	ADDRESS = "127.0.0.1"
	PORT = 6001

	def __init__(self, ip_address, port):
		self.address = (ip_address, port)
		self.sock = None
		self.reconnect_socket()

	def reconnect_socket(self):
		if self.sock is not None:
			self.sock.close()
			self.sock = None

		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sock.connect(self.address)

	def read_char(self):
		return self.sock.recv(1).decode("ascii")