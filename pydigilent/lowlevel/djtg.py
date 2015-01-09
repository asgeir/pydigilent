import ctypes
import sys

from common import HIF

if sys.platform.startswith("win"):
	_djtg = ctypes.cdll.djtg
else:
	_djtg = ctypes.cdll.LoadLibrary("libdjtg.so")

dprpJtgSetSpeed       = 0x00001
dprpJtgSetPinState    = 0x00002
dprpJtgTransBuffering = 0x00004
dprpJtgWait           = 0x00008
dprpJtgDelayCnt       = 0x00010
dprpJtgReadyCnt       = 0x00020
dprpJtgEscape         = 0x00040
dprpJtgMScan          = 0x00080
dprpJtgOScan0         = 0x00100
dprpJtgOScan1         = 0x00200
dprpJtgOScan2         = 0x00400
dprpJtgOScan3         = 0x00800
dprpJtgOScan4         = 0x01000
dprpJtgOScan5         = 0x02000
dprpJtgOScan6         = 0x04000
dprpJtgOScan7         = 0x08000
dprpJtgCheckPacket    = 0x10000
dprpJtgBatch          = 0x20000
dprpJtgSetAuxReset    = 0x40000

jtgsfNone   = 0
jtgsfJScan0 = 1
jtgsfJScan1 = 2
jtgsfJScan2 = 3
jtgsfJScan3 = 4
jtgsfMScan  = 5
jtgsfOScan0 = 6
jtgsfOScan1 = 7
jtgsfOScan2 = 8
jtgsfOScan3 = 9
jtgsfOScan4 = 10
jtgsfOScan5 = 11
jtgsfOScan6 = 12
jtgsfOScan7 = 13

cedgeJtgCustom   = 2  # Number of edges for a Custom Escape
cedgeJtgDeselect = 4  # Number of edges for a Deselection Escape
cedgeJtgSelect   = 6  # Number of edges for a Selection Escape
cedgeJtgReset    = 8  # Number of edges for a Reset Escape

djbpWaitUs      = 0x00000001
djbpSetAuxReset = 0x00000002


_DjtgGetVersion = _djtg.DjtgGetVersion
_DjtgGetVersion.argtypes = [ctypes.POINTER(ctypes.c_char * 32)]
_DjtgGetVersion.restype = bool

def DjtgGetVersion():
	tmp = ctypes.create_string_buffer(32)
	return (_DjtgGetVersion(ctypes.byref(tmp)), tmp.value)

_DjtgGetPortCount = _djtg.DjtgGetPortCount
_DjtgGetPortCount.argtypes = [HIF, ctypes.POINTER(ctypes.c_int32)]
_DjtgGetPortCount.restype = bool

def DjtgGetPortCount(hif):
	value = ctypes.c_int32()
	return (_DjtgGetPortCount(hif, ctypes.byref(value)), value.value)

_DjtgGetPortProperties = _djtg.DjtgGetPortProperties
_DjtgGetPortProperties.argtypes = [HIF, ctypes.c_int32, ctypes.POINTER(ctypes.c_uint32)]
_DjtgGetPortProperties.restype = bool

def DjtgGetPortProperties(hif, prtReq):
	info = ctypes.c_uint32()
	return (_DjtgGetPortProperties(hif, prtReq, ctypes.byref(info)), info.value)

_DjtgGetBatchProperties = _djtg.DjtgGetBatchProperties
_DjtgGetBatchProperties.argtypes = [HIF, ctypes.c_int32, ctypes.POINTER(ctypes.c_uint32)]
_DjtgGetBatchProperties.restype = bool

def DjtgGetBatchProperties(hif, prtReq):
	info = ctypes.c_uint32()
	return (_DjtgGetBatchProperties(hif, prtReq, ctypes.byref(info)), info.value)

DjtgEnable = _djtg.DjtgEnable
DjtgEnable.argtypes = [HIF]
DjtgEnable.restype = bool

DjtgEnableEx = _djtg.DjtgEnableEx
DjtgEnableEx.argtypes = [HIF, ctypes.c_int32]
DjtgEnableEx.restype = bool

DjtgDisable = _djtg.DjtgDisable
DjtgDisable.argtypes = [HIF]
DjtgDisable.restype = bool


# configuration functions
_DjtgGetSpeed = _djtg.DjtgGetSpeed
_DjtgGetSpeed.argtypes = [HIF, ctypes.POINTER(ctypes.c_uint32)]
_DjtgGetSpeed.restype = bool

def DjtgGetSpeed(hif):
	value = ctypes.c_uint32()
	return (_DjtgGetSpeed(hif, ctypes.byref(value)), value.value)

_DjtgSetSpeed = _djtg.DjtgSetSpeed
_DjtgSetSpeed.argtypes = [HIF, ctypes.c_uint32, ctypes.POINTER(ctypes.c_uint32)]
_DjtgSetSpeed.restype = bool

def DjtgSetSpeed(hif, frqReq):
	frqSet = ctypes.c_uint32()
	return (_DjtgSetSpeed(hif, frqReq, ctypes.byref(frqSet)), frqSet.value)

DjtgSetTmsTdiTck = _djtg.DjtgSetTmsTdiTck
DjtgSetTmsTdiTck.argtypes = [HIF, ctypes.c_ubyte, ctypes.c_ubyte, ctypes.c_ubyte]
DjtgSetTmsTdiTck.restype = bool

_DjtgGetTmsTdiTdoTck = _djtg.DjtgGetTmsTdiTdoTck
_DjtgGetTmsTdiTdoTck.argtypes = [HIF, ctypes.POINTER(ctypes.c_ubyte), ctypes.POINTER(ctypes.c_ubyte), ctypes.POINTER(ctypes.c_ubyte), ctypes.POINTER(ctypes.c_ubyte)]
_DjtgGetTmsTdiTdoTck.restype = bool

def DjtgGetTmsTdiTdoTck(hif):
	a = ctypes.c_ubyte()
	b = ctypes.c_ubyte()
	c = ctypes.c_ubyte()
	d = ctypes.c_ubyte()
	return (_DjtgGetTmsTdiTdoTck(hif, ctypes.byref(a), ctypes.byref(b), ctypes.byref(c), ctypes.byref(d)), a.value, b.value, c.value, d.value)

DjtgSetAuxReset = _djtg.DjtgSetAuxReset
DjtgSetAuxReset.argtypes = [HIF, ctypes.c_ubyte, ctypes.c_ubyte]
DjtgSetAuxReset.restype = bool

DjtgEnableTransBuffering = _djtg.DjtgEnableTransBuffering
DjtgEnableTransBuffering.argtypes = [HIF, ctypes.c_ubyte]
DjtgEnableTransBuffering.restype = bool

DjtgSyncBuffer = _djtg.DjtgSyncBuffer
DjtgSyncBuffer.argtypes = [HIF]
DjtgSyncBuffer.restype = bool


# misc. functions
_DjtgWait = _djtg.DjtgWait
_DjtgWait.argtypes = [HIF, ctypes.c_uint32, ctypes.POINTER(ctypes.c_uint32)]
_DjtgWait.restype = bool

def DjtgWait(hif, tusWait):
	value = ctypes.c_uint32()
	return (_DjtgWait(hif, tusWait, ctypes.byref(value)), value.value)


# overlapped functions
DjtgPutTdiBits = _djtg.DjtgPutTdiBits
DjtgPutTdiBits.argtypes = [HIF, ctypes.c_ubyte, ctypes.POINTER(ctypes.c_ubyte), ctypes.POINTER(ctypes.c_ubyte), ctypes.c_uint32, ctypes.c_ubyte]
DjtgPutTdiBits.restype = bool

DjtgPutTmsBits = _djtg.DjtgPutTmsBits
DjtgPutTmsBits.argtypes = [HIF, ctypes.c_ubyte, ctypes.POINTER(ctypes.c_ubyte), ctypes.POINTER(ctypes.c_ubyte), ctypes.c_uint32, ctypes.c_ubyte]
DjtgPutTmsBits.restype = bool

DjtgPutTmsTdiBits = _djtg.DjtgPutTmsTdiBits
DjtgPutTmsTdiBits.argtypes = [HIF, ctypes.POINTER(ctypes.c_ubyte), ctypes.POINTER(ctypes.c_ubyte), ctypes.c_uint32, ctypes.c_ubyte]
DjtgPutTmsTdiBits.restype = bool

DjtgGetTdoBits = _djtg.DjtgGetTdoBits
DjtgGetTdoBits.argtypes = [HIF, ctypes.c_ubyte, ctypes.c_ubyte, ctypes.POINTER(ctypes.c_ubyte), ctypes.c_uint32, ctypes.c_ubyte]
DjtgGetTdoBits.restype = bool

DjtgClockTck = _djtg.DjtgClockTck
DjtgClockTck.argtypes = [HIF, ctypes.c_ubyte, ctypes.c_ubyte, ctypes.c_uint32, ctypes.c_ubyte]
DjtgClockTck.restype = bool

DjtgBatch = _djtg.DjtgBatch
DjtgBatch.argtypes = [HIF, ctypes.c_uint32, ctypes.POINTER(ctypes.c_ubyte), ctypes.c_uint32, ctypes.POINTER(ctypes.c_ubyte), ctypes.c_ubyte]
DjtgBatch.restype = bool


# 1149.7-2009 configuration functions
DjtgSetScanFormat = _djtg.DjtgSetScanFormat
DjtgSetScanFormat.argtypes = [HIF, ctypes.c_ubyte, ctypes.c_ubyte]
DjtgSetScanFormat.restype = bool

DjtgGetScanFormat = _djtg.DjtgGetScanFormat
DjtgGetScanFormat.argtypes = [HIF, ctypes.POINTER(ctypes.c_ubyte), ctypes.POINTER(ctypes.c_ubyte)]
DjtgGetScanFormat.restype = bool

DjtgSetReadyCnt = _djtg.DjtgSetReadyCnt
DjtgSetReadyCnt.argtypes = [HIF, ctypes.c_ubyte, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(ctypes.c_uint32)]
DjtgSetReadyCnt.restype = bool

DjtgGetReadyCnt = _djtg.DjtgGetReadyCnt
DjtgGetReadyCnt.argtypes = [HIF, ctypes.POINTER(ctypes.c_ubyte), ctypes.POINTER(ctypes.c_uint32)]
DjtgGetReadyCnt.restype = bool

DjtgSetDelayCnt = _djtg.DjtgSetDelayCnt
DjtgSetDelayCnt.argtypes = [HIF, ctypes.c_uint32, ctypes.POINTER(ctypes.c_uint32), ctypes.c_ubyte]
DjtgSetDelayCnt.restype = bool

DjtgGetDelayCnt = _djtg.DjtgGetDelayCnt
DjtgGetDelayCnt.argtypes = [HIF, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(ctypes.c_ubyte)]
DjtgGetDelayCnt.restype = bool


# 1149.7-2009 misc. functions
DjtgCheckPacket = _djtg.DjtgCheckPacket
DjtgCheckPacket.argtypes = [HIF, ctypes.c_ubyte, ctypes.c_ubyte, ctypes.c_ubyte]
DjtgCheckPacket.restype = bool

DjtgEscape = _djtg.DjtgEscape
DjtgEscape.argtypes = [HIF, ctypes.c_ubyte, ctypes.c_ubyte]
DjtgEscape.restype = bool


__all__ = [
	'dprpJtgSetSpeed', 'dprpJtgSetPinState', 'dprpJtgTransBuffering', 'dprpJtgWait',
	'dprpJtgDelayCnt', 'dprpJtgReadyCnt', 'dprpJtgEscape', 'dprpJtgMScan', 'dprpJtgOScan0',
	'dprpJtgOScan1', 'dprpJtgOScan2', 'dprpJtgOScan3', 'dprpJtgOScan4', 'dprpJtgOScan5',
	'dprpJtgOScan6', 'dprpJtgOScan7', 'dprpJtgCheckPacket', 'dprpJtgBatch', 'dprpJtgSetAuxReset',
	'jtgsfNone', 'jtgsfJScan0', 'jtgsfJScan1', 'jtgsfJScan2', 'jtgsfJScan3', 'jtgsfMScan',
	'jtgsfOScan0', 'jtgsfOScan1', 'jtgsfOScan2', 'jtgsfOScan3', 'jtgsfOScan4', 'jtgsfOScan5',
	'jtgsfOScan6', 'jtgsfOScan7', 'cedgeJtgCustom', 'cedgeJtgDeselect', 'cedgeJtgSelect',
	'cedgeJtgReset', 'djbpWaitUs', 'djbpSetAuxReset', 'DjtgGetVersion', 'DjtgGetPortCount',
	'DjtgGetPortProperties', 'DjtgGetBatchProperties', 'DjtgEnable', 'DjtgEnableEx', 'DjtgDisable',
	'DjtgGetSpeed', 'DjtgSetSpeed', 'DjtgSetTmsTdiTck', 'DjtgGetTmsTdiTdoTck', 'DjtgSetAuxReset',
	'DjtgEnableTransBuffering', 'DjtgSyncBuffer', 'DjtgWait', 'DjtgPutTdiBits', 'DjtgPutTmsBits',
	'DjtgPutTmsTdiBits', 'DjtgGetTdoBits', 'DjtgClockTck', 'DjtgBatch', 'DjtgSetScanFormat',
	'DjtgGetScanFormat', 'DjtgSetReadyCnt', 'DjtgGetReadyCnt', 'DjtgSetDelayCnt', 'DjtgGetDelayCnt',
	'DjtgCheckPacket', 'DjtgEscape'
]
