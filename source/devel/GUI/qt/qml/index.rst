
.. index::
   Qt GUI (QML)
   GUI (Qt GUI QML)


.. _qt_gui_qml:

=============================
QML (Qt Meta-Object Language)
=============================


.. seealso::

   - https://secure.wikimedia.org/wikipedia/en/wiki/QML
   - http://qt.gitorious.org/qt-components/desktop
   - :ref:`javascript_language`


QML (Qt Meta-Object Language) is a JavaScript-based, declarative language for
designing user interface centric applications.

It is part of the Nokia Qt framework. QML is mainly used for mobile applications
where touch input, fluid animations (60 FPS) and user experience are crucial.

QML documents describe an object tree of elements. QML elements[2] shipped with
Qt are a sophisticated set of building blocks, graphical (e.g., rectangle, image)
and behavioral (e.g., state, transition, animation).

These elements can be combined to build components ranging in complexity from
simple buttons and sliders, to complete internet-enabled programs.

QML elements can be augmented by standard JavaScript both inline and via
included .js files.

Elements can also be seamlessly integrated and extended by C++ components using
the Qt framework.

The language name is QML. The runtime name is Qt Declarative.


QML components for desktop
==========================

.. seealso:: http://labs.qt.nokia.com/2011/03/10/qml-components-for-desktop/


While waiting for things to calm down a bit around here, I have been happily
hacking on a new research project.

Since most of you have probably guessed what it is about by now, I will start
by pointing you to this video

t Quick has been the main focus of Nokia for some time now. I wanted to see if
we could bring some of the fun and joy of working with QML to the good old
desktop. It is true that you can easily make your own widgets with Qt Quick,
but obviously not everyone wants to do that. Having personally invested quite
a bit of time in developing among others the GTK+ and Vista styles in Qt, I also
wanted to prove that we could make use of that effort even in the brave new world
of Qt Quick.

.. seealso:: http://qt-quarterly.developpez.com/qq-35/plusieurs-interfaces-meme-logique/#LIII


Préambule
=========

Je pense que la plupart d'entre vous ont entendu parler de QML ou de
``declarative UI``, mais sans vraiment trop savoir de quoi ça parle.

Je vais essayer de résumer.

L'architecture "widget" est une architecture robuste et structurée qui a fait
ses preuves. Mais cette architecture est peu flexible, peu adaptée aux
composants non rectangulaires et aux animations.
**Qui fournit donc des IHM très statiques.**

Seulement, le besoin change. Et à quoi devrait ressembler une IHM dans le futur
pour vous ? Sûrement à des IHM vivantes avec une plus grande interaction avec
l'utilisateur avec des petits effets visuels. Le meilleur exemple son les
téléphones mobiles et leurs interfaces de plus en plus attractives.

Il suffit de regarder l'interface de l'iPhone, Androïd, HTC et compagnie. Rien à
voir avec les logiciels d'aujourd'hui. Tout est en mouvement : on zoome, on fait
des rotations... On exploite le stylet, le doigt, la luminosité ambiante,
l'orientation de l'appareil...
L'application de visualisation de photo de l'iPhone est un très bon exemple.
Et bien sûr, la mode commence à s'étendre sur les PC.

En gros voilà declarative UI est un projet R&D de Nokia sur le développement
de ces IHM, et QML un langage pour exprimer de manière lisible (par un humain)
ces IHM.

Voici deux vidéos très intéressantes :

- La première est sur leur moteur de rendu QGraphics :
  Advanced Graphics Programming with Qt <http://blip.tv/file/2562072/>

- La deuxième sur les futures interfaces sur mobile (mais ça reste valide
  pour un PC) :
  New user interface paradigms on mobile devices <http://blip.tv/file/2561463/>


Pour être plus clair, voici quelques vidéos en plus.

Deux démonstrations utilisant QGraphics et QtAnimation.
Et donc ce qui sera déjà possible avec Qt 4.6 :

- YouTube- Qt Kinetic Animated Tiles Example
  <http://www.youtube.com/watch?v=NEVrwYAAUvU&feature=channel_page>

- YouTube- TubeWiz: Unleashing the power of Qt for S60
  <http://www.youtube.com/watch?v=NjxfEud_B6U&feature=channel_page>

Deux démonstrations utilisant QML et du javascript montrant ses premières
possibilités:

- YouTube- QML Same Game Demo <http://www.youtube.com/watch?v=8Bvm4E819UY>
- YouTube- QML flickr browser demo <http://www.youtube.com/watch?v=xoo_Ows1ExU>

De plus, Developpez.com met des binaires précompilés de Qt à votre disposition.
Dans les quel vous trouverez une version compilée pour visual 2008 SP1 de la
branche /kinetic-declarative-ui/ et donc voir à quoi cela va ressembler et bien
sûr de jouer avec

*Des binaires Qt à disposition !* <http://www.developpez.net/forums/m4657309-10/>

Et vous que pensez-vous de tout cela ? Vous êtes pour ? Contre ? Des remarques
positives ou négatives ?


Introduction
============

Une interface utilisateur Qt Quick est construite depuis QML.
Tout le code QML  est exécuté dans un contexte.
Chaque contexte est représenté par un objet QDeclarativeContext.

Pour QDeclarativeEngine, il y a un contexte racine qui contient les objets et
valeurs globalement disponibles.

Pour exposer un QObject en tant que pièce de code QML, l'objet est défini en
tant que valeur d'une propriété contextuelle, comme montré dans le code suivant::

    QObject *obj = new MyLogic();
    QDeclarativeEngine *engine = ...;
    engine->rootContext()->setContextProperty("logic", obj);

Cela expose l'objet au code QML dans lequel on peut y accéder en utilisant le
nom logic::

    MouseArea {
        ...
        onClicked: { logic.actOnClick(); }
    }

La bonne chose dans l'exposition de propriétés contextuelles à QML est qu'elles
s'associent bien avec la nature de binding de QML. Cela signifie que, si l'on
définit la propriété contextuelle sceneWidth à 400 et qu'on la modifie par
la suite à 500 (ou toute autre valeur), toutes les expressions dans QML
dépendant de sceneWidth seront automatiquement actualisées.


Qt quick applications
======================

.. seealso::

   - http://blogs.forum.nokia.com/blog/nokia-developer-news/2011/02/23/new-apps-showcase-qt-quick
   - https://projects.forum.nokia.com/qmultiwinexample
   - https://projects.forum.nokia.com/qtbubblelevel

Qt defis
--------

.. seealso:: - http://qt.developpez.com/defis/02-tablette-hopital/resultats


Capteurs et QML
---------------

.. seealso:: http://qt-quarterly.developpez.com/qq-35/pactole-capteurs/#LIV-B


En QML, il y a un élément pour chaque type de capteur. Pour les accéléromètres,
il s'agit d'Accelerometer. Les autres éléments sont nommés d'une manière très
similaire aux classes C++, comme RotationSensor et ProximitySensor::

    Accelerometer {
        id: sensor

        onReadingChanged: {
            xText.text = "X: " + reading.x.toFixed(2)
            yText.text = "Y: " + reading.y.toFixed(2)
            zText.text = "Z: " + reading.z.toFixed(2)

            var subFromAngle = screen.width > screen.height ? Math.PI : Math.PI/2
            var angle = Math.atan2(reading.y, -reading.x)
            theColumn.rotation = (angle-subFromAngle) * (180/Math.PI)
            ...
        }
    }

Pour lire les données, on utilise le gestionnaire de signal onReadingChanged,
appelé quand QSensor émet QSensor::readingChanged().
Les données sont disponibles dans la propriété Accelerometer::reading.
theColumn est une Column qui contient trois éléments Text, qui affichent les
données de l'accéléromètre.



.. toctree::
   :maxdepth: 4

   feeling_1





