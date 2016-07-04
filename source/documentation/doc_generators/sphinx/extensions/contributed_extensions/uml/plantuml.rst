
.. index::
   pair: sphinx extension ; plantuml
   pair: UML ; plantuml

.. _sphinx_plantuml_extension:

========================
Sphinx plantum extension
========================

.. seealso::

   - https://pypi.python.org/pypi/sphinxcontrib-plantuml
   - :ref:`plant_uml`



Usage
=====

First, you may need to specify plantuml command in your conf.py:

plantuml = ['java', '-jar', '/path/to/plantuml.jar']

Instead, you can install a wrapper script in your PATH:

% cat <<EOT > /usr/local/bin/plantuml
#!/bin/sh -e
java -jar /path/to/plantuml.jar "$@"
EOT
% chmod +x /usr/local/bin/plantuml

Then, write PlantUML text under .. uml:: directive::

    .. uml::

       Alice -> Bob: Hi!
       Alice <- Bob: How are you?



