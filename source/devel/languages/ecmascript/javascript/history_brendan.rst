



.. index::
   javascript history


.. _javascript_history:

===================
javascript history
===================

.. seealso:: http://brendaneich.com/2011/06/new-javascript-engine-module-owner/


As you may know, I wrote JavaScript in ten days. JS was born under the shadow of
Java, and in spite of support by marca and Bill Joy, JS in 1995 was essentially
a one-man show.

I had a bit of help, even at the start, that I’d like to acknowledge again.
Ken Smith, a Netscape acquiree from Borland, ported JDK 1.0-era java.util.Date
(we both just drafted off of the Java truck, per management orders; we did not
demur from the Y2K bugs in that Java class). My thanks also to Netscape 2's
front-end hackers, chouck, atotic, and garrett for their support.

EDIT: can’t forget spence on the X front end!

That was 1995. Engine prototype took ten days in May. Bytecode compiler and
interpreter from the start, because Netscape had a server-side JS product in
the works. The rest of the year was browser integration, mainly what became
known as “DOM level 0?. Only now standardized in HTML 5 and Anne’s wg.
Sentence fragments here show my PTSD from that sprint :-/.

In 1996 I finally received some needed assistance from RRJ, who helped port
David M. Gay and Guy Steele’s dtoa.c and fix date/time bugs.

Also in summer 1996, nix interned at Netscape while a grad student at CMU, and
wrote the first LiveConnect. I am still grateful for his generous contributions
in wide-ranging design discussions and code-level interactions.

At some point in late summer or early fall 1996, it became clear to me that JS
was going to be standardized. Bill Gates was bitching about us changing JS all
the time (some truth to it; but hello! Pot meet Kettle…). We had a standards
guru, Carl Cargill, who knew Jan van den Beld, then the Secretary-General of
ECMA (now Ecma). Carl steered our standardization of JS to ECMA.

Joining ECMA and participating in the first JS standards meeting was an
eye-opener. Microsoft sent a B-team, and Borland and a company called NOMBAS
also attended. “Success has many fathers” was the theme. The NOMBAS founder
greeted me by saying “oh, we’ve been doing JavaScript for *years*”. I did not
see how that could be the case, unless JS meant any scripting language with
C-based syntax. I had not heard of NOMBAS before then.

At that first meeting, I think I did well enough in meta-debate against the
Microsoft team that they sent their A-team to the next meeting. This was all
to the good, and Microsoft in full-blooded compete mode, but also with
individual initiative beyond the call of corporate duty by Shon Katzenberger,
materially helped create ES1. Sun contributed Guy Steele, who is composed of
pure awesome. Guy even brought RPG for fun to a few meetings (Richard
contributed ES1 Clause 4).

Meanwhile, in fall 1996, I was under some pressure from Netscape management to
write a proto-spec for JS, but that was not something I could do while also
maintaining the “Mocha” engine all by myself in both shipping and future
Netscape releases, along with all of the DOM code.

This was a ton of work, and on top of it I had to pay off substantial technical
debt that I had willingly taken on in the first year. So I actually stayed
home for two weeks to rewrite Mocha as the codebase that became known as
SpiderMonkey, mainly to get it done (no other way), also to go on a bit of a
strike against the Netscape management team that was still underinvesting in JS.
This entailed garbage collection and tagged values instead of slower
reference-counting and fat discriminated union values.

Also in fall 1996, chouck decided to join me as the second full-time
JS team-mate. He and I did some work targeting the (ultimately ill-fated)
Netscape 4 release. This work was ahead of its time. We put the JS engine
in a separate thread from the “main thread” in Netscape (still in Mozilla).
This allowed us to better overlap JS and HTML/CSS/image computations, years
ahead of multicore. You could run an iloop in JS and the “slow script dialog”
seamlessly floated above it, allowing you to stop the loop or permit it
to continue.

After summer 1996 and the start of ECMA-262 standardization, Netscape finally
invested more in JS. Clayton Lewis joined as manager, and hired Norris Boyd,
who ended up creating Rhino from SpiderMonkey’s DNA transcoded to Java.
This was ostensibly because Netscape was investing in Java on the server,
in particular in an AppServer that wanted JS scripting.

I met shaver for the first time in October 1996 at Netscape’s NY-based
Developer Conference, where he nimbly nerd-blocked some Netscape plugin API
fanboys and saved me from having to digress from the main thing, which was
increasingly JS.

Some time in 1997, shaver contributed “LiveConnect 2?, based on more mature
Java reflection APIs not available to nix in 1996. Clayton hired shaver and
the JS team grew large by end of 1997, when I decided to take a break from
JavaScript (having delivered ES1 and ES2) and join the nascent mozilla.org.

I handed the keys to the JS kingdom to Waldemar Horwat, now of Google, in
late 1997. Waldemar did much of the work on ES3, and threw his considerable
intellect into JS2/ES4 afterwards, but without overcoming the market power
and stalling tactics of Microsoft.

True story: Waldemar’s Microsoft nemesis on TC39 back then, at the time a
static language fan who hated JS, has come around and now endorses JS and
dynamic languages.

Throughout all of this, I maintained module ownership of SpiderMonkey.

Fast-forward to 2008. After a great (at the time) Firefox 3 release where
@shaver and I donned the aging super-hero suits one more time to compete
successfully on interpreter performance against JavaScriptCore in WebKit,
Andreas Gal joined us for the summer in which we hacked TraceMonkey, which we
launched ahead of Chrome and V8.

A note on V8: I’d learned of it in 2006, when I believe it was just starting.
At that point there was talk about open-sourcing it, and I welcomed the idea,
encouraging any of: hosting on code.google.com, hosting without any pressure
to integrate into Firefox on mozilla.org (just like Rhino), or hosting with
an integration plan to replace SpiderMonkey in Firefox. I had to disclose that
another company was about to release their derived-from-JS engine to Mozilla,
but my words included “the more the merrier”. It was early days as far as
JS JITs were concerned.

V8 never open-sourced in 2006, and stealthed its way to release in September
2008. This may have been a prudent move by Google to avoid exciting Microsoft.
Clearly, in 1995, the “Netscape + Java kills Windows” talk from Netscape
antagonized Microsoft. I have it on good authority that a Microsoft board
member wrote marca at the end of 1995 warning “you’ve waved the cape in the
bull’s face — prepare to get the horns!” One could argue that Chrome in 2008
was the new red cape in the bull’s face, which begot IE9 and Chakra.

Whatever Google’s reasoning, keeping V8 closed-source for over two years hurt
JS in this sense: it meant Apple and Mozilla had to climb the JIT learning
curves on their own (at first; then finally with the benefit of being able to
inspect V8 sources).
Sure, the Anamorphic work on Self and Smalltalk was somewhat documented, and I
had learned it in the ’90s, in part with a stint on loan from Netscape to Sun
when they were doing due dliigence in preparation for acquiring Anamorphic.
But the opportunity to build on a common engine codebase was lost to path
dependence.

On the upside, different competing open source engines have demonstrably
explored a larger design space than one engine codebase could under
consolidated management.

In any event, the roads not taken in JS’s past still give me pause, because
similar roads lie ahead. But the past is done, and once we had launched
TraceMonkey, and Apple had launched SquirrelFish Extreme, the world had
multiple proofs along with the V8 release that JS was no longer consigned to
be “slow” or “a toy”, as one referee dismissed it in rejecting a PLDI submission
from Andreas in 2006.

You know the rest: JS performance has grown an order of magnitude over the
last several years. Indeed, JS still has upside undreamed of in the Java world
where 1% performance win is remarkable. And, we are still at an early stage in
studying web workloads, in order to synthesize credible benchmarks. O
n top of all this, the web is still evolving rapidly, so there are no stable
workloads as far as I can tell.

Around the time TraceMonkey launched, Mozilla was lucky enough to hire Dave
Mandelin, fresh from PhD work at UCB under Ras Bodik.

The distributed, open source Mozilla JS team delivered the goods in Firefox 4,
and credit goes to all the contributors. I single Dave out here because of
his technical and personal leadership skills.
Dave is even-tempered, super-smart, and a true empirical/skeptical scientist in
the spirit of my hero, Richard Feynman.

So it is with gratitude and more than a bit of relief, after a very long 16
years in full, 13 years open source, that I’m announcing the transfer of
SpiderMonkey’s module ownership to @dmandelin.

Hail to the king, baby!






