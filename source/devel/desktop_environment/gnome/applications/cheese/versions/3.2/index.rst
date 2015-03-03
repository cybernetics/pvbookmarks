
.. index::
   pair: hotplug; gnome

.. _cheese_3.2:

===================
cheese 3.2
===================


what's changed in 3.3.2?
========================

Huge changes to the API reference documentation, and new hotplug support, as
well as many other updates.


- Pre-release version bump to 3.3.2
- Remove marshaller generation rules
  The generic marshallers, supplied by GLib, are used instead.
- Make preferences dialog more netbook-friendly
  Fixes bug 663146.
- Convert deprecated GtkVBox and GtkHBox to GtkBox
  Fixes bug 661661.
- Add chapter IDs to documentation
- Add Cheese architecture diagram to documentation
  Fixes bug 664333.
- Set camerabin to playing before start-capture
  Fixes bug 663998, with the camerabin documentation being updated in bug
  664048.
- Use private GObject pointer in Widget and Chooser
  Additionally, remove some dead code.
- Add gtk-doc comments to UmCropArea
  Currently, UmCropArea is internal (and will likely stay that way), so
  the comments are not included in the generated documentation.
- Use switch statement to select cases
- Use better API to notify and install properties
  Changed g_object_notify_by_pspec() to g_object_notify() and
  g_object_class_install_property() to
  g_object_class_install_properties(). Added properties static array to
  hold properties. Added enum constants identifying properties and
  sentinels for array length definitions. Fixes bug 663098.
- Improve CheeseAvatarChooser documentation
  Add documentation for private methods in CheeseAvatarChooser.
- Improve CheeseEffect documentation
  Document the private methods in CheeseEffect. Simplify effect
  construction, by making the name and pipeline-desc properties
  construct-only. Improve some variables names.
- Improve CheeseFileUtil filename handling
  Use GDateTime to format the time string. Use switch statements when
  selecting cases from an enum. Use g_build_filename() rather than
  g_strjoin(G_DIR_SEPARATOR_S, ...).
- Improve CheeseCamera documentation
  Document most of the private methods in CheeseCamera, and rename the
  device-name property to device-node.
- Improve CheeseCameraDevice documentation
  Document most of the private methods in CheeseCameraDevice, and rename
  some variables to more closely match the property names.
- Improve CheeseCameraDeviceMonitor documentation
- Make CheeseFlash a GtkWindow rather than a GObject
  Additionally, add further gtk-doc-like comments to the flash
  implementation.
- Comment Vala methods with Valadoc markup
  Add basic documentation to all methods in Vala sources.
- Add hotplug support to preferences dialog
  Adding and removing camera devices in the CheeseCamera is now propagated
  to the preferences dialog UI. Partially fixes bug 603612.
- Correct default brightness in the schema to zero
- Improve GSettings schema text and include ranges
- Also use the countdown duration for burst mode
- Add a countdown-duration key to GSettings schema
  Add a new GSettings key to allow configuration of the duration of the
  countdown when taking a photo. Partially fixes bug 594267.
- Bump required Vala version to 0.13.2
  Required for Clutter.TableLayout in clutter-1.0.vapi, which was added
  when Vala switched to use GIR files.
- Use STYLE_PROVIDER_PRIORITY_USER
- Use Vala ‘as’ operator where possible
  Use the as operator when fetching widgets from GtkBuilder files, to do a
  runtime type-check.
- Include the version in the man page
- Add generated man page to CLEANFILES
- Fix a typo so that the man page is generated
- Fix gtk-doc checks when srcdir != builddir
- Add man page, generated with xsltproc
- Add help button to the preferences dialog
- Improve documentation to pass gtk-doc tests
  Add the deprecated API index to the documentation. Complete the rename
  of cheese_camera_set_device_by_dev_file() to
  cheese_camera_set_device_by_device_node(). Add missing documentation to
  reach 100% symbol coverage.
- Enable gtk-doc tests during make check
- Check for GStreamer plugins required at runtime
  Add a GStreamer plugin check to configure.ac, which checks for
  individual plugins with gst-inspect, rather than relying on the plugins
  being provided by checking for GStreamer pkg-config files. The check is
  non-fatal, as the plugins are not build-time dependencies.
- Bump pkg-config requirement to 0.24
  Version 0.24 or greater of pkg-config is required in order to avoid the
  duplicate AC_SUBST macro calls for PKG_CHECK_MODULES substitutions.
- Remove unused FULL_LIBEXECDIR from configure.ac
- Add private pointers to libcheese GObject structs
  Speed up access to the private struct of the GObject by adding a
  pointer, so that * _GET_PRIVATE does not have to called each time. Create
  a typedef for the private structures in the headers, and hide the
  structs from the documentation by placing them inside a private
  subsection.
- Add basic documentation for remaining public API
  Add cheese-widget-private.h back to files ignored by gtk-doc. Add basic
  documentation for the remainder of the public API. Use UUID instead of
  ID or UDI. Add blurb and nick to all documented properties. Add
  CheeseVideoFormat documentation. Use unsigned integers where the values
  are always positive. Sprinkle some const qualifiers. Add some filename
  GObject Introspection annotations.
- Update TODO
- Fix several compiler warnings
  Add some missing prototypes, correct some pointer type mismatches, return
  a value from functions that returns values and improve GError handling.
- Use gnome-common compiler warnings
  Additionally, enable silent Automake rules by default so that warnings are
  more visible.
- Add more classes to gtk-doc documentation
  Add basic documentation for CheeseCamera, CheeseFileUtil and CheeseFlash
  classes. Split the API reference into libcheese and libcheese-gtk
  chapters.
- Add CheeseCameraDeviceMonitor::removed callback
  Added CheeseCameraDeviceMonitor::removed signal callback function in
  CheeseCamera. Fixes bug 662852.
- Improved CheeseCameraDeviceMonitor::added signal
  CheeseCameraDeviceMonitor:added has now a CheeseCameraDevice argument.
  CheeseCameraDeviceMonitor is also now a member of CheeseCamera.
- Add a long description to the DOAP file
- help: fixed another typo
- help: moving introduction page back to .page
- help: fixed typo in Makefile.am
- help: updated Makefile.am
- Overhaul the libcheese documentation
  Add documentation for CheeseCameraDevice. Remove bogus XML included in
  the library overview. Add section documentation to all classes, and mark
  them as unstable. Add GObject and GObjectClass struct documentation.
- help: renamed pages and rearranged sections
  Moved all pages, except introduction.page, into sections to make index
  look nicer.
- Use license-type in the about dialog
- Connect thumbnail nav button signals
  The thumb nav widget crashed when clicking the buttons to scroll the
  thumbnail view. This was caused by connecting to the wrong signals:
  ‘button-pressed-event’ and ‘button-released-event’, rather than
  ‘pressed’ and ‘released’. There was also some duplicate code for
  creating the left button, which led to a GtkButton being leaked when
  the thumb nav was created. Fixes bug 660686.
- Remove obsolete MAINTAINERS file
  http://live.gnome.org/Git/FAQ#How_do_I_add_a_description_to_the_git_web_view.3F__What_is_this_.22blah.doap.22.3F
- Remove obsolote cicl script
- Increase the photo count in burst mode to 100000
  Fixes bug 659977
- Use an idle handler to generate thumbnails
  A thread was used for generating thumbnails for CheeseThumbView, but
  this had problems with concurrent access to the GtkListStore which
  backs the thumb view, as in bug 648936. A simpler approach is to use an
  idle handler, which avoids the need for acquiring the GDK lock.
- Restore gudev checks during configure
- Added/Updated Translations
- be, courtesy of Yuri Matsuk
- de, courtesy of Mario Blättermann
- es, courtesy of Daniel Mustieles
- et, courtesy of Mattias Põldaru
- gl, courtesy of Fran Dieguez
- he, courtesy of Yaron Shahrabani
- lt, courtesy of Aurimas Černius
- nb, courtesy of Kjartan Maraas
- sv, courtesy of Daniel Nylander
- tr, courtesy of Muhammet Kara
- xh, courtesy of Andiswa Mvanyashe
- Added/Updated Documentation
- es, courtesy of Daniel Mustieles


what's changed in 3.2.0?
========================


- configure.ac: Bump Cheese version to 3.2.0
- Added/Updated Translations
- as, courtesy of Nilamdyuti Goswami
- gl, courtesy of Leandro Regueiro
- or, courtesy of Manoj Kumar Giri
- Added/Updated Documentation
- de, courtesy of Mario Blättermann
- es, courtesy of Daniel Mustieles
- gl, courtesy of Leandro Regueiro

