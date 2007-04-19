# A simple makefile for compiling and installing the tools 
# (as they do not use fancy libraries, autotools would be overkill for now).

all:
	$(MAKE) -C src

clean:
	$(MAKE) -C src clean

distclean:
	$(MAKE) -C src distclean

install:
	install src/cpuload $(DESTDIR)/usr/bin/
	install src/ioload $(DESTDIR)/usr/bin/
	install src/memload $(DESTDIR)/usr/bin/
