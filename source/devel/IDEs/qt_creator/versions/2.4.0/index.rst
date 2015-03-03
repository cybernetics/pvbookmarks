
.. index::
   pair: Qt Creator; 2.4.0




.. _qt_creator_2_4_0:

=============================================
Qt Creator 2.4.0
=============================================


.. seealso::

   - http://labs.qt.nokia.com/2011/12/13/qt-creator-2-4-0-released/
   - http://developer.qt.nokia.com/wiki/Qt_Creator_Releases
   - http://qt.developpez.com/actu/40030/Qt-Creator-2-4-est-sorti-cette-nouvelle-version-de-l-EDI-pour-Qt-ameliore-le-support-de-QML/


.. figure:: annonceur.jpeg


We are happy to announce that finally Qt Creator 2.4.0 is ready to be published.

I’ll summarize a few of the great amount of features and improvements in this
release.

You find a longer list in our change log, and you can also have a look at what
we fixed for 2.4.0 in our bugtracker.

The commit log from our repository is only recommended if you have a lot of time:
Around 1300 commits have been accepted since 2.3.1.

Lots of thanks go to the contributors, you find a list at the end of the change log :)

My personal highlight:

- The “synchronize declaration and definition” quick fix, and the fixes for
  the “create definition from declaration”. When you change either declaration
  or definition you’ll notice a little lightbulb appearing.
  If you now press “alt+return” (or click the bulb) your changes are applied
  to the counter part.
- “Schemes” for the coding styles (C++ and QML), reusable between projects
- QML rename usages and semantic highlighting
- Access most recent searches
- Encoding fixes for search & replace and the refactorings
- Subversion 1.7 support
- Netbook users will be glad to hear that the preferences dialog now has a
  decent size again


At the end a few words of advice: Because of the coding schemes, you’ll now need
to change the coding style to change tab and indentation settings for code
(was  done in text editor settings before).

Qt Creator tries to migrate existing text editor settings to the new style for
your projects, but if you had project specific settings before **you’ll need to
set them again**.

If you are confused where the Qt version settings have gone: They are now in the
“Build & Run” category, together with the tool chain and the general project
settings.

You can download the standalone release from `DevNet`_, and the release is going
out as an update to users of the Qt SDK (might take a few hours to spread through
the world).


.. _`DevNet`:  http://developer.qt.nokia.com/wiki/Qt_Creator_Releases








