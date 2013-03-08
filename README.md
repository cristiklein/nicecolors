nicecolors.py
=============

A simple Python library that tries to generate as many visually distinct colors as possible. This is useful, for example, to generate easy-to-read [Gantt charts](http://en.wikipedia.org/wiki/Gantt) with many tasks. Currently it supports 96 (more or less) visually distinct colors.

Principle
---------

Colors are initially generated in the [HSV](http://en.wikipedia.org/wiki/HSL_and_HSV). Different, "well-spaced" values are generated for hue, saturation and lightness, then the color is converted to RGB space.

Usage
-----

Stand-alone (for testing purposes):

	python ./nicecolors.py > test.html
	# Open test.html in browser
	xdg-open test.html

As a library:

	c = NiceColors()
	for _ in range(0, 96):
		color = next(c)
		# color[0] is red component as float from 0 to 1
		# color[0] is green component as float from 0 to 1
		# color[0] is blue component as float from 0 to 1

Final notes
-----------

This project should be considered work-in-progress. Questions and comments are welcome. I am especially looking for methods to increase the number of visually distinct colors and the "distance" between them.
