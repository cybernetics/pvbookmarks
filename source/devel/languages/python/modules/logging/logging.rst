
.. index::
   Python modules (logging)

=======  
Logging
=======

Le module de logging standard
=============================

- http://docs.python.org/library/logging.html

C'est le module que j'ai utilisé, le module Logbook
n'existant pas quand j'ai commencé.

voir la défense du module standard par son créateur:

- http://plumberjack.blogspot.com/2010/09/python-logging-functionality-facts-vs.html
  Some inaccuracies and misunderstandings about how stdlib logging works have been 
  expressed in the documentation and marketing presentations of a suggested alternative. 
  On closer examination, certain statements which imply a lack of functionality or other 
  shortcomings in stdlib logging have been shown to be inaccurate. You should feel 
  confident that in using the stdlib logging package you are very unlikely to find 
  it wanting, and that, if it seems too hard or not possible to achieve some result 
  that you want to achieve, you should raise the issue on comp.lang.python or 
  bugs.python.org and be assured of prompt responses and resolutions. Now, you 
  can read on if you want more details :-).
  
  Recently Armin Ronacher, developer of Werkzeug and Jinja among other things, 
  released a library for logging which, in his opinion, is preferable to the logging 
  package provided as part of Python since the 2.3 release. Now preferences are a 
  very personal thing, and since Armin has made worthy software contributions to 
  the Python community, there will no doubt be many people who trust his judgement 
  and follow where he leads. In general, choice in software is good, and people 
  should be free to make up their own minds about the software they want to use.   
  However, in order to make an informed decision, people need accurate information 
  on which to base that decision. For example, I chose to use argparse over the 
  stdlib's optparse even before argparse landed in the stdlib; in making that 
  choice, I looked at Steven Bethard's rationale as described here and was fortunate 
  to have the time to be able to examine and evaluate each of his points for myself.
  
