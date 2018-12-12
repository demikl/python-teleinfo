#!/usr/bin/env python

import serial
import time
from abc import ABCMeta, abstractmethod

class HW_vendor():
    __metaclass__ = ABCMeta

    @abstractmethod
    def read_char(self):
        pass

    def __iter__(self):
        while True:
            yield self.read_char()

class HW_serial_based(HW_vendor):
    __metaclass__ = ABCMeta

    BAUDRATE = 1200
    PARITY = serial.PARITY_EVEN
    STOP_BITS = serial.STOPBITS_ONE
    BYTE_SIZE = serial.SEVENBITS

    def __init__(self, port):
        self._serial_port = serial.Serial(
            port=port,
            baudrate=self.BAUDRATE,
            parity=self.PARITY,
            stopbits=self.STOP_BITS,
            bytesize=self.BYTE_SIZE)

class RpiDom(HW_serial_based):
    CHANNEL_TELEINFO1 = 'A'
    CHANNEL_TELEINFO2 = 'B'

    def __init__(self, port='/dev/ttyAMA0', *args, **kwargs):
        super(RpiDom, self).__init__(port, *args, **kwargs)
        self.select_channel(self.CHANNEL_TELEINFO1)

    def read_char(self):
        return self._serial_port.read(1)

    def select_channel(self, channel):
        assert channel in [self.CHANNEL_TELEINFO1, self.CHANNEL_TELEINFO2]
        self._serial_port.write(channel)
        time.sleep(1)

class SolarBox_USB(HW_serial_based):
    def __init__(self, port="/dev/ttyUSB0", *args, **kwargs):
        super(SolarBox_USB, self).__init__(port, *args, **kwargs)
        raise NotImplementedError()
