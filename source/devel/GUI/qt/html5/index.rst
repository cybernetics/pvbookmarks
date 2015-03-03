

.. index::
   pair: Qt ; HTML5


.. _qt_gui_html5:

==================
Qt GUI HTML5
==================

.. seealso:: http://qt-quarterly.developpez.com/qq-35/plusieurs-interfaces-meme-logique/#LIV


Dans quelques situations, Qt Quick se complète avec HTML 5. Utiliser HTML 5
signifie que l'on peut obtenir du code réutilisable si l'on possède une
interface utilisateur que l'on souhaite déployer à la fois sur des moteurs Web
standard et en tant qu'application personnalisée.

En utilisant le module QtWebKit, il est entièrement possible de réaliser une
interface utilisateur autour d'une page Web, c'est-à-dire du code HTML 5.
L'intégration de QtWebKit n'inclut pas seulement le rendu HTML et un moteur
JavaScript, elle met également en place un pont permettant l'intégration de
multiples QObject à l'intérieur de JavaScript.

Lors du rendu des contenus Web, chaque page Web est représentée par un objet
QWebPage. Chaque page est alors représentée par une ou plusieurs frames,
QWebFrame. Pour chaque frame, un contexte JavaScript existe.
Ce contexte est nettoyé lorsque de nouvelles URL sont chargées. Cela résulte
de l'émission du signal javaScriptWindowObjectCleared. Lorsqu'il est émis,
les objets peuvent être ajoutés au contexte JavaScript par le biais de la
méthode addToJavaScriptWindowObject comme montré plus bas.

Il est bon de noter que l'on peut accéder à une frame (ou plusieurs) d'une page
à travers la mainFrame::

    QObject *obj = new MyLogic();
    QWebFrame *frame = webPage->mainFrame();
    frame->addToJavaScriptWindowObject("logic", obj);

Il n'existe aucun moyen d'exposer les objets contextuels de la même manière que
pour l'intégration C++ et QML. Au lieu de cela, chaque objet doit être ajouté en
tant qu'objet séparé au contexte.

Il est possible d'accéder et de modifier les propriétés de QObject depuis le
JavaScript. On peut également appeler des méthodes depuis le C++ vers le
JavaScript et vice-versa, tout comme émettre des signaux et réaliser des
connexions depuis les deux camps.



