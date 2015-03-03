


.. index::
   pair: i18n ; Transifex
   pair: Localization ; Transifex
   pair: L10N ; Transifex
   ! Transifex


.. _transifex:

==========================================
Transifex
==========================================

.. seealso::

   - http://support.transifex.com/customer/portal/articles/869950-what-is-transifex-


.. contents::
   :depth: 3


What is Transifex ?
====================


Transifex is a novel web application for localization in an easy, agile, and
hassle-free way. It was designed from the ground-up for dynamic, frequently-published
content consolidated from multiple sources, such as software, documentation,
websites, and news publication.

Transifex seamlessly integrates with existing content infrastructure, such as a
software development repository or content management system, using a rich API.

Translation is “crowd-sourced” to a group of human translators using smart and
agile translation techniques adopted from the open source ecosystem.

Before going any further with more details, we’ll take a step back and explain
how Transifex fits in the ecosystem of localization.


Je suis un projet open source. Où puis-je m'inscrire ?
======================================================

Nous nous sommes engagés à appuyer les initiatives Open Source !

Les projets Open Source peuvent s'inscrire au régime libre et profiter de traductions
illimitées.

Si vous êtes un projet open-source et que vous avez besoin d'un compte premium
pour une raison quelconque, prenez contact avec nous.

Localization 101
================

Localization is the second phase of a larger process of product translation and
cultural adaptation (for specific countries, regions, or groups) to account for
differences in distinct markets, a process known as internationalisation and
localization.

Language localisation is not merely a translation activity, because it involves
a comprehensive study of the target culture in order to correctly adapt the
product to local needs. Localisation is sometimes referred to by the numeronym
“L10N” (as in: “L”, followed by ten more letters, and then “N”).

First, a software application is designed in a way so that it can be adapted to
various languages and regions without engineering changes. This is a developer
task, which enables a product to be used with multiple scripts and cultures
(globalization) and separating user interface resources in a localizable format.

The localisation process is most generally related to the cultural adaptation and
translation of software, video games, and websites, and less frequently to any
written translation (which may also involve cultural adaptation processes).

Localisation can be done for regions or countries where people speak different
languages, or where the same language is spoken: for instance, different dialects
of Spanish, with different idioms, are spoken in Spain than are spoken in
Latin America; likewise, word choices and idioms vary among countries where
English is the official language (e.g., in the United States, the United Kingdom,
and the Philippines).​​

Coding practice
===============

The current prevailing practice is for applications to place text in resource
strings which are loaded during program execution as needed.

These strings, stored in resource files, are relatively easy to translate.
Programs are often built to reference resource libraries depending on the selected
locale data. One software library that aids this is gettext.

Thus to get an application to support multiple languages one would design the
application to select the relevant language resource file at runtime.
Resource files are translated to the required languages. This method tends to be
application-specific and, at best, vendor-specific.

The code required to manage date entry verification and many other locale-sensitive
data types also must support differing locale requirements.

Modern development systems and operating systems include sophisticated libraries
for international support of these types.



Transifex tools
==================

.. toctree::
   :maxdepth: 3

   tools/index


