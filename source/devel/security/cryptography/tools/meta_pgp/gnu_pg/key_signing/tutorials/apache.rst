
.. index::
   pair: Apache; Key signing

.. _tuto_key_signing_apache:

===============================
Howto Key signing Apache
===============================


.. seealso::

   - https://people.apache.org/~henkp/sig/pgp-key-signing.txt


.. contents::
   :depth: 3

Introduction
=============

An oportunity!  A conference provides a great opportunity to get your
pgp key signed and to sign a the keys of others, but it is just
somewhat easier to assert somebody's identity in person.

Why bother?  Here at the ASF we use PGP keys to sign releases tar
files.  Careful users can then check that somebody from the ASF
actually indicated that he 'approved' those bits for release from the
foundation.  Extra careful users complain if the PGP key that did the
signing hasn't been signed by a few other people.  And yes, we always
have few of these and they do complain.

Act now!  A little prep can make all the difference. 

The most important thing is to have printed up your finger print on
some scraps of paper.  That might look like this::


    pub  1024R/187BD68D 1997-09-30 Ben Hyde <bhyde@pobox.com>
          Key fingerprint = 90 AA 4C 16 6C 9D 12 DC  3D 8B 86 E5 0E 33 CE 52



Good things to have done before hand:

- 1) Scraps of paper with your finger print on them.
- 2) Put your key on a few key servers.
- 3) Retrieved a key (at the MIT key server for example http://pgp.mit.edu)
- 4) Practice signing a key, using GPG probably.
- 5) Have something to capture other people keys prepared (who
     didn't come prepared with a scrap of paper) so you can sign their keys.
   

When you encounter folks who might sign your key offer them the scrap
of paper with your finger print on it and ask for one in return.

Later, but soon, you should: 

- (a) find their key, 
- (b) sign it 
- and (c) upload the result back to the key server from which you down loaded
  it.  You're done, you're cool.  
  With luck they will get around to signing your key at some point too.

**Don't sign somebody elses key if you haven't "authenticated" them.**

Pause and think about how many "factors" you have that convince you
that this is both the person who owns that key and the person who the key
names.  

There are lots of factors you might use.  

A shared experience.

An introduction from somebody you know.  Checking ID.

Don't go overboard with the authentication or you'll never sign anybody's
keys.

**Signing a key does not indicate that you "trust" the person**.  

It only indicates that you believe that key is tied to the correct person.  
In fact it is valuable to the network of signatures if you sign the keys
of members of other communities.  

So signing the keys of near strangers is a good thing.  
Just be confident of their identity.

Tricks for slightly improving the efficiency of this:

The slip of paper with the finger print is the important one.  
You can expedite that with some mass production.

I) Print the fingerprints of people you expect to encounter
------------------------------------------------------------

It is a pain writing down a fingerprint by hand.  

You can avoid that by printing up a sheet of paper with the fingerprint of 
everybody you hope to meet.  

Then when you meet them you can just check that they agree that is their 
fingerprint.  

Make a mark on your paper and do your signing later.

II) Make a handout with the fingerprints of attendees printed up on it
-----------------------------------------------------------------------

Sometimes people will hand out a paper like that.  
Do not sign all the keys on that paper.  
You must assert each identity one at a time.

You don't need a conference to do this.

You can carry a few of the scraps of paper in your wallet. (I never
remember to hand them to people when I meet them.)  Some people are so
cool they have the finger print printed on their business card; or
stored in their PDA for later "beaming."
