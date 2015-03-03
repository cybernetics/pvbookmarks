
.. index::
   pair: Batou ; Deployment
   pair: Batou ; Redmine

.. _batou:

============================
Batou
============================


.. seealso::

   - http://batou.readthedocs.org/en/latest/


.. contents::
   :depth: 3

Introduction
============

multi-(component | host | environment | platform) deployment

batou is a tool that makes it easy to define automated service deployments for
complex (web) applications.

It is developed at gocept and made available under the BSD license.



Redmine
=======

.. seealso:: https://projects.gocept.com/projects/batou


Bitbucket
=========

.. seealso::  https://bitbucket.org/gocept/batou

History
=======

Looking back we see that there's a long history of automating deployments:

* FTPing PHP scripts from a developer machine to a server (1999)
* Running shell scripts to automate Zope instance configuration (2001)
* Using Zope's built-in instance configuration mechanism and more shell scripts (2003)
* Using zc.buildout to automate Python environment configuration (2006)
* Using Fabric to automate zc.buildout deployment (2010)

Around 2008 we started making operations a major part of our business. In 2010
we got a big customer for whom we needed all the setup that is shown in the
diagrams above and started thinking harder about automating this deployment.

On the system configuration level we were already using puppet â€“ however, as
argued before, system configuration and service deployment are two different
beasts: with puppet we manage many machines that are similar (system
configuration) whereas the service deployment wants to individualize some of
those machines for a specific service.

Comparison with other tools
============================

**Puppet** is a system configuration tool and thus is designed around
assumptions that are detrimental to the goals of service deployment: no
orchestration, pull principle, root access. Also: check out Puppet Labs' `Fully
automated provisioning
<http://www.puppetlabs.com/wp-content/uploads/2010/03/FullyAutomatedProvisioning_Whitepaper7.pdf>`_
whitepaper which explicitly points to tools like Fabric, Capistrano,
ControlTier and others.

**Fabric + zc.buildout** was our basis when we started automating complex
setups. We used it to check out a Mercurial repository that contains a
buildout definition, run buildout on it, and do some additional shell stuff
around it. Give that to a list of hosts and you're good. We encountered two
substantial problems with this approach, though: we ended up with a single
large buildout and pretty complex Fabric code, both of which became
unmaintainable after a while. However, in general we did have a "single
command" deployment that worked very well â€“ most of the time.

What we were missing was the declarative modelling that we enjoyed with Puppet
on the system configuration level. Also, we wanted to be able to do more
fine-grained deployment and not be limited to a "per host" command execution
order.

**Salt** seems to try solving the same problem as Fabric and MCollective: a
scalable approach to Remote Command Execution. We have not looked deeply at
Salt and it might be an interesting alternative to SSH. However, it does
require additional runtime components in the target environment which are not
as widely available as SSH.


Architecture
------------

Batou consists of:

* a model to describe services in terms of "components" and "environments"
* a utility to realize a specific configuration locally (``batou-local``)
* a utility to deploy a whole environment remotely (``batou-remote``)
* a library of re-usable components

Components are Python objects with an API to construct a component hierarchy
(making the model recursive) as well as to perform actions on the target system in
a manner that makes it easy to achieve convergency and idempotency.

Environments represent different installations of a service: staging,
production, development, etc. For each environment you specify which hosts belong
to it, how the services shall be distributed to those hosts, and possibly some
customization of how components are configured in that environment.

The ``batou-local`` utility executes a given configuration (for a given host
and environment) locally.

The ``batou-remote`` utility executes a given configuration for a complete
environment by connecting to all hosts by SSH and running ``batou-local`` on
each host in a specific batch mode. It is able to coordinate the running order
of configuration tasks between different hosts as required by the model.

Features
--------

We have already achieved most of our initial goals with batou:

* Perform initial installation and continuous updates by a "single command"
* Local and remote deployments
* Version-control the configuration as a whole
* Support different platforms
* Handle different environments (dev, staging, production)
* Express relationships between components
* Declarative component and environment model
* Re-usable deployment code
* Managed secrets (SSL certificates, database passwords, etc)

One exception remains currently unsolved:

* Automatically perform parallel rolling deployments

Requirements
------------

batou has been tested and is known to run on Linux and Mac OS X.

We do not support deploying to non-UNIX targets. We *may* support running
:program:`batou-remote` on non-UNIX platforms in the future.

The batou software works with Python 2.7 but it can be used to deploy
components that may or may not use any version of Python (or any other
programming language, framework or general software package).

We also currently require using:

* Python 2.7
* Mercurial for version control
* SSH for performing remote tasks
* buildout and virtualenv for bootstrapping the Python environment for batou itself

These requirements are not set in stone for the future but open for change.

Remote machines must have available:

* Python 2.7
* virtualenv
* Mercurial


Values and guiding principles
-----------------------------

Single-command deployment
    A deployment should *always* only consist of running a single, simple command.

Repeatability, reliability
    If a deployment worked yesterday then it should also work today. And it
    should result in the same setup.

Expressiveness, readability
    Make service definitions readable: avoid having large blocks of mechanical code that does not communicate its intention.

Reusability
    When finding a good way to solve a specific deployment problem (like
    managing files, services, secrets, ...) we want to make the solution
    re-usable so that we can benefit from it whenever we meet the same problem
    again.

    An important point to reusability is to make re-use simple enough that you
    do not have to prefer short-cuts over doing it right.

Resistance to entropy, automatic repairs
    The target machine will likely accumulate entropy over time. Do not expect
    a perfect environment but make reasonable adjustments to achieve the
    deployment goal.

Platform-independence
    A service description should use a very broad model where the mechanics of
    the model do not depend on the specifics of any single platform: be it
    Unix, Windows or anything else.

    In our case the component model is completely agnostic to any platform.
    Only specific component implementations become tied to a platform, e.g. the
    Symlink component being specific to POSIX platforms.

    Also, make it possible to make platform-specific parts of the model
    explicit. Allow specifying multiple platform targets for a single service.

    We do rely on Python being available, though.

Simplicity
    Complex service deployments are bad enough as they are – we do not want to
    make them any more complicated. We especially do not want to break
    expectations about existing components; people who are experienced
    with them ought to be able to predict their behaviour.

Domain-agnostic
    Batou should not make any assumption about your service: we do mostly
    deploy web application stacks but honestly, the abstract model doesn't have
    to and should not know about that. The same is true of any other aspect
    of your service: it should be possible to deploy any software that you, as an
    administrator, can install on a system.

No additional components
    No additional active components in your service environment are required at
    runtime or needed in your application. See also: "Domain-agnostic".

Automatic dependencies
    Dependencies between separate components shall be determined automatically.

Continuity
    The same service model and tools should be useable for initial and
    incremental deployments.

Minimal downtimes
    Avoid unnecessarily taking components down. Ideally we can run deployments "in-flight".

    Also, deployments should be fast. They should be especially fast if
    nothing needs to be changed.
