

.. index::
   video (popcorn.js)
   video (HTML5)
   

.. _hypervideo_popcorn:

==========================
Hyper-video popcornjs tool
==========================


.. seealso::
 
   - http://popcornjs.org/
   - https://mozillafestival.org/2011/11/05/popcorn-1-0-launches-at-mozilla-festival-with-exclusive-world-premiere/



Video+html5+Popcorn.js=hyper-video
===================================

.. seealso::
 
   - http://standblog.org/blog/post/2010/08/20/Videohtml5Popcorn.jshyper-video


By Tristan on Friday 20 August 2010, 16:08 

- drumbeat
- html5
- popcorn.js
- video

You may have seen that `Brett Gaylor is joining Mozilla`_ (see also Mark Surman's 
post). For those who don't know Brett, he's particularly famous for his "Open 
Source documentary" `Rip! A remix Manifesto`_ [1].

One may ask why Mozilla has hired a film director[2], but it actually makes a 
lot of sense thanks to Mozilla Drumbeat, as Brett is working on a Drumbeat 
project called Web made movies.

Now Brett has been a Mozilla community member for quite some time, contributing 
with the good folks at CDOT / Seneca College to create popcorn.js, "a JavaScript 
library for merging video with semantic data". 

I understand that this is a bit of a mouthful, but don't close your browser 
window just yet! Popcorn.js is what I would describe as "hyper-video" ("hyper" 
as in "hypertext"): the ability to leverage data from the video and link to it, 
Web style. Such data include:

- location. Where on earth was this video sequence made? Then display it on an 
  interactive map
- subtitles. What is being said on the soundtrack. Display it as text, and offer 
  to translate it into the foreign language of your choice using an online 
  translation service
- license. Under which license is this video sequence made available? 
  (Copyright, Creative Commons, etc.)
- person. Who's on the screen? If we know, then link to his/her Twitter and 
  Flickr streams in real time
- topic. What is being discussed? Then link to the corresponding article in 
  Wikipedia and in the news.


Go and see for yourself the `PopCorn.js demo`_ (in case you're stuck with an older 
browser that is not capable of running the demo, `here is a video of the demo`_).

I think this is a very significant step further for video on the Web, which was 
until now a very TV-like, passive and linear approach, now merged with the 
hypertext nature of the Web (its ability to link to things in other places), so 
that users can click on links in order to learn more. Of course, this is just a 
demo. 

Tons of things need to be done, but I see this as a very cool way to show what 
HTML5 and its video element, combined with the power of JavaScript and mash-ups.


.. _`Brett Gaylor is joining Mozilla`: http://brettgaylor.tumblr.com/post/974861748/where-ive-been-where-im-going
.. _`Rip! A remix Manifesto`: http://en.wikipedia.org/wiki/RiP!:_A_Remix_Manifesto
.. _`PopCorn.js demo`: http://webmademovies.etherworks.ca/popcorndemo/
.. _`here is a video of the demo`: http://www.drumbeat.org/content/popcorn-js-semantic-video-demo

Notes
-----

- [1] I can't say how strongly I recommend watching this movie, starting with 
  its trailer.
- [2] It's actually the second one, as Henrik Moltke, co-author of Good copy, 
  bad copy, is already working at Mozilla... on Drumbeat!


Arte adopts Mozilla’s popcorn.js
================================

.. seealso::
 
   - http://webmademovies.org/arte-adopts-mozillas-popcorn-js

::

    “If you want to change the world, you should ship some software”

This little pearl of wisdom was delivered to me by my fellow Mozillian Chris 
Blizzard while I was interviewing him for a video. 

The recent adoption of our popcorn.js library by Arte, one of Europe’s most 
respected broadcasters, is making me agree.

Popcorn.js is a project of Web Made Movies, Mozilla’s open video lab. It came 
out of a frustration with the way filmmakers and media publishers were hosting 
their videos on the web. 

In most cases, we were seeing “TV in a webpage”, a block of proprietary code 
that was built on technologies that sidestepped the web’s “view source” ethic 
and didn’t actually interact with the rest of the page. While sites like YouTube 
have seen a fantastic surge of users and content over the last several years, 
the video itself has been a “black box” that the rest of the web page couldn’t 
understand. As a result, video and the rest of the web have never truly merged.

Enter HTML5 and the video tag, and suddenly we can apply web technologies like 
CSS and Javascript to videos. 

And with popcorn.js, we can share data ABOUT the video with web services like 
twitter, flickr and wikipedia, allowing us to create mashups of web services and 
moving images.

When Arte began noticing popcorn.js, they wondered if this work could be a good 
fit for some of their programming. They turned to the seasoned developers at 
Upian, who were able to pull our open source code from Github, and today we’re 
immensely proud to announce that the web versions of Notre Poison Quotidien have 
been augmented and remixed using popcorn.js.

As you can see on the beautiful pages they have put together, this content is 
an ideal use case for popcorn.js. Producers are often at a loss for how to 
deliver the reams of associated material that surround their content – well, t
hanks to the open technologies that make the web, now we can do that!

My colleague David Humphrey, whose students at Seneca College’s Center for 
Development of Open Technology are in fact among the core authors of the 
technology, expressed to me how happy he is to see the technology being adopted 
“in the wild”. “This is how we’ll make popcorn even better. Let’s see how people 
use it and learn from that”, he remarked in a recent discussion online. 

In collaboration with great partners like Arte, our growing community at Web 
Made Movies is changing the world of web video, a little bit of software at a 
time.

Posted on February 27, 2011 by brett 


http://butterapp.org/
=====================

The Popcorn.js Authoring Tool.

Please consider this source release to be an early development preview. 
This software is not stable, nor does it claim to be stable and is not 
recommended for production use. 

All aspects of this software are subject to be changed without notice or regard 
for previous revision compatibility.

This code has NOT been fully optimized and should not be treated as though it has.

Event emitters within the application are subject to change.
