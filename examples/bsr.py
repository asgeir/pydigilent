#!/bin/env python3

# Xilinx Kintex 7
# very rough BSR example

from pydigilent import DeviceManager
dm = DeviceManager()
devices = dm.connected_devices()
device  = devices[0].open()        # pick adapter if there are multiple
device.jtag.enable()

irShiftSetup = bytearray([ 0xaa, 0xa2, 0x00 ])
device.jtag.put_tms_tdi_bits(irShiftSetup, 10)

# SAMPLE 000001 + 0000 | 000001 1100 
sampleCodeAndGotoShiftDr = bytearray([ 0x01, 0xa8, 0x00 ]) 
device.jtag.put_tms_tdi_bits(sampleCodeAndGotoShiftDr, 10)

pins=device.jtag.get_tdo_bits(0, 0, 320)
print(''.join("{:08b}".format(y) for y in pins))

device.close()
