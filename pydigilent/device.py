from pydigilent import lowlevel
from pydigilent import djtg
from pydigilent import depp

class DeviceHandle(object):
	def __init__(self, hif):
		object.__init__(self)

		self._hif = hif
		self._device = None
		self._jtag = None
		self._epp = None

	@property
	def jtag(self):
		if self._jtag is None and (self._device.capabilities & Device.DEVICE_CAPABILITIES_JTAG) != 0:
			self._jtag = djtg.Jtag(self._hif)

		return self._jtag

	@property
	def epp(self):
		if self._epp is None and (self._device.capabilities & Device.DEVICE_CAPABILITIES_EPP) != 0:
			self._epp = depp.EPP(self._hif)

		return self._epp

	def close(self):
		if self._jtag is not None:
			self._jtag.disable()

		try:
			DeviceManager.close(self._hif)
		finally:
			self._hif = 0
			self._device = None

class Device(object):
	DEVICE_CAPABILITIES_JTAG = lowlevel.dcapJtag
	DEVICE_CAPABILITIES_PIO  = lowlevel.dcapPio
	DEVICE_CAPABILITIES_EPP  = lowlevel.dcapEpp
	DEVICE_CAPABILITIES_STM  = lowlevel.dcapStm
	DEVICE_CAPABILITIES_SPI  = lowlevel.dcapSpi
	DEVICE_CAPABILITIES_TWI  = lowlevel.dcapTwi
	DEVICE_CAPABILITIES_ACI  = lowlevel.dcapAci
	DEVICE_CAPABILITIES_AIO  = lowlevel.dcapAio
	DEVICE_CAPABILITIES_EMC  = lowlevel.dcapEmc
	DEVICE_CAPABILITIES_DCI  = lowlevel.dcapDci
	DEVICE_CAPABILITIES_GIO  = lowlevel.dcapGio
	DEVICE_CAPABILITIES_PTI  = lowlevel.dcapPti
	DEVICE_CAPABILITIES_ALL  = lowlevel.dcapAll

	def __init__(self, dvc):
		object.__init__(self)

		self._dvc = dvc
		self._product_name = None
		self._product_id = None
		self._serial_number = None
		self._capabilities = None
		self._product_family = None
		self._firmware_version = None

	@property
	def user_name(self):
		return DeviceManager.get_device_info(self._dvc, DeviceManager.DEVICE_INFO_USER_NAME)

	@user_name.setter
	def user_name_set(self, value):
		DeviceManager.set_device_info(self._dvc, DeviceManager.DEVICE_INFO_USER_NAME, value)

	@property
	def alias(self):
		return DeviceManager.get_device_info(self._dvc, DeviceManager.DEVICE_INFO_ALIAS)

	@alias.setter
	def alias_set(self, value):
		DeviceManager.set_device_info(self._dvc, DeviceManager.DEVICE_INFO_ALIAS, value)

	@property
	def product_name(self):
		if self._product_name is None:
			self._product_name = DeviceManager.get_device_info(self._dvc, DeviceManager.DEVICE_INFO_PRODUCT_NAME)
		return self._product_name

	@property
	def product_id(self):
		if self._product_id is None:
			self._product_id = DeviceManager.get_device_info(self._dvc, DeviceManager.DEVICE_INFO_PRODUCT_ID)
		return self._product_id

	@property
	def product_id_product(self):
		if self._product_id is None:
			self._product_id = DeviceManager.get_device_info(self._dvc, DeviceManager.DEVICE_INFO_PRODUCT_ID)
		return ((self._product_id >> 20) & 0xFFF)

	@property
	def product_id_variant(self):
		if self._product_id is None:
			self._product_id = DeviceManager.get_device_info(self._dvc, DeviceManager.DEVICE_INFO_PRODUCT_ID)
		return (self._product_id & 0xFF)

	@property
	def product_id_fwid(self):
		if self._product_id is None:
			self._product_id = DeviceManager.get_device_info(self._dvc, DeviceManager.DEVICE_INFO_PRODUCT_ID)
		return ((self._product_id >> 8) & 0xFFF)

	@property
	def serial_number(self):
		if self._serial_number is None:
			self._serial_number = DeviceManager.get_device_info(self._dvc, DeviceManager.DEVICE_INFO_SERIAL_NUMBER)
		return self._serial_number

	@property
	def ip_address(self):
		return DeviceManager.get_device_info(self._dvc, DeviceManager.DEVICE_INFO_IP_ADDRESS)

	@ip_address.setter
	def ip_address_set(self, value):
		DeviceManager.set_device_info(self._dvc, DeviceManager.DEVICE_INFO_IP_ADDRESS , value)

	@property
	def mac_address(self):
		return DeviceManager.get_device_info(self._dvc, DeviceManager.DEVICE_INFO_MAC_ADDRESS)

	@mac_address.setter
	def mac_address_set(self, value):
		DeviceManager.set_device_info(self._dvc, DeviceManager.DEVICE_INFO_MAC_ADDRESS , value)

	@property
	def capabilities(self):
		if self._capabilities is None:
			self._capabilities = DeviceManager.get_device_info(self._dvc, DeviceManager.DEVICE_INFO_CAPABILITIES)
		return self._capabilities

	@property
	def product_family(self):
		if self._product_family is None:
			self._product_family = DeviceManager.get_device_info(self._dvc, DeviceManager.DEVICE_INFO_PRODUCT_FAMILY)
		return self._product_family

	@property
	def open_count(self):
		return DeviceManager.get_device_info(self._dvc, DeviceManager.DEVICE_INFO_OPEN_COUNT)

	@property
	def firmware_version(self):
		if self._firmware_version is None:
			self._firmware_version = DeviceManager.get_device_info(self._dvc, DeviceManager.DEVICE_INFO_FIRMWARE_VERSION)
		return self._firmware_version

	def open(self):
		handle = DeviceManager.open(self.user_name.decode("utf-8"))
		handle._device = self
		return handle


class DeviceManagerError(Exception):
	def __init__(self, name, desc):
		Exception.__init__(self)

		self.name = name
		self.desc = desc

	def __str__(self):
		return 'DeviceManagerError: {0} - {1}'.format(self.name, self.desc)

class DeviceManager(object):
	def __int__(self):
		pass

	WAIT_INFINITE = lowlevel.tmsWaitInfinite

	DEVICE_TYPE_USB      = lowlevel.dtpUSB
	DEVICE_TYPE_ETHERNET = lowlevel.dtpEthernet
	DEVICE_TYPE_PARALLEL = lowlevel.dtpParallel
	DEVICE_TYPE_SERIAL   = lowlevel.dtpSerial
	DEVICE_TYPE_NONE     = lowlevel.dtpNone
	DEVICE_TYPE_ALL      = lowlevel.dtpAll
	DEVICE_TYPE_NIL      = lowlevel.dtpNil

	DEVICE_INFO_USER_NAME        = lowlevel.dinfoUsrName
	DEVICE_INFO_ALIAS            = lowlevel.dinfoAlias
	DEVICE_INFO_PRODUCT_NAME     = lowlevel.dinfoProdName
	DEVICE_INFO_PRODUCT_ID       = lowlevel.dinfoPDID
	DEVICE_INFO_SERIAL_NUMBER    = lowlevel.dinfoSN
	DEVICE_INFO_IP_ADDRESS       = lowlevel.dinfoIP
	DEVICE_INFO_MAC_ADDRESS      = lowlevel.dinfoMAC
	DEVICE_INFO_CAPABILITIES     = lowlevel.dinfoDCAP
	DEVICE_INFO_PRODUCT_FAMILY   = lowlevel.dinfoProdID
	DEVICE_INFO_OPEN_COUNT       = lowlevel.dinfoOpenCount
	DEVICE_INFO_FIRMWARE_VERSION = lowlevel.dinfoFWVER

	@classmethod
	def get_version(cls):
		(ok, version) = lowlevel.DmgrGetVersion()
		if not ok:
			raise DeviceManagerError('General Device Manager Error', 'Unable to fetch DMGR library version string')
		return version

	@classmethod
	def get_last_error(cls):
		return lowlevel.DmgrGetLastError().value

	@classmethod
	def error_code_to_string(cls, erc):
		(ok, name, desc) = lowlevel.DmgrSzFromErc(erc)
		if not ok:
			raise DeviceManagerError('General Device Manager Error', 'Unable to fetch error string for latest error')
		return (name, desc)

	@classmethod
	def open(cls, deviceid):
		(ok, hif) = lowlevel.DmgrOpen(deviceid)
		if not ok:
			raise DeviceManagerError(*cls.error_code_to_string(cls.get_last_error()))

		return DeviceHandle(hif.value)

	@classmethod
	def open_ex(cls, deviceid, trans_filter, disc_filter):
		(ok, hif) = lowlevel.DmgrOpenEx(deviceid, trans_filter, disc_filter)
		if not ok:
			raise DeviceManagerError(*cls.error_code_to_string(cls.get_last_error()))

		return DeviceHandle(hif.value)

	@classmethod
	def close(cls, hif):
		if not lowlevel.DmgrClose(hif):
			raise DeviceManagerError(*cls.error_code_to_string(cls.get_last_error()))

	@classmethod
	def connected_devices(cls):
		if not lowlevel.DmgrFreeDvcEnum():
			raise DeviceManagerError(*cls.error_code_to_string(cls.get_last_error()))

		(ok, num_devices) = lowlevel.DmgrEnumDevices()
		if not ok:
			raise DeviceManagerError(*cls.error_code_to_string(cls.get_last_error()))

		devices = []
		for i in range(num_devices):
			(ok, dvc) = lowlevel.DmgrGetDvc(i)
			if not ok:
				raise DeviceManagerError(*cls.error_code_to_string(cls.get_last_error()))

			devices.append(Device(dvc))

		return devices

	@classmethod
	def get_device_info(cls, dvc, dinfo):
		(ok, info) = lowlevel.DmgrGetInfo(dvc, dinfo)
		if not ok:
			raise DeviceManagerError(*cls.error_code_to_string(cls.get_last_error()))

		return info

	@classmethod
	def set_device_info(cls, dvc, dinfo, value):
		ok = lowlevel.DmgrSetInfo(dvc, dinfo, value)
		if not ok:
			raise DeviceManagerError(*cls.error_code_to_string(cls.get_last_error()))

__all__ = ['DeviceHandle', 'Device', 'DeviceManagerError', 'DeviceManager']
