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
FDwfEnum = _dwf.FDwfEnum
FDwfEnum.argtypes = [ENUMFILTER, _types.c_int_p]
FDwfEnum.restype = bool

FDwfEnumDeviceType = _dwf.FDwfEnumDeviceType
FDwfEnumDeviceType.argtypes = [ctypes.c_int, ctypes.POINTER(DEVID), ctypes.POINTER(DEVVER)]
FDwfEnumDeviceType.restype = bool

FDwfEnumDeviceIsOpened = _dwf.FDwfEnumDeviceIsOpened
FDwfEnumDeviceIsOpened.argtypes = [ctypes.c_int, _types.c_byte_p]
FDwfEnumDeviceIsOpened.restype = bool

FDwfEnumUserName = _dwf.FDwfEnumUserName
FDwfEnumUserName.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_char * 32)]
FDwfEnumUserName.restype = bool

FDwfEnumDeviceName = _dwf.FDwfEnumDeviceName
FDwfEnumDeviceName.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_char * 32)]
FDwfEnumDeviceName.restype = bool

FDwfEnumSN = _dwf.FDwfEnumSN
FDwfEnumSN.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_char * 32)]
FDwfEnumSN.restype = bool


# Open/Close:
FDwfDeviceOpen = _dwf.FDwfDeviceOpen
FDwfDeviceOpen.argtypes = [ctypes.c_int, ctypes.POINTER(HDWF)]
FDwfDeviceOpen.restype = bool

FDwfDeviceClose = _dwf.FDwfDeviceClose
FDwfDeviceClose.argtypes = [HDWF]
FDwfDeviceClose.restype = bool

FDwfDeviceCloseAll = _dwf.FDwfDeviceCloseAll
FDwfDeviceCloseAll.argtypes = []
FDwfDeviceCloseAll.restype = bool

FDwfDeviceAutoConfigureSet = _dwf.FDwfDeviceAutoConfigureSet
FDwfDeviceAutoConfigureSet.argtypes = [HDWF, ctypes.c_byte]
FDwfDeviceAutoConfigureSet.restype = bool

FDwfDeviceAutoConfigureGet = _dwf.FDwfDeviceAutoConfigureGet
FDwfDeviceAutoConfigureGet.argtypes = [HDWF, _types.c_byte_p]
FDwfDeviceAutoConfigureGet.restype = bool

FDwfDeviceReset = _dwf.FDwfDeviceReset
FDwfDeviceReset.argtypes = [HDWF]
FDwfDeviceReset.restype = bool

FDwfDeviceTriggerInfo = _dwf.FDwfDeviceTriggerInfo  # use IsBitSet
FDwfDeviceTriggerInfo.argtypes = [HDWF, _types.c_int_p]
FDwfDeviceTriggerInfo.restype = bool

FDwfDeviceTriggerSet = _dwf.FDwfDeviceTriggerSet
FDwfDeviceTriggerSet.argtypes = [HDWF, ctypes.c_int, TRIGSRC]
FDwfDeviceTriggerSet.restype = bool

FDwfDeviceTriggerGet = _dwf.FDwfDeviceTriggerGet
FDwfDeviceTriggerGet.argtypes = [HDWF, ctypes.c_int, ctypes.POINTER(TRIGSRC)]
FDwfDeviceTriggerGet.restype = bool

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

FDwfAnalogInStatus = _dwf.FDwfAnalogInStatus
FDwfAnalogInStatus.argtypes = [HDWF, ctypes.c_byte, ctypes.POINTER(DwfState)]
FDwfAnalogInStatus.restype = bool

FDwfAnalogInStatusSamplesLeft = _dwf.FDwfAnalogInStatusSamplesLeft
FDwfAnalogInStatusSamplesLeft.argtypes = [HDWF, _types.c_int_p]
FDwfAnalogInStatusSamplesLeft.restype = bool

FDwfAnalogInStatusSamplesValid = _dwf.FDwfAnalogInStatusSamplesValid
FDwfAnalogInStatusSamplesValid.argtypes = [HDWF, _types.c_int_p]
FDwfAnalogInStatusSamplesValid.restype = bool

FDwfAnalogInStatusIndexWrite = _dwf.FDwfAnalogInStatusIndexWrite
FDwfAnalogInStatusIndexWrite.argtypes = [HDWF, _types.c_int_p]
FDwfAnalogInStatusIndexWrite.restype = bool

FDwfAnalogInStatusAutoTriggered = _dwf.FDwfAnalogInStatusAutoTriggered
FDwfAnalogInStatusAutoTriggered.argtypes = [HDWF, _types.c_byte_p]
FDwfAnalogInStatusAutoTriggered.restype = bool

FDwfAnalogInStatusData = _dwf.FDwfAnalogInStatusData
FDwfAnalogInStatusData.argtypes = [HDWF, ctypes.c_int, _types.c_double_p, ctypes.c_int]
FDwfAnalogInStatusData.restype = bool

FDwfAnalogInStatusSample = _dwf.FDwfAnalogInStatusSample
FDwfAnalogInStatusSample.argtypes = [HDWF, ctypes.c_int, _types.c_double_p]
FDwfAnalogInStatusSample.restype = bool


FDwfAnalogInStatusRecord = _dwf.FDwfAnalogInStatusRecord
FDwfAnalogInStatusRecord.argtypes = [HDWF, _types.c_int_p, _types.c_int_p, _types.c_int_p]
FDwfAnalogInStatusRecord.restype = bool

FDwfAnalogInRecordLengthSet = _dwf.FDwfAnalogInRecordLengthSet
FDwfAnalogInRecordLengthSet.argtypes = [HDWF, ctypes.c_double]
FDwfAnalogInRecordLengthSet.restype = bool

FDwfAnalogInRecordLengthGet = _dwf.FDwfAnalogInRecordLengthGet
FDwfAnalogInRecordLengthGet.argtypes = [HDWF, _types.c_double_p]
FDwfAnalogInRecordLengthGet.restype = bool


# Acquistion configuration:
FDwfAnalogInFrequencyInfo = _dwf.FDwfAnalogInFrequencyInfo
FDwfAnalogInFrequencyInfo.argtypes = [HDWF, _types.c_double_p, _types.c_double_p]
FDwfAnalogInFrequencyInfo.restype = bool

FDwfAnalogInFrequencySet = _dwf.FDwfAnalogInFrequencySet
FDwfAnalogInFrequencySet.argtypes = [HDWF, ctypes.c_double]
FDwfAnalogInFrequencySet.restype = bool

FDwfAnalogInFrequencyGet = _dwf.FDwfAnalogInFrequencyGet
FDwfAnalogInFrequencyGet.argtypes = [HDWF, _types.c_double_p]
FDwfAnalogInFrequencyGet.restype = bool


FDwfAnalogInBitsInfo = _dwf.FDwfAnalogInBitsInfo
FDwfAnalogInBitsInfo.argtypes = [HDWF, _types.c_int_p]
FDwfAnalogInBitsInfo.restype = bool


FDwfAnalogInBufferSizeInfo = _dwf.FDwfAnalogInBufferSizeInfo
FDwfAnalogInBufferSizeInfo.argtypes = [HDWF, _types.c_int_p, _types.c_int_p]
FDwfAnalogInBufferSizeInfo.restype = bool

FDwfAnalogInBufferSizeSet = _dwf.FDwfAnalogInBufferSizeSet
FDwfAnalogInBufferSizeSet.argtypes = [HDWF, ctypes.c_int]
FDwfAnalogInBufferSizeSet.restype = bool

FDwfAnalogInBufferSizeGet = _dwf.FDwfAnalogInBufferSizeGet
FDwfAnalogInBufferSizeGet.argtypes = [HDWF, _types.c_int_p]
FDwfAnalogInBufferSizeGet.restype = bool


FDwfAnalogInAcquisitionModeInfo = _dwf.FDwfAnalogInAcquisitionModeInfo  # use IsBitSet
FDwfAnalogInAcquisitionModeInfo.argtypes = [HDWF, _types.c_int_p]
FDwfAnalogInAcquisitionModeInfo.restype = bool

FDwfAnalogInAcquisitionModeSet = _dwf.FDwfAnalogInAcquisitionModeSet
FDwfAnalogInAcquisitionModeSet.argtypes = [HDWF, ACQMODE]
FDwfAnalogInAcquisitionModeSet.restype = bool

FDwfAnalogInAcquisitionModeGet = _dwf.FDwfAnalogInAcquisitionModeGet
FDwfAnalogInAcquisitionModeGet.argtypes = [HDWF, ctypes.POINTER(ACQMODE)]
FDwfAnalogInAcquisitionModeGet.restype = bool


# Channel configuration:
FDwfAnalogInChannelCount = _dwf.FDwfAnalogInChannelCount
FDwfAnalogInChannelCount.argtypes = [HDWF, _types.c_int_p]
FDwfAnalogInChannelCount.restype = bool

FDwfAnalogInChannelEnableSet = _dwf.FDwfAnalogInChannelEnableSet
FDwfAnalogInChannelEnableSet.argtypes = [HDWF, ctypes.c_int, ctypes.c_byte]
FDwfAnalogInChannelEnableSet.restype = bool

FDwfAnalogInChannelEnableGet = _dwf.FDwfAnalogInChannelEnableGet
FDwfAnalogInChannelEnableGet.argtypes = [HDWF, ctypes.c_int, _types.c_byte_p]
FDwfAnalogInChannelEnableGet.restype = bool

FDwfAnalogInChannelFilterInfo = _dwf.FDwfAnalogInChannelFilterInfo  # use IsBitSet
FDwfAnalogInChannelFilterInfo.argtypes = [HDWF, _types.c_int_p]
FDwfAnalogInChannelFilterInfo.restype = bool

FDwfAnalogInChannelFilterSet = _dwf.FDwfAnalogInChannelFilterSet
FDwfAnalogInChannelFilterSet.argtypes = [HDWF, ctypes.c_int, FILTER]
FDwfAnalogInChannelFilterSet.restype = bool

FDwfAnalogInChannelFilterGet = _dwf.FDwfAnalogInChannelFilterGet
FDwfAnalogInChannelFilterGet.argtypes = [HDWF, ctypes.c_int, ctypes.POINTER(FILTER)]
FDwfAnalogInChannelFilterGet.restype = bool

FDwfAnalogInChannelRangeInfo = _dwf.FDwfAnalogInChannelRangeInfo
FDwfAnalogInChannelRangeInfo.argtypes = [HDWF, _types.c_double_p, _types.c_double_p, _types.c_double_p]
FDwfAnalogInChannelRangeInfo.restype = bool

FDwfAnalogInChannelRangeSteps = _dwf.FDwfAnalogInChannelRangeSteps
FDwfAnalogInChannelRangeSteps.argtypes = [HDWF, ctypes.POINTER(ctypes.c_double * 32), _types.c_int_p]
FDwfAnalogInChannelRangeSteps.restype = bool

FDwfAnalogInChannelRangeSet = _dwf.FDwfAnalogInChannelRangeSet
FDwfAnalogInChannelRangeSet.argtypes = [HDWF, ctypes.c_int, ctypes.c_double]
FDwfAnalogInChannelRangeSet.restype = bool

FDwfAnalogInChannelRangeGet = _dwf.FDwfAnalogInChannelRangeGet
FDwfAnalogInChannelRangeGet.argtypes = [HDWF, ctypes.c_int, _types.c_double_p]
FDwfAnalogInChannelRangeGet.restype = bool

FDwfAnalogInChannelOffsetInfo = _dwf.FDwfAnalogInChannelOffsetInfo
FDwfAnalogInChannelOffsetInfo.argtypes = [HDWF, _types.c_double_p, _types.c_double_p, _types.c_double_p]
FDwfAnalogInChannelOffsetInfo.restype = bool

FDwfAnalogInChannelOffsetSet = _dwf.FDwfAnalogInChannelOffsetSet
FDwfAnalogInChannelOffsetSet.argtypes = [HDWF, ctypes.c_int, ctypes.c_double]
FDwfAnalogInChannelOffsetSet.restype = bool

FDwfAnalogInChannelOffsetGet = _dwf.FDwfAnalogInChannelOffsetGet
FDwfAnalogInChannelOffsetGet.argtypes = [HDWF, ctypes.c_int, _types.c_double_p]
FDwfAnalogInChannelOffsetGet.restype = bool


# Trigger configuration:
FDwfAnalogInTriggerSourceInfo = _dwf.FDwfAnalogInTriggerSourceInfo  # use IsBitSet
FDwfAnalogInTriggerSourceInfo.argtypes = [HDWF, _types.c_int_p]
FDwfAnalogInTriggerSourceInfo.restype = bool

FDwfAnalogInTriggerSourceSet = _dwf.FDwfAnalogInTriggerSourceSet
FDwfAnalogInTriggerSourceSet.argtypes = [HDWF, TRIGSRC]
FDwfAnalogInTriggerSourceSet.restype = bool

FDwfAnalogInTriggerSourceGet = _dwf.FDwfAnalogInTriggerSourceGet
FDwfAnalogInTriggerSourceGet.argtypes = [HDWF, ctypes.POINTER(TRIGSRC)]
FDwfAnalogInTriggerSourceGet.restype = bool


FDwfAnalogInTriggerPositionInfo = _dwf.FDwfAnalogInTriggerPositionInfo
FDwfAnalogInTriggerPositionInfo.argtypes = [HDWF, _types.c_double_p, _types.c_double_p, _types.c_double_p]
FDwfAnalogInTriggerPositionInfo.restype = bool

FDwfAnalogInTriggerPositionSet = _dwf.FDwfAnalogInTriggerPositionSet
FDwfAnalogInTriggerPositionSet.argtypes = [HDWF, ctypes.c_double]
FDwfAnalogInTriggerPositionSet.restype = bool

FDwfAnalogInTriggerPositionGet = _dwf.FDwfAnalogInTriggerPositionGet
FDwfAnalogInTriggerPositionGet.argtypes = [HDWF, _types.c_double_p]
FDwfAnalogInTriggerPositionGet.restype = bool

FDwfAnalogInTriggerPositionStatus = _dwf.FDwfAnalogInTriggerPositionStatus
FDwfAnalogInTriggerPositionStatus.argtypes = [HDWF, _types.c_double_p]


FDwfAnalogInTriggerAutoTimeoutInfo = _dwf.FDwfAnalogInTriggerAutoTimeoutInfo
FDwfAnalogInTriggerAutoTimeoutInfo.argtypes = [HDWF, _types.c_double_p, _types.c_double_p, _types.c_double_p]
FDwfAnalogInTriggerAutoTimeoutInfo.restype = bool

FDwfAnalogInTriggerAutoTimeoutSet = _dwf.FDwfAnalogInTriggerAutoTimeoutSet
FDwfAnalogInTriggerAutoTimeoutSet.argtypes = [HDWF, ctypes.c_double]
FDwfAnalogInTriggerAutoTimeoutSet.restype = bool

FDwfAnalogInTriggerAutoTimeoutGet = _dwf.FDwfAnalogInTriggerAutoTimeoutGet
FDwfAnalogInTriggerAutoTimeoutGet.argtypes = [HDWF, _types.c_double_p]
FDwfAnalogInTriggerAutoTimeoutGet.restype = bool


FDwfAnalogInTriggerHoldOffInfo = _dwf.FDwfAnalogInTriggerHoldOffInfo
FDwfAnalogInTriggerHoldOffInfo.argtypes = [HDWF, _types.c_double_p, _types.c_double_p, _types.c_double_p]
FDwfAnalogInTriggerHoldOffInfo.restype = bool

FDwfAnalogInTriggerHoldOffSet = _dwf.FDwfAnalogInTriggerHoldOffSet
FDwfAnalogInTriggerHoldOffSet.argtypes = [HDWF, ctypes.c_double]
FDwfAnalogInTriggerHoldOffSet.restype = bool

FDwfAnalogInTriggerHoldOffGet = _dwf.FDwfAnalogInTriggerHoldOffGet
FDwfAnalogInTriggerHoldOffGet.argtypes = [HDWF, _types.c_double_p]
FDwfAnalogInTriggerHoldOffGet.restype = bool


FDwfAnalogInTriggerTypeInfo = _dwf.FDwfAnalogInTriggerTypeInfo  # use IsBitSet
FDwfAnalogInTriggerTypeInfo.argtypes = [HDWF, _types.c_int_p]
FDwfAnalogInTriggerTypeInfo.restype = bool

FDwfAnalogInTriggerTypeSet = _dwf.FDwfAnalogInTriggerTypeSet
FDwfAnalogInTriggerTypeSet.argtypes = [HDWF, TRIGTYPE]
FDwfAnalogInTriggerTypeSet.restype = bool

FDwfAnalogInTriggerTypeGet = _dwf.FDwfAnalogInTriggerTypeGet
FDwfAnalogInTriggerTypeGet.argtypes = [HDWF, ctypes.POINTER(TRIGTYPE)]
FDwfAnalogInTriggerTypeGet.restype = bool


FDwfAnalogInTriggerChannelInfo = _dwf.FDwfAnalogInTriggerChannelInfo
FDwfAnalogInTriggerChannelInfo.argtypes = [HDWF, _types.c_int_p, _types.c_int_p]
FDwfAnalogInTriggerChannelInfo.restype = bool

FDwfAnalogInTriggerChannelSet = _dwf.FDwfAnalogInTriggerChannelSet
FDwfAnalogInTriggerChannelSet.argtypes = [HDWF, ctypes.c_int]
FDwfAnalogInTriggerChannelSet.restype = bool

FDwfAnalogInTriggerChannelGet = _dwf.FDwfAnalogInTriggerChannelGet
FDwfAnalogInTriggerChannelGet.argtypes = [HDWF, _types.c_int_p]
FDwfAnalogInTriggerChannelGet.restype = bool


FDwfAnalogInTriggerFilterInfo = _dwf.FDwfAnalogInTriggerFilterInfo  # use IsBitSet
FDwfAnalogInTriggerFilterInfo.argtypes = [HDWF, _types.c_int_p]
FDwfAnalogInTriggerFilterInfo.restype = bool

FDwfAnalogInTriggerFilterSet = _dwf.FDwfAnalogInTriggerFilterSet
FDwfAnalogInTriggerFilterSet.argtypes = [HDWF, FILTER]
FDwfAnalogInTriggerFilterSet.restype = bool

FDwfAnalogInTriggerFilterGet = _dwf.FDwfAnalogInTriggerFilterGet
FDwfAnalogInTriggerFilterGet.argtypes = [HDWF, ctypes.POINTER(FILTER)]
FDwfAnalogInTriggerFilterGet.restype = bool


FDwfAnalogInTriggerLevelInfo = _dwf.FDwfAnalogInTriggerLevelInfo
FDwfAnalogInTriggerLevelInfo.argtypes = [HDWF, _types.c_double_p, _types.c_double_p, _types.c_double_p]
FDwfAnalogInTriggerLevelInfo.restype = bool

FDwfAnalogInTriggerLevelSet = _dwf.FDwfAnalogInTriggerLevelSet
FDwfAnalogInTriggerLevelSet.argtypes = [HDWF, ctypes.c_double]
FDwfAnalogInTriggerLevelSet.restype = bool

FDwfAnalogInTriggerLevelGet = _dwf.FDwfAnalogInTriggerLevelGet
FDwfAnalogInTriggerLevelGet.argtypes = [HDWF, _types.c_double_p]
FDwfAnalogInTriggerLevelGet.restype = bool


FDwfAnalogInTriggerHysteresisInfo = _dwf.FDwfAnalogInTriggerHysteresisInfo
FDwfAnalogInTriggerHysteresisInfo.argtypes = [HDWF, _types.c_double_p, _types.c_double_p, _types.c_double_p]
FDwfAnalogInTriggerHysteresisInfo.restype = bool

FDwfAnalogInTriggerHysteresisSet = _dwf.FDwfAnalogInTriggerHysteresisSet
FDwfAnalogInTriggerHysteresisSet.argtypes = [HDWF, ctypes.c_double]
FDwfAnalogInTriggerHysteresisSet.restype = bool

FDwfAnalogInTriggerHysteresisGet = _dwf.FDwfAnalogInTriggerHysteresisGet
FDwfAnalogInTriggerHysteresisGet.argtypes = [HDWF, _types.c_double_p]
FDwfAnalogInTriggerHysteresisGet.restype = bool


FDwfAnalogInTriggerConditionInfo = _dwf.FDwfAnalogInTriggerConditionInfo  # use IsBitSet
FDwfAnalogInTriggerConditionInfo.argtypes = [HDWF, _types.c_int_p]
FDwfAnalogInTriggerConditionInfo.restype = bool

FDwfAnalogInTriggerConditionSet = _dwf.FDwfAnalogInTriggerConditionSet
FDwfAnalogInTriggerConditionSet.argtypes = [HDWF, TRIGCOND]
FDwfAnalogInTriggerConditionSet.restype = bool

FDwfAnalogInTriggerConditionGet = _dwf.FDwfAnalogInTriggerConditionGet
FDwfAnalogInTriggerConditionGet.argtypes = [HDWF, ctypes.POINTER(TRIGCOND)]
FDwfAnalogInTriggerConditionGet.restype = bool


FDwfAnalogInTriggerLengthInfo = _dwf.FDwfAnalogInTriggerLengthInfo
FDwfAnalogInTriggerLengthInfo.argtypes = [HDWF, _types.c_double_p, _types.c_double_p, _types.c_double_p]
FDwfAnalogInTriggerLengthInfo.restype = bool

FDwfAnalogInTriggerLengthSet = _dwf.FDwfAnalogInTriggerLengthSet
FDwfAnalogInTriggerLengthSet.argtypes = [HDWF, ctypes.c_double]
FDwfAnalogInTriggerLengthSet.restype = bool

FDwfAnalogInTriggerLengthGet = _dwf.FDwfAnalogInTriggerLengthGet
FDwfAnalogInTriggerLengthGet.argtypes = [HDWF, _types.c_double_p]
FDwfAnalogInTriggerLengthGet.restype = bool


FDwfAnalogInTriggerLengthConditionInfo = _dwf.FDwfAnalogInTriggerLengthConditionInfo  # use IsBitSet
FDwfAnalogInTriggerLengthConditionInfo.argtypes = [HDWF, _types.c_int_p]
FDwfAnalogInTriggerLengthConditionInfo.restype = bool

FDwfAnalogInTriggerLengthConditionSet = _dwf.FDwfAnalogInTriggerLengthConditionSet
FDwfAnalogInTriggerLengthConditionSet.argtypes = [HDWF, TRIGLEN]
FDwfAnalogInTriggerLengthConditionSet.restype = bool

FDwfAnalogInTriggerLengthConditionGet = _dwf.FDwfAnalogInTriggerLengthConditionGet
FDwfAnalogInTriggerLengthConditionGet.argtypes = [HDWF, ctypes.POINTER(TRIGLEN)]
FDwfAnalogInTriggerLengthConditionGet.restype = bool


# ANALOG OUT INSTRUMENT FUNCTIONS
# Configuration:
FDwfAnalogOutCount = _dwf.FDwfAnalogOutCount
FDwfAnalogOutCount.argtypes = [HDWF, _types.c_int_p]
FDwfAnalogOutCount.restype = bool


FDwfAnalogOutMasterSet = _dwf.FDwfAnalogOutMasterSet
FDwfAnalogOutMasterSet.argtypes = [HDWF, ctypes.c_int, ctypes.c_int]
FDwfAnalogOutMasterSet.restype = bool

FDwfAnalogOutMasterGet = _dwf.FDwfAnalogOutMasterGet
FDwfAnalogOutMasterGet.argtypes = [HDWF, ctypes.c_int, _types.c_int_p]
FDwfAnalogOutMasterGet.restype = bool


FDwfAnalogOutTriggerSourceInfo = _dwf.FDwfAnalogOutTriggerSourceInfo  # use IsBitSet
FDwfAnalogOutTriggerSourceInfo.argtypes = [HDWF, ctypes.c_int, _types.c_int_p]
FDwfAnalogOutTriggerSourceInfo.restype = bool

FDwfAnalogOutTriggerSourceSet = _dwf.FDwfAnalogOutTriggerSourceSet
FDwfAnalogOutTriggerSourceSet.argtypes = [HDWF, ctypes.c_int, TRIGSRC]
FDwfAnalogOutTriggerSourceSet.restype = bool

FDwfAnalogOutTriggerSourceGet = _dwf.FDwfAnalogOutTriggerSourceGet
FDwfAnalogOutTriggerSourceGet.argtypes = [HDWF, ctypes.c_int, ctypes.POINTER(TRIGSRC)]
FDwfAnalogOutTriggerSourceGet.restype = bool


FDwfAnalogOutRunInfo = _dwf.FDwfAnalogOutRunInfo
FDwfAnalogOutRunInfo.argtypes = [HDWF, ctypes.c_int, _types.c_double_p, _types.c_double_p]
FDwfAnalogOutRunInfo.restype = bool

FDwfAnalogOutRunSet = _dwf.FDwfAnalogOutRunSet
FDwfAnalogOutRunSet.argtypes = [HDWF, ctypes.c_int, ctypes.c_double]
FDwfAnalogOutRunSet.restype = bool

FDwfAnalogOutRunGet = _dwf.FDwfAnalogOutRunGet
FDwfAnalogOutRunGet.argtypes = [HDWF, ctypes.c_int, _types.c_double_p]
FDwfAnalogOutRunGet.restype = bool

FDwfAnalogOutRunStatus = _dwf.FDwfAnalogOutRunStatus
FDwfAnalogOutRunStatus.argtypes = [HDWF, ctypes.c_int, _types.c_double_p]
FDwfAnalogOutRunStatus.restype = bool


FDwfAnalogOutWaitInfo = _dwf.FDwfAnalogOutWaitInfo
FDwfAnalogOutWaitInfo.argtypes = [HDWF, ctypes.c_int, _types.c_double_p, _types.c_double_p]
FDwfAnalogOutWaitInfo.restype = bool

FDwfAnalogOutWaitSet = _dwf.FDwfAnalogOutWaitSet
FDwfAnalogOutWaitSet.argtypes = [HDWF, ctypes.c_int, ctypes.c_double]
FDwfAnalogOutWaitSet.restype = bool

FDwfAnalogOutWaitGet = _dwf.FDwfAnalogOutWaitGet
FDwfAnalogOutWaitGet.argtypes = [HDWF, ctypes.c_int, _types.c_double_p]
FDwfAnalogOutWaitGet.restype = bool


FDwfAnalogOutRepeatInfo = _dwf.FDwfAnalogOutRepeatInfo
FDwfAnalogOutRepeatInfo.argtypes = [HDWF, ctypes.c_int, _types.c_int_p, _types.c_int_p]
FDwfAnalogOutRepeatInfo.restype = bool

FDwfAnalogOutRepeatSet = _dwf.FDwfAnalogOutRepeatSet
FDwfAnalogOutRepeatSet.argtypes = [HDWF, ctypes.c_int, ctypes.c_int]
FDwfAnalogOutRepeatSet.restype = bool

FDwfAnalogOutRepeatGet = _dwf.FDwfAnalogOutRepeatGet
FDwfAnalogOutRepeatGet.argtypes = [HDWF, ctypes.c_int, _types.c_int_p]
FDwfAnalogOutRepeatGet.restype = bool

FDwfAnalogOutRepeatStatus = _dwf.FDwfAnalogOutRepeatStatus
FDwfAnalogOutRepeatStatus.argtypes = [HDWF, ctypes.c_int, _types.c_int_p]
FDwfAnalogOutRepeatStatus.restype = bool


FDwfAnalogOutRepeatTriggerSet = _dwf.FDwfAnalogOutRepeatTriggerSet
FDwfAnalogOutRepeatTriggerSet.argtypes = [HDWF, ctypes.c_int, ctypes.c_byte]
FDwfAnalogOutRepeatTriggerSet.restype = bool

FDwfAnalogOutRepeatTriggerGet = _dwf.FDwfAnalogOutRepeatTriggerGet
FDwfAnalogOutRepeatTriggerGet.argtypes = [HDWF, ctypes.c_int, _types.c_byte_p]
FDwfAnalogOutRepeatTriggerGet.restype = bool


FDwfAnalogOutNodeInfo = _dwf.FDwfAnalogOutNodeInfo  # use IsBitSet
FDwfAnalogOutNodeInfo.argtypes = [HDWF, ctypes.c_int, _types.c_int_p]
FDwfAnalogOutNodeInfo.restype = bool


FDwfAnalogOutNodeEnableSet = _dwf.FDwfAnalogOutNodeEnableSet
FDwfAnalogOutNodeEnableSet.argtypes = [HDWF, ctypes.c_int, AnalogOutNode, ctypes.c_byte]
FDwfAnalogOutNodeEnableSet.restype = bool

FDwfAnalogOutNodeEnableGet = _dwf.FDwfAnalogOutNodeEnableGet
FDwfAnalogOutNodeEnableGet.argtypes = [HDWF, ctypes.c_int, AnalogOutNode, _types.c_byte_p]
FDwfAnalogOutNodeEnableGet.restype = bool


FDwfAnalogOutNodeFunctionInfo = _dwf.FDwfAnalogOutNodeFunctionInfo  # use IsBitSet
FDwfAnalogOutNodeFunctionInfo.argtypes = [HDWF, ctypes.c_int, AnalogOutNode, _types.c_int_p]
FDwfAnalogOutNodeFunctionInfo.restype = bool

FDwfAnalogOutNodeFunctionSet = _dwf.FDwfAnalogOutNodeFunctionSet
FDwfAnalogOutNodeFunctionSet.argtypes = [HDWF, ctypes.c_int, AnalogOutNode, FUNC]
FDwfAnalogOutNodeFunctionSet.restype = bool

FDwfAnalogOutNodeFunctionGet = _dwf.FDwfAnalogOutNodeFunctionGet
FDwfAnalogOutNodeFunctionGet.argtypes = [HDWF, ctypes.c_int, AnalogOutNode, ctypes.POINTER(FUNC)]
FDwfAnalogOutNodeFunctionGet.restype = bool


FDwfAnalogOutNodeFrequencyInfo = _dwf.FDwfAnalogOutNodeFrequencyInfo
FDwfAnalogOutNodeFrequencyInfo.argtypes = [HDWF, ctypes.c_int, AnalogOutNode, _types.c_double_p, _types.c_double_p]
FDwfAnalogOutNodeFrequencyInfo.restype = bool

FDwfAnalogOutNodeFrequencySet = _dwf.FDwfAnalogOutNodeFrequencySet
FDwfAnalogOutNodeFrequencySet.argtypes = [HDWF, ctypes.c_int, AnalogOutNode, ctypes.c_double]
FDwfAnalogOutNodeFrequencySet.restype = bool

FDwfAnalogOutNodeFrequencyGet = _dwf.FDwfAnalogOutNodeFrequencyGet
FDwfAnalogOutNodeFrequencyGet.argtypes = [HDWF, ctypes.c_int, AnalogOutNode, _types.c_double_p]
FDwfAnalogOutNodeFrequencyGet.restype = bool

# Carrier Amplitude or Modulation Index
FDwfAnalogOutNodeAmplitudeInfo = _dwf.FDwfAnalogOutNodeAmplitudeInfo
FDwfAnalogOutNodeAmplitudeInfo.argtypes = [HDWF, ctypes.c_int, AnalogOutNode, _types.c_double_p, _types.c_double_p]
FDwfAnalogOutNodeAmplitudeInfo.restype = bool

FDwfAnalogOutNodeAmplitudeSet = _dwf.FDwfAnalogOutNodeAmplitudeSet
FDwfAnalogOutNodeAmplitudeSet.argtypes = [HDWF, ctypes.c_int, AnalogOutNode, ctypes.c_double]
FDwfAnalogOutNodeAmplitudeSet.restype = bool

FDwfAnalogOutNodeAmplitudeGet = _dwf.FDwfAnalogOutNodeAmplitudeGet
FDwfAnalogOutNodeAmplitudeGet.argtypes = [HDWF, ctypes.c_int, AnalogOutNode, _types.c_double_p]
FDwfAnalogOutNodeAmplitudeGet.restype = bool


FDwfAnalogOutNodeOffsetInfo = _dwf.FDwfAnalogOutNodeOffsetInfo
FDwfAnalogOutNodeOffsetInfo.argtypes = [HDWF, ctypes.c_int, AnalogOutNode, _types.c_double_p, _types.c_double_p]
FDwfAnalogOutNodeOffsetInfo.restype = bool

FDwfAnalogOutNodeOffsetSet = _dwf.FDwfAnalogOutNodeOffsetSet
FDwfAnalogOutNodeOffsetSet.argtypes = [HDWF, ctypes.c_int, AnalogOutNode, ctypes.c_double]
FDwfAnalogOutNodeOffsetSet.restype = bool

FDwfAnalogOutNodeOffsetGet = _dwf.FDwfAnalogOutNodeOffsetGet
FDwfAnalogOutNodeOffsetGet.argtypes = [HDWF, ctypes.c_int, AnalogOutNode, _types.c_double_p]
FDwfAnalogOutNodeOffsetGet.restype = bool


FDwfAnalogOutNodeSymmetryInfo = _dwf.FDwfAnalogOutNodeSymmetryInfo
FDwfAnalogOutNodeSymmetryInfo.argtypes = [HDWF, ctypes.c_int, AnalogOutNode, _types.c_double_p, _types.c_double_p]
FDwfAnalogOutNodeSymmetryInfo.restype = bool

FDwfAnalogOutNodeSymmetrySet = _dwf.FDwfAnalogOutNodeSymmetrySet
FDwfAnalogOutNodeSymmetrySet.argtypes = [HDWF, ctypes.c_int, AnalogOutNode, ctypes.c_double]
FDwfAnalogOutNodeSymmetrySet.restype = bool

FDwfAnalogOutNodeSymmetryGet = _dwf.FDwfAnalogOutNodeSymmetryGet
FDwfAnalogOutNodeSymmetryGet.argtypes = [HDWF, ctypes.c_int, AnalogOutNode, _types.c_double_p]
FDwfAnalogOutNodeSymmetryGet.restype = bool


FDwfAnalogOutNodePhaseInfo = _dwf.FDwfAnalogOutNodePhaseInfo
FDwfAnalogOutNodePhaseInfo.argtypes = [HDWF, ctypes.c_int, AnalogOutNode, _types.c_double_p, _types.c_double_p]
FDwfAnalogOutNodePhaseInfo.restype = bool

FDwfAnalogOutNodePhaseSet = _dwf.FDwfAnalogOutNodePhaseSet
FDwfAnalogOutNodePhaseSet.argtypes = [HDWF, ctypes.c_int, AnalogOutNode, ctypes.c_double]
FDwfAnalogOutNodePhaseSet.restype = bool

FDwfAnalogOutNodePhaseGet = _dwf.FDwfAnalogOutNodePhaseGet
FDwfAnalogOutNodePhaseGet.argtypes = [HDWF, ctypes.c_int, AnalogOutNode, _types.c_double_p]
FDwfAnalogOutNodePhaseGet.restype = bool


FDwfAnalogOutNodeDataInfo = _dwf.FDwfAnalogOutNodeDataInfo
FDwfAnalogOutNodeDataInfo.argtypes = [HDWF, ctypes.c_int, AnalogOutNode, _types.c_int_p, _types.c_int_p]
FDwfAnalogOutNodeDataInfo.restype = bool

FDwfAnalogOutNodeDataSet = _dwf.FDwfAnalogOutNodeDataSet
FDwfAnalogOutNodeDataSet.argtypes = [HDWF, ctypes.c_int, AnalogOutNode, _types.c_double_p, ctypes.c_int]
FDwfAnalogOutNodeDataSet.restype = bool


# needed for EExplorer, don't care for ADiscovery
FDwfAnalogOutCustomAMFMEnableSet = _dwf.FDwfAnalogOutCustomAMFMEnableSet
FDwfAnalogOutCustomAMFMEnableSet.argtypes = [HDWF, ctypes.c_int, ctypes.c_byte]
FDwfAnalogOutCustomAMFMEnableSet.restype = bool

FDwfAnalogOutCustomAMFMEnableGet = _dwf.FDwfAnalogOutCustomAMFMEnableGet
FDwfAnalogOutCustomAMFMEnableGet.argtypes = [HDWF, ctypes.c_int, _types.c_byte_p]
FDwfAnalogOutCustomAMFMEnableGet.restype = bool


# Control:
FDwfAnalogOutReset = _dwf.FDwfAnalogOutReset
FDwfAnalogOutReset.argtypes = [HDWF, ctypes.c_int]
FDwfAnalogOutReset.restype = bool

FDwfAnalogOutConfigure = _dwf.FDwfAnalogOutConfigure
FDwfAnalogOutConfigure.argtypes = [HDWF, ctypes.c_int, ctypes.c_byte]
FDwfAnalogOutConfigure.restype = bool

FDwfAnalogOutStatus = _dwf.FDwfAnalogOutStatus
FDwfAnalogOutStatus.argtypes = [HDWF, ctypes.c_int, ctypes.POINTER(DwfState)]
FDwfAnalogOutStatus.restype = bool

FDwfAnalogOutNodePlayStatus = _dwf.FDwfAnalogOutNodePlayStatus
FDwfAnalogOutNodePlayStatus.argtypes = [HDWF, ctypes.c_int, AnalogOutNode, _types.c_int_p, _types.c_int_p, _types.c_int_p]
FDwfAnalogOutNodePlayStatus.restype = bool

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
FDwfAnalogIOEnableInfo = _dwf.FDwfAnalogIOEnableInfo
FDwfAnalogIOEnableInfo.argtypes = [HDWF, _types.c_byte_p, _types.c_byte_p]
FDwfAnalogIOEnableInfo.restype = bool

FDwfAnalogIOEnableSet = _dwf.FDwfAnalogIOEnableSet
FDwfAnalogIOEnableSet.argtypes = [HDWF, ctypes.c_byte]
FDwfAnalogIOEnableSet.restype = bool

FDwfAnalogIOEnableGet = _dwf.FDwfAnalogIOEnableGet
FDwfAnalogIOEnableGet.argtypes = [HDWF, _types.c_byte_p]
FDwfAnalogIOEnableGet.restype = bool

FDwfAnalogIOEnableStatus = _dwf.FDwfAnalogIOEnableStatus
FDwfAnalogIOEnableStatus.argtypes = [HDWF, _types.c_byte_p]
FDwfAnalogIOEnableStatus.restype = bool

FDwfAnalogIOChannelCount = _dwf.FDwfAnalogIOChannelCount
FDwfAnalogIOChannelCount.argtypes = [HDWF, _types.c_int_p]
FDwfAnalogIOChannelCount.restype = bool

FDwfAnalogIOChannelName = _dwf.FDwfAnalogIOChannelName
FDwfAnalogIOChannelName.argtypes = [HDWF, ctypes.c_int, ctypes.POINTER(ctypes.c_char * 32), ctypes.POINTER(ctypes.c_char * 16)]
FDwfAnalogIOChannelName.restype = bool

FDwfAnalogIOChannelInfo = _dwf.FDwfAnalogIOChannelInfo
FDwfAnalogIOChannelInfo.argtypes = [HDWF, ctypes.c_int, _types.c_int_p]
FDwfAnalogIOChannelInfo.restype = bool

FDwfAnalogIOChannelNodeName = _dwf.FDwfAnalogIOChannelNodeName
FDwfAnalogIOChannelNodeName.argtypes = [HDWF, ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.c_char * 32), ctypes.POINTER(ctypes.c_char * 16)]
FDwfAnalogIOChannelNodeName.restype = bool

FDwfAnalogIOChannelNodeInfo = _dwf.FDwfAnalogIOChannelNodeInfo
FDwfAnalogIOChannelNodeInfo.argtypes = [HDWF, ctypes.c_int, ctypes.c_int, ctypes.POINTER(ANALOGIO)]
FDwfAnalogIOChannelNodeInfo.restype = bool

FDwfAnalogIOChannelNodeSetInfo = _dwf.FDwfAnalogIOChannelNodeSetInfo
FDwfAnalogIOChannelNodeSetInfo.argtypes = [HDWF, ctypes.c_int, ctypes.c_int, _types.c_double_p, _types.c_double_p, _types.c_double_p]
FDwfAnalogIOChannelNodeSetInfo.restype = bool

FDwfAnalogIOChannelNodeSet = _dwf.FDwfAnalogIOChannelNodeSet
FDwfAnalogIOChannelNodeSet.argtypes = [HDWF, ctypes.c_int, ctypes.c_int, ctypes.c_double]
FDwfAnalogIOChannelNodeSet.restype = bool

FDwfAnalogIOChannelNodeGet = _dwf.FDwfAnalogIOChannelNodeGet
FDwfAnalogIOChannelNodeGet.argtypes = [HDWF, ctypes.c_int, ctypes.c_int, _types.c_double_p]
FDwfAnalogIOChannelNodeGet.restype = bool

FDwfAnalogIOChannelNodeStatusInfo = _dwf.FDwfAnalogIOChannelNodeStatusInfo
FDwfAnalogIOChannelNodeStatusInfo.argtypes = [HDWF, ctypes.c_int, ctypes.c_int, _types.c_double_p, _types.c_double_p, _types.c_double_p]
FDwfAnalogIOChannelNodeStatusInfo.restype = bool

FDwfAnalogIOChannelNodeStatus = _dwf.FDwfAnalogIOChannelNodeStatus
FDwfAnalogIOChannelNodeStatus.argtypes = [HDWF, ctypes.c_int, ctypes.c_int, _types.c_double_p]
FDwfAnalogIOChannelNodeStatus.restype = bool



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
FDwfDigitalIOOutputEnableInfo = _dwf.FDwfDigitalIOOutputEnableInfo
FDwfDigitalIOOutputEnableInfo.argtypes = [HDWF, _types.c_uint_p]
FDwfDigitalIOOutputEnableInfo.restype = bool

FDwfDigitalIOOutputEnableSet = _dwf.FDwfDigitalIOOutputEnableSet
FDwfDigitalIOOutputEnableSet.argtypes = [HDWF, ctypes.c_uint]
FDwfDigitalIOOutputEnableSet.restype = bool

FDwfDigitalIOOutputEnableGet = _dwf.FDwfDigitalIOOutputEnableGet
FDwfDigitalIOOutputEnableGet.argtypes = [HDWF, _types.c_uint_p]
FDwfDigitalIOOutputEnableGet.restype = bool

FDwfDigitalIOOutputInfo = _dwf.FDwfDigitalIOOutputInfo
FDwfDigitalIOOutputInfo.argtypes = [HDWF, _types.c_uint_p]
FDwfDigitalIOOutputInfo.restype = bool

FDwfDigitalIOOutputSet = _dwf.FDwfDigitalIOOutputSet
FDwfDigitalIOOutputSet.argtypes = [HDWF, ctypes.c_uint]
FDwfDigitalIOOutputSet.restype = bool

FDwfDigitalIOOutputGet = _dwf.FDwfDigitalIOOutputGet
FDwfDigitalIOOutputGet.argtypes = [HDWF, _types.c_uint_p]
FDwfDigitalIOOutputGet.restype = bool

FDwfDigitalIOInputInfo = _dwf.FDwfDigitalIOInputInfo
FDwfDigitalIOInputInfo.argtypes = [HDWF, _types.c_uint_p]
FDwfDigitalIOInputInfo.restype = bool

FDwfDigitalIOInputStatus = _dwf.FDwfDigitalIOInputStatus
FDwfDigitalIOInputStatus.argtypes = [HDWF, _types.c_uint_p]
FDwfDigitalIOInputStatus.restype = bool



# DIGITAL IN INSTRUMENT FUNCTIONS
# Control and status:
FDwfDigitalInReset = _dwf.FDwfDigitalInReset
FDwfDigitalInReset.argtypes = [HDWF]
FDwfDigitalInReset.restype = bool

FDwfDigitalInConfigure = _dwf.FDwfDigitalInConfigure
FDwfDigitalInConfigure.argtypes = [HDWF, ctypes.c_byte, ctypes.c_byte]
FDwfDigitalInConfigure.restype = bool

FDwfDigitalInStatus = _dwf.FDwfDigitalInStatus
FDwfDigitalInStatus.argtypes = [HDWF, ctypes.c_byte, ctypes.POINTER(DwfState)]
FDwfDigitalInStatus.restype = bool

FDwfDigitalInStatusSamplesLeft = _dwf.FDwfDigitalInStatusSamplesLeft
FDwfDigitalInStatusSamplesLeft.argtypes = [HDWF, _types.c_int_p]
FDwfDigitalInStatusSamplesLeft.restype = bool

FDwfDigitalInStatusSamplesValid = _dwf.FDwfDigitalInStatusSamplesValid
FDwfDigitalInStatusSamplesValid.argtypes = [HDWF, _types.c_int_p]
FDwfDigitalInStatusSamplesValid.restype = bool

FDwfDigitalInStatusIndexWrite = _dwf.FDwfDigitalInStatusIndexWrite
FDwfDigitalInStatusIndexWrite.argtypes = [HDWF, _types.c_int_p]
FDwfDigitalInStatusIndexWrite.restype = bool

FDwfDigitalInStatusAutoTriggered = _dwf.FDwfDigitalInStatusAutoTriggered
FDwfDigitalInStatusAutoTriggered.argtypes = [HDWF, _types.c_byte_p]
FDwfDigitalInStatusAutoTriggered.restype = bool

FDwfDigitalInStatusData = _dwf.FDwfDigitalInStatusData
FDwfDigitalInStatusData.argtypes = [HDWF, ctypes.c_void_p, ctypes.c_int]
FDwfDigitalInStatusData.restype = bool


# Acquistion configuration:
FDwfDigitalInInternalClockInfo = _dwf.FDwfDigitalInInternalClockInfo
FDwfDigitalInInternalClockInfo.argtypes = [HDWF, _types.c_double_p]
FDwfDigitalInInternalClockInfo.restype = bool


FDwfDigitalInClockSourceInfo = _dwf.FDwfDigitalInClockSourceInfo
FDwfDigitalInClockSourceInfo.argtypes = [HDWF, _types.c_int_p]  # use IsBitSet
FDwfDigitalInClockSourceInfo.restype = bool

FDwfDigitalInClockSourceSet = _dwf.FDwfDigitalInClockSourceSet
FDwfDigitalInClockSourceSet.argtypes = [HDWF, DwfDigitalInClockSource]
FDwfDigitalInClockSourceSet.restype = bool

FDwfDigitalInClockSourceGet = _dwf.FDwfDigitalInClockSourceGet
FDwfDigitalInClockSourceGet.argtypes = [HDWF, ctypes.POINTER(DwfDigitalInClockSource)]
FDwfDigitalInClockSourceGet.restype = bool


FDwfDigitalInDividerInfo = _dwf.FDwfDigitalInDividerInfo
FDwfDigitalInDividerInfo.argtypes = [HDWF, _types.c_uint_p]
FDwfDigitalInDividerInfo.restype = bool

FDwfDigitalInDividerSet = _dwf.FDwfDigitalInDividerSet
FDwfDigitalInDividerSet.argtypes = [HDWF, ctypes.c_uint]
FDwfDigitalInDividerSet.restype = bool

FDwfDigitalInDividerGet = _dwf.FDwfDigitalInDividerGet
FDwfDigitalInDividerGet.argtypes = [HDWF, _types.c_uint_p]
FDwfDigitalInDividerGet.restype = bool


FDwfDigitalInBitsInfo = _dwf.FDwfDigitalInBitsInfo  # Returns the number of Digital In bits
FDwfDigitalInBitsInfo.argtypes = [HDWF, _types.c_int_p]
FDwfDigitalInBitsInfo.restype = bool

FDwfDigitalInSampleFormatSet = _dwf.FDwfDigitalInSampleFormatSet  # valid options 8/16/32
FDwfDigitalInSampleFormatSet.argtypes = [HDWF, ctypes.c_int]
FDwfDigitalInSampleFormatSet.restype = bool

FDwfDigitalInSampleFormatGet = _dwf.FDwfDigitalInSampleFormatGet
FDwfDigitalInSampleFormatGet.argtypes = [HDWF, _types.c_int_p]
FDwfDigitalInSampleFormatGet.restype = bool


FDwfDigitalInBufferSizeInfo = _dwf.FDwfDigitalInBufferSizeInfo
FDwfDigitalInBufferSizeInfo.argtypes = [HDWF, _types.c_int_p]
FDwfDigitalInBufferSizeInfo.restype = bool

FDwfDigitalInBufferSizeSet = _dwf.FDwfDigitalInBufferSizeSet
FDwfDigitalInBufferSizeSet.argtypes = [HDWF, ctypes.c_int]
FDwfDigitalInBufferSizeSet.restype = bool

FDwfDigitalInBufferSizeGet = _dwf.FDwfDigitalInBufferSizeGet
FDwfDigitalInBufferSizeGet.argtypes = [HDWF, _types.c_int_p]
FDwfDigitalInBufferSizeGet.restype = bool


FDwfDigitalInSampleModeInfo = _dwf.FDwfDigitalInSampleModeInfo  # use IsBitSet
FDwfDigitalInSampleModeInfo.argtypes = [HDWF, _types.c_int_p]
FDwfDigitalInSampleModeInfo.restype = bool

FDwfDigitalInSampleModeSet = _dwf.FDwfDigitalInSampleModeSet
FDwfDigitalInSampleModeSet.argtypes = [HDWF, DwfDigitalInSampleMode]
FDwfDigitalInSampleModeSet.restype = bool

FDwfDigitalInSampleModeGet = _dwf.FDwfDigitalInSampleModeGet
FDwfDigitalInSampleModeGet.argtypes = [HDWF, ctypes.POINTER(DwfDigitalInSampleMode)]
FDwfDigitalInSampleModeGet.restype = bool


FDwfDigitalInAcquisitionModeInfo = _dwf.FDwfDigitalInAcquisitionModeInfo  # use IsBitSet
FDwfDigitalInAcquisitionModeInfo.argtypes = [HDWF, _types.c_int_p]
FDwfDigitalInAcquisitionModeInfo.restype = bool

FDwfDigitalInAcquisitionModeSet = _dwf.FDwfDigitalInAcquisitionModeSet
FDwfDigitalInAcquisitionModeSet.argtypes = [HDWF, ACQMODE]
FDwfDigitalInAcquisitionModeSet.restype = bool

FDwfDigitalInAcquisitionModeGet = _dwf.FDwfDigitalInAcquisitionModeGet
FDwfDigitalInAcquisitionModeGet.argtypes = [HDWF, ctypes.POINTER(ACQMODE)]
FDwfDigitalInAcquisitionModeGet.restype = bool


# Trigger configuration:
FDwfDigitalInTriggerSourceInfo = _dwf.FDwfDigitalInTriggerSourceInfo  # use IsBitSet
FDwfDigitalInTriggerSourceInfo.argtypes = [HDWF, _types.c_int_p]
FDwfDigitalInTriggerSourceInfo.restype = bool

FDwfDigitalInTriggerSourceSet = _dwf.FDwfDigitalInTriggerSourceSet
FDwfDigitalInTriggerSourceSet.argtypes = [HDWF, TRIGSRC]
FDwfDigitalInTriggerSourceSet.restype = bool

FDwfDigitalInTriggerSourceGet = _dwf.FDwfDigitalInTriggerSourceGet
FDwfDigitalInTriggerSourceGet.argtypes = [HDWF, ctypes.POINTER(TRIGSRC)]
FDwfDigitalInTriggerSourceGet.restype = bool


FDwfDigitalInTriggerPositionInfo = _dwf.FDwfDigitalInTriggerPositionInfo
FDwfDigitalInTriggerPositionInfo.argtypes = [HDWF, _types.c_uint_p]
FDwfDigitalInTriggerPositionInfo.restype = bool

FDwfDigitalInTriggerPositionSet = _dwf.FDwfDigitalInTriggerPositionSet
FDwfDigitalInTriggerPositionSet.argtypes = [HDWF, ctypes.c_uint]
FDwfDigitalInTriggerPositionSet.restype = bool

FDwfDigitalInTriggerPositionGet = _dwf.FDwfDigitalInTriggerPositionGet
FDwfDigitalInTriggerPositionGet.argtypes = [HDWF, _types.c_uint_p]
FDwfDigitalInTriggerPositionGet.restype = bool


FDwfDigitalInTriggerAutoTimeoutInfo = _dwf.FDwfDigitalInTriggerAutoTimeoutInfo
FDwfDigitalInTriggerAutoTimeoutInfo.argtypes = [HDWF, _types.c_double_p, _types.c_double_p, _types.c_double_p]
FDwfDigitalInTriggerAutoTimeoutInfo.restype = bool

FDwfDigitalInTriggerAutoTimeoutSet = _dwf.FDwfDigitalInTriggerAutoTimeoutSet
FDwfDigitalInTriggerAutoTimeoutSet.argtypes = [HDWF, ctypes.c_double]
FDwfDigitalInTriggerAutoTimeoutSet.restype = bool

FDwfDigitalInTriggerAutoTimeoutGet = _dwf.FDwfDigitalInTriggerAutoTimeoutGet
FDwfDigitalInTriggerAutoTimeoutGet.argtypes = [HDWF, _types.c_double_p]
FDwfDigitalInTriggerAutoTimeoutGet.restype = bool


FDwfDigitalInTriggerInfo = _dwf.FDwfDigitalInTriggerInfo
FDwfDigitalInTriggerInfo.argtypes = [HDWF, _types.c_uint_p, _types.c_uint_p, _types.c_uint_p, _types.c_uint_p]
FDwfDigitalInTriggerInfo.restype = bool

FDwfDigitalInTriggerSet = _dwf.FDwfDigitalInTriggerSet
FDwfDigitalInTriggerSet.argtypes = [HDWF, ctypes.c_uint, ctypes.c_uint, ctypes.c_uint, ctypes.c_uint]
FDwfDigitalInTriggerSet.restype = bool

FDwfDigitalInTriggerGet = _dwf.FDwfDigitalInTriggerGet
FDwfDigitalInTriggerGet.argtypes = [HDWF, _types.c_uint_p, _types.c_uint_p, _types.c_uint_p, _types.c_uint_p]
FDwfDigitalInTriggerGet.restype = bool

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

FDwfDigitalOutStatus = _dwf.FDwfDigitalOutStatus
FDwfDigitalOutStatus.argtypes = [HDWF, ctypes.POINTER(DwfState)]
FDwfDigitalOutStatus.restype = bool


# Configuration:
FDwfDigitalOutInternalClockInfo = _dwf.FDwfDigitalOutInternalClockInfo
FDwfDigitalOutInternalClockInfo.argtypes = [HDWF, _types.c_double_p]
FDwfDigitalOutInternalClockInfo.restype = bool


FDwfDigitalOutTriggerSourceInfo = _dwf.FDwfDigitalOutTriggerSourceInfo  # use IsBitSet
FDwfDigitalOutTriggerSourceInfo.argtypes = [HDWF, _types.c_int_p]
FDwfDigitalOutTriggerSourceInfo.restype = bool

FDwfDigitalOutTriggerSourceSet = _dwf.FDwfDigitalOutTriggerSourceSet
FDwfDigitalOutTriggerSourceSet.argtypes = [HDWF, TRIGSRC]
FDwfDigitalOutTriggerSourceSet.restype = bool

FDwfDigitalOutTriggerSourceGet = _dwf.FDwfDigitalOutTriggerSourceGet
FDwfDigitalOutTriggerSourceGet.argtypes = [HDWF, ctypes.POINTER(TRIGSRC)]
FDwfDigitalOutTriggerSourceGet.restype = bool


FDwfDigitalOutRunInfo = _dwf.FDwfDigitalOutRunInfo
FDwfDigitalOutRunInfo.argtypes = [HDWF, _types.c_double_p, _types.c_double_p]
FDwfDigitalOutRunInfo.restype = bool

FDwfDigitalOutRunSet = _dwf.FDwfDigitalOutRunSet
FDwfDigitalOutRunSet.argtypes = [HDWF, ctypes.c_double]
FDwfDigitalOutRunSet.restype = bool

FDwfDigitalOutRunGet = _dwf.FDwfDigitalOutRunGet
FDwfDigitalOutRunGet.argtypes = [HDWF, _types.c_double_p]
FDwfDigitalOutRunGet.restype = bool

FDwfDigitalOutRunStatus = _dwf.FDwfDigitalOutRunStatus
FDwfDigitalOutRunStatus.argtypes = [HDWF, _types.c_double_p]
FDwfDigitalOutRunStatus.restype = bool


FDwfDigitalOutWaitInfo = _dwf.FDwfDigitalOutWaitInfo
FDwfDigitalOutWaitInfo.argtypes = [HDWF, _types.c_double_p, _types.c_double_p]
FDwfDigitalOutWaitInfo.restype = bool

FDwfDigitalOutWaitSet = _dwf.FDwfDigitalOutWaitSet
FDwfDigitalOutWaitSet.argtypes = [HDWF, ctypes.c_double]
FDwfDigitalOutWaitSet.restype = bool

FDwfDigitalOutWaitGet = _dwf.FDwfDigitalOutWaitGet
FDwfDigitalOutWaitGet.argtypes = [HDWF, _types.c_double_p]
FDwfDigitalOutWaitGet.restype = bool


FDwfDigitalOutRepeatInfo = _dwf.FDwfDigitalOutRepeatInfo
FDwfDigitalOutRepeatInfo.argtypes = [HDWF, _types.c_uint_p, _types.c_uint_p]
FDwfDigitalOutRepeatInfo.restype = bool

FDwfDigitalOutRepeatSet = _dwf.FDwfDigitalOutRepeatSet
FDwfDigitalOutRepeatSet.argtypes = [HDWF, ctypes.c_uint]
FDwfDigitalOutRepeatSet.restype = bool

FDwfDigitalOutRepeatGet = _dwf.FDwfDigitalOutRepeatGet
FDwfDigitalOutRepeatGet.argtypes = [HDWF, _types.c_uint_p]
FDwfDigitalOutRepeatGet.restype = bool

FDwfDigitalOutRepeatStatus = _dwf.FDwfDigitalOutRepeatStatus
FDwfDigitalOutRepeatStatus.argtypes = [HDWF, _types.c_uint_p]
FDwfDigitalOutRepeatStatus.restype = bool


FDwfDigitalOutRepeatTriggerSet = _dwf.FDwfDigitalOutRepeatTriggerSet
FDwfDigitalOutRepeatTriggerSet.argtypes = [HDWF, ctypes.c_byte]
FDwfDigitalOutRepeatTriggerSet.restype = bool

FDwfDigitalOutRepeatTriggerGet = _dwf.FDwfDigitalOutRepeatTriggerGet
FDwfDigitalOutRepeatTriggerGet.argtypes = [HDWF, _types.c_byte_p]
FDwfDigitalOutRepeatTriggerGet.restype = bool


FDwfDigitalOutCount = _dwf.FDwfDigitalOutCount
FDwfDigitalOutCount.argtypes = [HDWF, _types.c_int_p]
FDwfDigitalOutCount.restype = bool

FDwfDigitalOutEnableSet = _dwf.FDwfDigitalOutEnableSet
FDwfDigitalOutEnableSet.argtypes = [HDWF, ctypes.c_int, ctypes.c_byte]
FDwfDigitalOutEnableSet.restype = bool

FDwfDigitalOutEnableGet = _dwf.FDwfDigitalOutEnableGet
FDwfDigitalOutEnableGet.argtypes = [HDWF, ctypes.c_int, _types.c_byte_p]
FDwfDigitalOutEnableGet.restype = bool


FDwfDigitalOutOutputInfo = _dwf.FDwfDigitalOutOutputInfo  # use IsBitSet
FDwfDigitalOutOutputInfo.argtypes = [HDWF, ctypes.c_int, _types.c_int_p]
FDwfDigitalOutOutputInfo.restype = bool

FDwfDigitalOutOutputSet = _dwf.FDwfDigitalOutOutputSet
FDwfDigitalOutOutputSet.argtypes = [HDWF, ctypes.c_int, DwfDigitalOutOutput]
FDwfDigitalOutOutputSet.restype = bool

FDwfDigitalOutOutputGet = _dwf.FDwfDigitalOutOutputGet
FDwfDigitalOutOutputGet.argtypes = [HDWF, ctypes.c_int, ctypes.POINTER(DwfDigitalOutOutput)]
FDwfDigitalOutOutputGet.restype = bool


FDwfDigitalOutTypeInfo = _dwf.FDwfDigitalOutTypeInfo  # use IsBitSet
FDwfDigitalOutTypeInfo.argtypes = [HDWF, ctypes.c_int, _types.c_int_p]
FDwfDigitalOutTypeInfo.restype = bool

FDwfDigitalOutTypeSet = _dwf.FDwfDigitalOutTypeSet
FDwfDigitalOutTypeSet.argtypes = [HDWF, ctypes.c_int, DwfDigitalOutType]
FDwfDigitalOutTypeSet.restype = bool

FDwfDigitalOutTypeGet = _dwf.FDwfDigitalOutTypeGet
FDwfDigitalOutTypeGet.argtypes = [HDWF, ctypes.c_int, ctypes.POINTER(DwfDigitalOutType)]
FDwfDigitalOutTypeGet.restype = bool


FDwfDigitalOutIdleInfo = _dwf.FDwfDigitalOutIdleInfo  # use IsBitSet
FDwfDigitalOutIdleInfo.argtypes = [HDWF, ctypes.c_int, _types.c_int_p]
FDwfDigitalOutIdleInfo.restype = bool

FDwfDigitalOutIdleSet = _dwf.FDwfDigitalOutIdleSet
FDwfDigitalOutIdleSet.argtypes = [HDWF, ctypes.c_int, DwfDigitalOutIdle]
FDwfDigitalOutIdleSet.restype = bool

FDwfDigitalOutIdleGet = _dwf.FDwfDigitalOutIdleGet
FDwfDigitalOutIdleGet.argtypes = [HDWF, ctypes.c_int, ctypes.POINTER(DwfDigitalOutIdle)]
FDwfDigitalOutIdleGet.restype = bool


FDwfDigitalOutDividerInfo = _dwf.FDwfDigitalOutDividerInfo
FDwfDigitalOutDividerInfo.argtypes = [HDWF, ctypes.c_int, _types.c_uint_p, _types.c_uint_p]
FDwfDigitalOutDividerInfo.restype = bool

FDwfDigitalOutDividerInitSet = _dwf.FDwfDigitalOutDividerInitSet
FDwfDigitalOutDividerInitSet.argtypes = [HDWF, ctypes.c_int, ctypes.c_uint]
FDwfDigitalOutDividerInitSet.restype = bool

FDwfDigitalOutDividerInitGet = _dwf.FDwfDigitalOutDividerInitGet
FDwfDigitalOutDividerInitGet.argtypes = [HDWF, ctypes.c_int, _types.c_uint_p]
FDwfDigitalOutDividerInitGet.restype = bool

FDwfDigitalOutDividerSet = _dwf.FDwfDigitalOutDividerSet
FDwfDigitalOutDividerSet.argtypes = [HDWF, ctypes.c_int, ctypes.c_uint]
FDwfDigitalOutDividerSet.restype = bool

FDwfDigitalOutDividerGet = _dwf.FDwfDigitalOutDividerGet
FDwfDigitalOutDividerGet.argtypes = [HDWF, ctypes.c_int, _types.c_uint_p]
FDwfDigitalOutDividerGet.restype = bool


FDwfDigitalOutCounterInfo = _dwf.FDwfDigitalOutCounterInfo
FDwfDigitalOutCounterInfo.argtypes = [HDWF, ctypes.c_int, _types.c_uint_p, _types.c_uint_p]
FDwfDigitalOutCounterInfo.restype = bool

FDwfDigitalOutCounterInitSet = _dwf.FDwfDigitalOutCounterInitSet
FDwfDigitalOutCounterInitSet.argtypes = [HDWF, ctypes.c_int, ctypes.c_byte, ctypes.c_uint]
FDwfDigitalOutCounterInitSet.restype = bool

FDwfDigitalOutCounterInitGet = _dwf.FDwfDigitalOutCounterInitGet
FDwfDigitalOutCounterInitGet.argtypes = [HDWF, ctypes.c_int, _types.c_int_p, _types.c_uint_p]
FDwfDigitalOutCounterInitGet.restype = bool

FDwfDigitalOutCounterSet = _dwf.FDwfDigitalOutCounterSet
FDwfDigitalOutCounterSet.argtypes = [HDWF, ctypes.c_int, ctypes.c_uint, ctypes.c_uint]
FDwfDigitalOutCounterSet.restype = bool

FDwfDigitalOutCounterGet = _dwf.FDwfDigitalOutCounterGet
FDwfDigitalOutCounterGet.argtypes = [HDWF, ctypes.c_int, _types.c_uint_p, _types.c_uint_p]
FDwfDigitalOutCounterGet.restype = bool


FDwfDigitalOutDataInfo = _dwf.FDwfDigitalOutDataInfo
FDwfDigitalOutDataInfo.argtypes = [HDWF, ctypes.c_int, _types.c_uint_p]
FDwfDigitalOutDataInfo.restype = bool

FDwfDigitalOutDataSet = _dwf.FDwfDigitalOutDataSet
FDwfDigitalOutDataSet.argtypes = [HDWF, ctypes.c_int, ctypes.c_void_p, ctypes.c_uint]
FDwfDigitalOutDataSet.restype = bool
