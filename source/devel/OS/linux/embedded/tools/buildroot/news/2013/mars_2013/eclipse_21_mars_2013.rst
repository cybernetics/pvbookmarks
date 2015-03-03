
.. index::
   pair: Buildroot; Eclipse
   pair: Mélanie ; Bats


.. _buildroot_news_21_mars_2013:

=================================================================================
Release 2.0.0 of the Buildroot/Eclipse integration (Thu Mar 21 22:53:15 UTC 2013)
=================================================================================


.. seealso::

   - https://github.com/mbats/eclipse-buildroot-bundle/wiki
   - http://www.eclipsecon.org/2013/sessions/buildroot-eclipse-bundle-powerful-ide-embedded-linux-developers
   - :ref:`eclipse_con_2013`
   - https://www.eclipsecon.org/2013/users/901 (Mélanie Bats)


.. figure:: melanie_bats.jpg
   :align: center

Hello,

We are proud to announce the second release of the Buildroot/Eclipse
integration.

Compared to the previous 1.0.0 release, this 2.0.0 release brings the
following new features:

* Integration with the Autotools Eclipse plugin. Buildroot toolchains
  are now selectable for Autotools projects, which allows you to
  autoreconf and configure your Autotools-based project directly
  within Eclipse.

  .. seealso:: https://github.com/mbats/eclipse-buildroot-bundle/wiki/Tutorial-:-How-to-create-a-new-Autotools-C-project-using-the-Buildroot-toolchain-%3F

* Integration with the Make Eclipse infrastructure.
  Buildroot toolchains are now selectable for Makefile-based projects, where the
  Makefile is written by the developer.

  .. seealso:: https://github.com/mbats/eclipse-buildroot-bundle/wiki/Tutorial-:-How-to-create-a-new-Makefile-C-project-using-the-Buildroot-toolchain-%3F

Until now, only "Managed Build" projects were supported, where Eclipse
is responsible for building the project, which means that it is not
possible to build the project outside of Eclipse.

**We believe that the integration with the Autotools and Make based projects makes
the Eclipse/Buildroot integration much more useful**.

The update site has not changed, so users will automatically receive
this new version when they update the packages in their Eclipse.

There is one known issue in this release:

* The pkg-config integration is not perfect, and it is for now needed
  to Close and Re-open a project to get pkg-config settings changes
  taken into account properly.

  ..seealso:: https://github.com/mbats/eclipse-buildroot-bundle/issues/12

We have also fixed a number of minor issues in our tutorials, following
the feedback of several users.

For more informations about this Eclipse/Buildroot integration, please
visit the project's web page at
https://github.com/mbats/eclipse-buildroot-bundle/wiki.

This work will be presented next week at EclipseCon US in Boston, see
http://www.eclipsecon.org/2013/sessions/buildroot-eclipse-bundle-powerful-ide-embedded-linux-developers.

We are again very interested in receiving feedback from users.

All the Eclipse development and integration work has been done by
Mélanie Bats <melanie.bats at obeo.fr>.

Best regards,

Mélanie and Thomas
