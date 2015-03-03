
===============================
Compiling gtk+ under centos 5.5
===============================

To compile the gtk+ library the following libraries must be compiled
in this order:

- fontconfig
- pixmap
- cairo
- glib
- atk
- pango
- gtk+


Setiing the environment variables
=================================


::

	export PATH=$PATH:/opt/gtk2/bin
	export PKG_CONFIG_PATH=/opt/gtk2/lib/pkgconfig
	export LD_LIBRARY_PATH=/opt/gtk2/lib


	./configure --prefix=/opt/gtk2



	  

==============================
Compilations examples for GIMP
==============================

Instructions to compile the current GIMP source code (master version in GIT 
repository) with Ubuntu Linux 9.04 + 9.10

Important: The current GIT master version is a snapshot, an intermediate 
version that can be used to follow current developments (for instance, 
the single window mode). For production use, always use a stable GIMP 
version (2.6)!

The procedure is the same for Ubuntu 9.04 and 9.10, but with Ubuntu 9.04 
you have to download & compile the newest Gtk version.


# (as non-root user)

:: 

	cd ~
	mkdir -p tmp
	cd tmp

# Important! These variables have to be set and
# are required for all further commands. If you close the
# terminal window, you have to give the 3 export commands
# again.

:: 

	export PATH=$PATH:/opt/gimp-2.7/bin
	export PKG_CONFIG_PATH=/opt/gimp-2.7/lib/pkgconfig
	export LD_LIBRARY_PATH=/opt/gimp-2.7/lib


	# Fetch the most important packages
	sudo apt-get build-dep gimp
	# Additional packages
	sudo aptitude install checkinstall git-core libtool libopenexr-dev libopenraw-dev libspiro-dev
	### BEGIN: ONLY NEEDED FOR UBUNTU 9.04 ###
	# Fetch, compile, install Glib (needed for Gtk)
	wget http://ftp.gnome.org/pub/gnome/sources/glib/2.22/glib-2.22.2.tar.bz2
	tar -xjf glib-2.22.2.tar.bz2
	cd glib-2.22.2
	./configure --prefix=/opt/gimp-2.7
	make -j3
	sudo make install -j3
	cd ..
	# Fetch, compile, install Gtk
	wget http://ftp.gnome.org/pub/gnome/sources/gtk+/2.18/gtk+-2.18.2.tar.bz2
	tar -xjf gtk+-2.18.2.tar.bz2
	cd gtk+-2.18.2
	./configure --prefix=/opt/gimp-2.7
	make -j3
	sudo make install -j3
	cd ..
	### END: ONLY NEEDED FOR UBUNTU 9.04 ###

	# Fetch, compile, install BABL
	git clone --depth 1 git://git.gnome.org/babl
	cd babl
	./autogen.sh --prefix=/opt/gimp-2.7
	make -j3
	sudo make install -j3
	cd ..
	# Fetch, compile, install GEGL
	git clone --depth 1 git://git.gnome.org/gegl
	cd gegl
	./autogen.sh --prefix=/opt/gimp-2.7 --disable-gtk-doc
	make -j3
	sudo make install -j3
	cd ..
	# Fetch, compile, install GIMP
	git clone --depth 1 git://git.gnome.org/gimp
	cd gimp
	./autogen.sh --prefix=/opt/gimp-2.7 --disable-gtk-doc
	make -j3
	sudo make install -j3
	cd ..
	Launch GIMP with:
	/opt/gimp-2.7/bin/gimp-2.7 
	


