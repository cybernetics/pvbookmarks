
.. _i18n_problems:

===========================
i18n problems
===========================


filelistview: transform filename to unicode
===========================================

::

    # HG changeset patch
    # User André Sintzoff <andre.sintzoff@gmail.com>
    # Date 1300821371 -3600
    # Node ID 59002a185e7b8937db2ee189f97de049b5426758
    # Parent  7eb2cdb2f684053fd1d444f0646122da88152610
    filelistview: transform filename to unicode


Since fd2662ea0068, changes from a file containing non ASCII
characters in its name are no more displayed in fileview as the
filename is incorrectly handled.

::

    @@ -95,7 +95,7 @@
                 index = self.currentIndex()
             data = self.model().dataFromIndex(index)
             if data:
    -            self.fileSelected.emit(data['path'], data['status'])
    +            self.fileSelected.emit(hglib.tounicode(data['path']), data['status'])
             else:
                 self.clearDisplay.emit()


guess: convert paths to unicode before display (fixes #410)
===========================================================

::

    @@ -209,9 +209,10 @@
             for index in self.matchtv.selectionModel().selectedRows():
                 src, dest, percent = self.matchtv.model().getRow(index)
                 if dest in remdests:
    +                udest = hglib.tounicode(dest)
                     QMessageBox.warning(self, _('Multiple sources chosen'),
                         _('You have multiple renames selected for '
    -                      'destination file:\n%s. Aborting!') % dest)
    +                      'destination file:\n%s. Aborting!') % udest)
                     return
                 remdests[dest] = src
             for dest, src in remdests.iteritems():
    @@ -233,7 +234,8 @@
             date = hglib.displaytime(ctx.date())
             difftext = mdiff.unidiff(rr, date, aa, date, src, dest, None)
             if not difftext:
    -            t = _('%s and %s have identical contents\n\n') % (src, dest)
    +            t = _('%s and %s have identical contents\n\n') % \
    +                    (hglib.tounicode(src), hglib.tounicode(dest))
                 hu.write(t, label='ui.error')
             else:
                 for t, l in patch.difflabel(difftext.splitlines, True):




Re: [PySide] I can not load files with non-utf8 names
=====================================================


::

    de  Benoît HERVIER <khertan@khertan.net>
    heure de l'expéditeur   Envoyé à 16:09 (GMT+01:00). Heure locale : 17:15. ✆
    à   hipersayan x <hipersayan.x@gmail.com>
    cc  pyside@lists.pyside.org
    date    23 mars 2011 16:09
    objet   Re: [PySide] I can not load files with non-utf8 names


Hi,

::

    # -*- coding: utf-8 -*-
    # ^ Declare that the file should be read by the python parser as utf-8
    img = QtGui.QImage()
    results = img.load(u'/home/MyHome/Imágenes/Vacación_En_España.png')
    #                          ^ create the string as unicode stringe


Should do the trick, and save your py file in utf-8.

For more informations with utf-8 and python, i often suggest
http://www.evanjones.ca/python-utf8.html

Regards,
