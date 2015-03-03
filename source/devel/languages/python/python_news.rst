.. module:: PythonNews
    :synopsis: Python
 
 
======
Python
======
   
   
.. index::
   ./configure --with-pydebug
   python ./configure --with-pydebug
   
   
Modifying Grammar/grammar and other foul acts
=============================================

.. seealso:: http://writeonly.wordpress.com/2010/04/01/whython-python-for-people-who-hate-whitespace/

::

    from    Gregg Lind <gregg.lind@gmail.com>
    to  
    cc  python-dev@python.org
    date    Sat, Mar 6, 2010 at 7:26 PM
    subject Re: [Python-Dev] Modifying Grammar/grammar and other foul acts
    mailing list    python-dev.python.org Filter messages from this mailing list

    
Sorry, re: question one, forgive the ill-formed question.  I meant more, are 
the parser rules applied "first matching".   Essentially trying to confirm 
that the parser is "top down" or "bottom up" or whether or not it even matters. 

Thanks for the tip -- it seems to be exactly what I want.  To make it explicit, 
this seems to be fuller (unix) recipe for how to make this style of debugging 
happen::

    $ ./configure --with-pydebug
    $ make
    $ set PYTHONDEBUG=1
    $ ./python -d   # then this shows the parsing info
    
    
::

    Guido van Rossum <guido@python.org>
    to  Gregg Lind <gregg.lind@gmail.com>
    cc  python-dev@python.org
    date    Sat, Mar 6, 2010 at 10:41 PM
    subject Re: [Python-Dev] Modifying Grammar/grammar and other foul acts
    mailing list    python-dev.python.org Filter messages from this mailing list

    
On Sat, Mar 6, 2010 at 10:26 AM, Gregg Lind <gregg.lind@gmail.com> wrote:
> Sorry, re: question one, forgive the ill-formed question.  I meant more, are
> the parser rules applied "first matching".   Essentially trying to confirm
> that the parser is "top down" or "bottom up" or whether or not it even
> matters.

That's not how it works at all. I can't explain it in a few words --
but any text on LL(1) parsing should clarify this. The parser uses no
backtracking and a 1-token lookahead. The only unusual thing is that
individual rules use a regex-like notation, but that is all converted
to a DFA. If one token is not enough to know which path to take
through the DFA (this may invoke another rule -- but you always know
which one) you're hosed.

I suspect you've introduced ambiguities, though I don't immediately
see where (they could be in the combination of different rules).

Another possibility is that you may be running into problems where the
parser expects a newline at the end of a suite.

(FWIW since you're not proposing a language change, this is
technically off-topic for python-dev. :-)

::

    from    Gregg Lind <gregg.lind@gmail.com>
    to  python-dev@python.org
    date    Thu, Apr 1, 2010 at 5:38 AM
    subject Re: [Python-Dev] Modifying Grammar/grammar and other foul acts
    mailing list    python-dev.python.org Filter messages from this mailing list

    
Thank you for the advice everyone.  This seed has finally born (rotten) fruit at:

http://writeonly.wordpress.com/2010/04/01/whython-python-for-people-who-hate-whitespace/
http://bitbucket.org/gregglind/python-whython3k/


.. index::
   book Dragon kook

http://writeonly.wordpress.com/2010/04/01/whython-python-for-people-who-hate-whitespace/
========================================================================================


More seriously:

* reading the Dragon Book Aho86_ gives a person dangerous ideas
* good excuse to deep dive into the python interpreter source code and the AST, dis modules
* finally wanted to learn GDB and python -d debug mode
* humoring trolls is fun
* for education, the whitespace thing really can cause problems. When
  copying code out of books into IDLE or IPython, there are corner cases when
  it terminates blocks “too early”, confusing new learners.
* preparation for the “Python Spring Cleaning” project, to see how hard it is
  to get and modify source, write a PEP, raise bug ideas, talk in irc, etc.
* since this is unlikely to ever be adopted by Python (I hope!), it will
  remain a useful exercise, unlike othe “bugs” which get fixed once and for
  all


.. _Aho86: http://www.amazon.com/exec/obidos/tg/detail/-/0201100886/104-0162389-6419108


.. index::
   PySide
   Mark Summerfield
   
PySide for Python 3 ?
=====================

:: 

    from    Mark Summerfield <list@qtrac.plus.com>
    reply-to    Mark Summerfield <mark@qtrac.eu>
    to  pyside@lists.openbossa.org
    date    Fri, Apr 9, 2010 at 4:19 PM
    subject [PySide] PySide for Python 3?
    mailing list    pyside.lists.openbossa.org Filter messages from this mailing list
    unsubscribe Unsubscribe from this mailing-list
    
    
Hi,

I am hoping that at some point this year there will be a PySide for
Python 3?

If there is, will it support PyQt's API 2 (which IMO is nicer than the
API 1 provided by PySide and PyQt for Python 2)?

I'd really like to convert all my PyQt apps to Python 3, and ideally I'd
like them all to work with both PyQt and PySide with as few changes as
possible to account for the differences (i.e., just having an import
that tries for one and falls back to the other).

--
Mark Summerfield, Qtrac Ltd, www.qtrac.eu
C++, Python, Qt, PyQt - training and consultancy
"Advanced Qt Programming" - ISBN 0321635906
       
    
::
    
    from    Matti Airas <matti.p.airas@nokia.com>
    to  pyside@srvrec006.openbossa.org
    date    Mon, Apr 12, 2010 at 9:31 AM
    subject Re: [PySide] PySide for Python 3 ?
    
    

That's definitely on our roadmap, but with the Shiboken schedules already 
slipping, it's a bit premature to say when the core team will be able to 
allocate time for it.

Adding Python 3 CPython API code generation support to Shiboken sounds like 
a perfect project for some enterprising Python hacker. ;-)::

    If there is, will it support PyQt's API 2 (which IMO is nicer than the
    API 1 provided by PySide and PyQt for Python 2)?

I have to admit I've had very limited experience on the PyQt's API v2 other 
than  reading through the relevant reference pages. They'd generally seem 
like the right thing (apart from the implementation-specific way of selecting 
the API version) but since these changes would imply making slightly 
incompatible API modifications between PySide versions, I'd really prefer 
making an reasoned decision using the `PSEP process <http://www.pyside.org/docs/pseps/psep-0001.html>`_.

Also, with my very limited experience on the API changes, I don't feel 
comfortable about being the champion for that PSEP. Anyone willing to 
take the ball ? It shouldn't be too much work to write the proposal.::


    I'd really like to convert all my PyQt apps to Python 3, and ideally I'd
    like them all to work with both PyQt and PySide with as few changes as
    possible to account for the differences (i.e., just having an import
    that tries for one and falls back to the other).


Yep, that'd definitely be a preferable goal.

Cheers,

.. index::
   PyQt's API 2

   
PyQt's API v2
-------------

.. seealso:: http://www.qtrac.eu/pyqtbook.html#pyqtapis


About PyQt's APIs—From PyQt4.6, PyQt has two APIs, API#1 (the original), 
and API#2 (new). API#2 is more Pythonic and eliminates QString and QVariant, 
and is a bit nicer to use. API#1 remains best for those using PyQt to 
prototype C++/Qt applications. API#1 is the default for PyQt4.x with 
Python 2.x, and for PyQt4.0-4.5 with Python 3.x, and is the API used 
by PySide. API#2 is the default for PyQt4.6+ with Python 3.x. 

The book, and all its examples use API#1, so they don't work with 
PyQt4.6+ with Python 3.x—but they do work with PyQt4.x with Python 2.x, 
and for PyQt4.0-4.5 with Python 3.x. 

.. warning:: Although I personally prefer API#2, I am not planning to port the examples 
   to use it, since it would make the examples so far out of sync with the 
   book as to be confusing. 

       
[Python-Dev] [RELEASED] 2.7 beta 1
==================================

from    Guido van Rossum <guido@python.org>
-------------------------------------------

:: 


    from    Guido van Rossum <guido@python.org>
    to  Antoine Pitrou <solipsis@pitrou.net>
    cc  python-dev@python.org
    date    Sun, Apr 11, 2010 at 9:36 PM
    subject Re: [Python-Dev] [RELEASED] 2.7 beta 1

        
hide details 9:36 PM (11 hours ago)
    
On Sat, Apr 10, 2010 at 11:57 AM, Antoine Pitrou <solipsis@pitrou.net> wrote:
> Benjamin Peterson <benjamin <at> python.org> writes:
>>
>> On behalf of the Python development team, I'm merry to announce the first beta
>> release of Python 2.7.
>
> Congratulations, and thanks for your patience :)

Congratulations indeed!

Let me use this occasion to point out what an awesome community
python-dev is. Not only do we have an great release manager (kudos to
Benjamin for taking on this thankless job of herding cats), but the
whole developer community has been contributing to some excellent
releases. This makes me very happy and confident that Python will
continue to thrive for many, many years, with or without my direct
involvement in the details. While rumors of my retirement are greatly
exaggerated, I am very glad to be able to leave the details to the
community.

Keep them coming, folks!

--
--Guido van Rossum (python.org/~guido)


