from util import djtg as djtg_util

class Jtag(object):
	def __init__(self, hif):
		object.__init__(self)

		self._hif = hif

	def open(self):
		pass

	def close(self):
		pass
