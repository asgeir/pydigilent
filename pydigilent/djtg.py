import struct
from pydigilent import lowlevel
from pydigilent.util import djtg as djtg_util

class JtagError(Exception):
	def __init__(self, name, desc):
		Exception.__init__(self)

		self.name = name
		self.desc = desc

	def __str__(self):
		return 'DeviceManagerError: {0} - {1}'.format(self.name, self.desc)

class JtagBatchBuffer(object):
	JCB_SET_TMS_TDI_TCK     = 1
	JCB_GET_TMS_TDI_TDO_TCK = 2
	JCB_PUT_TMS             = 3
	JCB_PUT_TMS_GET_TDO     = 4
	JCB_PUT_TDI             = 5
	JCB_PUT_TDI_GET_TDO     = 6
	JCB_GET_TDO             = 7
	JCB_CLOCK_TCK           = 8
	JCB_WAIT_US             = 9
	JCB_SET_AUX_RESET       = 10

	def __init__(self):
		object.__init__(self)
		self._buffer = []

	def clear(self):
		self._buffer = []

	def buffer(self):
		return ''.join(self._buffer)

	def set_tms_tdi_tck(self, tms, tdi, tck):
		self._buffer.append(chr(JtagBatchBuffer.JCB_SET_TMS_TDI_TCK))
		self._buffer.append(chr(tms << 2 | tdi << 1 | tck))

	def get_tms_tdi_tdo_tck(self):
		self._buffer.append(chr(JtagBatchBuffer.JCB_GET_TMS_TDI_TDO_TCK))

	def put_tms(self, tms_bytes, cbits, reverse=True):
		self._buffer.append(chr(JtagBatchBuffer.JCB_PUT_TMS))
		self._buffer.append(struct.pack('<I', cbits))
		if reverse:
			self._buffer.append(tms_bytes[::-1])
		else:
			self._buffer.append(tms_bytes[::-1])

	def put_tms_get_tdo(self, tms_bytes, cbits, reverse=True):
		self._buffer.append(chr(JtagBatchBuffer.JCB_PUT_TMS_GET_TDO))
		self._buffer.append(struct.pack('<I', cbits))
		if reverse:
			self._buffer.append(tms_bytes[::-1])
		else:
			self._buffer.append(tms_bytes)

	def put_tdi(self, tdi_bytes, cbits, last_tms, reverse=True):
		self._buffer.append(chr(JtagBatchBuffer.JCB_PUT_TDI))
		self._buffer.append(struct.pack('<I', cbits))
		self._buffer.append(chr(int(last_tms) & 1))
		if reverse:
			self._buffer.append(tdi_bytes[::-1])
		else:
			self._buffer.append(tdi_bytes)

	def put_tdi_get_tdo(self, tdi_bytes, cbits, last_tms, reverse=True):
		self._buffer.append(chr(JtagBatchBuffer.JCB_PUT_TDI_GET_TDO))
		self._buffer.append(struct.pack('<I', cbits))
		self._buffer.append(chr(int(last_tms) & 1))
		if reverse:
			self._buffer.append(tdi_bytes[::-1])
		else:
			self._buffer.append(tdi_bytes)

	def get_tdo(self, cbits, last_tms):
		self._buffer.append(chr(JtagBatchBuffer.JCB_GET_TDO))
		self._buffer.append(struct.pack('<I', cbits))
		self._buffer.append(chr(int(last_tms) & 1))

	def clock_tck(self, num_ticks):
		self._buffer.append(chr(JtagBatchBuffer.JCB_CLOCK_TCK))
		self._buffer.append(struct.pack('<I', num_ticks))

	def wait_us(self, num_us):
		self._buffer.append(chr(JtagBatchBuffer.JCB_WAIT_US))
		self._buffer.append(struct.pack('<I', num_us))

	def set_aux_reset(self, output_enable, reset_state):
		self._buffer.append(chr(JtagBatchBuffer.JCB_SET_AUX_RESET))
		self._buffer.append(chr(output_enable << 1 | reset_state))

class Jtag(object):
	PORT_PROPERTY_SET_SPEED       = lowlevel.dprpJtgSetSpeed
	PORT_PROPERTY_SET_PIN_STATE   = lowlevel.dprpJtgSetPinState
	PORT_PROPERTY_TRANS_BUFFERING = lowlevel.dprpJtgTransBuffering
	PORT_PROPERTY_WAIT            = lowlevel.dprpJtgWait
	PORT_PROPERTY_DELAY_COUNT     = lowlevel.dprpJtgDelayCnt
	PORT_PROPERTY_READY_COUNT     = lowlevel.dprpJtgReadyCnt
	PORT_PROPERTY_ESCAPE          = lowlevel.dprpJtgEscape
	PORT_PROPERTY_MSCAN           = lowlevel.dprpJtgMScan
	PORT_PROPERTY_OSCAN0          = lowlevel.dprpJtgOScan0
	PORT_PROPERTY_OSCAN1          = lowlevel.dprpJtgOScan1
	PORT_PROPERTY_OSCAN2          = lowlevel.dprpJtgOScan2
	PORT_PROPERTY_OSCAN3          = lowlevel.dprpJtgOScan3
	PORT_PROPERTY_OSCAN4          = lowlevel.dprpJtgOScan4
	PORT_PROPERTY_OSCAN5          = lowlevel.dprpJtgOScan5
	PORT_PROPERTY_OSCAN6          = lowlevel.dprpJtgOScan6
	PORT_PROPERTY_OSCAN7          = lowlevel.dprpJtgOScan7
	PORT_PROPERTY_CHECK_PACKET    = lowlevel.dprpJtgCheckPacket
	PORT_PROPERTY_BATCH           = lowlevel.dprpJtgBatch
	PORT_PROPERTY_AUX_RESET       = lowlevel.dprpJtgSetAuxReset

	PORT_BATCH_PROPERTY_WAIT_US       = lowlevel.djbpWaitUs
	PORT_BATCH_PROPERTY_SET_AUX_RESET = lowlevel.djbpSetAuxReset

	def __init__(self, hif):
		object.__init__(self)

		self._hif = hif

	@classmethod
	def get_version(self):
		(ok, version) = lowlevel.DjtgGetVersion()
		if not ok:
			raise JtagError('General Jtag Error', 'Unable to fetch DJTG library version string')
		return version

	@property
	def port_count(self):
		(ok, count) = lowlevel.DjtgGetPortCount(self._hif)
		if not ok:
			raise JtagError('General Jtag Error', 'Unable to fetch jtag port count for device')
		return count

	def get_port_properties(self, portidx):
		(ok, properties) = lowlevel.DjtgGetPortProperties(self._hif, portidx)
		if not ok:
			raise JtagError('General Jtag Error', 'Unable to fetch jtag port properties for device')
		return properties

	def get_port_batch_properties(self, portidx):
		(ok, properties) = lowlevel.DjtgGetBatchProperties(self._hif, portidx)
		if not ok:
			raise JtagError('General Jtag Error', 'Unable to fetch jtag port batch properties for device')
		return properties

	def enable(self, portidx=-1):
		if portidx < 0:
			if not lowlevel.DjtgEnable(self._hif):
				raise JtagError('General Jtag Error', 'Unable to enable default jtag port')
		else:
			if not lowlevel.DjtgEnableEx(self._hif, portidx):
				raise JtagError('General Jtag Error', 'Unable to enable specified jtag port')

	def disable(self):
		lowlevel.DjtgDisable(self._hif)

	def get_speed(self):
		(ok, sp) = lowlevel.DjtgGetSpeed(self._hif)
		if not ok:
			raise JtagError('General Jtag Error', 'Unable to fetch jtag port speed')
		return sp

	def set_speed(self, rqspeed):
		(ok, sp) = lowlevel.DjtgSetSpeed(self._hif, rqspeed)
		if not ok:
			raise JtagError('General Jtag Error', 'Unable to set jtag port speed')
		return sp

	def get_tms_tdi_tck(self):
		(ok, tms, tdi, tck) = lowlevel.DjtgSetTmsTdiTck(self._hif, tms, tdi, tck)
		if not ok:
			raise JtagError('General Jtag Error', 'Unable to get jtag port tms, tdi, tck')
		return (tms, tdi, tck)

	def set_tms_tdi_tck(self, tms, tdi, tck):
		if not lowlevel.DjtgSetTmsTdiTck(self._hif, tms, tdi, tck):
			raise JtagError('General Jtag Error', 'Unable to set jtag port tms, tdi, tck')

	def set_aux_reset(self, reset_pin_value, output_enable):
		if not lowlevel.DjtgSetAuxReset(self._hif, reset_pin_value, output_enable):
			raise JtagError('General Jtag Error', 'Unable to set aux reset')

	def enable_trans_buffering(self, enable):
		if not lowlevel.DjtgEnableTransBuffering(self._hif, enable):
			raise JtagError('General Jtag Error', 'Unable to set trans buffering')

	def sync_buffer(self):
		if not lowlevel.DjtgSyncBuffer(self._hif):
			raise JtagError('General Jtag Error', 'Unable to sync buffer')

	def wait(self, us_to_wait):
		(ok, us_waited) = lowlevel.DjtgWait(self._hif, us_to_wait)
		if not ok:
			raise JtagError('General Jtag Error', 'Unable to wait')
		return us_waited

	def put_tdi_bits(self, tms, buffer, cbits, overlap=False, want_reply=False):
		# TODO: reconsider this allocation strategy if speed or memory usage becomes an issue
		import ctypes
		send_buffer = (ctypes.c_ubyte * len(buffer))()
		for i in range(len(buffer)):
			send_buffer[i] = ctypes.c_ubyte(buffer[i] & 0xff)

		recv_buffer = None
		if want_reply:
			recv_buffer = (ctypes.c_ubyte * len(buffer))()

		if not lowlevel.DjtgPutTdiBits(self._hif, tms, send_buffer, recv_buffer, cbits, overlap):
			raise JtagError('General Jtag Error', 'Unable to send tdi bits')

		if want_reply:
			return recv_buffer[:]

	def put_tms_bits(self, tdi, buffer, cbits, overlap=False, want_reply=False):
		# TODO: reconsider this allocation strategy if speed or memory usage becomes an issue
		import ctypes
		send_buffer = (ctypes.c_ubyte * len(buffer))()
		for i in range(len(buffer)):
			send_buffer[i] = ctypes.c_ubyte(buffer[i] & 0xff)

		recv_buffer = None
		if want_reply:
			recv_buffer = (ctypes.c_ubyte * len(buffer))()

		if not lowlevel.DjtgPutTmsBits(self._hif, tdi, send_buffer, recv_buffer, cbits, overlap):
			raise JtagError('General Jtag Error', 'Unable to send tms bits')

		if want_reply:
			return recv_buffer[:]

	def put_tms_tdi_bits(self, buffer, cbitpairs, overlap=False, want_reply=False):
		# TODO: reconsider this allocation strategy if speed or memory usage becomes an issue
		import ctypes
		send_buffer = (ctypes.c_ubyte * len(buffer))()
		for i in range(len(buffer)):
			send_buffer[i] = ctypes.c_ubyte(buffer[i] & 0xff)

		recv_buffer = None
		if want_reply:
			recv_buffer = (ctypes.c_ubyte * len(buffer))()

		if not lowlevel.DjtgPutTmsTdiBits(self._hif, send_buffer, recv_buffer, cbitpairs, overlap):
			raise JtagError('General Jtag Error', 'Unable to send tms, tdi bits')

		if want_reply:
			return recv_buffer[:]

	def get_tdo_bits(self, tdi, tms, cbits, overlap=False):
		import ctypes
		recv_buffer = (ctypes.c_ubyte * int(((cbits + 7) & ~7) / 8))()

		if not lowlevel.DjtgGetTdoBits(self._hif, tdi, tms, recv_buffer, cbits, overlap):
			raise JtagError('General Jtag Error', 'Unable to fetch tdo bits')

		return recv_buffer[:]

	def clock_tick(self, tms, tdi, cclk, overlap=False):
		if not lowlevel.DjtgClockTck(self._hif, tms, tdi, cclk, overlap):
			raise JtagError('General Jtag Error', 'Unable to tick clock')

	def batch(self, buffer, num_bytes_received, overlap=False):
		import ctypes
		send_buffer = (ctypes.c_ubyte * len(buffer))()
		for i in range(len(buffer)):
			send_buffer[i] = ctypes.c_ubyte(buffer[i] & 0xff)

		recv_buffer = None
		if num_bytes_received > 0:
			recv_buffer = (ctypes.c_ubyte * num_bytes_received)()

		if not lowlevel.DjtgBatch(self._hif, len(send_buffer), send_buffer, num_bytes_received, recv_buffer, overlap):
			raise JtagError('General Jtag Error', 'Unable to send batch commands')

		if num_bytes_received > 0:
			return recv_buffer

__all__ = ['JtagBatchBuffer', 'JtagError', 'Jtag']
