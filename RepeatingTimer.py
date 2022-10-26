
from threading import Thread, Timer

class RepeatingTimer(Thread):

	def __init__(self, interval, callback):
		super().__init__()
		self._interval = interval
		self._callback = callback
		self._timer    = Timer(interval, self._timeout)
	
	def _timeout(self):
		self._callback()
		self._timer = Timer(self._interval, self._timeout)
		self._timer.start()
		
	def start(self):
		self._timer.start()