A Python wrapper for Digilent Adept and Waveforms SDKs
======================================================

**Please note that this project is not actively maintained. I will accept pull requests but won't be doing further development myself.**

This is a simple project that aims to provide a convenient
wrapper around the Digilent Adept and Digilent Waveforms
SDKs.

Low-level access to the api is available through pydigilent.lowlevel
but only DMGR, DJTG, and Waveforms have been implemented.

Future
------

	* Create a high level object oriented wrapper around the low-level APIs
	* Create a PyQt interface for, at least, the Waveforms part (most likely using matplotlib)
