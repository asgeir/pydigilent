import struct
from pydigilent import lowlevel

class EPPError(Exception):
    def __init__(self, name, desc):
        Exception.__init__(self)

        self.name = name
        self.desc = desc

    def __str__(self):
        return 'EPPError: {0} - {1}'.format(self.name, self.desc)

class EPP(object):
    def __init__(self, hif):
        object.__init__(self)

        self._hif = hif

    @classmethod
    def get_version(cls):
        (ok, version) = lowlevel.DeppGetVersion()
        if not ok:
            raise EPPError('General EPP Error', 'Unable to fetch DEPP library version string')
        return version

    @property
    def port_count(self):
        (ok, count) = lowlevel.DeppGetPortCount(self._hif)
        if not ok:
            raise EPPError('General EPP Error', 'Unable to fetch EPP port count for device')
        return count

    def get_port_properties(self, portidx):
        (ok, properties) = lowlevel.DeppGetPortProperties(self._hif, portidx)
        if not ok:
            raise EPPError('General EPP Error', 'Unable to fetch EPP port properties for device')
        return properties

    def enable(self, portidx=-1):
        if portidx < 0:
            if not lowlevel.DeppEnable(self._hif):
                raise EPPError('General EPP Error', 'Unable to enable default epp port')
        else:
            if not lowlevel.DeppEnableEx(self._hif, portidx):
                raise EPPError('General EPP Error', 'Unable to enable specified epp port')

    def disable(self):
        lowlevel.DjtgDisable(self._hif)

    def put_reg(self, addr, data, overlap=False):
        if not lowlevel.DeppPutReg(self._hif, addr, data, overlap):
            raise EPPError('General EPP Error', 'Unable to set epp register')

    def get_reg(self, addr, overlap=False):
        (ok, ret) = lowlevel.DeppGetReg(self._hif, addr, overlap)
        if not ok:
            raise EPPError('General EPP Error', 'Unable to get epp register')
        return ret

    def put_reg_set(self, addr_datas, overlap=False):
        import ctypes
        buf = (ctypes.c_ubyte * len(addr_datas) * 2)()
        for i in range(len(addr_datas)):
            buf[2*i] = addr_datas[i][0]
            buf[2*i+1] = addr_datas[i][1]
        if not lowlevel.DeppPutRegSet(self._hif, buf, len(addr_datas), overlap):
            raise EPPError('General EPP Error', 'Unable to put epp registers')

    def get_reg_set(self, addrs, overlap=False):
        import ctypes
        buf_addrs = (ctypes.c_ubyte * len(addrs))()
        buf_datas = (ctypes.c_ubyte * len(addrs))()
        for i in range(len(addrs)):
            buf_addrs[i] = addrs[i]
        if not lowlevel.DeppGetRegSet(self._hif, buf_addrs, buf_datas, len(addrs), overlap):
            raise EPPError('General EPP Error', 'Unable to get epp registers')
        datas = []
        for i in range(len(addrs)):
            datas.append(buf_datas[i])
        return datas

    def put_reg_repeat(self, addr, datas, overlap=False):
        import ctypes
        buf = (ctypes.c_ubyte * len(datas))()
        for i in range(len(datas)):
            buf[i] = datas[i]
        if not lowlevel.DeppPutRegRepeat(self._hif, addr, buf, len(datas), overlap):
            raise EPPError('General EPP Error', 'Unable to put epp registers')

    def get_reg_repeat(self, addr, count, overlap=False):
        import ctypes
        buf = (ctypes.c_ubyte * count)()
        if not lowlevel.DeppGetRegRepeat(self._hif, addr, buf, count, overlap):
            raise EPPError('General EPP Error', 'Unable to get epp registers')
        datas = []
        for i in range(count):
            datas.append(buf[i])
        return datas

