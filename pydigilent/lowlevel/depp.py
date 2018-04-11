import ctypes
import sys

from pydigilent.lowlevel.common import HIF

if sys.platform.startswith("win"):
    _depp = ctypes.cdll.depp
else:
    _depp = ctypes.cdll.LoadLibrary("libdepp.so")

_DeppGetVersion = _depp.DeppGetVersion
_DeppGetVersion.argtypes = [ctypes.POINTER(ctypes.c_char * 32)]
_DeppGetVersion.restype = bool

def DeppGetVersion():
    tmp = ctypes.create_string_buffer(32)
    return (_DeppGetVersion(ctypes.byref(tmp)), tmp.value)

_DeppGetPortCount = _depp.DeppGetPortCount
_DeppGetPortCount.argtypes = [HIF, ctypes.POINTER(ctypes.c_int32)]
_DeppGetPortCount.restype = bool

def DeppGetPortCount(hif):
    value = ctypes.c_int32()
    return (_DeppGetPortCount(hif, ctypes.byref(value)), value.value)

_DeppGetPortProperties = _depp.DeppGetPortProperties
_DeppGetPortProperties.argtypes = [HIF, ctypes.c_int32, ctypes.POINTER(ctypes.c_uint32)]
_DeppGetPortProperties.restype = bool

def DeppGetPortProperties(hif, prtReq):
    info = ctypes.c_uint32()
    return (_DeppGetPortProperties(hif, prtReq, ctypes.byref(info)), info.value)

DeppEnable = _depp.DeppEnable
DeppEnable.argtypes = [HIF]
DeppEnable.restype = bool

DeppEnableEx = _depp.DeppEnableEx
DeppEnableEx.argtypes = [HIF, ctypes.c_int32]
DeppEnableEx.restype = bool

DeppDisable = _depp.DeppDisable
DeppDisable.argtypes = [HIF]
DeppDisable.restype = bool

DeppPutReg = _depp.DeppPutReg
DeppPutReg.argtypes = [HIF, ctypes.c_ubyte, ctypes.c_ubyte, ctypes.c_ubyte]
DeppPutReg.restype = bool

_DeppGetReg = _depp.DeppGetReg
_DeppGetReg.argtypes = [HIF, ctypes.c_ubyte, ctypes.POINTER(ctypes.c_ubyte), ctypes.c_ubyte]
_DeppGetReg.restype = bool

def DeppGetReg(hif, bAddr, fOverlap):
    bData = ctypes.c_ubyte()
    return (_DeppGetReg(hif, bAddr, ctypes.byref(bData), fOverlap), bData.value)

DeppPutRegSet = _depp.DeppPutRegSet
DeppPutRegSet.argtypes = [HIF, ctypes.POINTER(ctypes.c_ubyte), ctypes.c_uint32, ctypes.c_ubyte]
DeppPutRegSet.restype = bool

DeppGetRegSet = _depp.DeppGetRegSet
DeppGetRegSet.argtypes = [HIF, ctypes.POINTER(ctypes.c_ubyte), ctypes.POINTER(ctypes.c_ubyte), ctypes.c_uint32, ctypes.c_ubyte]
DeppGetRegSet.restype = bool

DeppPutRegRepeat = _depp.DeppPutRegRepeat
DeppPutRegRepeat.argtypes = [HIF, ctypes.c_ubyte, ctypes.POINTER(ctypes.c_ubyte), ctypes.c_uint32, ctypes.c_ubyte]
DeppPutRegRepeat.restype = bool

DeppGetRegRepeat = _depp.DeppGetRegRepeat
DeppGetRegRepeat.argtypes = [HIF, ctypes.c_ubyte, ctypes.POINTER(ctypes.c_ubyte), ctypes.c_uint32, ctypes.c_ubyte]
DeppGetRegRepeat.restype = bool

__all__ = [
    'DeppGetVersion', 'DeppGetPortCount', 'DeppGetPortProperties', 'DeppEnable', 'DeppEnableEx', 'DeppDisable',
    'DeppPutReg', 'DeppGetReg', 'DeppPutRegSet', 'DeppGetRegSet', 'DeppPutRegRepeat', 'DeppGetRegRepeat'
]


