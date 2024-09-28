#!/bin/env python3

# IDCODE:
#   4 bit version
#  16 bit part
#  11 bit manufacturer e.g. 0000 1001 001  -- Xilinx
#   1 bit leading = 1
#
# .....093 = Xilinx

# for all adapters enumerate idcodes of all devices

from pydigilent import DeviceManager
dm = DeviceManager()
devices = dm.connected_devices()

for devicex in devices:
    device_name = devicex.user_name.decode("utf-8")
    device = devicex.open()
    device.jtag.enable()

    print(f'Device: {device_name}')
    # print(f'Device: {devicex.user_name.decode("utf-8")}')
    # print(f'Device: {devicex.user_name.decode("utf-8")} {devicex.serial_number.decode("utf-8")}')

    drShiftSetup = bytearray([ 0xaa, 0x22, 0x00 ])
    device.jtag.put_tms_tdi_bits(drShiftSetup, 9)
    device_id=0
    while 1:
       idcode_rev=device.jtag.get_tdo_bits(0, 0, 32)
       if idcode_rev == [0x0, 0x0, 0x0, 0x0]:
           break
       device_id = device_id + 1
       idcode = idcode_rev[::-1]
       print(f'Device {device_id}: 0x'+''.join('{:02X}'.format(a) for a in idcode))
    
    device.close()
