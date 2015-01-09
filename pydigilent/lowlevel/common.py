import ctypes

class ERC(ctypes.c_int):
	pass
ercNoError        = 0
# The following error codes can be directly mapped to the device error codes.
ercNotSupported             = 1    #  Capability or function not supported by the device
ercTransferCancelled        = 2    #  The transfer was cancelled or timeout occured
ercCapabilityConflict       = 3    #  Tried to enable capabilities that use shared resources, check device datasheet
ercCapabilityNotEnabled     = 4    #  The protocol is not enabled
ercEppAddressTimeout        = 5    #  EPP Address strobe timeout
ercEppDataTimeout           = 6    #  EPP Data strobe timeout
ercDataSndLess              = 7    #  Data send failed or peripheral did not received all the sent data
ercDataRcvLess              = 8    #  Data receive failed or peripheral sent less data
ercDataRcvMore              = 9    #  Peripheral sent more data
ercDataSndLessRcvLess       = 10   #  Two errors: ercDataSndLess and ercDataRcvLess
ercDataSndLessRcvMore       = 11   #  Two errors: ercDataSndLess and ercDataSndFailRcvMore
ercInvalidPort              = 12   #  Attempt to enable port when another port is already enabled
ercBadParameter             = 13   #  Command parameter out of range

# ACI error codes, directly mapped to device error codes.
ercAciFifoFull              = 0x20  #  Transmit FIFO overflow

# TWI error codes, directly mapped to device error codes.
ercTwiBadBatchCmd           = 0x20  #  Bad command in TWI batch buffer
ercTwiBusBusy               = 0x21  #  Timed out waiting for TWI bus
ercTwiAdrNak                = 0x22  #  TWI address not ack'd
ercTwiDataNak               = 0x23  #  TWI data not ack'd
ercTwiSmbPecError           = 0x24  #  Packet error when using packet error checking

# Most likely the user did something wrong.
ercAlreadyOpened            = 1024  #  Device already opened
ercInvalidHif               = 1025  #  Invalid interface handle provided, fist call DmgrOpen(Ex)
ercInvalidParameter         = 1026  #  Invalid parameter sent in API call
ercTransferPending          = 1031  #  The last API called in overlapped mode was not finished. Use DmgrGetTransStat or DmgrCancelTrans
ercApiLockTimeout           = 1032  #  API waiting on pending API timed out
ercPortConflict             = 1033  #  Attempt to enable port when another port is already enabled

# Not the user's fault.
ercConnectionFailed         = 3072  #  Unknown fail of connection
ercControlTransferFailed    = 3075  #  Control transfer failed
ercCmdSendFailed            = 3076  #  Command sending failed
ercStsReceiveFailed         = 3077  #  Status receiving failed
ercInsufficientResources    = 3078  #  Memory allocation failed, insufficient system resources
ercInvalidTFP               = 3079  #  Internal protocol error, DVT rejected the transfer strcuture sent by public API
ercInternalError            = 3080  #  Internal error
ercTooManyOpenedDevices     = 3081  #  Internal error
ercConfigFileError          = 3082  #  Processing of configuration file failed
ercDeviceNotConnected       = 3083  #  Device not connected
ercEnumNotFree              = 3084  #  Device Enumeration failed because another enumeration is still running.
ercEnumFreeFail             = 3085  #  Device Enumeration list could not be freed
ercInvalidDevice            = 3086  #  OEM ID check failed
ercDeviceBusy               = 3087  #  The device is currently claimed by another process.
ercCorruptInstallation      = 3088  #  One or more critical file is missing from the system.

# jtag errors
ercConnReject     = 3001
ercConnType       = 3002
ercConnNoMode     = 3003
ercInvParam       = 3004
ercInvCmd         = 3005
ercUnknown        = 3006
ercJtagConflict   = 3007
ercNotImp         = 3008
ercNoMem          = 3009
ercTimeout        = 3010
ercConflict       = 3011
ercBadPacket      = 3012
ercInvOption      = 3013
ercAlreadyCon     = 3014
ercConnected      = 3101
ercNotInit        = 3102
ercCantConnect    = 3103
ercAlreadyConnect = 3104
ercSendError      = 3105
ercRcvError       = 3106
ercAbort          = 3107
ercTimeOut        = 3108
ercOutOfOrder     = 3109
ercExtraData      = 3110
ercMissingData    = 3111
ercTridNotFound   = 3201
ercNotComplete    = 3202
ercNotConnected   = 3203
ercWrongMode      = 3204
ercWrongVersion   = 3205
ercDvctableDne    = 3301
ercDvctableCorrupt= 3302
ercDvcDne         = 3303
ercDpcutilInitFail= 3304
ercUnknownErr     = 3305
ercDvcTableOpen   = 3306
ercRegError       = 3307
ercNotifyRegFull  = 3308
ercNotifyNotFound = 3309
ercOldDriverNewFw = 3310
ercInvHandle      = 3311
ercInterfaceNotSupported = 3312

class DINFO(ctypes.c_uint32):
	pass
dinfoNone       = 0
dinfoAlias      = 1
dinfoUsrName    = 2
dinfoProdName   = 3
dinfoPDID       = 4
dinfoSN         = 5
dinfoIP         = 6
dinfoMAC        = 7    # Ethernet MAC and SN are the same
dinfoDCAP       = 9
dinfoSerParam   = 10
dinfoParAddr    = 11
dinfoUsbPath    = 12
dinfoProdID     = 13   # the ProductID from PDID
dinfoOpenCount  = 14   # how many times a device is opened
dinfoFWVER      = 15

class HIF(ctypes.c_uint32):
	pass
hifInvalid = HIF(0)

class DCAP(ctypes.c_uint32):
	pass
dcapJtag = 0x00000001
dcapJtg  = 0x00000001
dcapPio  = 0x00000002
dcapEpp  = 0x00000004
dcapStm  = 0x00000008
dcapSpi  = 0x00000010
dcapTwi  = 0x00000020
dcapAci  = 0x00000040
dcapAio  = 0x00000080
dcapEmc  = 0x00000100
dcapDci  = 0x00000200
dcapGio  = 0x00000400
dcapPti  = 0x00000800
dcapAll  = 0xFFFFFFFF

class DTP(ctypes.c_uint32):
	pass
dtpUSB        = 0x00000001
dtpEthernet   = 0x00000002
dtpParallel   = 0x00000004
dtpSerial     = 0x00000008
dtpNone       = 0x00000000
dtpAll        = 0xFFFFFFFF
dtpNil        = 0

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
	'dinfoProdID', 'dinfoOpenCount', 'dinfoFWVER', 'HIF', 'hifInvalid', 'DCAP', 'dcapJtag',
	'dcapJtg', 'dcapPio', 'dcapEpp', 'dcapStm', 'dcapSpi', 'dcapTwi', 'dcapAci', 'dcapAio',
	'dcapEmc', 'dcapDci', 'dcapGio', 'dcapPti', 'dcapAll', 'DTP', 'dtpUSB', 'dtpEthernet',
	'dtpParallel', 'dtpSerial', 'dtpNone', 'dtpAll', 'dtpNil', 'DVC'
]
