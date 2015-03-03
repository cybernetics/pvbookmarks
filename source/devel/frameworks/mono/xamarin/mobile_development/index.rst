
.. index::
   pair: Xamarin ; Mobile development
   pair: UX ; User Experience


.. _xamarin_mobile_development:

============================
Xamarin Mobile development
============================

.. seealso::

   - :ref:`xamarin_mobile_development_ref`:
   - http://docs.xamarin.com/guides/cross-platform/getting_started/introduction_to_mobile_development/


.. contents::
   :depth: 3


.. _xamarin_sdlc:

Xamarin Mobile Development SDLC ( systems development life cycle)
=================================================================

.. seealso::

   - http://en.wikipedia.org/wiki/Systems_development_life-cycle


The lifecycle of mobile development is largely no different than the SDLC for 
web or desktop applications. 

As with those, there are usually 5 major portions of the process:

- Inception – All apps start with an idea. That idea is usually refined into a 
  solid basis for an application.
- Design – The design phase consists of defining the app’s User Experience (UX) 
  such as what the general layout is, how it works, etc., as well as turning 
  that UX into a proper User Interface (UI) design, usually with the help of a 
  graphic designer.
- Development – Usually the most resource intensive phase, this is the actual 
  building of the application.
- Stabilization – When development is far enough along, QA usually begins to 
  test the application and bugs are fixed. Often times an application will go 
  into a limited beta phase in which a wider user audience is given a chance 
  to use it and provide feedback and inform changes.
- Deployment

Often many of these pieces are overlapped, for example, it’s common for development 
to be going on while the UI is being finalized, and it may even inform the 
UI design. 

Additionally, an application may be going into a stabilization phase at the 
same that new features are being added to a new version.

Furthermore, these phases can be used in any number of SDLC methodologies such 
as Agile, Spiral, Waterfall, etc.

Let’s cover how each of these phases play a part in Mobile Development.


.. _xamarin_inception:

Xamarin Inception
=================

The ubiquity and level of interaction people have with mobile devices means 
that nearly everyone has an idea for a mobile app. 

Mobile devices open up a whole new way to interact with computing, the web, 
and even corporate infrastructure.

**The inception stage is all about defining and refining the idea for an app**. 

In order to create a successful app, it’s important to ask some fundamental 
questions. 

For example, if you’re developing an app for distribution in a public app store, 
some considerations are:


Competitive Advantage 

   Are there similar apps out there already? If so, how does this application 
   differentiate from others?

If you’re intending for the app to be distributed in the enterprise


Infrastructure Integration 

   What existing infrastructure will it integrate with or extend?

Additionally, you should evaluate the usage of the app in a mobile form factor:

- Value – What value does this app bring users? How will they use it ?
- Form/Mobility – How will this app work in a mobile form factor ? 
  How can I add value using mobile technologies such as location awareness, 
  the camera, etc. ?

To help with designing the functionality of an app, it can be useful to define 
Actors and Use Cases. 

Actors are roles within an application and are often users. 

Use cases are typically actions or intents.

For instance, if you’re building a task tracking application, you might have 
two Actors: User and Friend. A User might Create a Task, and Share a Task with 
a Friend. In this case, creating a task and sharing a task are two distinct 
use cases that, in tandem with the Actors, will inform what screens you’ll 
need to build, as well as what business entities and logic will need to be 
developed.

If you’ve captured the appropriate use cases and actors, it’s much easier to 
begin designing an application because you know exactly what you need to design, 
so the question becomes, how to design it, rather than what to design.


.. _xamarin_ux_design:

Xamarin UX (User Experience) Design
===================================

``UX`` is usually done via wireframes or mockups using tools such as Balsamiq_, 
Mockingbird_, Visio, or just plain ol’ pen and paper. 

UX Mockups allow you to quickly design UX without having to worry about the 
actual UI design:


.. _Balsamiq:  http://www.balsamiq.com/
.. _Mockingbird:  https://gomockingbird.com/


When creating UX Mockups, it’s important to consider the Interface Guidelines 
for the various platforms that you’re designing for. 

By adhering to platform-specific guidelines, you can ensure that your apps feel 
at home on each platform. You can find each guide as follows:

- Apple - `Human Interface Guidelines`_
- Android – `Design Guidelines`_
- Windows Phone 7 – `UX Design Guidelines for WP7`_


.. _`Human Interface Guidelines`:  http://developer.apple.com/library/ios/#DOCUMENTATION/UserExperience/Conceptual/MobileHIG/Introduction/Introduction.html
.. _`Design Guidelines`:   http://developer.android.com/design/index.html
.. _`UX Design Guidelines for WP7`:   http://msdn.microsoft.com/en-us/library/windowsphone/develop/hh202915(v=vs.92).aspx


For example, each app has a metaphor for switching between sections in an 
application. iOS uses a tabbar at the bottom of the screen, Android uses a 
tabbar at the top of the screen, and Windows Phone 7 uses the Panorama view:


.. _xamarin_ui_design:

Xamarin User Interface (UI) Design
==================================

Once you’ve nailed down the UX in your application, the next step is to create 
the UI design. While UX is typically just black and white mockups, 
the UI Design phase is where colors, graphics, etc., are introduced and finalized. 

**Spending time on good UI design is important and generally, the most popular 
apps have a professional design**.

As with UX, it’s important to understand that each platform has it’s own design 
language, so a well-designed application may still look different on each platform.


For good UI design inspiration, check out some of the following sites:

- pttrns.com_ – (iOS only)
- androidpttrns.com_ - (Android only)
- lovelyui.com_ – (iOS, Android, and Windows Phone)
- mobiledesignpatterngallery.com_ – (iOS, Android, and Windows Phone)


.. _androidpttrns.com:  http://androidpttrns.com/
.. _pttrns.com:  http://pttrns.com/
.. _lovelyui.com:  http://lovelyui.com/
.. _mobiledesignpatterngallery.com:   http://mobiledesignpatterngallery.com/


Additionally, you can find graphic designer portfolios at sites such as 
Behance.com and Dribbble.com. 

Designers from all over the world can be found there, often times in places 
where the exchange rate is favorable, so good graphic design doesn’t necessarily 
have to cost a lot.





