import ctypes
import sys

if sys.platform.startswith("win"):
	_dwf = ctypes.cdll.dwf
else:
	_dwf = ctypes.cdll.LoadLibrary("libdwf.so")

class _types(object):
	c_byte_p = ctypes.POINTER(ctypes.c_byte)
	c_double_p = ctypes.POINTER(ctypes.c_double)
	c_int_p = ctypes.POINTER(ctypes.c_int)
	c_uint_p = ctypes.POINTER(ctypes.c_uint)

class HDWF(ctypes.c_int):
	pass
hdwfNone = HDWF(0)

class ENUMFILTER(ctypes.c_int):
	pass
enumfilterAll       = ENUMFILTER(0)
enumfilterEExplorer = ENUMFILTER(1)
enumfilterDiscovery = ENUMFILTER(2)

class DEVID(ctypes.c_int):
	pass
devidEExplorer = DEVID(1)
devidDiscovery = DEVID(2)

class DEVVER(ctypes.c_int):
	pass
devverEExplorerC = DEVVER(2)
devverEExplorerE = DEVVER(4)
devverEExplorerF = DEVVER(5)
devverDiscoveryA = DEVVER(1)
devverDiscoveryB = DEVVER(2)
devverDiscoveryC = DEVVER(3)

class TRIGSRC(ctypes.c_byte):
	pass
trigsrcNone              = TRIGSRC(0)
trigsrcPC                = TRIGSRC(1)
trigsrcDetectorAnalogIn  = TRIGSRC(2)
trigsrcDetectorDigitalIn = TRIGSRC(3)
trigsrcAnalogIn          = TRIGSRC(4)
trigsrcDigitalIn         = TRIGSRC(5)
trigsrcDigitalOut        = TRIGSRC(6)
trigsrcAnalogOut1        = TRIGSRC(7)
trigsrcAnalogOut2        = TRIGSRC(8)
trigsrcAnalogOut3        = TRIGSRC(9)
trigsrcAnalogOut4        = TRIGSRC(10)
trigsrcExternal1         = TRIGSRC(11)
trigsrcExternal2         = TRIGSRC(12)
trigsrcExternal3         = TRIGSRC(13)
trigsrcExternal4         = TRIGSRC(14)

class DwfState(ctypes.c_byte):
	pass
DwfStateReady     = DwfState(0)
DwfStateConfig    = DwfState(4)
DwfStatePrefill   = DwfState(5)
DwfStateArmed     = DwfState(1)
DwfStateWait      = DwfState(7)
DwfStateTriggered = DwfState(3)
DwfStateRunning   = DwfState(3)
DwfStateDone      = DwfState(2)

class ACQMODE(ctypes.c_int):
	pass
acqmodeSingle     = ACQMODE(0)
acqmodeScanShift  = ACQMODE(1)
acqmodeScanScreen = ACQMODE(2)
acqmodeRecord     = ACQMODE(3)

class FILTER(ctypes.c_int):
	pass
filterDecimate = FILTER(0)
filterAverage  = FILTER(1)
filterMinMax   = FILTER(2)

class TRIGTYPE(ctypes.c_int):
	pass
trigtypeEdge       = TRIGTYPE(0)
trigtypePulse      = TRIGTYPE(1)
trigtypeTransition = TRIGTYPE(2)

class TRIGCOND(ctypes.c_int):
	pass
trigcondRisingPositive  = TRIGCOND(0)
trigcondFallingNegative = TRIGCOND(1)

class TRIGLEN(ctypes.c_int):
	pass
triglenLess    = TRIGLEN(0)
triglenTimeout = TRIGLEN(1)
triglenMore    = TRIGLEN(2)

class DWFERC(ctypes.c_int):
	pass
dwfercNoErc             = DWFERC(0)        # No error occurred
dwfercUnknownError      = DWFERC(1)        # API waiting on pending API timed out
dwfercApiLockTimeout    = DWFERC(2)        # API waiting on pending API timed out
dwfercAlreadyOpened     = DWFERC(3)        # Device already opened
dwfercNotSupported      = DWFERC(4)        # Device not supported
dwfercInvalidParameter0 = DWFERC(0x10)     # Invalid parameter sent in API call
dwfercInvalidParameter1 = DWFERC(0x11)     # Invalid parameter sent in API call
dwfercInvalidParameter2 = DWFERC(0x12)     # Invalid parameter sent in API call
dwfercInvalidParameter3 = DWFERC(0x13)     # Invalid parameter sent in API call
dwfercInvalidParameter4 = DWFERC(0x14)     # Invalid parameter sent in API call

class FUNC(ctypes.c_byte):
	pass
funcDC       = FUNC(0)
funcSine     = FUNC(1)
funcSquare   = FUNC(2)
funcTriangle = FUNC(3)
funcRampUp   = FUNC(4)
funcRampDown = FUNC(5)
funcNoise    = FUNC(6)
funcCustom   = FUNC(30)
funcPlay     = FUNC(31)

class ANALOGIO(ctypes.c_byte):
	pass
analogioEnable      = ANALOGIO(1)
analogioVoltage     = ANALOGIO(2)
analogioCurrent     = ANALOGIO(3)
analogioPower       = ANALOGIO(4)
analogioTemperature = ANALOGIO(5)

class AnalogOutNode(ctypes.c_int):
	pass
AnalogOutNodeCarrier = AnalogOutNode(0)
AnalogOutNodeFM      = AnalogOutNode(1)
AnalogOutNodeAM      = AnalogOutNode(2)

class DwfDigitalInClockSource(ctypes.c_int):
	pass
DwfDigitalInClockSourceInternal = DwfDigitalInClockSource(0)
DwfDigitalInClockSourceExternal = DwfDigitalInClockSource(1)

class DwfDigitalInSampleMode(ctypes.c_int):
	pass
DwfDigitalInSampleModeSimple = DwfDigitalInSampleMode(0)
DwfDigitalInSampleModeNoise  = DwfDigitalInSampleMode(1)

class DwfDigitalOutOutput(ctypes.c_int):
	pass
DwfDigitalOutOutputPushPull   = DwfDigitalOutOutput(0)
DwfDigitalOutOutputOpenDrain  = DwfDigitalOutOutput(1)
DwfDigitalOutOutputOpenSource = DwfDigitalOutOutput(2)
DwfDigitalOutOutputThreeState = DwfDigitalOutOutput(3)

class DwfDigitalOutType(ctypes.c_int):
	pass
DwfDigitalOutTypePulse  = DwfDigitalOutType(0)
DwfDigitalOutTypeCustom = DwfDigitalOutType(1)
DwfDigitalOutTypeRandom = DwfDigitalOutType(2)

class DwfDigitalOutIdle(ctypes.c_int):
	pass
DwfDigitalOutIdleInit = DwfDigitalOutIdle(0)
DwfDigitalOutIdleLow  = DwfDigitalOutIdle(1)
DwfDigitalOutIdleHigh = DwfDigitalOutIdle(2)
DwfDigitalOutIdleZet  = DwfDigitalOutIdle(3)

def IsBitSet(fs, bit):
	return ((fs & (1 << bit)) != 0)

# Error and version APIs:
_FDwfGetLastError = _dwf.FDwfGetLastError
_FDwfGetLastError.argtypes = [ctypes.POINTER(DWFERC)]
_FDwfGetLastError.restype = bool

def FDwfGetLastError():
	erc = DWFERC()
	return (_FDwfGetLastError(ctypes.byref(erc)), erc)

_FDwfGetLastErrorMsg = _dwf.FDwfGetLastErrorMsg
_FDwfGetLastErrorMsg.argtypes = [ctypes.POINTER(ctypes.c_char * 512)]
_FDwfGetLastErrorMsg.restype = bool

def FDwfGetLastErrorMsg():
	buf = ctypes.create_string_buffer(512)
	return (_FDwfGetLastErrorMsg(ctypes.byref(buf)), buf.value)

_FDwfGetVersion = _dwf.FDwfGetVersion  # Returns DLL version, for instance: "2.4.3"
_FDwfGetVersion.argtypes = [ctypes.POINTER(ctypes.c_char * 32)]
_FDwfGetVersion.restype = bool

def FDwfGetVersion():
	buf = ctypes.create_string_buffer(32)
	return (_FDwfGetVersion(ctypes.byref(buf)), buf.value)

# DEVICE MANAGMENT FUNCTIONS
# Enumeration:
_FDwfEnum = _dwf.FDwfEnum
_FDwfEnum.argtypes = [ENUMFILTER, _types.c_int_p]
_FDwfEnum.restype = bool

def FDwfEnum(enumFilter):
	tmp = ctypes.c_int()
	return (_FDwfEnum(enumFilter, ctypes.byref(tmp)), tmp.value)

_FDwfEnumDeviceType = _dwf.FDwfEnumDeviceType
_FDwfEnumDeviceType.argtypes = [ctypes.c_int, ctypes.POINTER(DEVID), ctypes.POINTER(DEVVER)]
_FDwfEnumDeviceType.restype = bool

def FDwfEnumDeviceType(idxDevice):
	devid = DEVID()
	devver = DEVVER()
	return (_FDwfEnumDeviceType(idxDevice, ctypes.byref(devid), ctypes.byref(devver)), devid, devver)

_FDwfEnumDeviceIsOpened = _dwf.FDwfEnumDeviceIsOpened
_FDwfEnumDeviceIsOpened.argtypes = [ctypes.c_int, _types.c_byte_p]
_FDwfEnumDeviceIsOpened.restype = bool

def FDwfEnumDeviceIsOpened(idxDevice):
	isopen = ctypes.c_byte()
	return (_FDwfEnumDeviceIsOpened(idxDevice, ctypes.byref(isopen)), bool(isopen.value))

_FDwfEnumUserName = _dwf.FDwfEnumUserName
_FDwfEnumUserName.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_char * 32)]
_FDwfEnumUserName.restype = bool

def FDwfEnumUserName(idxDevice):
	name = ctypes.create_string_buffer(32)
	return (_FDwfEnumUserName(idxDevice, ctypes.byref(name)), name.value)

_FDwfEnumDeviceName = _dwf.FDwfEnumDeviceName
_FDwfEnumDeviceName.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_char * 32)]
_FDwfEnumDeviceName.restype = bool

def FDwfEnumDeviceName(idxDevice):
	name = ctypes.create_string_buffer(32)
	return (_FDwfEnumDeviceName(idxDevice, ctypes.byref(name)), name.value)

_FDwfEnumSN = _dwf.FDwfEnumSN
_FDwfEnumSN.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_char * 32)]
_FDwfEnumSN.restype = bool

def FDwfEnumSN(idxDevice):
	sn = ctypes.create_string_buffer(32)
	return (_FDwfEnumSN(idxDevice, ctypes.byref(sn)), sn.value)


# Open/Close:
_FDwfDeviceOpen = _dwf.FDwfDeviceOpen
_FDwfDeviceOpen.argtypes = [ctypes.c_int, ctypes.POINTER(HDWF)]
_FDwfDeviceOpen.restype = bool

def FDwfDeviceOpen(idxDevice):
	hdwf = HDWF()
	return (_FDwfDeviceOpen(idxDevice, ctypes.byref(hdwf)), hdwf)

FDwfDeviceClose = _dwf.FDwfDeviceClose
FDwfDeviceClose.argtypes = [HDWF]
FDwfDeviceClose.restype = bool

FDwfDeviceCloseAll = _dwf.FDwfDeviceCloseAll
FDwfDeviceCloseAll.argtypes = []
FDwfDeviceCloseAll.restype = bool

FDwfDeviceAutoConfigureSet = _dwf.FDwfDeviceAutoConfigureSet
FDwfDeviceAutoConfigureSet.argtypes = [HDWF, ctypes.c_byte]
FDwfDeviceAutoConfigureSet.restype = bool

_FDwfDeviceAutoConfigureGet = _dwf.FDwfDeviceAutoConfigureGet
_FDwfDeviceAutoConfigureGet.argtypes = [HDWF, _types.c_byte_p]
_FDwfDeviceAutoConfigureGet.restype = bool

def FDwfDeviceAutoConfigureGet(hdwf):
	value = ctypes.c_byte()
	return (_FDwfDeviceAutoConfigureGet(hdwf, ctypes.byref(value)), bool(value.value))

FDwfDeviceReset = _dwf.FDwfDeviceReset
FDwfDeviceReset.argtypes = [HDWF]
FDwfDeviceReset.restype = bool

_FDwfDeviceTriggerInfo = _dwf.FDwfDeviceTriggerInfo  # use IsBitSet
_FDwfDeviceTriggerInfo.argtypes = [HDWF, _types.c_int_p]
_FDwfDeviceTriggerInfo.restype = bool

def FDwfDeviceTriggerInfo(hdwf):
	info = ctypes.c_int()
	if not _FDwfDeviceTriggerInfo(hdwf, ctypes.byref(info)):
		return (False, [])
	supported = []
	for i in range(8 * ctypes.sizeof(ctypes.c_int)):
		if info.value & (1 << i) != 0:
			supported.append(TRIGSRC(i))
	return (True, supported)

FDwfDeviceTriggerSet = _dwf.FDwfDeviceTriggerSet
FDwfDeviceTriggerSet.argtypes = [HDWF, ctypes.c_int, TRIGSRC]
FDwfDeviceTriggerSet.restype = bool

_FDwfDeviceTriggerGet = _dwf.FDwfDeviceTriggerGet
_FDwfDeviceTriggerGet.argtypes = [HDWF, ctypes.c_int, ctypes.POINTER(TRIGSRC)]
_FDwfDeviceTriggerGet.restype = bool

def FDwfDeviceTriggerGet(hdwf, idxPin):
	src = TRIGSRC()
	return (_FDwfDeviceTriggerGet(hdwf, idxPin, ctypes.byref(src)), src)

FDwfDeviceTriggerPC = _dwf.FDwfDeviceTriggerPC
FDwfDeviceTriggerPC.argtypes = [HDWF]
FDwfDeviceTriggerPC.restype = bool


# ANALOG IN INSTRUMENT FUNCTIONS
# Control and status:
FDwfAnalogInReset = _dwf.FDwfAnalogInReset
FDwfAnalogInReset.argtypes = [HDWF]
FDwfAnalogInReset.restype = bool

FDwfAnalogInConfigure = _dwf.FDwfAnalogInConfigure
FDwfAnalogInConfigure.argtypes = [HDWF, ctypes.c_byte, ctypes.c_byte]
FDwfAnalogInConfigure.restype = bool

_FDwfAnalogInStatus = _dwf.FDwfAnalogInStatus
_FDwfAnalogInStatus.argtypes = [HDWF, ctypes.c_byte, ctypes.POINTER(DwfState)]
_FDwfAnalogInStatus.restype = bool

def FDwfAnalogInStatus(hdwf, fReadData):
	state = DwfState()
	return (_FDwfAnalogInStatus(hdwf, fReadData, ctypes.byref(state)), state)

_FDwfAnalogInStatusSamplesLeft = _dwf.FDwfAnalogInStatusSamplesLeft
_FDwfAnalogInStatusSamplesLeft.argtypes = [HDWF, _types.c_int_p]
_FDwfAnalogInStatusSamplesLeft.restype = bool

def FDwfAnalogInStatusSamplesLeft(hdwf):
	value = ctypes.c_int()
	return (_FDwfAnalogInStatusSamplesLeft(hdwf, ctypes.byref(value)), value.value)

_FDwfAnalogInStatusSamplesValid = _dwf.FDwfAnalogInStatusSamplesValid
_FDwfAnalogInStatusSamplesValid.argtypes = [HDWF, _types.c_int_p]
_FDwfAnalogInStatusSamplesValid.restype = bool

def FDwfAnalogInStatusSamplesValid(hdwf):
	value = ctypes.c_int()
	return (_FDwfAnalogInStatusSamplesValid(hdwf, ctypes.byref(value)), value.value)

_FDwfAnalogInStatusIndexWrite = _dwf.FDwfAnalogInStatusIndexWrite
_FDwfAnalogInStatusIndexWrite.argtypes = [HDWF, _types.c_int_p]
_FDwfAnalogInStatusIndexWrite.restype = bool

def FDwfAnalogInStatusIndexWrite(hdwf):
	value = ctypes.c_int()
	return (_FDwfAnalogInStatusIndexWrite(hdwf, ctypes.byref(value)), value.value)

_FDwfAnalogInStatusAutoTriggered = _dwf.FDwfAnalogInStatusAutoTriggered
_FDwfAnalogInStatusAutoTriggered.argtypes = [HDWF, _types.c_byte_p]
_FDwfAnalogInStatusAutoTriggered.restype = bool

def FDwfAnalogInStatusAutoTriggered(hdwf):
	value = ctypes.c_byte()
	return (_FDwfAnalogInStatusAutoTriggered(hdwf, ctypes.byref(value)), bool(value.value))

FDwfAnalogInStatusData = _dwf.FDwfAnalogInStatusData
FDwfAnalogInStatusData.argtypes = [HDWF, ctypes.c_int, _types.c_double_p, ctypes.c_int]
FDwfAnalogInStatusData.restype = bool

_FDwfAnalogInStatusSample = _dwf.FDwfAnalogInStatusSample
_FDwfAnalogInStatusSample.argtypes = [HDWF, ctypes.c_int, _types.c_double_p]
_FDwfAnalogInStatusSample.restype = bool

def FDwfAnalogInStatusSample(hdwf, idxChannel):
	value = ctypes.c_double()
	return (_FDwfAnalogInStatusSample(hdwf, idxChannel, ctypes.byref(value)), value.value)


_FDwfAnalogInStatusRecord = _dwf.FDwfAnalogInStatusRecord
_FDwfAnalogInStatusRecord.argtypes = [HDWF, _types.c_int_p, _types.c_int_p, _types.c_int_p]
_FDwfAnalogInStatusRecord.restype = bool

def FDwfAnalogInStatusRecord(hdwf):
	available = ctypes.c_int()
	lost = ctypes.c_int()
	corrupt = ctypes.c_int()
	return (_FDwfAnalogInStatusRecord(hdwf, ctypes.byref(available), ctypes.byref(lost), ctypes.byref(corrupt)), available.value, lost.value, corrupt.value)

FDwfAnalogInRecordLengthSet = _dwf.FDwfAnalogInRecordLengthSet
FDwfAnalogInRecordLengthSet.argtypes = [HDWF, ctypes.c_double]
FDwfAnalogInRecordLengthSet.restype = bool

_FDwfAnalogInRecordLengthGet = _dwf.FDwfAnalogInRecordLengthGet
_FDwfAnalogInRecordLengthGet.argtypes = [HDWF, _types.c_double_p]
_FDwfAnalogInRecordLengthGet.restype = bool

def FDwfAnalogInRecordLengthGet(hdwf):
	value = ctypes.c_double()
	return (_FDwfAnalogInRecordLengthGet(hdwf, ctypes.byref(value)), value.value)


# Acquistion configuration:
_FDwfAnalogInFrequencyInfo = _dwf.FDwfAnalogInFrequencyInfo
_FDwfAnalogInFrequencyInfo.argtypes = [HDWF, _types.c_double_p, _types.c_double_p]
_FDwfAnalogInFrequencyInfo.restype = bool

def FDwfAnalogInFrequencyInfo(hdwf):
	min = ctypes.c_double()
	max = ctypes.c_double()
	return (_FDwfAnalogInFrequencyInfo(hdwf, ctypes.byref(min), ctypes.byref(max)), min.value, max.value)

FDwfAnalogInFrequencySet = _dwf.FDwfAnalogInFrequencySet
FDwfAnalogInFrequencySet.argtypes = [HDWF, ctypes.c_double]
FDwfAnalogInFrequencySet.restype = bool

_FDwfAnalogInFrequencyGet = _dwf.FDwfAnalogInFrequencyGet
_FDwfAnalogInFrequencyGet.argtypes = [HDWF, _types.c_double_p]
_FDwfAnalogInFrequencyGet.restype = bool

def FDwfAnalogInFrequencyGet(hdwf):
	value = ctypes.c_double()
	return (_FDwfAnalogInFrequencyGet(hdwf, ctypes.byref(value)), value.value)


_FDwfAnalogInBitsInfo = _dwf.FDwfAnalogInBitsInfo
_FDwfAnalogInBitsInfo.argtypes = [HDWF, _types.c_int_p]
_FDwfAnalogInBitsInfo.restype = bool

def FDwfAnalogInBitsInfo(hdwf):
	value = ctypes.c_int()
	return (_FDwfAnalogInBitsInfo(hdwf, ctypes.byref(value)), value.value)


_FDwfAnalogInBufferSizeInfo = _dwf.FDwfAnalogInBufferSizeInfo
_FDwfAnalogInBufferSizeInfo.argtypes = [HDWF, _types.c_int_p, _types.c_int_p]
_FDwfAnalogInBufferSizeInfo.restype = bool

def FDwfAnalogInBufferSizeInfo(hdwf):
	min = ctypes.c_int()
	max = ctypes.c_int()
	return (_FDwfAnalogInBufferSizeInfo(hdwf, ctypes.byref(min), ctypes.byref(max)), min.value, max.value)

FDwfAnalogInBufferSizeSet = _dwf.FDwfAnalogInBufferSizeSet
FDwfAnalogInBufferSizeSet.argtypes = [HDWF, ctypes.c_int]
FDwfAnalogInBufferSizeSet.restype = bool

_FDwfAnalogInBufferSizeGet = _dwf.FDwfAnalogInBufferSizeGet
_FDwfAnalogInBufferSizeGet.argtypes = [HDWF, _types.c_int_p]
_FDwfAnalogInBufferSizeGet.restype = bool

def FDwfAnalogInBufferSizeGet(hdwf):
	value = ctypes.c_int()
	return (_FDwfAnalogInBufferSizeGet(hdwf, ctypes.byref(value)), value.value)


_FDwfAnalogInAcquisitionModeInfo = _dwf.FDwfAnalogInAcquisitionModeInfo  # use IsBitSet
_FDwfAnalogInAcquisitionModeInfo.argtypes = [HDWF, _types.c_int_p]
_FDwfAnalogInAcquisitionModeInfo.restype = bool

def FDwfAnalogInAcquisitionModeInfo(hdwf):
	info = ctypes.c_int()
	if not _FDwfAnalogInAcquisitionModeInfo(hdwf, ctypes.byref(info)):
		return (False, [])
	supported = []
	for i in range(8 * ctypes.sizeof(ctypes.c_int)):
		if info.value & (1 << i) != 0:
			supported.append(ACQMODE(i))
	return (True, supported)

FDwfAnalogInAcquisitionModeSet = _dwf.FDwfAnalogInAcquisitionModeSet
FDwfAnalogInAcquisitionModeSet.argtypes = [HDWF, ACQMODE]
FDwfAnalogInAcquisitionModeSet.restype = bool

_FDwfAnalogInAcquisitionModeGet = _dwf.FDwfAnalogInAcquisitionModeGet
_FDwfAnalogInAcquisitionModeGet.argtypes = [HDWF, ctypes.POINTER(ACQMODE)]
_FDwfAnalogInAcquisitionModeGet.restype = bool

def FDwfAnalogInAcquisitionModeGet(hdwf):
	value = ctypes.ACQMODE()
	return (_FDwfAnalogInAcquisitionModeGet(hdwf, ctypes.byref(value)), value)


# Channel configuration:
_FDwfAnalogInChannelCount = _dwf.FDwfAnalogInChannelCount
_FDwfAnalogInChannelCount.argtypes = [HDWF, _types.c_int_p]
_FDwfAnalogInChannelCount.restype = bool

def FDwfAnalogInChannelCount(hdwf):
	value = ctypes.c_int()
	return (_FDwfAnalogInChannelCount(hdwf, ctypes.byref(value)), value.value)

FDwfAnalogInChannelEnableSet = _dwf.FDwfAnalogInChannelEnableSet
FDwfAnalogInChannelEnableSet.argtypes = [HDWF, ctypes.c_int, ctypes.c_byte]
FDwfAnalogInChannelEnableSet.restype = bool

_FDwfAnalogInChannelEnableGet = _dwf.FDwfAnalogInChannelEnableGet
_FDwfAnalogInChannelEnableGet.argtypes = [HDWF, ctypes.c_int, _types.c_byte_p]
_FDwfAnalogInChannelEnableGet.restype = bool

def FDwfAnalogInChannelEnableGet(hdwf, idxChannel):
	value = ctypes.c_byte()
	return (_FDwfAnalogInChannelEnableGet(hdwf, idxChannel, ctypes.byref(value)), bool(value.value))

_FDwfAnalogInChannelFilterInfo = _dwf.FDwfAnalogInChannelFilterInfo  # use IsBitSet
_FDwfAnalogInChannelFilterInfo.argtypes = [HDWF, _types.c_int_p]
_FDwfAnalogInChannelFilterInfo.restype = bool

def FDwfAnalogInChannelFilterInfo(hdwf):
	info = ctypes.c_int()
	if not _FDwfAnalogInChannelFilterInfo(hdwf, ctypes.byref(info)):
		return (False, [])
	supported = []
	for i in range(8 * ctypes.sizeof(ctypes.c_int)):
		if info.value & (1 << i) != 0:
			supported.append(FILTER(i))
	return (True, supported)

FDwfAnalogInChannelFilterSet = _dwf.FDwfAnalogInChannelFilterSet
FDwfAnalogInChannelFilterSet.argtypes = [HDWF, ctypes.c_int, FILTER]
FDwfAnalogInChannelFilterSet.restype = bool

_FDwfAnalogInChannelFilterGet = _dwf.FDwfAnalogInChannelFilterGet
_FDwfAnalogInChannelFilterGet.argtypes = [HDWF, ctypes.c_int, ctypes.POINTER(FILTER)]
_FDwfAnalogInChannelFilterGet.restype = bool

def FDwfAnalogInChannelFilterGet(hdwf, idxChannel):
	value = ctypes.FILTER()
	return (_FDwfAnalogInChannelFilterGet(hdwf, idxChannel, ctypes.byref(value)), value)

_FDwfAnalogInChannelRangeInfo = _dwf.FDwfAnalogInChannelRangeInfo
_FDwfAnalogInChannelRangeInfo.argtypes = [HDWF, _types.c_double_p, _types.c_double_p, _types.c_double_p]
_FDwfAnalogInChannelRangeInfo.restype = bool

def FDwfAnalogInChannelRangeInfo(hdwf):
	val_a = ctypes.c_double()
	val_b = ctypes.c_double()
	val_c = ctypes.c_double()
	return (_FDwfAnalogInChannelRangeInfo(hdwf, ctypes.byref(val_a), ctypes.byref(val_b), ctypes.byref(val_c)), val_a.value, val_b.value, val_c.value)

_FDwfAnalogInChannelRangeSteps = _dwf.FDwfAnalogInChannelRangeSteps
_FDwfAnalogInChannelRangeSteps.argtypes = [HDWF, ctypes.POINTER(ctypes.c_double * 32), _types.c_int_p]
_FDwfAnalogInChannelRangeSteps.restype = bool

def FDwfAnalogInChannelRangeSteps(hdwf):
	steps = (ctypes.c_double * 32)()
	numSteps = ctypes.c_int()
	if not _FDwfAnalogInChannelRangeSteps(hdwf, ctypes.byref(steps), ctypes.byref(numSteps)):
		return (False, [])
	return (True, steps[:numSteps.value])

FDwfAnalogInChannelRangeSet = _dwf.FDwfAnalogInChannelRangeSet
FDwfAnalogInChannelRangeSet.argtypes = [HDWF, ctypes.c_int, ctypes.c_double]
FDwfAnalogInChannelRangeSet.restype = bool

_FDwfAnalogInChannelRangeGet = _dwf.FDwfAnalogInChannelRangeGet
_FDwfAnalogInChannelRangeGet.argtypes = [HDWF, ctypes.c_int, _types.c_double_p]
_FDwfAnalogInChannelRangeGet.restype = bool

def FDwfAnalogInChannelRangeGet(hdwf, idxChannel):
	value = ctypes.c_double()
	return (_FDwfAnalogInChannelRangeGet(hdwf, idxChannel, ctypes.byref(value)), value.value)

_FDwfAnalogInChannelOffsetInfo = _dwf.FDwfAnalogInChannelOffsetInfo
_FDwfAnalogInChannelOffsetInfo.argtypes = [HDWF, _types.c_double_p, _types.c_double_p, _types.c_double_p]
_FDwfAnalogInChannelOffsetInfo.restype = bool

def FDwfAnalogInChannelOffsetInfo(hdwf):
	val_a = ctypes.c_double()
	val_b = ctypes.c_double()
	val_c = ctypes.c_double()
	return (_FDwfAnalogInChannelOffsetInfo(hdwf, ctypes.byref(val_a), ctypes.byref(val_b), ctypes.byref(val_c)), val_a.value, val_b.value, val_c.value)

FDwfAnalogInChannelOffsetSet = _dwf.FDwfAnalogInChannelOffsetSet
FDwfAnalogInChannelOffsetSet.argtypes = [HDWF, ctypes.c_int, ctypes.c_double]
FDwfAnalogInChannelOffsetSet.restype = bool

_FDwfAnalogInChannelOffsetGet = _dwf.FDwfAnalogInChannelOffsetGet
_FDwfAnalogInChannelOffsetGet.argtypes = [HDWF, ctypes.c_int, _types.c_double_p]
_FDwfAnalogInChannelOffsetGet.restype = bool

def FDwfAnalogInChannelOffsetGet(hdwf, idxChannel):
	value = ctypes.c_double()
	return (_FDwfAnalogInChannelOffsetGet(hdwf, idxChannel, ctypes.byref(value)), value.value)


# Trigger configuration:
_FDwfAnalogInTriggerSourceInfo = _dwf.FDwfAnalogInTriggerSourceInfo  # use IsBitSet
_FDwfAnalogInTriggerSourceInfo.argtypes = [HDWF, _types.c_int_p]
_FDwfAnalogInTriggerSourceInfo.restype = bool

def FDwfAnalogInTriggerSourceInfo(hdwf):
	info = ctypes.c_int()
	if not _FDwfAnalogInTriggerSourceInfo(hdwf, ctypes.byref(info)):
		return (False, [])
	supported = []
	for i in range(8 * ctypes.sizeof(ctypes.c_int)):
		if info.value & (1 << i) != 0:
			supported.append(TRIGSRC(i))
	return (True, supported)

FDwfAnalogInTriggerSourceSet = _dwf.FDwfAnalogInTriggerSourceSet
FDwfAnalogInTriggerSourceSet.argtypes = [HDWF, TRIGSRC]
FDwfAnalogInTriggerSourceSet.restype = bool

_FDwfAnalogInTriggerSourceGet = _dwf.FDwfAnalogInTriggerSourceGet
_FDwfAnalogInTriggerSourceGet.argtypes = [HDWF, ctypes.POINTER(TRIGSRC)]
_FDwfAnalogInTriggerSourceGet.restype = bool

def FDwfAnalogInTriggerSourceGet(hdwf):
	value = ctypes.TRIGSRC()
	return (_FDwfAnalogInTriggerSourceGet(hdwf, ctypes.byref(value)), value)


_FDwfAnalogInTriggerPositionInfo = _dwf.FDwfAnalogInTriggerPositionInfo
_FDwfAnalogInTriggerPositionInfo.argtypes = [HDWF, _types.c_double_p, _types.c_double_p, _types.c_double_p]
_FDwfAnalogInTriggerPositionInfo.restype = bool

def FDwfAnalogInTriggerPositionInfo(hdwf):
	val_a = ctypes.c_double()
	val_b = ctypes.c_double()
	val_c = ctypes.c_double()
	return (_FDwfAnalogInTriggerPositionInfo(hdwf, ctypes.byref(val_a), ctypes.byref(val_b), ctypes.byref(val_c)), val_a.value, val_b.value, val_c.value)

FDwfAnalogInTriggerPositionSet = _dwf.FDwfAnalogInTriggerPositionSet
FDwfAnalogInTriggerPositionSet.argtypes = [HDWF, ctypes.c_double]
FDwfAnalogInTriggerPositionSet.restype = bool

_FDwfAnalogInTriggerPositionGet = _dwf.FDwfAnalogInTriggerPositionGet
_FDwfAnalogInTriggerPositionGet.argtypes = [HDWF, _types.c_double_p]
_FDwfAnalogInTriggerPositionGet.restype = bool

def FDwfAnalogInTriggerPositionGet(hdwf):
	value = ctypes.c_double()
	return (_FDwfAnalogInTriggerPositionGet(hdwf, ctypes.byref(value)), value.value)

_FDwfAnalogInTriggerPositionStatus = _dwf.FDwfAnalogInTriggerPositionStatus
_FDwfAnalogInTriggerPositionStatus.argtypes = [HDWF, _types.c_double_p]
_FDwfAnalogInTriggerPositionStatus.restype = bool

def FDwfAnalogInTriggerPositionStatus(hdwf):
	value = ctypes.c_double()
	return (_FDwfAnalogInTriggerPositionStatus(hdwf, ctypes.byref(value)), value.value)


_FDwfAnalogInTriggerAutoTimeoutInfo = _dwf.FDwfAnalogInTriggerAutoTimeoutInfo
_FDwfAnalogInTriggerAutoTimeoutInfo.argtypes = [HDWF, _types.c_double_p, _types.c_double_p, _types.c_double_p]
_FDwfAnalogInTriggerAutoTimeoutInfo.restype = bool

def FDwfAnalogInTriggerAutoTimeoutInfo(hdwf):
	val_a = ctypes.c_double()
	val_b = ctypes.c_double()
	val_c = ctypes.c_double()
	return (_FDwfAnalogInTriggerAutoTimeoutInfo(hdwf, ctypes.byref(val_a), ctypes.byref(val_b), ctypes.byref(val_c)), val_a.value, val_b.value, val_c.value)

FDwfAnalogInTriggerAutoTimeoutSet = _dwf.FDwfAnalogInTriggerAutoTimeoutSet
FDwfAnalogInTriggerAutoTimeoutSet.argtypes = [HDWF, ctypes.c_double]
FDwfAnalogInTriggerAutoTimeoutSet.restype = bool

_FDwfAnalogInTriggerAutoTimeoutGet = _dwf.FDwfAnalogInTriggerAutoTimeoutGet
_FDwfAnalogInTriggerAutoTimeoutGet.argtypes = [HDWF, _types.c_double_p]
_FDwfAnalogInTriggerAutoTimeoutGet.restype = bool

def FDwfAnalogInTriggerAutoTimeoutGet(hdwf):
	value = ctypes.c_double()
	return (_FDwfAnalogInTriggerAutoTimeoutGet(hdwf, ctypes.byref(value)), value.value)


_FDwfAnalogInTriggerHoldOffInfo = _dwf.FDwfAnalogInTriggerHoldOffInfo
_FDwfAnalogInTriggerHoldOffInfo.argtypes = [HDWF, _types.c_double_p, _types.c_double_p, _types.c_double_p]
_FDwfAnalogInTriggerHoldOffInfo.restype = bool

def FDwfAnalogInTriggerHoldOffInfo(hdwf):
	val_a = ctypes.c_double()
	val_b = ctypes.c_double()
	val_c = ctypes.c_double()
	return (_FDwfAnalogInTriggerHoldOffInfo(hdwf, ctypes.byref(val_a), ctypes.byref(val_b), ctypes.byref(val_c)), val_a.value, val_b.value, val_c.value)

FDwfAnalogInTriggerHoldOffSet = _dwf.FDwfAnalogInTriggerHoldOffSet
FDwfAnalogInTriggerHoldOffSet.argtypes = [HDWF, ctypes.c_double]
FDwfAnalogInTriggerHoldOffSet.restype = bool

_FDwfAnalogInTriggerHoldOffGet = _dwf.FDwfAnalogInTriggerHoldOffGet
_FDwfAnalogInTriggerHoldOffGet.argtypes = [HDWF, _types.c_double_p]
_FDwfAnalogInTriggerHoldOffGet.restype = bool

def FDwfAnalogInTriggerHoldOffGet(hdwf):
	value = ctypes.c_double()
	return (_FDwfAnalogInTriggerHoldOffGet(hdwf, ctypes.byref(value)), value.value)


_FDwfAnalogInTriggerTypeInfo = _dwf.FDwfAnalogInTriggerTypeInfo  # use IsBitSet
_FDwfAnalogInTriggerTypeInfo.argtypes = [HDWF, _types.c_int_p]
_FDwfAnalogInTriggerTypeInfo.restype = bool

def FDwfAnalogInTriggerTypeInfo(hdwf):
	info = ctypes.c_int()
	if not _FDwfAnalogInTriggerTypeInfo(hdwf, ctypes.byref(info)):
		return (False, [])
	supported = []
	for i in range(8 * ctypes.sizeof(ctypes.c_int)):
		if info.value & (1 << i) != 0:
			supported.append(TRIGTYPE(i))
	return (True, supported)

FDwfAnalogInTriggerTypeSet = _dwf.FDwfAnalogInTriggerTypeSet
FDwfAnalogInTriggerTypeSet.argtypes = [HDWF, TRIGTYPE]
FDwfAnalogInTriggerTypeSet.restype = bool

_FDwfAnalogInTriggerTypeGet = _dwf.FDwfAnalogInTriggerTypeGet
_FDwfAnalogInTriggerTypeGet.argtypes = [HDWF, ctypes.POINTER(TRIGTYPE)]
_FDwfAnalogInTriggerTypeGet.restype = bool

def FDwfAnalogInTriggerTypeGet(hdwf):
	value = ctypes.TRIGTYPE()
	return (_FDwfAnalogInTriggerTypeGet(hdwf, ctypes.byref(value)), value)


_FDwfAnalogInTriggerChannelInfo = _dwf.FDwfAnalogInTriggerChannelInfo
_FDwfAnalogInTriggerChannelInfo.argtypes = [HDWF, _types.c_int_p, _types.c_int_p]
_FDwfAnalogInTriggerChannelInfo.restype = bool

def FDwfAnalogInTriggerChannelInfo(hdwf):
	min = ctypes.c_int()
	max = ctypes.c_int()
	return (_FDwfAnalogInTriggerChannelInfo(hdwf, ctypes.byref(min), ctypes.byref(max)), min.value, max.value)

FDwfAnalogInTriggerChannelSet = _dwf.FDwfAnalogInTriggerChannelSet
FDwfAnalogInTriggerChannelSet.argtypes = [HDWF, ctypes.c_int]
FDwfAnalogInTriggerChannelSet.restype = bool

_FDwfAnalogInTriggerChannelGet = _dwf.FDwfAnalogInTriggerChannelGet
_FDwfAnalogInTriggerChannelGet.argtypes = [HDWF, _types.c_int_p]
_FDwfAnalogInTriggerChannelGet.restype = bool

def FDwfAnalogInTriggerChannelGet(hdwf):
	value = ctypes.c_int()
	return (_FDwfAnalogInTriggerChannelGet(hdwf, ctypes.byref(value)), value.value)


_FDwfAnalogInTriggerFilterInfo = _dwf.FDwfAnalogInTriggerFilterInfo  # use IsBitSet
_FDwfAnalogInTriggerFilterInfo.argtypes = [HDWF, _types.c_int_p]
_FDwfAnalogInTriggerFilterInfo.restype = bool

def FDwfAnalogInTriggerFilterInfo(hdwf):
	info = ctypes.c_int()
	if not _FDwfAnalogInTriggerFilterInfo(hdwf, ctypes.byref(info)):
		return (False, [])
	supported = []
	for i in range(8 * ctypes.sizeof(ctypes.c_int)):
		if info.value & (1 << i) != 0:
			supported.append(FILTER(i))
	return (True, supported)

FDwfAnalogInTriggerFilterSet = _dwf.FDwfAnalogInTriggerFilterSet
FDwfAnalogInTriggerFilterSet.argtypes = [HDWF, FILTER]
FDwfAnalogInTriggerFilterSet.restype = bool

_FDwfAnalogInTriggerFilterGet = _dwf.FDwfAnalogInTriggerFilterGet
_FDwfAnalogInTriggerFilterGet.argtypes = [HDWF, ctypes.POINTER(FILTER)]
_FDwfAnalogInTriggerFilterGet.restype = bool

def FDwfAnalogInTriggerFilterGet(hdwf):
	value = ctypes.TRIGTYPE()
	return (_FDwfAnalogInTriggerFilterGet(hdwf, ctypes.byref(value)), value)


_FDwfAnalogInTriggerLevelInfo = _dwf.FDwfAnalogInTriggerLevelInfo
_FDwfAnalogInTriggerLevelInfo.argtypes = [HDWF, _types.c_double_p, _types.c_double_p, _types.c_double_p]
_FDwfAnalogInTriggerLevelInfo.restype = bool

def FDwfAnalogInTriggerLevelInfo(hdwf):
	val_a = ctypes.c_double()
	val_b = ctypes.c_double()
	val_c = ctypes.c_double()
	return (_FDwfAnalogInTriggerLevelInfo(hdwf, ctypes.byref(val_a), ctypes.byref(val_b), ctypes.byref(val_c)), val_a.value, val_b.value, val_c.value)

FDwfAnalogInTriggerLevelSet = _dwf.FDwfAnalogInTriggerLevelSet
FDwfAnalogInTriggerLevelSet.argtypes = [HDWF, ctypes.c_double]
FDwfAnalogInTriggerLevelSet.restype = bool

_FDwfAnalogInTriggerLevelGet = _dwf.FDwfAnalogInTriggerLevelGet
_FDwfAnalogInTriggerLevelGet.argtypes = [HDWF, _types.c_double_p]
_FDwfAnalogInTriggerLevelGet.restype = bool

def FDwfAnalogInTriggerLevelGet(hdwf):
	value = ctypes.c_double()
	return (_FDwfAnalogInTriggerLevelGet(hdwf, ctypes.byref(value)), value.value)


_FDwfAnalogInTriggerHysteresisInfo = _dwf.FDwfAnalogInTriggerHysteresisInfo
_FDwfAnalogInTriggerHysteresisInfo.argtypes = [HDWF, _types.c_double_p, _types.c_double_p, _types.c_double_p]
_FDwfAnalogInTriggerHysteresisInfo.restype = bool

def FDwfAnalogInTriggerHysteresisInfo(hdwf):
	val_a = ctypes.c_double()
	val_b = ctypes.c_double()
	val_c = ctypes.c_double()
	return (_FDwfAnalogInTriggerHysteresisInfo(hdwf, ctypes.byref(val_a), ctypes.byref(val_b), ctypes.byref(val_c)), val_a.value, val_b.value, val_c.value)

FDwfAnalogInTriggerHysteresisSet = _dwf.FDwfAnalogInTriggerHysteresisSet
FDwfAnalogInTriggerHysteresisSet.argtypes = [HDWF, ctypes.c_double]
FDwfAnalogInTriggerHysteresisSet.restype = bool

_FDwfAnalogInTriggerHysteresisGet = _dwf.FDwfAnalogInTriggerHysteresisGet
_FDwfAnalogInTriggerHysteresisGet.argtypes = [HDWF, _types.c_double_p]
_FDwfAnalogInTriggerHysteresisGet.restype = bool

def FDwfAnalogInTriggerHysteresisGet(hdwf):
	value = ctypes.c_double()
	return (_FDwfAnalogInTriggerHysteresisGet(hdwf, ctypes.byref(value)), value.value)


_FDwfAnalogInTriggerConditionInfo = _dwf.FDwfAnalogInTriggerConditionInfo  # use IsBitSet
_FDwfAnalogInTriggerConditionInfo.argtypes = [HDWF, _types.c_int_p]
_FDwfAnalogInTriggerConditionInfo.restype = bool

def FDwfAnalogInTriggerConditionInfo(hdwf):
	info = ctypes.c_int()
	if not _FDwfAnalogInTriggerConditionInfo(hdwf, ctypes.byref(info)):
		return (False, [])
	supported = []
	for i in range(8 * ctypes.sizeof(ctypes.c_int)):
		if info.value & (1 << i) != 0:
			supported.append(TRIGCOND(i))
	return (True, supported)

FDwfAnalogInTriggerConditionSet = _dwf.FDwfAnalogInTriggerConditionSet
FDwfAnalogInTriggerConditionSet.argtypes = [HDWF, TRIGCOND]
FDwfAnalogInTriggerConditionSet.restype = bool

_FDwfAnalogInTriggerConditionGet = _dwf.FDwfAnalogInTriggerConditionGet
_FDwfAnalogInTriggerConditionGet.argtypes = [HDWF, ctypes.POINTER(TRIGCOND)]
_FDwfAnalogInTriggerConditionGet.restype = bool

def FDwfAnalogInTriggerConditionGet(hdwf):
	value = ctypes.TRIGCOND()
	return (_FDwfAnalogInTriggerConditionGet(hdwf, ctypes.byref(value)), value)


_FDwfAnalogInTriggerLengthInfo = _dwf.FDwfAnalogInTriggerLengthInfo
_FDwfAnalogInTriggerLengthInfo.argtypes = [HDWF, _types.c_double_p, _types.c_double_p, _types.c_double_p]
_FDwfAnalogInTriggerLengthInfo.restype = bool

def FDwfAnalogInTriggerLengthInfo(hdwf):
	val_a = ctypes.c_double()
	val_b = ctypes.c_double()
	val_c = ctypes.c_double()
	return (_FDwfAnalogInTriggerLengthInfo(hdwf, ctypes.byref(val_a), ctypes.byref(val_b), ctypes.byref(val_c)), val_a.value, val_b.value, val_c.value)

FDwfAnalogInTriggerLengthSet = _dwf.FDwfAnalogInTriggerLengthSet
FDwfAnalogInTriggerLengthSet.argtypes = [HDWF, ctypes.c_double]
FDwfAnalogInTriggerLengthSet.restype = bool

_FDwfAnalogInTriggerLengthGet = _dwf.FDwfAnalogInTriggerLengthGet
_FDwfAnalogInTriggerLengthGet.argtypes = [HDWF, _types.c_double_p]
_FDwfAnalogInTriggerLengthGet.restype = bool

def FDwfAnalogInTriggerLengthGet(hdwf):
	value = ctypes.c_double()
	return (_FDwfAnalogInTriggerLengthGet(hdwf, ctypes.byref(value)), value.value)


_FDwfAnalogInTriggerLengthConditionInfo = _dwf.FDwfAnalogInTriggerLengthConditionInfo  # use IsBitSet
_FDwfAnalogInTriggerLengthConditionInfo.argtypes = [HDWF, _types.c_int_p]
_FDwfAnalogInTriggerLengthConditionInfo.restype = bool

def FDwfAnalogInTriggerLengthConditionInfo(hdwf):
	info = ctypes.c_int()
	if not _FDwfAnalogInTriggerLengthConditionInfo(hdwf, ctypes.byref(info)):
		return (False, [])
	supported = []
	for i in range(8 * ctypes.sizeof(ctypes.c_int)):
		if info.value & (1 << i) != 0:
			supported.append(TRIGLEN(i))
	return (True, supported)

FDwfAnalogInTriggerLengthConditionSet = _dwf.FDwfAnalogInTriggerLengthConditionSet
FDwfAnalogInTriggerLengthConditionSet.argtypes = [HDWF, TRIGLEN]
FDwfAnalogInTriggerLengthConditionSet.restype = bool

_FDwfAnalogInTriggerLengthConditionGet = _dwf.FDwfAnalogInTriggerLengthConditionGet
_FDwfAnalogInTriggerLengthConditionGet.argtypes = [HDWF, ctypes.POINTER(TRIGLEN)]
_FDwfAnalogInTriggerLengthConditionGet.restype = bool

def FDwfAnalogInTriggerLengthConditionGet(hdwf):
	value = ctypes.TRIGLEN()
	return (_FDwfAnalogInTriggerLengthConditionGet(hdwf, ctypes.byref(value)), value)


# ANALOG OUT INSTRUMENT FUNCTIONS
# Configuration:
_FDwfAnalogOutCount = _dwf.FDwfAnalogOutCount
_FDwfAnalogOutCount.argtypes = [HDWF, _types.c_int_p]
_FDwfAnalogOutCount.restype = bool

def FDwfAnalogOutCount(hdwf):
	value = ctypes.c_int()
	return (_FDwfAnalogOutCount(hdwf, ctypes.byref(value)), value.value)


FDwfAnalogOutMasterSet = _dwf.FDwfAnalogOutMasterSet
FDwfAnalogOutMasterSet.argtypes = [HDWF, ctypes.c_int, ctypes.c_int]
FDwfAnalogOutMasterSet.restype = bool

_FDwfAnalogOutMasterGet = _dwf.FDwfAnalogOutMasterGet
_FDwfAnalogOutMasterGet.argtypes = [HDWF, ctypes.c_int, _types.c_int_p]
_FDwfAnalogOutMasterGet.restype = bool

def FDwfAnalogOutMasterGet(hdwf, idxChannel):
	value = ctypes.c_int()
	return (_FDwfAnalogOutMasterGet(hdwf, idxChannel, ctypes.byref(value)), value.value)


_FDwfAnalogOutTriggerSourceInfo = _dwf.FDwfAnalogOutTriggerSourceInfo  # use IsBitSet
_FDwfAnalogOutTriggerSourceInfo.argtypes = [HDWF, ctypes.c_int, _types.c_int_p]
_FDwfAnalogOutTriggerSourceInfo.restype = bool

def FDwfAnalogOutTriggerSourceInfo(hdwf, idxChannel):
	info = ctypes.c_int()
	if not _FDwfAnalogOutTriggerSourceInfo(hdwf, idxChannel, ctypes.byref(info)):
		return (False, [])
	supported = []
	for i in range(8 * ctypes.sizeof(ctypes.c_int)):
		if info.value & (1 << i) != 0:
			supported.append(TRIGSRC(i))
	return (True, supported)

FDwfAnalogOutTriggerSourceSet = _dwf.FDwfAnalogOutTriggerSourceSet
FDwfAnalogOutTriggerSourceSet.argtypes = [HDWF, ctypes.c_int, TRIGSRC]
FDwfAnalogOutTriggerSourceSet.restype = bool

_FDwfAnalogOutTriggerSourceGet = _dwf.FDwfAnalogOutTriggerSourceGet
_FDwfAnalogOutTriggerSourceGet.argtypes = [HDWF, ctypes.c_int, ctypes.POINTER(TRIGSRC)]
_FDwfAnalogOutTriggerSourceGet.restype = bool

def FDwfAnalogOutTriggerSourceGet(hdwf, idxChannel):
	value = TRIGSRC()
	return (_FDwfAnalogOutTriggerSourceGet(hdwf, idxChannel, ctypes.byref(value)), value)


_FDwfAnalogOutRunInfo = _dwf.FDwfAnalogOutRunInfo
_FDwfAnalogOutRunInfo.argtypes = [HDWF, ctypes.c_int, _types.c_double_p, _types.c_double_p]
_FDwfAnalogOutRunInfo.restype = bool

def FDwfAnalogOutRunInfo(hdwf, idxChannel):
	min = ctypes.c_double()
	max = ctypes.c_double()
	return (_FDwfAnalogOutRunInfo(hdwf, idxChannel, ctypes.byref(min), ctypes.byref(max)), min.value, max.value)

FDwfAnalogOutRunSet = _dwf.FDwfAnalogOutRunSet
FDwfAnalogOutRunSet.argtypes = [HDWF, ctypes.c_int, ctypes.c_double]
FDwfAnalogOutRunSet.restype = bool

_FDwfAnalogOutRunGet = _dwf.FDwfAnalogOutRunGet
_FDwfAnalogOutRunGet.argtypes = [HDWF, ctypes.c_int, _types.c_double_p]
_FDwfAnalogOutRunGet.restype = bool

def FDwfAnalogOutRunGet(hdwf, idxChannel):
	value = ctypes.c_double()
	return (_FDwfAnalogOutRunGet(hdwf, idxChannel, ctypes.byref(value)), value.value)

_FDwfAnalogOutRunStatus = _dwf.FDwfAnalogOutRunStatus
_FDwfAnalogOutRunStatus.argtypes = [HDWF, ctypes.c_int, _types.c_double_p]
_FDwfAnalogOutRunStatus.restype = bool

def FDwfAnalogOutRunStatus(hdwf, idxChannel):
	value = ctypes.c_double()
	return (_FDwfAnalogOutRunStatus(hdwf, idxChannel, ctypes.byref(value)), value.value)


_FDwfAnalogOutWaitInfo = _dwf.FDwfAnalogOutWaitInfo
_FDwfAnalogOutWaitInfo.argtypes = [HDWF, ctypes.c_int, _types.c_double_p, _types.c_double_p]
_FDwfAnalogOutWaitInfo.restype = bool

def FDwfAnalogOutWaitInfo(hdwf, idxChannel):
	min = ctypes.c_double()
	max = ctypes.c_double()
	return (_FDwfAnalogOutWaitInfo(hdwf, idxChannel, ctypes.byref(min), ctypes.byref(max)), min.value, max.value)

FDwfAnalogOutWaitSet = _dwf.FDwfAnalogOutWaitSet
FDwfAnalogOutWaitSet.argtypes = [HDWF, ctypes.c_int, ctypes.c_double]
FDwfAnalogOutWaitSet.restype = bool

_FDwfAnalogOutWaitGet = _dwf.FDwfAnalogOutWaitGet
_FDwfAnalogOutWaitGet.argtypes = [HDWF, ctypes.c_int, _types.c_double_p]
_FDwfAnalogOutWaitGet.restype = bool

def FDwfAnalogOutWaitGet(hdwf, idxChannel):
	value = ctypes.c_double()
	return (_FDwfAnalogOutWaitGet(hdwf, idxChannel, ctypes.byref(value)), value.value)


_FDwfAnalogOutRepeatInfo = _dwf.FDwfAnalogOutRepeatInfo
_FDwfAnalogOutRepeatInfo.argtypes = [HDWF, ctypes.c_int, _types.c_int_p, _types.c_int_p]
_FDwfAnalogOutRepeatInfo.restype = bool

def FDwfAnalogOutRepeatInfo(hdwf, idxChannel):
	min = ctypes.c_double()
	max = ctypes.c_double()
	return (_FDwfAnalogOutRepeatInfo(hdwf, idxChannel, ctypes.byref(min), ctypes.byref(max)), min.value, max.value)

FDwfAnalogOutRepeatSet = _dwf.FDwfAnalogOutRepeatSet
FDwfAnalogOutRepeatSet.argtypes = [HDWF, ctypes.c_int, ctypes.c_int]
FDwfAnalogOutRepeatSet.restype = bool

_FDwfAnalogOutRepeatGet = _dwf.FDwfAnalogOutRepeatGet
_FDwfAnalogOutRepeatGet.argtypes = [HDWF, ctypes.c_int, _types.c_int_p]
_FDwfAnalogOutRepeatGet.restype = bool

def FDwfAnalogOutRepeatGet(hdwf, idxChannel):
	value = ctypes.c_int()
	return (_FDwfAnalogOutRepeatGet(hdwf, idxChannel, ctypes.byref(value)), value.value)

_FDwfAnalogOutRepeatStatus = _dwf.FDwfAnalogOutRepeatStatus
_FDwfAnalogOutRepeatStatus.argtypes = [HDWF, ctypes.c_int, _types.c_int_p]
_FDwfAnalogOutRepeatStatus.restype = bool

def FDwfAnalogOutRepeatStatus(hdwf, idxChannel):
	value = ctypes.c_int()
	return (_FDwfAnalogOutRepeatStatus(hdwf, idxChannel, ctypes.byref(value)), value.value)


FDwfAnalogOutRepeatTriggerSet = _dwf.FDwfAnalogOutRepeatTriggerSet
FDwfAnalogOutRepeatTriggerSet.argtypes = [HDWF, ctypes.c_int, ctypes.c_byte]
FDwfAnalogOutRepeatTriggerSet.restype = bool

_FDwfAnalogOutRepeatTriggerGet = _dwf.FDwfAnalogOutRepeatTriggerGet
_FDwfAnalogOutRepeatTriggerGet.argtypes = [HDWF, ctypes.c_int, _types.c_byte_p]
_FDwfAnalogOutRepeatTriggerGet.restype = bool

def FDwfAnalogOutRepeatTriggerGet(hdwf, idxChannel):
	value = ctypes.c_byte()
	return (_FDwfAnalogOutRepeatTriggerGet(hdwf, idxChannel, ctypes.byref(value)), bool(value.value))


_FDwfAnalogOutNodeInfo = _dwf.FDwfAnalogOutNodeInfo  # use IsBitSet
_FDwfAnalogOutNodeInfo.argtypes = [HDWF, ctypes.c_int, _types.c_int_p]
_FDwfAnalogOutNodeInfo.restype = bool

def FDwfAnalogOutNodeInfo(hdwf, idxChannel):
	info = ctypes.c_int()
	if not _FDwfAnalogOutNodeInfo(hdwf, idxChannel, ctypes.byref(info)):
		return (False, [])
	supported = []
	for i in range(8 * ctypes.sizeof(ctypes.c_int)):
		if info.value & (1 << i) != 0:
			supported.append(AnalogOutNode(i))
	return (True, supported)


FDwfAnalogOutNodeEnableSet = _dwf.FDwfAnalogOutNodeEnableSet
FDwfAnalogOutNodeEnableSet.argtypes = [HDWF, ctypes.c_int, AnalogOutNode, ctypes.c_byte]
FDwfAnalogOutNodeEnableSet.restype = bool

_FDwfAnalogOutNodeEnableGet = _dwf.FDwfAnalogOutNodeEnableGet
_FDwfAnalogOutNodeEnableGet.argtypes = [HDWF, ctypes.c_int, AnalogOutNode, _types.c_byte_p]
_FDwfAnalogOutNodeEnableGet.restype = bool

def FDwfAnalogOutNodeEnableGet(hdwf, idxChannel, node):
	value = ctypes.c_byte()
	return (_FDwfAnalogOutNodeEnableGet(hdwf, idxChannel, node, ctypes.byref(value)), value.value)


_FDwfAnalogOutNodeFunctionInfo = _dwf.FDwfAnalogOutNodeFunctionInfo  # use IsBitSet
_FDwfAnalogOutNodeFunctionInfo.argtypes = [HDWF, ctypes.c_int, AnalogOutNode, _types.c_int_p]
_FDwfAnalogOutNodeFunctionInfo.restype = bool

def FDwfAnalogOutNodeFunctionInfo(hdwf, idxChannel):
	info = ctypes.c_int()
	if not _FDwfAnalogOutNodeFunctionInfo(hdwf, idxChannel, ctypes.byref(info)):
		return (False, [])
	supported = []
	for i in range(8 * ctypes.sizeof(ctypes.c_int)):
		if info.value & (1 << i) != 0:
			supported.append(FUNC(i))
	return (True, supported)

FDwfAnalogOutNodeFunctionSet = _dwf.FDwfAnalogOutNodeFunctionSet
FDwfAnalogOutNodeFunctionSet.argtypes = [HDWF, ctypes.c_int, AnalogOutNode, FUNC]
FDwfAnalogOutNodeFunctionSet.restype = bool

_FDwfAnalogOutNodeFunctionGet = _dwf.FDwfAnalogOutNodeFunctionGet
_FDwfAnalogOutNodeFunctionGet.argtypes = [HDWF, ctypes.c_int, AnalogOutNode, ctypes.POINTER(FUNC)]
_FDwfAnalogOutNodeFunctionGet.restype = bool

def FDwfAnalogOutNodeFunctionGet(hdwf, idxChannel, node):
	value = FUNC()
	return (_FDwfAnalogOutNodeFunctionGet(hdwf, idxChannel, node, ctypes.byref(value)), value)


_FDwfAnalogOutNodeFrequencyInfo = _dwf.FDwfAnalogOutNodeFrequencyInfo
_FDwfAnalogOutNodeFrequencyInfo.argtypes = [HDWF, ctypes.c_int, AnalogOutNode, _types.c_double_p, _types.c_double_p]
_FDwfAnalogOutNodeFrequencyInfo.restype = bool

def FDwfAnalogOutNodeFrequencyInfo(hdwf, idxChannel, node):
	min = ctypes.c_double()
	max = ctypes.c_double()
	return (_FDwfAnalogOutNodeFrequencyInfo(hdwf, idxChannel, node, ctypes.byref(min), ctypes.byref(max)), min.value, max.value)

FDwfAnalogOutNodeFrequencySet = _dwf.FDwfAnalogOutNodeFrequencySet
FDwfAnalogOutNodeFrequencySet.argtypes = [HDWF, ctypes.c_int, AnalogOutNode, ctypes.c_double]
FDwfAnalogOutNodeFrequencySet.restype = bool

_FDwfAnalogOutNodeFrequencyGet = _dwf.FDwfAnalogOutNodeFrequencyGet
_FDwfAnalogOutNodeFrequencyGet.argtypes = [HDWF, ctypes.c_int, AnalogOutNode, _types.c_double_p]
_FDwfAnalogOutNodeFrequencyGet.restype = bool

def FDwfAnalogOutNodeFrequencyGet(hdwf, idxChannel, node):
	value = ctypes.c_double()
	return (_FDwfAnalogOutNodeFrequencyGet(hdwf, idxChannel, node, ctypes.byref(value)), value.value)

# Carrier Amplitude or Modulation Index
_FDwfAnalogOutNodeAmplitudeInfo = _dwf.FDwfAnalogOutNodeAmplitudeInfo
_FDwfAnalogOutNodeAmplitudeInfo.argtypes = [HDWF, ctypes.c_int, AnalogOutNode, _types.c_double_p, _types.c_double_p]
_FDwfAnalogOutNodeAmplitudeInfo.restype = bool

def FDwfAnalogOutNodeAmplitudeInfo(hdwf, idxChannel, node):
	min = ctypes.c_double()
	max = ctypes.c_double()
	return (_FDwfAnalogOutNodeAmplitudeInfo(hdwf, idxChannel, node, ctypes.byref(min), ctypes.byref(max)), min.value, max.value)

FDwfAnalogOutNodeAmplitudeSet = _dwf.FDwfAnalogOutNodeAmplitudeSet
FDwfAnalogOutNodeAmplitudeSet.argtypes = [HDWF, ctypes.c_int, AnalogOutNode, ctypes.c_double]
FDwfAnalogOutNodeAmplitudeSet.restype = bool

_FDwfAnalogOutNodeAmplitudeGet = _dwf.FDwfAnalogOutNodeAmplitudeGet
_FDwfAnalogOutNodeAmplitudeGet.argtypes = [HDWF, ctypes.c_int, AnalogOutNode, _types.c_double_p]
_FDwfAnalogOutNodeAmplitudeGet.restype = bool

def FDwfAnalogOutNodeAmplitudeGet(hdwf, idxChannel, node):
	value = ctypes.c_double()
	return (_FDwfAnalogOutNodeAmplitudeGet(hdwf, idxChannel, node, ctypes.byref(value)), value.value)


_FDwfAnalogOutNodeOffsetInfo = _dwf.FDwfAnalogOutNodeOffsetInfo
_FDwfAnalogOutNodeOffsetInfo.argtypes = [HDWF, ctypes.c_int, AnalogOutNode, _types.c_double_p, _types.c_double_p]
_FDwfAnalogOutNodeOffsetInfo.restype = bool

def FDwfAnalogOutNodeOffsetInfo(hdwf, idxChannel, node):
	min = ctypes.c_double()
	max = ctypes.c_double()
	return (_FDwfAnalogOutNodeOffsetInfo(hdwf, idxChannel, node, ctypes.byref(min), ctypes.byref(max)), min.value, max.value)

FDwfAnalogOutNodeOffsetSet = _dwf.FDwfAnalogOutNodeOffsetSet
FDwfAnalogOutNodeOffsetSet.argtypes = [HDWF, ctypes.c_int, AnalogOutNode, ctypes.c_double]
FDwfAnalogOutNodeOffsetSet.restype = bool

_FDwfAnalogOutNodeOffsetGet = _dwf.FDwfAnalogOutNodeOffsetGet
_FDwfAnalogOutNodeOffsetGet.argtypes = [HDWF, ctypes.c_int, AnalogOutNode, _types.c_double_p]
_FDwfAnalogOutNodeOffsetGet.restype = bool

def FDwfAnalogOutNodeOffsetGet(hdwf, idxChannel, node):
	value = ctypes.c_double()
	return (_FDwfAnalogOutNodeOffsetGet(hdwf, idxChannel, node, ctypes.byref(value)), value.value)


_FDwfAnalogOutNodeSymmetryInfo = _dwf.FDwfAnalogOutNodeSymmetryInfo
_FDwfAnalogOutNodeSymmetryInfo.argtypes = [HDWF, ctypes.c_int, AnalogOutNode, _types.c_double_p, _types.c_double_p]
_FDwfAnalogOutNodeSymmetryInfo.restype = bool

def FDwfAnalogOutNodeSymmetryInfo(hdwf, idxChannel, node):
	min = ctypes.c_double()
	max = ctypes.c_double()
	return (_FDwfAnalogOutNodeSymmetryInfo(hdwf, idxChannel, node, ctypes.byref(min), ctypes.byref(max)), min.value, max.value)

FDwfAnalogOutNodeSymmetrySet = _dwf.FDwfAnalogOutNodeSymmetrySet
FDwfAnalogOutNodeSymmetrySet.argtypes = [HDWF, ctypes.c_int, AnalogOutNode, ctypes.c_double]
FDwfAnalogOutNodeSymmetrySet.restype = bool

_FDwfAnalogOutNodeSymmetryGet = _dwf.FDwfAnalogOutNodeSymmetryGet
_FDwfAnalogOutNodeSymmetryGet.argtypes = [HDWF, ctypes.c_int, AnalogOutNode, _types.c_double_p]
_FDwfAnalogOutNodeSymmetryGet.restype = bool

def FDwfAnalogOutNodeSymmetryGet(hdwf, idxChannel, node):
	value = ctypes.c_double()
	return (_FDwfAnalogOutNodeSymmetryGet(hdwf, idxChannel, node, ctypes.byref(value)), value.value)


_FDwfAnalogOutNodePhaseInfo = _dwf.FDwfAnalogOutNodePhaseInfo
_FDwfAnalogOutNodePhaseInfo.argtypes = [HDWF, ctypes.c_int, AnalogOutNode, _types.c_double_p, _types.c_double_p]
_FDwfAnalogOutNodePhaseInfo.restype = bool

def FDwfAnalogOutNodePhaseInfo(hdwf, idxChannel, node):
	min = ctypes.c_double()
	max = ctypes.c_double()
	return (_FDwfAnalogOutNodePhaseInfo(hdwf, idxChannel, node, ctypes.byref(min), ctypes.byref(max)), min.value, max.value)

FDwfAnalogOutNodePhaseSet = _dwf.FDwfAnalogOutNodePhaseSet
FDwfAnalogOutNodePhaseSet.argtypes = [HDWF, ctypes.c_int, AnalogOutNode, ctypes.c_double]
FDwfAnalogOutNodePhaseSet.restype = bool

_FDwfAnalogOutNodePhaseGet = _dwf.FDwfAnalogOutNodePhaseGet
_FDwfAnalogOutNodePhaseGet.argtypes = [HDWF, ctypes.c_int, AnalogOutNode, _types.c_double_p]
_FDwfAnalogOutNodePhaseGet.restype = bool

def FDwfAnalogOutNodePhaseGet(hdwf, idxChannel, node):
	value = ctypes.c_double()
	return (_FDwfAnalogOutNodePhaseGet(hdwf, idxChannel, node, ctypes.byref(value)), value.value)


_FDwfAnalogOutNodeDataInfo = _dwf.FDwfAnalogOutNodeDataInfo
_FDwfAnalogOutNodeDataInfo.argtypes = [HDWF, ctypes.c_int, AnalogOutNode, _types.c_int_p, _types.c_int_p]
_FDwfAnalogOutNodeDataInfo.restype = bool

def FDwfAnalogOutNodeDataInfo(hdwf, idxChannel, node):
	min = ctypes.c_int()
	max = ctypes.c_int()
	return (_FDwfAnalogOutNodeDataInfo(hdwf, idxChannel, node, ctypes.byref(min), ctypes.byref(max)), min.value, max.value)

FDwfAnalogOutNodeDataSet = _dwf.FDwfAnalogOutNodeDataSet
FDwfAnalogOutNodeDataSet.argtypes = [HDWF, ctypes.c_int, AnalogOutNode, _types.c_double_p, ctypes.c_int]
FDwfAnalogOutNodeDataSet.restype = bool


# needed for EExplorer, don't care for ADiscovery
FDwfAnalogOutCustomAMFMEnableSet = _dwf.FDwfAnalogOutCustomAMFMEnableSet
FDwfAnalogOutCustomAMFMEnableSet.argtypes = [HDWF, ctypes.c_int, ctypes.c_byte]
FDwfAnalogOutCustomAMFMEnableSet.restype = bool

_FDwfAnalogOutCustomAMFMEnableGet = _dwf.FDwfAnalogOutCustomAMFMEnableGet
_FDwfAnalogOutCustomAMFMEnableGet.argtypes = [HDWF, ctypes.c_int, _types.c_byte_p]
_FDwfAnalogOutCustomAMFMEnableGet.restype = bool

def FDwfAnalogOutCustomAMFMEnableGet(hdwf, idxChannel):
	value = ctypes.c_byte()
	return (_FDwfAnalogOutCustomAMFMEnableGet(hdwf, idxChannel, ctypes.byref(value)), bool(value.value))


# Control:
FDwfAnalogOutReset = _dwf.FDwfAnalogOutReset
FDwfAnalogOutReset.argtypes = [HDWF, ctypes.c_int]
FDwfAnalogOutReset.restype = bool

FDwfAnalogOutConfigure = _dwf.FDwfAnalogOutConfigure
FDwfAnalogOutConfigure.argtypes = [HDWF, ctypes.c_int, ctypes.c_byte]
FDwfAnalogOutConfigure.restype = bool

_FDwfAnalogOutStatus = _dwf.FDwfAnalogOutStatus
_FDwfAnalogOutStatus.argtypes = [HDWF, ctypes.c_int, ctypes.POINTER(DwfState)]
_FDwfAnalogOutStatus.restype = bool

def FDwfAnalogOutStatus(hdwf, idxChannel):
	value = DwfState()
	return (_FDwfAnalogOutStatus(hdwf, idxChannel, ctypes.byref(value)), value)

_FDwfAnalogOutNodePlayStatus = _dwf.FDwfAnalogOutNodePlayStatus
_FDwfAnalogOutNodePlayStatus.argtypes = [HDWF, ctypes.c_int, AnalogOutNode, _types.c_int_p, _types.c_int_p, _types.c_int_p]
_FDwfAnalogOutNodePlayStatus.restype = bool

def FDwfAnalogOutNodePlayStatus(hdwf, idxChannel, node):
	val_a = ctypes.c_int()
	val_b = ctypes.c_int()
	val_c = ctypes.c_int()
	return (_FDwfAnalogOutNodePlayStatus(hdwf, idxChannel, node, ctypes.byref(val_a), ctypes.byref(val_b), ctypes.byref(val_c)), val_a.value, val_b.value, val_c.value)

FDwfAnalogOutNodePlayData = _dwf.FDwfAnalogOutNodePlayData
FDwfAnalogOutNodePlayData.argtypes = [HDWF, ctypes.c_int, AnalogOutNode, _types.c_double_p, ctypes.c_int]
FDwfAnalogOutNodePlayData.restype = bool



# ANALOG IO INSTRUMENT FUNCTIONS
# Control:
FDwfAnalogIOReset = _dwf.FDwfAnalogIOReset
FDwfAnalogIOReset.argtypes = [HDWF]
FDwfAnalogIOReset.restype = bool

FDwfAnalogIOConfigure = _dwf.FDwfAnalogIOConfigure
FDwfAnalogIOConfigure.argtypes = [HDWF]
FDwfAnalogIOConfigure.restype = bool

FDwfAnalogIOStatus = _dwf.FDwfAnalogIOStatus
FDwfAnalogIOStatus.argtypes = [HDWF]
FDwfAnalogIOStatus.restype = bool


# Configure:
_FDwfAnalogIOEnableInfo = _dwf.FDwfAnalogIOEnableInfo
_FDwfAnalogIOEnableInfo.argtypes = [HDWF, _types.c_byte_p, _types.c_byte_p]
_FDwfAnalogIOEnableInfo.restype = bool

def FDwfAnalogIOEnableInfo(hdwf):
	val_a = ctypes.c_byte()
	val_b = ctypes.c_byte()
	return (_FDwfAnalogIOEnableInfo(hdwf, ctypes.byref(val_a), ctypes.byref(val_b)), bool(val_a.value), bool(val_b.value))

FDwfAnalogIOEnableSet = _dwf.FDwfAnalogIOEnableSet
FDwfAnalogIOEnableSet.argtypes = [HDWF, ctypes.c_byte]
FDwfAnalogIOEnableSet.restype = bool

_FDwfAnalogIOEnableGet = _dwf.FDwfAnalogIOEnableGet
_FDwfAnalogIOEnableGet.argtypes = [HDWF, _types.c_byte_p]
_FDwfAnalogIOEnableGet.restype = bool

def FDwfAnalogIOEnableGet(hdwf):
	value = ctypes.c_byte()
	return (_FDwfAnalogIOEnableGet(hdwf, ctypes.byref(value)), bool(value.value))

_FDwfAnalogIOEnableStatus = _dwf.FDwfAnalogIOEnableStatus
_FDwfAnalogIOEnableStatus.argtypes = [HDWF, _types.c_byte_p]
_FDwfAnalogIOEnableStatus.restype = bool

def FDwfAnalogIOEnableStatus(hdwf):
	value = ctypes.c_byte()
	return (_FDwfAnalogIOEnableStatus(hdwf, ctypes.byref(value)), bool(value.value))

_FDwfAnalogIOChannelCount = _dwf.FDwfAnalogIOChannelCount
_FDwfAnalogIOChannelCount.argtypes = [HDWF, _types.c_int_p]
_FDwfAnalogIOChannelCount.restype = bool

def FDwfAnalogIOChannelCount(hdwf):
	value = ctypes.c_int()
	return (_FDwfAnalogIOChannelCount(hdwf, ctypes.byref(value)), value.value)

_FDwfAnalogIOChannelName = _dwf.FDwfAnalogIOChannelName
_FDwfAnalogIOChannelName.argtypes = [HDWF, ctypes.c_int, ctypes.POINTER(ctypes.c_char * 32), ctypes.POINTER(ctypes.c_char * 16)]
_FDwfAnalogIOChannelName.restype = bool

def FDwfAnalogIOChannelName(hdwf, idxChannel):
	val_a = ctypes.create_string_buffer(32)
	val_b = ctypes.create_string_buffer(16)
	return (_FDwfAnalogIOChannelName(hdwf, idxChannel, ctypes.byref(val_a), ctypes.byref(val_b)), val_a.value, val_b.value)

_FDwfAnalogIOChannelInfo = _dwf.FDwfAnalogIOChannelInfo
_FDwfAnalogIOChannelInfo.argtypes = [HDWF, ctypes.c_int, _types.c_int_p]
_FDwfAnalogIOChannelInfo.restype = bool

def FDwfAnalogIOChannelInfo(hdwf, idxChannel):
	value = ctypes.c_int()
	return (_FDwfAnalogIOChannelInfo(hdwf, idxChannel, ctypes.byref(value)), value.value)

_FDwfAnalogIOChannelNodeName = _dwf.FDwfAnalogIOChannelNodeName
_FDwfAnalogIOChannelNodeName.argtypes = [HDWF, ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.c_char * 32), ctypes.POINTER(ctypes.c_char * 16)]
_FDwfAnalogIOChannelNodeName.restype = bool

def FDwfAnalogIOChannelNodeName(hdwf, idxChannel, idxNode):
	val_a = ctypes.create_string_buffer(32)
	val_b = ctypes.create_string_buffer(16)
	return (_FDwfAnalogIOChannelNodeName(hdwf, idxChannel, idxNode, ctypes.byref(val_a), ctypes.byref(val_b)), val_a.value, val_b.value)

_FDwfAnalogIOChannelNodeInfo = _dwf.FDwfAnalogIOChannelNodeInfo
_FDwfAnalogIOChannelNodeInfo.argtypes = [HDWF, ctypes.c_int, ctypes.c_int, ctypes.POINTER(ANALOGIO)]
_FDwfAnalogIOChannelNodeInfo.restype = bool

def FDwfAnalogIOChannelNodeInfo(hdwf, idxChannel, idxNode):
	value = ANALOGIO()
	return (_FDwfAnalogIOChannelNodeInfo(hdwf, idxChannel, idxNode, ctypes.byref(value)), value)

_FDwfAnalogIOChannelNodeSetInfo = _dwf.FDwfAnalogIOChannelNodeSetInfo
_FDwfAnalogIOChannelNodeSetInfo.argtypes = [HDWF, ctypes.c_int, ctypes.c_int, _types.c_double_p, _types.c_double_p, _types.c_int_p]
_FDwfAnalogIOChannelNodeSetInfo.restype = bool

def FDwfAnalogIOChannelNodeSetInfo(hdwf, idxChannel, idxNode):
	val_a = ctypes.c_double()
	val_b = ctypes.c_double()
	val_c = ctypes.c_int()
	return (_FDwfAnalogIOChannelNodeSetInfo(hdwf, idxChannel, idxNode, ctypes.byref(val_a), ctypes.byref(val_b), ctypes.byref(val_c)), val_a.value, val_b.value, val_c.value)

FDwfAnalogIOChannelNodeSet = _dwf.FDwfAnalogIOChannelNodeSet
FDwfAnalogIOChannelNodeSet.argtypes = [HDWF, ctypes.c_int, ctypes.c_int, ctypes.c_double]
FDwfAnalogIOChannelNodeSet.restype = bool

_FDwfAnalogIOChannelNodeGet = _dwf.FDwfAnalogIOChannelNodeGet
_FDwfAnalogIOChannelNodeGet.argtypes = [HDWF, ctypes.c_int, ctypes.c_int, _types.c_double_p]
_FDwfAnalogIOChannelNodeGet.restype = bool

def FDwfAnalogIOChannelNodeGet(hdwf, idxChannel, idxNode):
	value = ctypes.c_double()
	return (_FDwfAnalogIOChannelNodeGet(hdwf, idxChannel, idxNode, ctypes.byref(value)), value.value)

_FDwfAnalogIOChannelNodeStatusInfo = _dwf.FDwfAnalogIOChannelNodeStatusInfo
_FDwfAnalogIOChannelNodeStatusInfo.argtypes = [HDWF, ctypes.c_int, ctypes.c_int, _types.c_double_p, _types.c_double_p, _types.c_int_p]
_FDwfAnalogIOChannelNodeStatusInfo.restype = bool

def FDwfAnalogIOChannelNodeStatusInfo(hdwf, idxChannel, idxNode):
	val_a = ctypes.c_double()
	val_b = ctypes.c_double()
	val_c = ctypes.c_int()
	return (_FDwfAnalogIOChannelNodeStatusInfo(hdwf, idxChannel, idxNode, ctypes.byref(val_a), ctypes.byref(val_b), ctypes.byref(val_c)), val_a.value, val_b.value, val_c.value)

_FDwfAnalogIOChannelNodeStatus = _dwf.FDwfAnalogIOChannelNodeStatus
_FDwfAnalogIOChannelNodeStatus.argtypes = [HDWF, ctypes.c_int, ctypes.c_int, _types.c_double_p]
_FDwfAnalogIOChannelNodeStatus.restype = bool

def FDwfAnalogIOChannelNodeStatus(hdwf, idxChannel, idxNode):
	value = ctypes.c_double()
	return (_FDwfAnalogIOChannelNodeStatus(hdwf, idxChannel, idxNode, ctypes.byref(value)), value.value)



# DIGITAL IO INSTRUMENT FUNCTIONS
# Control:
FDwfDigitalIOReset = _dwf.FDwfDigitalIOReset
FDwfDigitalIOReset.argtypes = [HDWF]
FDwfDigitalIOReset.restype = bool

FDwfDigitalIOConfigure = _dwf.FDwfDigitalIOConfigure
FDwfDigitalIOConfigure.argtypes = [HDWF]
FDwfDigitalIOConfigure.restype = bool

FDwfDigitalIOStatus = _dwf.FDwfDigitalIOStatus
FDwfDigitalIOStatus.argtypes = [HDWF]
FDwfDigitalIOStatus.restype = bool


# Configure:
_FDwfDigitalIOOutputEnableInfo = _dwf.FDwfDigitalIOOutputEnableInfo
_FDwfDigitalIOOutputEnableInfo.argtypes = [HDWF, _types.c_uint_p]
_FDwfDigitalIOOutputEnableInfo.restype = bool

def FDwfDigitalIOOutputEnableInfo(hdwf):
	value = ctypes.c_uint()
	return (_FDwfDigitalIOOutputEnableInfo(hdwf, ctypes.byref(value)), value.value)

FDwfDigitalIOOutputEnableSet = _dwf.FDwfDigitalIOOutputEnableSet
FDwfDigitalIOOutputEnableSet.argtypes = [HDWF, ctypes.c_uint]
FDwfDigitalIOOutputEnableSet.restype = bool

_FDwfDigitalIOOutputEnableGet = _dwf.FDwfDigitalIOOutputEnableGet
_FDwfDigitalIOOutputEnableGet.argtypes = [HDWF, _types.c_uint_p]
_FDwfDigitalIOOutputEnableGet.restype = bool

def FDwfDigitalIOOutputEnableGet(hdwf):
	value = ctypes.c_uint()
	return (_FDwfDigitalIOOutputEnableGet(hdwf, ctypes.byref(value)), value.value)

_FDwfDigitalIOOutputInfo = _dwf.FDwfDigitalIOOutputInfo
_FDwfDigitalIOOutputInfo.argtypes = [HDWF, _types.c_uint_p]
_FDwfDigitalIOOutputInfo.restype = bool

def FDwfDigitalIOOutputInfo(hdwf):
	value = ctypes.c_uint()
	return (_FDwfDigitalIOOutputInfo(hdwf, ctypes.byref(value)), value.value)

FDwfDigitalIOOutputSet = _dwf.FDwfDigitalIOOutputSet
FDwfDigitalIOOutputSet.argtypes = [HDWF, ctypes.c_uint]
FDwfDigitalIOOutputSet.restype = bool

_FDwfDigitalIOOutputGet = _dwf.FDwfDigitalIOOutputGet
_FDwfDigitalIOOutputGet.argtypes = [HDWF, _types.c_uint_p]
_FDwfDigitalIOOutputGet.restype = bool

def FDwfDigitalIOOutputGet(hdwf):
	value = ctypes.c_uint()
	return (_FDwfDigitalIOOutputGet(hdwf, ctypes.byref(value)), value.value)

_FDwfDigitalIOInputInfo = _dwf.FDwfDigitalIOInputInfo
_FDwfDigitalIOInputInfo.argtypes = [HDWF, _types.c_uint_p]
_FDwfDigitalIOInputInfo.restype = bool

def FDwfDigitalIOInputInfo(hdwf):
	value = ctypes.c_uint()
	return (_FDwfDigitalIOInputInfo(hdwf, ctypes.byref(value)), value.value)

_FDwfDigitalIOInputStatus = _dwf.FDwfDigitalIOInputStatus
_FDwfDigitalIOInputStatus.argtypes = [HDWF, _types.c_uint_p]
_FDwfDigitalIOInputStatus.restype = bool

def FDwfDigitalIOInputStatus(hdwf):
	value = ctypes.c_uint()
	return (_FDwfDigitalIOInputStatus(hdwf, ctypes.byref(value)), value.value)



# DIGITAL IN INSTRUMENT FUNCTIONS
# Control and status:
FDwfDigitalInReset = _dwf.FDwfDigitalInReset
FDwfDigitalInReset.argtypes = [HDWF]
FDwfDigitalInReset.restype = bool

FDwfDigitalInConfigure = _dwf.FDwfDigitalInConfigure
FDwfDigitalInConfigure.argtypes = [HDWF, ctypes.c_byte, ctypes.c_byte]
FDwfDigitalInConfigure.restype = bool

_FDwfDigitalInStatus = _dwf.FDwfDigitalInStatus
_FDwfDigitalInStatus.argtypes = [HDWF, ctypes.c_byte, ctypes.POINTER(DwfState)]
_FDwfDigitalInStatus.restype = bool

def FDwfDigitalInStatus(hdwf, fReadData):
	value = DwfState()
	return (_FDwfDigitalInStatus(hdwf, ctypes.byref(value)), value)

_FDwfDigitalInStatusSamplesLeft = _dwf.FDwfDigitalInStatusSamplesLeft
_FDwfDigitalInStatusSamplesLeft.argtypes = [HDWF, _types.c_int_p]
_FDwfDigitalInStatusSamplesLeft.restype = bool

def FDwfDigitalInStatusSamplesLeft(hdwf):
	value = ctypes.c_int()
	return (_FDwfDigitalInStatusSamplesLeft(hdwf, ctypes.byref(value)), value.value)

_FDwfDigitalInStatusSamplesValid = _dwf.FDwfDigitalInStatusSamplesValid
_FDwfDigitalInStatusSamplesValid.argtypes = [HDWF, _types.c_int_p]
_FDwfDigitalInStatusSamplesValid.restype = bool

def FDwfDigitalInStatusSamplesValid(hdwf):
	value = ctypes.c_int()
	return (_FDwfDigitalInStatusSamplesValid(hdwf, ctypes.byref(value)), value.value)

_FDwfDigitalInStatusIndexWrite = _dwf.FDwfDigitalInStatusIndexWrite
_FDwfDigitalInStatusIndexWrite.argtypes = [HDWF, _types.c_int_p]
_FDwfDigitalInStatusIndexWrite.restype = bool

def FDwfDigitalInStatusIndexWrite(hdwf):
	value = ctypes.c_int()
	return (_FDwfDigitalInStatusIndexWrite(hdwf, ctypes.byref(value)), value.value)

_FDwfDigitalInStatusAutoTriggered = _dwf.FDwfDigitalInStatusAutoTriggered
_FDwfDigitalInStatusAutoTriggered.argtypes = [HDWF, _types.c_byte_p]
_FDwfDigitalInStatusAutoTriggered.restype = bool

def FDwfDigitalInStatusAutoTriggered(hdwf):
	value = ctypes.c_byte()
	return (_FDwfDigitalInStatusAutoTriggered(hdwf, ctypes.byref(value)), value.value)

FDwfDigitalInStatusData = _dwf.FDwfDigitalInStatusData
FDwfDigitalInStatusData.argtypes = [HDWF, ctypes.c_void_p, ctypes.c_int]
FDwfDigitalInStatusData.restype = bool


# Acquistion configuration:
_FDwfDigitalInInternalClockInfo = _dwf.FDwfDigitalInInternalClockInfo
_FDwfDigitalInInternalClockInfo.argtypes = [HDWF, _types.c_double_p]
_FDwfDigitalInInternalClockInfo.restype = bool

def FDwfDigitalInInternalClockInfo(hdwf):
	value = ctypes.c_double()
	return (_FDwfDigitalInInternalClockInfo(hdwf, ctypes.byref(value)), value.value)


_FDwfDigitalInClockSourceInfo = _dwf.FDwfDigitalInClockSourceInfo
_FDwfDigitalInClockSourceInfo.argtypes = [HDWF, _types.c_int_p]  # use IsBitSet
_FDwfDigitalInClockSourceInfo.restype = bool

def FDwfDigitalInClockSourceInfo(hdwf):
	info = ctypes.c_int()
	if not _FDwfDigitalInClockSourceInfo(hdwf, ctypes.byref(info)):
		return (False, [])
	supported = []
	for i in range(8 * ctypes.sizeof(ctypes.c_int)):
		if info.value & (1 << i) != 0:
			supported.append(DwfDigitalInClockSource(i))
	return (True, supported)

FDwfDigitalInClockSourceSet = _dwf.FDwfDigitalInClockSourceSet
FDwfDigitalInClockSourceSet.argtypes = [HDWF, DwfDigitalInClockSource]
FDwfDigitalInClockSourceSet.restype = bool

_FDwfDigitalInClockSourceGet = _dwf.FDwfDigitalInClockSourceGet
_FDwfDigitalInClockSourceGet.argtypes = [HDWF, ctypes.POINTER(DwfDigitalInClockSource)]
_FDwfDigitalInClockSourceGet.restype = bool

def FDwfDigitalInClockSourceGet(hdwf):
	value = DwfDigitalInClockSource()
	return (_FDwfDigitalInClockSourceGet(hdwf, ctypes.byref(value)), value)


_FDwfDigitalInDividerInfo = _dwf.FDwfDigitalInDividerInfo
_FDwfDigitalInDividerInfo.argtypes = [HDWF, _types.c_uint_p]
_FDwfDigitalInDividerInfo.restype = bool

def FDwfDigitalInDividerInfo(hdwf):
	value = ctypes.c_uint()
	return (_FDwfDigitalInDividerInfo(hdwf, ctypes.byref(value)), value.value)

FDwfDigitalInDividerSet = _dwf.FDwfDigitalInDividerSet
FDwfDigitalInDividerSet.argtypes = [HDWF, ctypes.c_uint]
FDwfDigitalInDividerSet.restype = bool

_FDwfDigitalInDividerGet = _dwf.FDwfDigitalInDividerGet
_FDwfDigitalInDividerGet.argtypes = [HDWF, _types.c_uint_p]
_FDwfDigitalInDividerGet.restype = bool

def FDwfDigitalInDividerGet(hdwf):
	value = ctypes.c_uint()
	return (_FDwfDigitalInDividerGet(hdwf, ctypes.byref(value)), value.value)


_FDwfDigitalInBitsInfo = _dwf.FDwfDigitalInBitsInfo  # Returns the number of Digital In bits
_FDwfDigitalInBitsInfo.argtypes = [HDWF, _types.c_int_p]
_FDwfDigitalInBitsInfo.restype = bool

def FDwfDigitalInBitsInfo(hdwf):
	value = ctypes.c_int()
	return (_FDwfDigitalInBitsInfo(hdwf, ctypes.byref(value)), value.value)

FDwfDigitalInSampleFormatSet = _dwf.FDwfDigitalInSampleFormatSet  # valid options 8/16/32
FDwfDigitalInSampleFormatSet.argtypes = [HDWF, ctypes.c_int]
FDwfDigitalInSampleFormatSet.restype = bool

_FDwfDigitalInSampleFormatGet = _dwf.FDwfDigitalInSampleFormatGet
_FDwfDigitalInSampleFormatGet.argtypes = [HDWF, _types.c_int_p]
_FDwfDigitalInSampleFormatGet.restype = bool

def FDwfDigitalInSampleFormatGet(hdwf):
	value = ctypes.c_int()
	return (_FDwfDigitalInSampleFormatGet(hdwf, ctypes.byref(value)), value.value)


_FDwfDigitalInBufferSizeInfo = _dwf.FDwfDigitalInBufferSizeInfo
_FDwfDigitalInBufferSizeInfo.argtypes = [HDWF, _types.c_int_p]
_FDwfDigitalInBufferSizeInfo.restype = bool

def FDwfDigitalInBufferSizeInfo(hdwf):
	value = ctypes.c_int()
	return (_FDwfDigitalInBufferSizeInfo(hdwf, ctypes.byref(value)), value.value)

FDwfDigitalInBufferSizeSet = _dwf.FDwfDigitalInBufferSizeSet
FDwfDigitalInBufferSizeSet.argtypes = [HDWF, ctypes.c_int]
FDwfDigitalInBufferSizeSet.restype = bool

_FDwfDigitalInBufferSizeGet = _dwf.FDwfDigitalInBufferSizeGet
_FDwfDigitalInBufferSizeGet.argtypes = [HDWF, _types.c_int_p]
_FDwfDigitalInBufferSizeGet.restype = bool

def FDwfDigitalInBufferSizeGet(hdwf):
	value = ctypes.c_int()
	return (_FDwfDigitalInBufferSizeGet(hdwf, ctypes.byref(value)), value.value)


_FDwfDigitalInSampleModeInfo = _dwf.FDwfDigitalInSampleModeInfo  # use IsBitSet
_FDwfDigitalInSampleModeInfo.argtypes = [HDWF, _types.c_int_p]
_FDwfDigitalInSampleModeInfo.restype = bool

def FDwfDigitalInSampleModeInfo(hdwf):
	info = ctypes.c_int()
	if not _FDwfDigitalInSampleModeInfo(hdwf, ctypes.byref(info)):
		return (False, [])
	supported = []
	for i in range(8 * ctypes.sizeof(ctypes.c_int)):
		if info.value & (1 << i) != 0:
			supported.append(DwfDigitalInSampleMode(i))
	return (True, supported)

FDwfDigitalInSampleModeSet = _dwf.FDwfDigitalInSampleModeSet
FDwfDigitalInSampleModeSet.argtypes = [HDWF, DwfDigitalInSampleMode]
FDwfDigitalInSampleModeSet.restype = bool

_FDwfDigitalInSampleModeGet = _dwf.FDwfDigitalInSampleModeGet
_FDwfDigitalInSampleModeGet.argtypes = [HDWF, ctypes.POINTER(DwfDigitalInSampleMode)]
_FDwfDigitalInSampleModeGet.restype = bool

def FDwfDigitalInSampleModeGet(hdwf):
	value = DwfDigitalInSampleMode()
	return (_FDwfDigitalInSampleModeGet(hdwf, ctypes.byref(value)), value)


_FDwfDigitalInAcquisitionModeInfo = _dwf.FDwfDigitalInAcquisitionModeInfo  # use IsBitSet
_FDwfDigitalInAcquisitionModeInfo.argtypes = [HDWF, _types.c_int_p]
_FDwfDigitalInAcquisitionModeInfo.restype = bool

def FDwfDigitalInAcquisitionModeInfo(hdwf):
	info = ctypes.c_int()
	if not _FDwfDigitalInAcquisitionModeInfo(hdwf, ctypes.byref(info)):
		return (False, [])
	supported = []
	for i in range(8 * ctypes.sizeof(ctypes.c_int)):
		if info.value & (1 << i) != 0:
			supported.append(ACQMODE(i))
	return (True, supported)

FDwfDigitalInAcquisitionModeSet = _dwf.FDwfDigitalInAcquisitionModeSet
FDwfDigitalInAcquisitionModeSet.argtypes = [HDWF, ACQMODE]
FDwfDigitalInAcquisitionModeSet.restype = bool

_FDwfDigitalInAcquisitionModeGet = _dwf.FDwfDigitalInAcquisitionModeGet
_FDwfDigitalInAcquisitionModeGet.argtypes = [HDWF, ctypes.POINTER(ACQMODE)]
_FDwfDigitalInAcquisitionModeGet.restype = bool

def FDwfDigitalInAcquisitionModeGet(hdwf):
	value = ACQMODE()
	return (_FDwfDigitalInAcquisitionModeGet(hdwf, ctypes.byref(value)), value)


# Trigger configuration:
_FDwfDigitalInTriggerSourceInfo = _dwf.FDwfDigitalInTriggerSourceInfo  # use IsBitSet
_FDwfDigitalInTriggerSourceInfo.argtypes = [HDWF, _types.c_int_p]
_FDwfDigitalInTriggerSourceInfo.restype = bool

def FDwfDigitalInTriggerSourceInfo(hdwf):
	info = ctypes.c_int()
	if not _FDwfDigitalInTriggerSourceInfo(hdwf, ctypes.byref(info)):
		return (False, [])
	supported = []
	for i in range(8 * ctypes.sizeof(ctypes.c_int)):
		if info.value & (1 << i) != 0:
			supported.append(TRIGSRC(i))
	return (True, supported)

FDwfDigitalInTriggerSourceSet = _dwf.FDwfDigitalInTriggerSourceSet
FDwfDigitalInTriggerSourceSet.argtypes = [HDWF, TRIGSRC]
FDwfDigitalInTriggerSourceSet.restype = bool

_FDwfDigitalInTriggerSourceGet = _dwf.FDwfDigitalInTriggerSourceGet
_FDwfDigitalInTriggerSourceGet.argtypes = [HDWF, ctypes.POINTER(TRIGSRC)]
_FDwfDigitalInTriggerSourceGet.restype = bool

def FDwfDigitalInTriggerSourceGet(hdwf):
	value = TRIGSRC()
	return (_FDwfDigitalInTriggerSourceGet(hdwf, ctypes.byref(value)), value)


_FDwfDigitalInTriggerPositionInfo = _dwf.FDwfDigitalInTriggerPositionInfo
_FDwfDigitalInTriggerPositionInfo.argtypes = [HDWF, _types.c_uint_p]
_FDwfDigitalInTriggerPositionInfo.restype = bool

def FDwfDigitalInTriggerPositionInfo(hdwf):
	value = ctypes.c_uint()
	return (_FDwfDigitalInTriggerPositionInfo(hdwf, ctypes.byref(value)), value.value)

FDwfDigitalInTriggerPositionSet = _dwf.FDwfDigitalInTriggerPositionSet
FDwfDigitalInTriggerPositionSet.argtypes = [HDWF, ctypes.c_uint]
FDwfDigitalInTriggerPositionSet.restype = bool

_FDwfDigitalInTriggerPositionGet = _dwf.FDwfDigitalInTriggerPositionGet
_FDwfDigitalInTriggerPositionGet.argtypes = [HDWF, _types.c_uint_p]
_FDwfDigitalInTriggerPositionGet.restype = bool

def FDwfDigitalInTriggerPositionGet(hdwf):
	value = ctypes.c_uint()
	return (_FDwfDigitalInTriggerPositionGet(hdwf, ctypes.byref(value)), value.value)


_FDwfDigitalInTriggerAutoTimeoutInfo = _dwf.FDwfDigitalInTriggerAutoTimeoutInfo
_FDwfDigitalInTriggerAutoTimeoutInfo.argtypes = [HDWF, _types.c_double_p, _types.c_double_p, _types.c_double_p]
_FDwfDigitalInTriggerAutoTimeoutInfo.restype = bool

def FDwfDigitalInTriggerAutoTimeoutInfo(hdwf):
	val_a = ctypes.c_double()
	val_b = ctypes.c_double()
	val_c = ctypes.c_double()
	return (_FDwfDigitalInTriggerAutoTimeoutInfo(hdwf, ctypes.byref(val_a), ctypes.byref(val_b), ctypes.byref(val_c)), val_a.value, val_b.value, val_c.value)

FDwfDigitalInTriggerAutoTimeoutSet = _dwf.FDwfDigitalInTriggerAutoTimeoutSet
FDwfDigitalInTriggerAutoTimeoutSet.argtypes = [HDWF, ctypes.c_double]
FDwfDigitalInTriggerAutoTimeoutSet.restype = bool

_FDwfDigitalInTriggerAutoTimeoutGet = _dwf.FDwfDigitalInTriggerAutoTimeoutGet
_FDwfDigitalInTriggerAutoTimeoutGet.argtypes = [HDWF, _types.c_double_p]
_FDwfDigitalInTriggerAutoTimeoutGet.restype = bool

def FDwfDigitalInTriggerAutoTimeoutGet(hdwf):
	value = ctypes.c_double()
	return (_FDwfDigitalInTriggerAutoTimeoutGet(hdwf, ctypes.byref(value)), value.value)


_FDwfDigitalInTriggerInfo = _dwf.FDwfDigitalInTriggerInfo
_FDwfDigitalInTriggerInfo.argtypes = [HDWF, _types.c_uint_p, _types.c_uint_p, _types.c_uint_p, _types.c_uint_p]
_FDwfDigitalInTriggerInfo.restype = bool

def FDwfDigitalInTriggerInfo(hdwf):
	val_a = ctypes.c_uint()
	val_b = ctypes.c_uint()
	val_c = ctypes.c_uint()
	val_d = ctypes.c_uint()
	return (_FDwfDigitalInTriggerInfo(hdwf, ctypes.byref(val_a), ctypes.byref(val_b), ctypes.byref(val_c), ctypes.byref(val_d)), val_a.value, val_b.value, val_c.value, val_d.value)

FDwfDigitalInTriggerSet = _dwf.FDwfDigitalInTriggerSet
FDwfDigitalInTriggerSet.argtypes = [HDWF, ctypes.c_uint, ctypes.c_uint, ctypes.c_uint, ctypes.c_uint]
FDwfDigitalInTriggerSet.restype = bool

_FDwfDigitalInTriggerGet = _dwf.FDwfDigitalInTriggerGet
_FDwfDigitalInTriggerGet.argtypes = [HDWF, _types.c_uint_p, _types.c_uint_p, _types.c_uint_p, _types.c_uint_p]
_FDwfDigitalInTriggerGet.restype = bool

def FDwfDigitalInTriggerGet(hdwf):
	val_a = ctypes.c_uint()
	val_b = ctypes.c_uint()
	val_c = ctypes.c_uint()
	val_d = ctypes.c_uint()
	return (_FDwfDigitalInTriggerGet(hdwf, ctypes.byref(val_a), ctypes.byref(val_b), ctypes.byref(val_c), ctypes.byref(val_d)), val_a.value, val_b.value, val_c.value, val_d.value)

# the logic for trigger bits: Low and High and   # (Rise or Fall)
# bits set in Rise and Fall means any edge

# DIGITAL OUT INSTRUMENT FUNCTIONS
# Control:
FDwfDigitalOutReset = _dwf.FDwfDigitalOutReset
FDwfDigitalOutReset.argtypes = [HDWF]
FDwfDigitalOutReset.restype = bool

FDwfDigitalOutConfigure = _dwf.FDwfDigitalOutConfigure
FDwfDigitalOutConfigure.argtypes = [HDWF, ctypes.c_byte]
FDwfDigitalOutConfigure.restype = bool

_FDwfDigitalOutStatus = _dwf.FDwfDigitalOutStatus
_FDwfDigitalOutStatus.argtypes = [HDWF, ctypes.POINTER(DwfState)]
_FDwfDigitalOutStatus.restype = bool

def FDwfDigitalOutStatus(hdwf):
	value = DwfState()
	return (_FDwfDigitalOutStatus(hdwf, ctypes.byref(value)), value)


# Configuration:
_FDwfDigitalOutInternalClockInfo = _dwf.FDwfDigitalOutInternalClockInfo
_FDwfDigitalOutInternalClockInfo.argtypes = [HDWF, _types.c_double_p]
_FDwfDigitalOutInternalClockInfo.restype = bool

def FDwfDigitalOutInternalClockInfo(hdwf):
	value = ctypes.c_double()
	return (_FDwfDigitalOutInternalClockInfo(hdwf, ctypes.byref(value)), value.value)


_FDwfDigitalOutTriggerSourceInfo = _dwf.FDwfDigitalOutTriggerSourceInfo  # use IsBitSet
_FDwfDigitalOutTriggerSourceInfo.argtypes = [HDWF, _types.c_int_p]
_FDwfDigitalOutTriggerSourceInfo.restype = bool

def FDwfDigitalOutTriggerSourceInfo(hdwf):
	info = ctypes.c_int()
	if not _FDwfDigitalOutTriggerSourceInfo(hdwf, ctypes.byref(info)):
		return (False, [])
	supported = []
	for i in range(8 * ctypes.sizeof(ctypes.c_int)):
		if info.value & (1 << i) != 0:
			supported.append(TRIGSRC(i))
	return (True, supported)

FDwfDigitalOutTriggerSourceSet = _dwf.FDwfDigitalOutTriggerSourceSet
FDwfDigitalOutTriggerSourceSet.argtypes = [HDWF, TRIGSRC]
FDwfDigitalOutTriggerSourceSet.restype = bool

_FDwfDigitalOutTriggerSourceGet = _dwf.FDwfDigitalOutTriggerSourceGet
_FDwfDigitalOutTriggerSourceGet.argtypes = [HDWF, ctypes.POINTER(TRIGSRC)]
_FDwfDigitalOutTriggerSourceGet.restype = bool

def FDwfDigitalOutTriggerSourceGet(hdwf):
	value = TRIGSRC()
	return (_FDwfDigitalOutTriggerSourceGet(hdwf, ctypes.byref(value)), value)


_FDwfDigitalOutRunInfo = _dwf.FDwfDigitalOutRunInfo
_FDwfDigitalOutRunInfo.argtypes = [HDWF, _types.c_double_p, _types.c_double_p]
_FDwfDigitalOutRunInfo.restype = bool

def FDwfDigitalOutRunInfo(hdwf):
	min = ctypes.c_double()
	max = ctypes.c_double()
	return (_FDwfDigitalOutRunInfo(hdwf, ctypes.byref(min), ctypes.byref(max)), min.value, max.value)

FDwfDigitalOutRunSet = _dwf.FDwfDigitalOutRunSet
FDwfDigitalOutRunSet.argtypes = [HDWF, ctypes.c_double]
FDwfDigitalOutRunSet.restype = bool

_FDwfDigitalOutRunGet = _dwf.FDwfDigitalOutRunGet
_FDwfDigitalOutRunGet.argtypes = [HDWF, _types.c_double_p]
_FDwfDigitalOutRunGet.restype = bool

def FDwfDigitalOutRunGet(hdwf):
	value = ctypes.c_double()
	return (_FDwfDigitalOutRunGet(hdwf, ctypes.byref(value)), value.value)

_FDwfDigitalOutRunStatus = _dwf.FDwfDigitalOutRunStatus
_FDwfDigitalOutRunStatus.argtypes = [HDWF, _types.c_double_p]
_FDwfDigitalOutRunStatus.restype = bool

def FDwfDigitalOutRunStatus(hdwf):
	value = ctypes.c_double()
	return (_FDwfDigitalOutRunStatus(hdwf, ctypes.byref(value)), value.value)


_FDwfDigitalOutWaitInfo = _dwf.FDwfDigitalOutWaitInfo
_FDwfDigitalOutWaitInfo.argtypes = [HDWF, _types.c_double_p, _types.c_double_p]
_FDwfDigitalOutWaitInfo.restype = bool

def FDwfDigitalOutWaitInfo(hdwf):
	min = ctypes.c_double()
	max = ctypes.c_double()
	return (_FDwfDigitalOutWaitInfo(hdwf, ctypes.byref(min), ctypes.byref(max)), min.value, max.value)

FDwfDigitalOutWaitSet = _dwf.FDwfDigitalOutWaitSet
FDwfDigitalOutWaitSet.argtypes = [HDWF, ctypes.c_double]
FDwfDigitalOutWaitSet.restype = bool

_FDwfDigitalOutWaitGet = _dwf.FDwfDigitalOutWaitGet
_FDwfDigitalOutWaitGet.argtypes = [HDWF, _types.c_double_p]
_FDwfDigitalOutWaitGet.restype = bool

def FDwfDigitalOutWaitGet(hdwf):
	value = ctypes.c_double()
	return (_FDwfDigitalOutWaitGet(hdwf, ctypes.byref(value)), value.value)


_FDwfDigitalOutRepeatInfo = _dwf.FDwfDigitalOutRepeatInfo
_FDwfDigitalOutRepeatInfo.argtypes = [HDWF, _types.c_uint_p, _types.c_uint_p]
_FDwfDigitalOutRepeatInfo.restype = bool

def FDwfDigitalOutRepeatInfo(hdwf):
	min = ctypes.c_uint()
	max = ctypes.c_uint()
	return (_FDwfDigitalOutRepeatInfo(hdwf, ctypes.byref(min), ctypes.byref(max)), min.value, max.value)

FDwfDigitalOutRepeatSet = _dwf.FDwfDigitalOutRepeatSet
FDwfDigitalOutRepeatSet.argtypes = [HDWF, ctypes.c_uint]
FDwfDigitalOutRepeatSet.restype = bool

_FDwfDigitalOutRepeatGet = _dwf.FDwfDigitalOutRepeatGet
_FDwfDigitalOutRepeatGet.argtypes = [HDWF, _types.c_uint_p]
_FDwfDigitalOutRepeatGet.restype = bool

def FDwfDigitalOutRepeatGet(hdwf):
	value = ctypes.c_uint()
	return (_FDwfDigitalOutRepeatGet(hdwf, ctypes.byref(value)), value.value)

_FDwfDigitalOutRepeatStatus = _dwf.FDwfDigitalOutRepeatStatus
_FDwfDigitalOutRepeatStatus.argtypes = [HDWF, _types.c_uint_p]
_FDwfDigitalOutRepeatStatus.restype = bool

def FDwfDigitalOutRepeatStatus(hdwf):
	value = ctypes.c_uint()
	return (_FDwfDigitalOutRepeatStatus(hdwf, ctypes.byref(value)), value.value)


FDwfDigitalOutRepeatTriggerSet = _dwf.FDwfDigitalOutRepeatTriggerSet
FDwfDigitalOutRepeatTriggerSet.argtypes = [HDWF, ctypes.c_byte]
FDwfDigitalOutRepeatTriggerSet.restype = bool

_FDwfDigitalOutRepeatTriggerGet = _dwf.FDwfDigitalOutRepeatTriggerGet
_FDwfDigitalOutRepeatTriggerGet.argtypes = [HDWF, _types.c_byte_p]
_FDwfDigitalOutRepeatTriggerGet.restype = bool

def FDwfDigitalOutRepeatTriggerGet(hdwf):
	value = ctypes.c_byte()
	return (_FDwfDigitalOutRepeatTriggerGet(hdwf, ctypes.byref(value)), bool(value.value))


_FDwfDigitalOutCount = _dwf.FDwfDigitalOutCount
_FDwfDigitalOutCount.argtypes = [HDWF, _types.c_int_p]
_FDwfDigitalOutCount.restype = bool

def FDwfDigitalOutCount(hdwf):
	value = ctypes.c_int()
	return (_FDwfDigitalOutCount(hdwf, ctypes.byref(value)), value.value)

FDwfDigitalOutEnableSet = _dwf.FDwfDigitalOutEnableSet
FDwfDigitalOutEnableSet.argtypes = [HDWF, ctypes.c_int, ctypes.c_byte]
FDwfDigitalOutEnableSet.restype = bool

_FDwfDigitalOutEnableGet = _dwf.FDwfDigitalOutEnableGet
_FDwfDigitalOutEnableGet.argtypes = [HDWF, ctypes.c_int, _types.c_byte_p]
_FDwfDigitalOutEnableGet.restype = bool

def FDwfDigitalOutEnableGet(hdwf):
	value = ctypes.c_byte()
	return (_FDwfDigitalOutEnableGet(hdwf, ctypes.byref(value)), bool(value.value))


_FDwfDigitalOutOutputInfo = _dwf.FDwfDigitalOutOutputInfo  # use IsBitSet
_FDwfDigitalOutOutputInfo.argtypes = [HDWF, ctypes.c_int, _types.c_int_p]
_FDwfDigitalOutOutputInfo.restype = bool

def FDwfDigitalOutOutputInfo(hdwf):
	info = ctypes.c_int()
	if not _FDwfDigitalOutOutputInfo(hdwf, ctypes.byref(info)):
		return (False, [])
	supported = []
	for i in range(8 * ctypes.sizeof(ctypes.c_int)):
		if info.value & (1 << i) != 0:
			supported.append(DwfDigitalOutOutput(i))
	return (True, supported)

FDwfDigitalOutOutputSet = _dwf.FDwfDigitalOutOutputSet
FDwfDigitalOutOutputSet.argtypes = [HDWF, ctypes.c_int, DwfDigitalOutOutput]
FDwfDigitalOutOutputSet.restype = bool

_FDwfDigitalOutOutputGet = _dwf.FDwfDigitalOutOutputGet
_FDwfDigitalOutOutputGet.argtypes = [HDWF, ctypes.c_int, ctypes.POINTER(DwfDigitalOutOutput)]
_FDwfDigitalOutOutputGet.restype = bool

def FDwfDigitalOutOutputGet(hdwf):
	value = DwfDigitalOutOutput()
	return (_FDwfDigitalOutOutputGet(hdwf, ctypes.byref(value)), value)


_FDwfDigitalOutTypeInfo = _dwf.FDwfDigitalOutTypeInfo  # use IsBitSet
_FDwfDigitalOutTypeInfo.argtypes = [HDWF, ctypes.c_int, _types.c_int_p]
_FDwfDigitalOutTypeInfo.restype = bool

def FDwfDigitalOutTypeInfo(hdwf):
	info = ctypes.c_int()
	if not _FDwfDigitalOutTypeInfo(hdwf, ctypes.byref(info)):
		return (False, [])
	supported = []
	for i in range(8 * ctypes.sizeof(ctypes.c_int)):
		if info.value & (1 << i) != 0:
			supported.append(DwfDigitalOutType(i))
	return (True, supported)

FDwfDigitalOutTypeSet = _dwf.FDwfDigitalOutTypeSet
FDwfDigitalOutTypeSet.argtypes = [HDWF, ctypes.c_int, DwfDigitalOutType]
FDwfDigitalOutTypeSet.restype = bool

_FDwfDigitalOutTypeGet = _dwf.FDwfDigitalOutTypeGet
_FDwfDigitalOutTypeGet.argtypes = [HDWF, ctypes.c_int, ctypes.POINTER(DwfDigitalOutType)]
_FDwfDigitalOutTypeGet.restype = bool

def FDwfDigitalOutTypeGet(hdwf):
	value = DwfDigitalOutType()
	return (_FDwfDigitalOutTypeGet(hdwf, ctypes.byref(value)), value)


_FDwfDigitalOutIdleInfo = _dwf.FDwfDigitalOutIdleInfo  # use IsBitSet
_FDwfDigitalOutIdleInfo.argtypes = [HDWF, ctypes.c_int, _types.c_int_p]
_FDwfDigitalOutIdleInfo.restype = bool

def FDwfDigitalOutIdleInfo(hdwf):
	info = ctypes.c_int()
	if not _FDwfDigitalOutIdleInfo(hdwf, ctypes.byref(info)):
		return (False, [])
	supported = []
	for i in range(8 * ctypes.sizeof(ctypes.c_int)):
		if info.value & (1 << i) != 0:
			supported.append(DwfDigitalOutIdle(i))
	return (True, supported)

FDwfDigitalOutIdleSet = _dwf.FDwfDigitalOutIdleSet
FDwfDigitalOutIdleSet.argtypes = [HDWF, ctypes.c_int, DwfDigitalOutIdle]
FDwfDigitalOutIdleSet.restype = bool

_FDwfDigitalOutIdleGet = _dwf.FDwfDigitalOutIdleGet
_FDwfDigitalOutIdleGet.argtypes = [HDWF, ctypes.c_int, ctypes.POINTER(DwfDigitalOutIdle)]
_FDwfDigitalOutIdleGet.restype = bool

def FDwfDigitalOutIdleGet(hdwf):
	value = DwfDigitalOutIdle()
	return (_FDwfDigitalOutIdleGet(hdwf, ctypes.byref(value)), value)


_FDwfDigitalOutDividerInfo = _dwf.FDwfDigitalOutDividerInfo
_FDwfDigitalOutDividerInfo.argtypes = [HDWF, ctypes.c_int, _types.c_uint_p, _types.c_uint_p]
_FDwfDigitalOutDividerInfo.restype = bool

def FDwfDigitalOutDividerInfo(hdwf, idxChannel):
	min = ctypes.c_uint()
	max = ctypes.c_uint()
	return (_FDwfDigitalOutDividerInfo(hdwf, idxChannel, ctypes.byref(min), ctypes.byref(max)), min.value, max.value)

FDwfDigitalOutDividerInitSet = _dwf.FDwfDigitalOutDividerInitSet
FDwfDigitalOutDividerInitSet.argtypes = [HDWF, ctypes.c_int, ctypes.c_uint]
FDwfDigitalOutDividerInitSet.restype = bool

_FDwfDigitalOutDividerInitGet = _dwf.FDwfDigitalOutDividerInitGet
_FDwfDigitalOutDividerInitGet.argtypes = [HDWF, ctypes.c_int, _types.c_uint_p]
_FDwfDigitalOutDividerInitGet.restype = bool

def FDwfDigitalOutDividerInitGet(hdwf, idxChannel):
	value = ctypes.c_uint()
	return (_FDwfDigitalOutDividerInitGet(hdwf, idxChannel, ctypes.byref(value)), value.value)

FDwfDigitalOutDividerSet = _dwf.FDwfDigitalOutDividerSet
FDwfDigitalOutDividerSet.argtypes = [HDWF, ctypes.c_int, ctypes.c_uint]
FDwfDigitalOutDividerSet.restype = bool

_FDwfDigitalOutDividerGet = _dwf.FDwfDigitalOutDividerGet
_FDwfDigitalOutDividerGet.argtypes = [HDWF, ctypes.c_int, _types.c_uint_p]
_FDwfDigitalOutDividerGet.restype = bool

def FDwfDigitalOutDividerGet(hdwf, idxChannel):
	value = ctypes.c_uint()
	return (_FDwfDigitalOutDividerGet(hdwf, idxChannel, ctypes.byref(value)), value.value)


_FDwfDigitalOutCounterInfo = _dwf.FDwfDigitalOutCounterInfo
_FDwfDigitalOutCounterInfo.argtypes = [HDWF, ctypes.c_int, _types.c_uint_p, _types.c_uint_p]
_FDwfDigitalOutCounterInfo.restype = bool

def FDwfDigitalOutCounterInfo(hdwf, idxChannel):
	min = ctypes.c_uint()
	max = ctypes.c_uint()
	return (_FDwfDigitalOutCounterInfo(hdwf, idxChannel, ctypes.byref(min), ctypes.byref(max)), min.value, max.value)

FDwfDigitalOutCounterInitSet = _dwf.FDwfDigitalOutCounterInitSet
FDwfDigitalOutCounterInitSet.argtypes = [HDWF, ctypes.c_int, ctypes.c_byte, ctypes.c_uint]
FDwfDigitalOutCounterInitSet.restype = bool

_FDwfDigitalOutCounterInitGet = _dwf.FDwfDigitalOutCounterInitGet
_FDwfDigitalOutCounterInitGet.argtypes = [HDWF, ctypes.c_int, _types.c_int_p, _types.c_uint_p]
_FDwfDigitalOutCounterInitGet.restype = bool

def FDwfDigitalOutCounterInitGet(hdwf, idxChannel):
	val_a = ctypes.c_int()
	val_b = ctypes.c_uint()
	return (_FDwfDigitalOutCounterInitGet(hdwf, idxChannel, ctypes.byref(val_a), ctypes.byref(val_b)), val_a.value, val_b.value)

FDwfDigitalOutCounterSet = _dwf.FDwfDigitalOutCounterSet
FDwfDigitalOutCounterSet.argtypes = [HDWF, ctypes.c_int, ctypes.c_uint, ctypes.c_uint]
FDwfDigitalOutCounterSet.restype = bool

_FDwfDigitalOutCounterGet = _dwf.FDwfDigitalOutCounterGet
_FDwfDigitalOutCounterGet.argtypes = [HDWF, ctypes.c_int, _types.c_uint_p, _types.c_uint_p]
_FDwfDigitalOutCounterGet.restype = bool

def FDwfDigitalOutCounterGet(hdwf, idxChannel):
	val_a = ctypes.c_uint()
	val_b = ctypes.c_uint()
	return (_FDwfDigitalOutCounterGet(hdwf, idxChannel, ctypes.byref(val_a), ctypes.byref(val_b)), val_a.value, val_b.value)


_FDwfDigitalOutDataInfo = _dwf.FDwfDigitalOutDataInfo
_FDwfDigitalOutDataInfo.argtypes = [HDWF, ctypes.c_int, _types.c_uint_p]
_FDwfDigitalOutDataInfo.restype = bool

def FDwfDigitalOutDataInfo(hdwf, idxChannel):
	value = ctypes.c_uint()
	return (_FDwfDigitalOutDataInfo(hdwf, idxChannel, ctypes.byref(value)), value.value)

FDwfDigitalOutDataSet = _dwf.FDwfDigitalOutDataSet
FDwfDigitalOutDataSet.argtypes = [HDWF, ctypes.c_int, ctypes.c_void_p, ctypes.c_uint]
FDwfDigitalOutDataSet.restype = bool
