

.. index::
   pair: Time ; iCal
   ! iCalendar


.. _icalendar:

==================
icalendar
==================

.. seealso::

   - http://fr.wikipedia.org/wiki/ICalendar


.. contents::
   :depth: 3


Introduction
============

iCalendar est un standard (RFC 5545) pour les échanges de données de calendrier.

Ce standard est aussi connu sous le nom d'iCal.

Il définit la structuration des données dans un fichier de type événement de
calendrier, ce n'est donc pas un protocole.

Les partages de calendrier par abonnement sont en réalité des échanges de
fichiers au format iCalendar à travers un protocole CalDAV ou Web Calendar
Access Protocol — le premier échangeant des calendriers en tant qu'agrégats
d'événements, le second en tant qu'élément global à part entière.


Il est implémenté/supporté par un grand nombre de logiciels, tels que : iCal
d'Apple, Chandler, Lotus Notes, Zimbra, ScheduleWorld, SOGo, KOrganizer,
Mozilla Lightning (y compris Mozilla Sunbird), Mulberry, Evolution, Windows Calendar
et, via une extension, Microsoft Outlook (voir ci-dessous).
L'application en ligne Google Agenda utilise également cette norme.

Les widgets utilisés dans les portails personnalisables tels que Netvibes,
IGoogle ou Posh peuvent également supporter ce format.


Python icalendar library
========================

.. seealso::

   - http://icalendar.readthedocs.org/en/latest


Python pyICSParser library
==========================

.. seealso::

   - http://pypi.python.org/pypi/pyICSParser


pyICSParser parses icalendar files (.ics or ical files) as defined by RFC5545
(previously RFC2445)and returns json structure with explicit dates.






