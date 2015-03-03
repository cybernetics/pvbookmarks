
.. index::
   pair: Qt ; GUI


.. _qt_GUI:

=======
Qt GUI
=======


.. seealso::

   - :ref:`qt_ide`
   - http://qt-quarterly.developpez.com/qq-35/plusieurs-interfaces-meme-logique/


.. contents::
   :depth: 3


Introduction
=============

C++ a été écrit à de nombreuses reprises dans cet article mais tout cela
s'applique également à tout langage tel que Python, Ruby ou tout autre langage
avec les bindings Qt.

L'objectif n'est pas d'apprendre à réaliser une interface utilisateur en
utilisant le C++ et Qt. Au lieu de cela, pourquoi ne pas regarder comment
garantir que l'interface utilisateur et la partie logique soient gardées séparées ?

Lorsque l'on s'appuie sur Qt Quick ou HTML 5, on est forcé de définir une
interface entre la partie logique et l'interface utilisateur.
Lors de l'utilisation du C++ pour réaliser à la fois la partie logique et
l'interface utilisateur, il est nécessaire de placer ces restrictions sur soi-même.

La clé ici est que tout code affectant uniquement l'interface utilisateur fait
partie de l'interface utilisateur tandis que tout code affectant l'état de
l'application (par exemple, le contenu d'un document) est membre de la partie logique.

La partie logique nécessite d'être maintenue dans un ensemble séparé de classes.
Pour réellement se forcer à atteindre cet objectif, un objet de document pour
chaque fenêtre de document est une bonne idée.

Pour les autres types d'applications, l'objet contextuel en provenance d'une
intégration Qt Quick peut être réutilisé.


Différents utilisateurs attendent différentes interfaces utilisateur. Dans des
systèmes multiutilisateurs, ces interfaces pourraient se différencier non
seulement par l'apparence et les fonctionnalités, mais encore par la manière
dont elles sont implémentées.

Qt supporte des interfaces classiques basées sur des widgets, tout comme des
interfaces plus modernes via Qt Quick. En plus de ces deux technologies
spécifiques à Qt, HTML5 est aussi supporté, grâce à l'intégration avec WebKit.

En séparant l'application en des parties séparées et réutilisables, on peut
utiliser le même code logique pour créer des expériences utilisateur pour tous
les utilisateurs - le tout avec Qt.


Qt on ubuntu
============

.. seealso:: http://www.markshuttleworth.com/archives/568


As part of our planning for Natty+1, we’ll need to find some space on the CD
for Qt libraries, and we will evaluate applications developed with Qt for
inclusion on the CD and default install of Ubuntu.

Ease of use, and effective integration, are key values in our user experience.
We care that the applications we choose are harmonious with one another and the
system as a whole.

Historically, that has meant that we’ve given very strong preference to
applications written using Gtk, because a certain amount of harmony comes by
default from the use of the same developer toolkit.

That said, with OpenOffice and Firefox having been there from the start, Gtk is
clearly not an absolute requirement.

What I’m arguing now is that it’s the values which are important, and the
toolkit is only a means to that end. We should evaluate apps on the basis of
how well they meet the requirement, not prejudice them on the basis of technical
choices made by the developer.

In evaluating an app for the Ubuntu default install, we should ask:

* is it free software?
* is it best-in-class?
* does it integrate with the system settings and preferences?
* does it integrate with other applications?
* is it accessible to people who cannot use a mouse, or keyboard?
* does it look and feel consistent with the rest of the system?

Of course, the developer’s choice of Qt has no influence on the first two.

Qt itself has been available under the GPL for a long time, and more recently
became available under the LGPL.

And there’s plenty of best-in-class software written with Qt, it’s a very
capable toolkit.

...

The decision to be open to Qt is in no way a criticism of GNOME. It’s a
celebration of free software’s diversity and complexity. Those values of ease
of use and integration remain shared values with GNOME, and a great basis for
collaboration with GNOME developers and project members.

Perhaps GNOME itself will embrace Qt, perhaps not, but if it does then our
willingness to blaze this trail would be a contribution in leadership. It’s
much easier to make a vibrant ecosystem if you accept a certain amount of
divergence from the canonical way, so to speak  Our work on design is centered
around GNOME, with settings and preferences the current focus as we move to
GNOME 3.0 and gtk3.

Of course, this is a perfect opportunity for those who would poke fun at that
relationship to do so, but in my view what matters most is the solid
relationship we have with people who actually write applications under the
GNOME banner.

We want to be the very best way to make the hard work of those free software
developers *matter*, by which we mean, the best way to ensure it makes a real
difference in millions of lives every day, and the best way to connect them to
their users.

To the good folks at Trolltech, now Nokia, who have made Qt a great toolkit
– thank you.

To developers who wish to use it and be part of the Ubuntu experience – welcome.


.. seealso:: http://qt.developpez.com/doc/4.7/liste-des-pages-traduites/



Qt doc
======


.. toctree::
   :maxdepth: 4

   accessibility/index
   applis/index
   extensions/index
   generators/index
   html5/index
   news/index
   qml/index
   qt_widgets/index
   ui/index


Qt Quick
========


.. toctree::
   :maxdepth: 4

   qt_quick/index



pyside, pyqt, pythonqt
======================


.. toctree::
   :maxdepth: 4

   pyside/index
   pyqt/index
   pythonqt/index





