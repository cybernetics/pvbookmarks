

.. index::
   python (filesystem shutil)


.. _python_filesystem_shutil:

=========================
python filesystem shutil
=========================

.. seealso::

    - http://docs.python.org/py3k/library/shutil.html

copytree example
================

This example is the implementation of the :func:`copytree` function, described
above, with the docstring omitted.  It demonstrates many of the other functions
provided by this module. ::

   def copytree(src, dst, symlinks=False):
       names = os.listdir(src)
       os.makedirs(dst)
       errors = []
       for name in names:
           srcname = os.path.join(src, name)
           dstname = os.path.join(dst, name)
           try:
               if symlinks and os.path.islink(srcname):
                   linkto = os.readlink(srcname)
                   os.symlink(linkto, dstname)
               elif os.path.isdir(srcname):
                   copytree(srcname, dstname, symlinks)
               else:
                   copy2(srcname, dstname)
               # XXX What about devices, sockets etc.?
           except (IOError, os.error) as why:
               errors.append((srcname, dstname, str(why)))
           # catch the Error from the recursive copytree so that we can
           # continue with other files
           except Error as err:
               errors.extend(err.args[0])
       try:
           copystat(src, dst)
       except WindowsError:
           # can't copy file access times on Windows
           pass
       except OSError as why:
           errors.extend((src, dst, str(why)))
       if errors:
           raise Error(errors)

Another example that uses the :func:`ignore_patterns` helper::

   from shutil import copytree, ignore_patterns

   copytree(source, destination, ignore=ignore_patterns('*.pyc', 'tmp*'))

This will copy everything except ``.pyc`` files and files or directories whose
name starts with ``tmp``.








