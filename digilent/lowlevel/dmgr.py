import ctypes
import sys

from common import ERC, DINFO, HIF, DTP, DVC

if sys.platform.startswith("win"):
	_dmgr = ctypes.cdll.dmgr
else:
	_dmgr = ctypes.cdll.LoadLibrary("libdmgr.so")

tmsWaitInfinite = 0xFFFFFFFF

DmgrGetVersion = _dmgr.DmgrGetVersion
DmgrGetVersion.argtypes = [ctypes.POINTER(ctypes.c_char * 256)]
DmgrGetVersion.restype = bool

#DmgrGetLastError returns the last error per process which is updated when a DVC API function fails.
DmgrGetLastError = _dmgr.DmgrGetLastError
DmgrGetLastError.argtypes = []
DmgrGetLastError.restype = ERC

DmgrSzFromErc = _dmgr.DmgrSzFromErc
DmgrSzFromErc.argtypes = [ERC, ctypes.POINTER(ctypes.c_char * 48), ctypes.POINTER(ctypes.c_char * 128)]
DmgrSzFromErc.restype = bool


#OPEN & CLOSE functions
DmgrOpen = _dmgr.DmgrOpen
DmgrOpen.argtypes = [ctypes.POINTER(HIF), ctypes.c_char_p]
DmgrOpen.restype = bool

DmgrOpenEx = _dmgr.DmgrOpenEx
DmgrOpenEx.argtypes = [ctypes.POINTER(HIF), ctypes.c_char_p, DTP, DTP]
DmgrOpenEx.restype = bool

DmgrClose = _dmgr.DmgrClose
DmgrClose.argtypes = [HIF]
DmgrClose.restype = bool


#ENUMERATION functions
DmgrEnumDevices = _dmgr.DmgrEnumDevices
DmgrEnumDevices.argtypes = [ctypes.POINTER(ctypes.c_int)]
DmgrEnumDevices.restype = bool

DmgrEnumDevicesEx = _dmgr.DmgrEnumDevicesEx
DmgrEnumDevicesEx.argtypes = [ctypes.POINTER(ctypes.c_int), DTP, DTP, DINFO, ctypes.c_void_p]
DmgrEnumDevicesEx.restype = bool

DmgrStartEnum = _dmgr.DmgrStartEnum
DmgrStartEnum.argtypes = [DTP, DTP, DINFO, ctypes.c_void_p]
DmgrStartEnum.restype = bool

DmgrIsEnumFinished = _dmgr.DmgrIsEnumFinished
DmgrIsEnumFinished.argtypes = []
DmgrIsEnumFinished.restype = bool

DmgrStopEnum = _dmgr.DmgrStopEnum
DmgrStopEnum.argtypes = []
DmgrStopEnum.restype = bool

DmgrGetEnumCount = _dmgr.DmgrGetEnumCount
DmgrGetEnumCount.argtypes = [ctypes.POINTER(ctypes.c_int)]
DmgrGetEnumCount.restype = bool

DmgrGetDvc = _dmgr.DmgrGetDvc
DmgrGetDvc.argtypes = [ctypes.c_int, ctypes.POINTER(DVC)]
DmgrGetDvc.restype = bool

DmgrFreeDvcEnum = _dmgr.DmgrFreeDvcEnum
DmgrFreeDvcEnum.argtypes = []
DmgrFreeDvcEnum.restype = bool


#TRANSFER status and control functions
DmgrGetTransResult = _dmgr.DmgrGetTransResult
DmgrGetTransResult.argtypes = [HIF, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(ctypes.c_uint32), ctypes.c_uint32]
DmgrGetTransResult.restype = bool

DmgrCancelTrans = _dmgr.DmgrCancelTrans
DmgrCancelTrans.argtypes = [HIF]
DmgrCancelTrans.restype = bool

DmgrSetTransTimeout = _dmgr.DmgrSetTransTimeout
DmgrSetTransTimeout.argtypes = [HIF, ctypes.c_uint32]
DmgrSetTransTimeout.restype = bool

DmgrGetTransTimeout = _dmgr.DmgrGetTransTimeout
DmgrGetTransTimeout.argtypes = [HIF, ctypes.POINTER(ctypes.c_uint32)]
DmgrGetTransTimeout.restype = bool


#DVC Table manipulation functions
if sys.platform.startswith("win"):
	DmgrOpenDvcMg = _dmgr.DmgrOpenDvcMg  # opens device manager dialog box
	DmgrOpenDvcMg.argtypes = ['dunno']
	DmgrOpenDvcMg.restype = bool

DmgrDvcTblAdd = _dmgr.DmgrDvcTblAdd
DmgrDvcTblAdd.argtypes = [ctypes.POINTER(DVC)]
DmgrDvcTblAdd.restype = bool

DmgrDvcTblRem = _dmgr.DmgrDvcTblRem
DmgrDvcTblRem.argtypes = [ctypes.c_char_p]
DmgrDvcTblRem.restype = bool

DmgrDvcTblSave = _dmgr.DmgrDvcTblSave
DmgrDvcTblSave.argtypes = []
DmgrDvcTblSave.restype = bool


#Device transport type management functions
DmgrGetDtpCount = _dmgr.DmgrGetDtpCount
DmgrGetDtpCount.argtypes = []
DmgrGetDtpCount.restype = int

DmgrGetDtpFromIndex = _dmgr.DmgrGetDtpFromIndex
DmgrGetDtpFromIndex.argtypes = [ctypes.c_int, ctypes.POINTER(DTP)]
DmgrGetDtpFromIndex.restype = bool

DmgrGetDtpString = _dmgr.DmgrGetDtpString
DmgrGetDtpString.argtypes = [DTP, ctypes.c_char_p]
DmgrGetDtpString.restype = bool


#Miscellaneous functions
DmgrSetInfo = _dmgr.DmgrSetInfo
DmgrSetInfo.argtypes = [ctypes.POINTER(DVC), DINFO, ctypes.c_void_p]
DmgrSetInfo.restype = bool

DmgrGetInfo = _dmgr.DmgrGetInfo
DmgrGetInfo.argtypes = [ctypes.POINTER(DVC), DINFO, ctypes.c_void_p]
DmgrGetInfo.restype = bool


DmgrGetDvcFromHif = _dmgr.DmgrGetDvcFromHif
DmgrGetDvcFromHif.argtypes = [HIF, ctypes.POINTER(DVC)]
DmgrGetDvcFromHif.restype = bool


__all__ = [
	'tmsWaitInfinite', 'DmgrGetVersion', 'DmgrGetLastError', 'DmgrSzFromErc', 'DmgrOpen',
	'DmgrOpenEx', 'DmgrClose', 'DmgrEnumDevices', 'DmgrEnumDevicesEx', 'DmgrStartEnum',
	'DmgrIsEnumFinished', 'DmgrStopEnum', 'DmgrGetEnumCount', 'DmgrGetDvc', 'DmgrFreeDvcEnum',
	'DmgrGetTransResult', 'DmgrCancelTrans', 'DmgrSetTransTimeout', 'DmgrGetTransTimeout',
	'DmgrDvcTblAdd', 'DmgrDvcTblRem', 'DmgrDvcTblSave', 'DmgrGetDtpCount', 'DmgrGetDtpFromIndex',
	'DmgrGetDtpString', 'DmgrSetInfo', 'DmgrGetInfo', 'DmgrGetDvcFromHif'
]
