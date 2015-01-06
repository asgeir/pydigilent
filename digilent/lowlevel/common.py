import ctypes

class ERC(ctypes.c_int):
	pass
ercNoError        = ERC(0)
# The following error codes can be directly mapped to the device error codes.
ercNotSupported             = ERC(1)    #  Capability or function not supported by the device
ercTransferCancelled        = ERC(2)    #  The transfer was cancelled or timeout occured
ercCapabilityConflict       = ERC(3)    #  Tried to enable capabilities that use shared resources, check device datasheet
ercCapabilityNotEnabled     = ERC(4)    #  The protocol is not enabled
ercEppAddressTimeout        = ERC(5)    #  EPP Address strobe timeout
ercEppDataTimeout           = ERC(6)    #  EPP Data strobe timeout
ercDataSndLess              = ERC(7)    #  Data send failed or peripheral did not received all the sent data
ercDataRcvLess              = ERC(8)    #  Data receive failed or peripheral sent less data
ercDataRcvMore              = ERC(9)    #  Peripheral sent more data
ercDataSndLessRcvLess       = ERC(10)   #  Two errors: ercDataSndLess and ercDataRcvLess
ercDataSndLessRcvMore       = ERC(11)   #  Two errors: ercDataSndLess and ercDataSndFailRcvMore
ercInvalidPort              = ERC(12)   #  Attempt to enable port when another port is already enabled
ercBadParameter             = ERC(13)   #  Command parameter out of range

# ACI error codes, directly mapped to device error codes.
ercAciFifoFull              = ERC(0x20)  #  Transmit FIFO overflow

# TWI error codes, directly mapped to device error codes.
ercTwiBadBatchCmd           = ERC(0x20)  #  Bad command in TWI batch buffer
ercTwiBusBusy               = ERC(0x21)  #  Timed out waiting for TWI bus
ercTwiAdrNak                = ERC(0x22)  #  TWI address not ack'd
ercTwiDataNak               = ERC(0x23)  #  TWI data not ack'd
ercTwiSmbPecError           = ERC(0x24)  #  Packet error when using packet error checking

# Most likely the user did something wrong.
ercAlreadyOpened            = ERC(1024)  #  Device already opened
ercInvalidHif               = ERC(1025)  #  Invalid interface handle provided, fist call DmgrOpen(Ex)
ercInvalidParameter         = ERC(1026)  #  Invalid parameter sent in API call
ercTransferPending          = ERC(1031)  #  The last API called in overlapped mode was not finished. Use DmgrGetTransStat or DmgrCancelTrans
ercApiLockTimeout           = ERC(1032)  #  API waiting on pending API timed out
ercPortConflict             = ERC(1033)  #  Attempt to enable port when another port is already enabled

# Not the user's fault.
ercConnectionFailed         = ERC(3072)  #  Unknown fail of connection
ercControlTransferFailed    = ERC(3075)  #  Control transfer failed
ercCmdSendFailed            = ERC(3076)  #  Command sending failed
ercStsReceiveFailed         = ERC(3077)  #  Status receiving failed
ercInsufficientResources    = ERC(3078)  #  Memory allocation failed, insufficient system resources
ercInvalidTFP               = ERC(3079)  #  Internal protocol error, DVT rejected the transfer strcuture sent by public API
ercInternalError            = ERC(3080)  #  Internal error
ercTooManyOpenedDevices     = ERC(3081)  #  Internal error
ercConfigFileError          = ERC(3082)  #  Processing of configuration file failed
ercDeviceNotConnected       = ERC(3083)  #  Device not connected
ercEnumNotFree              = ERC(3084)  #  Device Enumeration failed because another enumeration is still running.
ercEnumFreeFail             = ERC(3085)  #  Device Enumeration list could not be freed
ercInvalidDevice            = ERC(3086)  #  OEM ID check failed
ercDeviceBusy               = ERC(3087)  #  The device is currently claimed by another process.
ercCorruptInstallation      = ERC(3088)  #  One or more critical file is missing from the system.

# jtag errors
ercConnReject     = ERC(3001)
ercConnType       = ERC(3002)
ercConnNoMode     = ERC(3003)
ercInvParam       = ERC(3004)
ercInvCmd         = ERC(3005)
ercUnknown        = ERC(3006)
ercJtagConflict   = ERC(3007)
ercNotImp         = ERC(3008)
ercNoMem          = ERC(3009)
ercTimeout        = ERC(3010)
ercConflict       = ERC(3011)
ercBadPacket      = ERC(3012)
ercInvOption      = ERC(3013)
ercAlreadyCon     = ERC(3014)
ercConnected      = ERC(3101)
ercNotInit        = ERC(3102)
ercCantConnect    = ERC(3103)
ercAlreadyConnect = ERC(3104)
ercSendError      = ERC(3105)
ercRcvError       = ERC(3106)
ercAbort          = ERC(3107)
ercTimeOut        = ERC(3108)
ercOutOfOrder     = ERC(3109)
ercExtraData      = ERC(3110)
ercMissingData    = ERC(3111)
ercTridNotFound   = ERC(3201)
ercNotComplete    = ERC(3202)
ercNotConnected   = ERC(3203)
ercWrongMode      = ERC(3204)
ercWrongVersion   = ERC(3205)
ercDvctableDne    = ERC(3301)
ercDvctableCorrupt= ERC(3302)
ercDvcDne         = ERC(3303)
ercDpcutilInitFail= ERC(3304)
ercUnknownErr     = ERC(3305)
ercDvcTableOpen   = ERC(3306)
ercRegError       = ERC(3307)
ercNotifyRegFull  = ERC(3308)
ercNotifyNotFound = ERC(3309)
ercOldDriverNewFw = ERC(3310)
ercInvHandle      = ERC(3311)
ercInterfaceNotSupported = ERC(3312)

class DINFO(ctypes.c_uint32):
	pass
dinfoNone       = DINFO(0)
dinfoAlias      = DINFO(1)
dinfoUsrName    = DINFO(2)
dinfoProdName   = DINFO(3)
dinfoPDID       = DINFO(4)
dinfoSN         = DINFO(5)
dinfoIP         = DINFO(6)
dinfoMAC        = DINFO(7)    # Ethernet MAC and SN are the same
dinfoDCAP       = DINFO(9)
dinfoSerParam   = DINFO(10)
dinfoParAddr    = DINFO(11)
dinfoUsbPath    = DINFO(12)
dinfoProdID     = DINFO(13)   # the ProductID from PDID
dinfoOpenCount  = DINFO(14)   # how many times a device is opened
dinfoFWVER      = DINFO(15)

class HIF(ctypes.c_uint32):
	pass
hifInvalid = HIF(0)

class DTP(ctypes.c_uint32):
	pass
dtpUSB        = DTP(0x00000001)
dtpEthernet   = DTP(0x00000002)
dtpParallel   = DTP(0x00000004)
dtpSerial     = DTP(0x00000008)
dtpNone       = DTP(0x00000000)
dtpAll        = DTP(0xFFFFFFFF)
dtpNil        = DTP(0)

class DVC(ctypes.Structure):
	_pack_ = 16
	_fields_ = [
		('name', ctypes.c_char * 64),
		('connectionString', ctypes.c_char * 261),
		('dtp', DTP)
	]

__all__ =[
	'ERC', 'ercNoError', 'ercNotSupported', 'ercTransferCancelled', 'ercCapabilityConflict',
	'ercCapabilityNotEnabled', 'ercEppAddressTimeout', 'ercEppDataTimeout', 'ercDataSndLess',
	'ercDataRcvLess', 'ercDataRcvMore', 'ercDataSndLessRcvLess', 'ercDataSndLessRcvMore',
	'ercInvalidPort', 'ercBadParameter', 'ercAciFifoFull', 'ercTwiBadBatchCmd',
	'ercTwiBusBusy', 'ercTwiAdrNak', 'ercTwiDataNak', 'ercTwiSmbPecError', 'ercAlreadyOpened',
	'ercInvalidHif', 'ercInvalidParameter', 'ercTransferPending', 'ercApiLockTimeout',
	'ercPortConflict', 'ercConnectionFailed', 'ercControlTransferFailed', 'ercCmdSendFailed',
	'ercStsReceiveFailed', 'ercInsufficientResources', 'ercInvalidTFP', 'ercInternalError',
	'ercTooManyOpenedDevices', 'ercConfigFileError', 'ercDeviceNotConnected', 'ercEnumNotFree',
	'ercEnumFreeFail', 'ercInvalidDevice', 'ercDeviceBusy', 'ercCorruptInstallation',
	'ercConnReject', 'ercConnType', 'ercConnNoMode', 'ercInvParam', 'ercInvCmd', 'ercUnknown',
	'ercJtagConflict', 'ercNotImp', 'ercNoMem', 'ercTimeout', 'ercConflict', 'ercBadPacket',
	'ercInvOption', 'ercAlreadyCon', 'ercConnected', 'ercNotInit', 'ercCantConnect',
	'ercAlreadyConnect', 'ercSendError', 'ercRcvError', 'ercAbort', 'ercTimeOut', 'ercOutOfOrder',
	'ercExtraData', 'ercMissingData', 'ercTridNotFound', 'ercNotComplete', 'ercNotConnected',
	'ercWrongMode', 'ercWrongVersion', 'ercDvctableDne', 'ercDvctableCorrupt', 'ercDvcDne',
	'ercDpcutilInitFail', 'ercUnknownErr', 'ercDvcTableOpen', 'ercRegError', 'ercNotifyRegFull',
	'ercNotifyNotFound', 'ercOldDriverNewFw', 'ercInvHandle', 'ercInterfaceNotSupported',
	'DINFO', 'dinfoNone', 'dinfoAlias', 'dinfoUsrName', 'dinfoProdName', 'dinfoPDID',
	'dinfoSN', 'dinfoIP', 'dinfoMAC', 'dinfoDCAP', 'dinfoSerParam', 'dinfoParAddr', 'dinfoUsbPath',
	'dinfoProdID', 'dinfoOpenCount', 'dinfoFWVER', 'HIF', 'hifInvalid', 'DTP', 'dtpUSB', 'dtpEthernet',
	'dtpParallel', 'dtpSerial', 'dtpNone', 'dtpAll', 'dtpNil', 'DVC'
]
