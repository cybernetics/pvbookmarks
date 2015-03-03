

.. _smartcard_io_5_august_2013:

===========================================
Intarsys smartcard.io August 5 2013
===========================================



::

    Frank Marien <frank@apsu.be>
    répondre à:	 MUSCLE <muscle@lists.musclecard.com>
    à:	 muscle@lists.musclecard.com
    date:	 5 août 2013 09:50
    objet:	 Re: [Muscle] Alternate javax.smartcardio provider

On 08/04/13 17:47, Michael Traut wrote::

    > Hello,
    >
    > For the deployment, we wanted to create a deliverable that is able to
    > compile without much effort. We will have a look if we can manage this
    > in a more standard way.
    >
    >
    
    
(for java) I would recommend using :ref:`Maven <maven>` if possible.

http://maven.apache.org/

This implies creating a pom.xml file describing the project and its
dependencies.

Maven has all sorts of packaging and deployment plugins, and even an
eclipse plugin that creates the eclipse project files for you.

inside the project, running::

    mvn eclipse:eclipse

will do just that: after that command the project can be imported into
eclipse and ran, debugged, etc..

In this way you can just ship your code + pom.xml, and have maven
download dependencies etc.. Makes it a lot easier for others, and for
everyone to to continuous builds etc..::

    build:
        mvn clean install

One step further is setting up a maven repository for your project: With
this in place everyone wanting to
use your code can just add a few dependency lines to their own pom.xml.

I'd be happy to help you get started.

