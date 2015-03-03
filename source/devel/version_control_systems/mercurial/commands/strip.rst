
.. index::
   hg strip

=========
hg strip
=========


.. seealso::

   - http://mercurial.selenic.com/wiki/Strip
   - http://hgbook.red-bean.com/read/mercurial-queues-reference.html#id446269


The hg strip command removes a revision, and all of its descendants, from the
repository. It undoes the effects of the removed revisions from the repository,
and updates the working directory to the first parent of the removed revision.


[Python-Dev] Re: [Python-Dev] Workflow proposal
===============================================

::

    de Antoine Pitrou <solipsis@pitrou.net>
    heure de l'expéditeur   Envoyé à 03:41 (GMT+01:00). Heure locale : 10:18. ✆
    à   python-dev@python.org
    date    23 mars 2011 03:41
    objet   Re: [Python-Dev] Workflow proposal
    On Wed, 23 Mar 2011 10:39:01 +0900

::

    "Stephen J. Turnbull" <stephen@xemacs.org> wrote:
    > Executive summary:
    >
    > If we're really serious about serializing the public branches, mq
    > seems to be the way to go.

I really think that at this point we should continue practicing with
the current setup before deciding on refinements or changes.


::

    >  > 6. Use "hg strip" (dangerous!) to delete the local merges to 3.2 and
    >  > "default". Leave the original commit in "3.1" alone.
    >
    > I would suggest "hg strip --keep" which leaves the working copy
    > unchanged.


Now, "hg strip" should definitely be absent of any recommended or even
suggested workflow. It's a power user tool for the experimented
developer/admin. Not the average hg command.

By the way, whether or not mq gets used is pretty much anyone's private
decision (unless we decide that patches must get split into logical
units and mailbombed for review ala mercurial-devel, which would be a
significant departure from our development habits).

Regards

