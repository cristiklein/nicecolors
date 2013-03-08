from __future__ import division

import colorsys

class NiceColors:
	def __init__(self):
		self.i = 0

	def __iter__(self):
		return self

	def next(self):
		i = self.i # Copy i, so we don't overwrite it
		self.i += 1

		h = (i % 12) / 12
		i //= 12
		s = 1
		v = (i % 8 + 3) / 10

		return colorsys.hsv_to_rgb(h, s, v)

if __name__ == "__main__":
	c = NiceColors()
	
	print """
<?xml version="1.0" encoding="utf-8" ?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en" dir="ltr">
<head>
	<title>Nice Color Test</title>
</head>
<body>"""

	for i in range(0, 96):
		i = next(c)
		print '<div style="float: left; width: 10px; height: 10px; background-color: #{r:02x}{g:02x}{b:02x}">&nbsp;</div>'.\
			format(r = int(i[0]*255), g = int(i[1]*255), b = int(i[2]*255) )

	print """</body></html>"""

