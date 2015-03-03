
.. index::
   0MQ use cases

===================
ØMQ? use cases
===================


ØMQ? use case 1
===============


Hi all,

I recently encountered 0MQ and am very intrigued by its capabilities.
I have what I think is an unusual use-case and am hoping someone might have
suggestions on how 0MQ could be part of a solution, or where I might run into
trouble. (Who knows, maybe it will be a useful use case to think about for
development purposes too?)

I have a number of hardware devices (up to perhaps 300) that sample and spit out
data. Such data will come in on many different channels (e.g., TCP, UDP,
bluetooth, WiFi, 802.11.4 radio, USB, A/V, maybe even RS232).

Maximally simplified, I need to (1) capture this data, (2) distribute the data
to subscribed clients as rapidly as possible, and (3) allow clients to send
command messages back to individual devices.
At any given time, there may be up to 50 or so clients, ranging from being
link-local (which should have essentially real-time performance) to being on the
other side of the planet (where some delays are expected). The capture step will
be handled in python, perhaps using a Twisted Python reactor setup.

The requirements/restrictions are as follows:

1) Robustness in the face of link failure or slow links (i.e., delay-tolerant
   networking, tear-away networking)
2) Quality of service capabilities (or at least an ability to easily prioritize,
   and re-prioritize, queued messages for sending)
3) Devices and clients may blink in and out of existence, as hardware is turned
   on/off; this shouldn't affect the system at all
4) A few "key" clients--at least one per tear-away subnet--will require reliable
   receipt of device data. Such data will be stored in a local database.
   These clients are expected to remain up in the three-9s sense, but should
   also be easy to duplicate/replace. Loss of such a key client should not
   prevent the system from continuing to function.
5) Key clients will need reliable comm with other key clients, store-and-forward
   style, for database sync/aggregation
6) Minimal (zero?) maintenance is important (i.e., auto-discovery of client
   type--key vs. non-key; zero-config service discovery on devices,
   self-monitoring daemons, etc) are strongly preferred as this will be deployed
   in a setting with minimal IT-resources.
7) Variable data rates and payload sizes (ranging from a single integer each hour
   to 1080p video)

#3 suggests a pub/sub design, while #4-5 suggest store-and-forward. #3 plus #6
   make store-and-forward more difficult, if clients will appear/disappear and
   also need to be discovered and configured with minimal IT intervention.

I don't think 0MQ (or, in fact, anything) can do all of this, but maybe it can
do a lot. I've considered lower level comm (e.g., pub/sub via multicast), but
that requires too much wheel-reinvention. I've also considered RabbitMQ, but
that appears less friendly on config and expects links will be more up/stable
than I am promised.

I briefly looked at bigger DDS options (openDDS, OpenSplice, RTI) but they
seemed a combination of complete overkill in some areas and insufficient in
others. Any suggestions on how to best utilize 0MQ in such a setting (with or
without other packages)? Any (even random) thoughts are welcome. :-)

-best

Gary


.. index::
   openPGM


Response from Steven McCoy
--------------------------


::

    de  Steven McCoy steven.mccoy@miru.hk
    heure de l'expéditeur   Envoyé à 05:12 (GMT-04:00). Heure locale : 03:34. ✆
    répondre à  ZeroMQ development list <zeromq-dev@lists.zeromq.org>
    à   ZeroMQ development list <zeromq-dev@lists.zeromq.org>
    date    21 juin 2011 05:12
    objet   Re: [zeromq-dev] Use case suggestions?



Note that The Guide™ has most of this covered already, certainly queuing and
queue functionality is above the remit of basic ØMQ socket implementation.
This is also all certainly possible with products like IBM WebSphere MQ,
TIBCO Rendezvous, etc, but there are obviously downsides with each product to
be considered, from expense to complexity.
It is definitely a good idea to head towards a common middleware system that is
flexible enough to be adapted to each situation.

There are a few things not listed, such as disconnected proxies, high data-loss
aware transports, multi-pathing, and possibly congestion control, rate limiting
not explicitly mentioned but implied that certainly limit your choices a bit.
Note that you can integrate solutions like both ØMQ and RabbitMQ which may make
disconnected operation significantly easier: https://github.com/rabbitmq/rmq-0mq


Also, ØMQ  is already integrated with OpenPGM_ so you get a great TCP and
multicast interchangeable pub/sub system for scaling to a significant number of
recipients with options to target a variety of different deployments.

The only real question that springs to mind is in regard to performance
requirements and pricing limitations, it is clear some queuing and synchronous
storage looks required but it's not obvious how far you wish to push beyond a
basic queue system like SMTP or UUCP.

--
Steve-o


.. _OpenPGM: http://code.google.com/p/openpgm/

