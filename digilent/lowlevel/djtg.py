import ctypes
import struct
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

jcbSetTmsTdiTck    = 1
jcbGetTmsTdiTdoTck = 2
jcbPutTms          = 3
jcbPutTmsGetTdo    = 4
jcbPutTdi          = 5
jcbPutTdiGetTdo    = 6
jcbGetTdo          = 7
jcbClockTck        = 8
jcbWaitUs          = 9
jcbSetAuxReset     = 10

djbpWaitUs      = 0x00000001
djbpSetAuxReset = 0x00000002

class JtagBatchBuffer(object):
	def __init__(self):
		object.__init__(self)
		self._buffer = []

	def clear(self):
		self._buffer = []

	def buffer(self):
		return ''.join(self._buffer)

	def SetTmsTdiTck(self, tms, tdi, tck):
		self._buffer.append(chr(jcbSetTmsTdiTck))
		self._buffer.append(chr(tms << 2 | tdi << 1 | tck))

	def GetTmsTdiTdoTck(self):
		self._buffer.append(chr(jcbGetTmsTdiTdoTck))

	def PutTms(self, tmsBytes, cbits):
		self._buffer.append(chr(jcbPutTms))
		self._buffer.append(struct.pack('<I', cbits))
		self._buffer.append(tmsBytes)

	def PutTmsGetTdo(self, tmsBytes, cbits):
		self._buffer.append(chr(jcbPutTmsGetTdo))
		self._buffer.append(struct.pack('<I', cbits))
		self._buffer.append(tmsBytes)

	def PutTdi(self, tdiBytes, cbits, lastTms):
		self._buffer.append(chr(jcbPutTdi))
		self._buffer.append(struct.pack('<I', cbits))
		self._buffer.append(chr(int(lastTms) & 1))
		self._buffer.append(tdiBytes)

	def PutTdiGetTdo(self, tdiBytes, cbits, lastTms):
		self._buffer.append(chr(jcbPutTdiGetTdo))
		self._buffer.append(struct.pack('<I', cbits))
		self._buffer.append(chr(int(lastTms) & 1))
		self._buffer.append(tdiBytes)

	def GetTdo(self, cbits, lastTms):
		self._buffer.append(chr(jcbGetTdo))
		self._buffer.append(struct.pack('<I', cbits))
		self._buffer.append(chr(int(lastTms) & 1))

	def ClockTck(self, numTicks):
		self._buffer.append(chr(jcbClockTck))
		self._buffer.append(struct.pack('<I', numTicks))

	def WaitUs(self, numUs):
		self._buffer.append(chr(jcbWaitUs))
		self._buffer.append(struct.pack('<I', numUs))

	def SetAuxReset(self, outputEnable, resetState):
		self._buffer.append(chr(jcbSetAuxReset))
		self._buffer.append(chr(outputEnable << 1 | resetState))


DjtgGetVersion = _djtg.DjtgGetVersion
DjtgGetVersion.argtypes = [ctypes.POINTER(ctypes.c_char * 32)]
DjtgGetVersion.restype = bool

DjtgGetPortCount = _djtg.DjtgGetPortCount
DjtgGetPortCount.argtypes = [HIF, ctypes.POINTER(ctypes.c_int32)]
DjtgGetPortCount.restype = bool

DjtgGetPortProperties = _djtg.DjtgGetPortProperties
DjtgGetPortProperties.argtypes = [HIF, ctypes.c_int32, ctypes.POINTER(ctypes.c_uint32)]
DjtgGetPortProperties.restype = bool

DjtgGetBatchProperties = _djtg.DjtgGetBatchProperties
DjtgGetBatchProperties.argtypes = [HIF, ctypes.c_int32, ctypes.POINTER(ctypes.c_uint32)]
DjtgGetBatchProperties.restype = bool

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
DjtgGetSpeed = _djtg.DjtgGetSpeed
DjtgGetSpeed.argtypes = [HIF, ctypes.POINTER(ctypes.c_uint32)]
DjtgGetSpeed.restype = bool

DjtgSetSpeed = _djtg.DjtgSetSpeed
DjtgSetSpeed.argtypes = [HIF, ctypes.c_uint32, ctypes.POINTER(ctypes.c_uint32)]
DjtgSetSpeed.restype = bool

DjtgSetTmsTdiTck = _djtg.DjtgSetTmsTdiTck
DjtgSetTmsTdiTck.argtypes = [HIF, ctypes.c_byte, ctypes.c_byte, ctypes.c_byte]
DjtgSetTmsTdiTck.restype = bool

DjtgGetTmsTdiTdoTck = _djtg.DjtgGetTmsTdiTdoTck
DjtgGetTmsTdiTdoTck.argtypes = [HIF, ctypes.POINTER(ctypes.c_byte), ctypes.POINTER(ctypes.c_byte), ctypes.POINTER(ctypes.c_byte), ctypes.POINTER(ctypes.c_byte)]
DjtgGetTmsTdiTdoTck.restype = bool

DjtgSetAuxReset = _djtg.DjtgSetAuxReset
DjtgSetAuxReset.argtypes = [HIF, ctypes.c_byte, ctypes.c_byte]
DjtgSetAuxReset.restype = bool

DjtgEnableTransBuffering = _djtg.DjtgEnableTransBuffering
DjtgEnableTransBuffering.argtypes = [HIF, ctypes.c_byte]
DjtgEnableTransBuffering.restype = bool

DjtgSyncBuffer = _djtg.DjtgSyncBuffer
DjtgSyncBuffer.argtypes = [HIF]
DjtgSyncBuffer.restype = bool


# misc. functions
DjtgWait = _djtg.DjtgWait
DjtgWait.argtypes = [HIF, ctypes.c_uint32, ctypes.POINTER(ctypes.c_uint32)]
DjtgWait.restype = bool


# overlapped functions
DjtgPutTdiBits = _djtg.DjtgPutTdiBits
DjtgPutTdiBits.argtypes = [HIF, ctypes.c_byte, ctypes.POINTER(ctypes.c_byte), ctypes.POINTER(ctypes.c_byte), ctypes.c_uint32, ctypes.c_byte]
DjtgPutTdiBits.restype = bool

DjtgPutTmsBits = _djtg.DjtgPutTmsBits
DjtgPutTmsBits.argtypes = [HIF, ctypes.c_byte, ctypes.POINTER(ctypes.c_byte), ctypes.POINTER(ctypes.c_byte), ctypes.c_uint32, ctypes.c_byte]
DjtgPutTmsBits.restype = bool

DjtgPutTmsTdiBits = _djtg.DjtgPutTmsTdiBits
DjtgPutTmsTdiBits.argtypes = [HIF, ctypes.POINTER(ctypes.c_byte), ctypes.POINTER(ctypes.c_byte), ctypes.c_uint32, ctypes.c_byte]
DjtgPutTmsTdiBits.restype = bool

DjtgGetTdoBits = _djtg.DjtgGetTdoBits
DjtgGetTdoBits.argtypes = [HIF, ctypes.c_byte, ctypes.c_byte, ctypes.POINTER(ctypes.c_byte), ctypes.c_uint32, ctypes.c_byte]
DjtgGetTdoBits.restype = bool

DjtgClockTck = _djtg.DjtgClockTck
DjtgClockTck.argtypes = [HIF, ctypes.c_byte, ctypes.c_byte, ctypes.c_uint32, ctypes.c_byte]
DjtgClockTck.restype = bool

DjtgBatch = _djtg.DjtgBatch
DjtgBatch.argtypes = [HIF, ctypes.c_uint32, ctypes.POINTER(ctypes.c_byte), ctypes.c_uint32, ctypes.POINTER(ctypes.c_byte), ctypes.c_byte]
DjtgBatch.restype = bool


# 1149.7-2009 configuration functions
DjtgSetScanFormat = _djtg.DjtgSetScanFormat
DjtgSetScanFormat.argtypes = [HIF, ctypes.c_byte, ctypes.c_byte]
DjtgSetScanFormat.restype = bool

DjtgGetScanFormat = _djtg.DjtgGetScanFormat
DjtgGetScanFormat.argtypes = [HIF, ctypes.POINTER(ctypes.c_byte), ctypes.POINTER(ctypes.c_byte)]
DjtgGetScanFormat.restype = bool

DjtgSetReadyCnt = _djtg.DjtgSetReadyCnt
DjtgSetReadyCnt.argtypes = [HIF, ctypes.c_byte, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(ctypes.c_uint32)]
DjtgSetReadyCnt.restype = bool

DjtgGetReadyCnt = _djtg.DjtgGetReadyCnt
DjtgGetReadyCnt.argtypes = [HIF, ctypes.POINTER(ctypes.c_byte), ctypes.POINTER(ctypes.c_uint32)]
DjtgGetReadyCnt.restype = bool

DjtgSetDelayCnt = _djtg.DjtgSetDelayCnt
DjtgSetDelayCnt.argtypes = [HIF, ctypes.c_uint32, ctypes.POINTER(ctypes.c_uint32), ctypes.c_byte]
DjtgSetDelayCnt.restype = bool

DjtgGetDelayCnt = _djtg.DjtgGetDelayCnt
DjtgGetDelayCnt.argtypes = [HIF, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(ctypes.c_byte)]
DjtgGetDelayCnt.restype = bool


# 1149.7-2009 misc. functions
DjtgCheckPacket = _djtg.DjtgCheckPacket
DjtgCheckPacket.argtypes = [HIF, ctypes.c_byte, ctypes.c_byte, ctypes.c_byte]
DjtgCheckPacket.restype = bool

DjtgEscape = _djtg.DjtgEscape
DjtgEscape.argtypes = [HIF, ctypes.c_byte, ctypes.c_byte]
DjtgEscape.restype = bool


__all__ = [
	'dprpJtgSetSpeed', 'dprpJtgSetPinState', 'dprpJtgTransBuffering', 'dprpJtgWait',
	'dprpJtgDelayCnt', 'dprpJtgReadyCnt', 'dprpJtgEscape', 'dprpJtgMScan', 'dprpJtgOScan0',
	'dprpJtgOScan1', 'dprpJtgOScan2', 'dprpJtgOScan3', 'dprpJtgOScan4', 'dprpJtgOScan5',
	'dprpJtgOScan6', 'dprpJtgOScan7', 'dprpJtgCheckPacket', 'dprpJtgBatch', 'dprpJtgSetAuxReset',
	'jtgsfNone', 'jtgsfJScan0', 'jtgsfJScan1', 'jtgsfJScan2', 'jtgsfJScan3', 'jtgsfMScan',
	'jtgsfOScan0', 'jtgsfOScan1', 'jtgsfOScan2', 'jtgsfOScan3', 'jtgsfOScan4', 'jtgsfOScan5',
	'jtgsfOScan6', 'jtgsfOScan7', 'cedgeJtgCustom', 'cedgeJtgDeselect', 'cedgeJtgSelect',
	'cedgeJtgReset', 'jcbSetTmsTdiTck', 'jcbGetTmsTdiTdoTck', 'jcbPutTms', 'jcbPutTmsGetTdo',
	'jcbPutTdi', 'jcbPutTdiGetTdo', 'jcbGetTdo', 'jcbClockTck', 'jcbWaitUs', 'jcbSetAuxReset',
	'djbpWaitUs', 'djbpSetAuxReset', 'JtagBatchBuffer', 'DjtgGetVersion', 'DjtgGetPortCount',
	'DjtgGetPortProperties', 'DjtgGetBatchProperties', 'DjtgEnable', 'DjtgEnableEx', 'DjtgDisable',
	'DjtgGetSpeed', 'DjtgSetSpeed', 'DjtgSetTmsTdiTck', 'DjtgGetTmsTdiTdoTck', 'DjtgSetAuxReset',
	'DjtgEnableTransBuffering', 'DjtgSyncBuffer', 'DjtgWait', 'DjtgPutTdiBits', 'DjtgPutTmsBits',
	'DjtgPutTmsTdiBits', 'DjtgGetTdoBits', 'DjtgClockTck', 'DjtgBatch', 'DjtgSetScanFormat',
	'DjtgGetScanFormat', 'DjtgSetReadyCnt', 'DjtgGetReadyCnt', 'DjtgSetDelayCnt', 'DjtgGetDelayCnt',
	'DjtgCheckPacket', 'DjtgEscape'
]
