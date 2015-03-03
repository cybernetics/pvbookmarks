

.. index::
   ! OpenERP


.. _openERP:

=====================================================================
OpenERP an open source integrated enterprise resource planning (ERP)
=====================================================================

.. seealso::

   - http://en.wikipedia.org/wiki/OpenERP
   - http://fr.wikipedia.org/wiki/GPAO


.. figure:: OpenERP_Official_Logo.jpg
   :align: center

.. contents::
   :depth: 3

Introduction
=============


OpenERP (previously known as TinyERP) is an open source integrated enterprise
resource planning (ERP) software manufactured by OpenERP s.a.

OpenERP was founded in 2005 by CEO Fabien Pinckaers and consists of a unique
ecosystem combining the resources of its community, partner network and editor.

The community (2000 active members as of 2012) contributes every day to the
enrichment of OpenERP.

The network of partners, established in more than 80 countries, deploys the
solution locally.

OpenERP s.a. has 5 offices worldwide (2 in Belgium, one in California, one in
Luxembourg and one in India), with its headquarters in Belgium.


Architecture
============


Client-server architecture
---------------------------

OpenERP has separate client and server components.
The server runs separately from the client. It handles the business logic and
communicates with the database application.

The client presents information to users and allow them to inter-operate with
the server.
Multiple client applications are available.

Server and modules
++++++++++++++++++

The server part is written in Python programming language.
The client communicates with the server using XML-RPC interfaces.

Business functionality is organised into modules.

A module is a folder with a  pre-defined structure containing Python code and
XML files.

A module defines data structure, forms, reports, menus, procedures, workflows,
etc... Modules are defined using a client-independent syntax.
So, adding new objects, such as menus or forms, makes it available to any client.

Client applications
+++++++++++++++++++

The clients are thin clients as they contain no business logic.

Two client applications are officially supported:

- A web application, which is deployed as an HTTP server to allow users to
  connect using their Web browser.
- A desktop application, written in Python and using the GTK+ toolkit.

Other alternative clients have also been developed by the community:

- Koo at https://launchpad.net/openobject-client-kde

Database
========

OpenERP uses PostgreSQL as database management system.

Reporting
=========

OpenERP also provides a reporting system with OpenOffice.org integration allowing
customization of reports.

Alternative report engines are available using Webkit, or Jaspersoft.

Source code and contributions
=============================

The source code of OpenERP is hosted on Launchpad, using the Bazaar revision
control system, and the contributions are also handled using Launchpad.

The documentations are also managed using this service but a website dedicated
to all publications has been set up in 2009.

License and impacts on business model
=====================================

Most parts of OpenERP are released under the AGPL license version 3 or later
(previously the GPL) and some parts use a derivative of the Mozilla Public
License.

As a direct consequence OpenERP can be used without payment of license fees and
can be modified to suit the users requirements. This also implies that, as long
as the terms of the licences are respected, the software may also be distributed
by third parties in its original form as well as in a modified form free of costs
or for a fee.

The original manufacturer of OpenERP as well as other businesses generate revenue
by providing customers with support and customization services, which are also
major costs applying to ERP software requiring a license fee for its usage.

Software as a service
=====================

Businesses may offer OpenERP using the Software as a service model, which
OpenERP s.a. itself does since version 6.

The AGPL requires third party vendors to release all modifications they made to
parts of OpenERP covered by the license in the version they provide to customers
under the same license.

OpenERP Apps
============

OpenERP s.a. provides a web site referencing the officially supported modules
as well as contribution modules.

The principle is similar to Apple's App Store. Contribution modules can be
referenced for free as long as they respect some submission rules.

As of November 2012, the number of OpenERP apps reached more than 2500.

Development environment
========================

Module development mainly relies around edition of Python and XML files.

There is no official editor, but community tutorials tend to go towards
Eclipse/PyDev based development.

Some application logic (i.e. workflows and data structure) can be changed through
the client interface.

Fork
====

Tryton is a fork of OpenERP which began development in November 2008.


Other softwares
===============

- `List of free and open source software packages concerning finance`_
- `Comparison of Tryton and Open ERP`_




.. _`List of free and open source software packages concerning finance`: http://en.wikipedia.org/wiki/List_of_free_and_open_source_software_packages#Finance

.. _`Comparison of Tryton and Open ERP`: http://en.wikipedia.org/wiki/Comparison_of_Tryton_and_Open_ERP


