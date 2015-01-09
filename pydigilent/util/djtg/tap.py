# adapted from https://github.com/ktemkin/ruby-adept

# original copyright:
# Copyright (c) 2012 Kyle J. Temkin
#
# MIT License
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

class TapState(object):
	def __init__(self, name, onZero, onOne):
		object.__init__(self)

		self._name = name
		self._transitions = { 0: onZero, 1: onOne }

	def next_state(self, on):
		return getattr(Tap, self._transitions[on])

	def advance_toward(self, state):
		if self._name == 'SELECT_DR' and state._name.endswith('_DR'):
			return (0, self._transitions[0])

		zero = getattr(Tap, self._transitions[0])
		one = getattr(Tap, self._transitions[1])

		if zero == state or one == self or self._transitions[1] == 'RESET':
			return (0, self._transitions[0])

		return (1, self._transitions[1])

class Tap(object):
	RESET = TapState('RESET', 'IDLE', 'RESET')
	IDLE  = TapState('IDLE',  'IDLE', 'SELECT_DR')

	SELECT_DR  = TapState('SELECT_DR',  'CAPTURE_DR', 'SELECT_IR')
	CAPTURE_DR = TapState('CAPTURE_DR', 'SHIFT_DR',   'EXIT1_DR')
	SHIFT_DR   = TapState('SHIFT_DR',   'SHIFT_DR',   'EXIT1_DR')
	EXIT1_DR   = TapState('EXIT1_DR',   'PAUSE_DR',   'UPDATE_DR')
	PAUSE_DR   = TapState('PAUSE_DR',   'PAUSE_DR',   'EXIT2_DR')
	EXIT2_DR   = TapState('EXIT2_DR',   'SHIFT_DR',   'UPDATE_DR')
	UPDATE_DR  = TapState('UPDATE_DR',  'IDLE',       'SELECT_DR')

	SELECT_IR  = TapState('SELECT_IR',  'CAPTURE_IR', 'RESET')
	CAPTURE_IR = TapState('CAPTURE_IR', 'SHIFT_IR',   'EXIT1_IR')
	SHIFT_IR   = TapState('SHIFT_IR',   'SHIFT_IR',   'EXIT1_IR')
	EXIT1_IR   = TapState('EXIT1_IR',   'PAUSE_IR',   'UPDATE_IR')
	PAUSE_IR   = TapState('PAUSE_IR',   'PAUSE_IR',   'EXIT2_IR')
	EXIT2_IR   = TapState('EXIT2_IR',   'SHIFT_IR',   'UPDATE_IR')
	UPDATE_IR  = TapState('UPDATE_IR',  'IDLE',       'SELECT_DR')

__all__ = ['TapState', 'Tap']
