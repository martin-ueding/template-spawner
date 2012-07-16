# Copyright © 2012 Martin Ueding <dev@martin-ueding.de>

all:
	@echo "Nothing to do."

install:
	install -d "$(DESTDIR)/usr/bin/"
	install spawn -t "$(DESTDIR)/usr/bin/"
