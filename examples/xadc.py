#!/bin/env python3

# Read XADC (Temp, Vccint, Vccaux) from Xilinx

XILINX=147
# 0x43651093 = XC7K325T, IR6, XADC
# 0x04001093 = XC6SLX, IR6 no XADC


def read_sensor(reg, label, unit): # reg.. 0 or 1 or 2
    dr = bytearray([ 0x00, 0x00, reg, 0x04 ]) # Temp
    device.jtag.put_tdi_bits(0, dr, 31)

    # update-dr and back to shift-dr
    UpdateDRAndGotoShiftDr = bytearray([ 0x2a, 0x00 ]) # TMS=1, TMS=1, TMS=1, TMS=0, TMS=0
    device.jtag.put_tms_tdi_bits(UpdateDRAndGotoShiftDr, 5)

    value_rev = device.jtag.get_tdo_bits(0, 0, 32)
    value_dec = value_rev[1]*256+value_rev[0]
    if unit == "C":
       value = (( value_dec / 16 ) * 503.975 / 4096 ) - 273.15
    else:
       value = (( value_dec / 16 ) / 4096 ) * 3
    print(f'{label} = {value:.2f}{unit}')

def get_idcodes():
    drShiftSetup = bytearray([ 0xaa, 0x22, 0x00 ])
    device.jtag.put_tms_tdi_bits(drShiftSetup, 9)
    idcodes=dict()
    device_id=0
    while 1:
       idcode_rev=device.jtag.get_tdo_bits(0, 0, 32)
       if idcode_rev == [0x0, 0x0, 0x0, 0x0]:
           break
       idcodes[device_id]=idcode_rev[::-1]
       device_id = device_id + 1

    return idcodes

def is_manufacturer(idcode, manuf):
    return ((idcode[2]&15)<<8) + idcode[3] == manuf

from pydigilent import DeviceManager
dm = DeviceManager()
devices = dm.connected_devices()

for devicex in devices:
    device_name = devicex.user_name.decode("utf-8")
    device = devicex.open()
    device.jtag.enable()

    idcodes = get_idcodes()

    if is_manufacturer(idcodes[0], XILINX):

        irShiftSetup = bytearray([ 0xaa, 0xa2, 0x00 ])
        device.jtag.put_tms_tdi_bits(irShiftSetup, 10)

        # XADC_DRP 110111 (reverse 0x01 + 0x04 + 0x10 + 0x00 | 0x01 + 0x0c (TMS=1+TDI=1) + TMS=1, TMS=1 | TMS=0, TMS=0
        adcCodeAndGotoShiftDr = bytearray([ 0x15, 0xad, 0x00 ]) 
        device.jtag.put_tms_tdi_bits(adcCodeAndGotoShiftDr, 10)

        read_sensor(0, "Temp", "C")
        read_sensor(1, "Vccint", "V")
        read_sensor(2, "Vccaux", "V")

    device.close()
