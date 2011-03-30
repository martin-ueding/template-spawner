#!/usr/bin/python
# Copyright (c) 2011 Martin Ueding <dev@martin-ueding.de>

import time
import sys

if len(sys.argv) < 2:
	print "usage: tspawn FORMAT [FILENAME]"
	sys.exit(1)

copyright = "Copyright (c) "+time.strftime("%Y")+" Martin Ueding <dev@martin-ueding.de>"

filename = "new-template"
if len(sys.argv) == 3:
	filename = sys.argv[2]


with open(filename, 'w') as f:
	if sys.argv[1] == 'html':
		f.write("""<!doctype html>
	<head>
		<title></title>
	</head>
	<body>
	</body>
</html>""")

	if sys.argv[1] == 'py':
		f.write("""#!/usr/bin/python
# """+copyright+"""

""")


	if sys.argv[1] == 'bash':
		f.write("""#!/bin/bash
# """+copyright+"""

""")
