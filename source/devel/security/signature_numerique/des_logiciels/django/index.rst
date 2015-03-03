
.. index::
   pair: Signature Electronique ; Django


.. _signature_electronique_django:

================================================
Signature électronique du logiciel Django
================================================

.. seealso::

   - https://docs.djangoproject.com/en/dev/internals/howto-release-django/
   - https://www.djangoproject.com/m/pgp/django-releasers.txt
   - http://blog.mathieui.net/introducing-django-gpg-fr.html
   - :ref:`gnupg_sign`



django-releasers.txt
=====================

::

    -----BEGIN PGP SIGNED MESSAGE-----
    Hash: SHA256

    This file contains a list of everyone who is authorized to release Django.
    When we issue an official release of Django, it'll come with a checksum file
    for the release. That file will be signed by one of the authorized users
    listed below, and will contain instructions on how to verify that the release
    hasn't been tampered with.

    This releasers document is itself signed by a master key with key ID
    ``1767F12E10DEFBF3``. You can verify the authenticity of this list by fetching
    this key from the MIT keyserver and verifying this file. For example, to verify
    this list using GPG:

        gpg --keyserver pgp.mit.edu --recv-key 1767F12E10DEFBF3
        gpg --verify django-releasers.txt

    Once you have verified this list, you can compare the keys used for the release
    with the list of keys below.

    If a release is ever issued with a checksum that does not verify, or if those
    checksums are signed by someone not on this list, the release is fradulent
    and should be considered dangerous.

    Those people who have been authorized to issue a release of Django are:

        Key ID              Name
        ------------------  -----------------------------------------------
        3684C0C08C8B2AE1    James Bennett <james@b-list.org>
        69666DFEB00E963E    Jacob Kaplan-Moss <jacob@jacobian.org>

    -----BEGIN PGP SIGNATURE-----
    Version: GnuPG v1.4.11 (Darwin)

    iQIcBAEBCAAGBQJRVG2fAAoJEBdn8S4Q3vvzK58QAK2iwcYyvjGoNoGd4Ny79WEY
    9Q6IEYWbQGNf1iJEfUFp1EZRDOmr0rAlHEpqsQIZ5dAFVMMr5IS4DzHMpLO5sjFk
    GTieOtlU3aoHYOT0+ePcgz2oSNvRl/8ezMgMU52b1aWvVl+IWq84e6HCAcZYTuKE
    PxSdl4/kTwK6ZCKKbd4HQR6L19btW5+Gr2ZmJYcpouRjKcqTsK2boXgFJHOrEZta
    iDL4jmqSe4955QILgQYcmAsKhcU17u0k9iR9a11qOoQOX4/TRl9UlsJyDQY1mR2O
    P3ndi+T94c3u2gGwfizUqY2AJBeTRBsWU+eSSrolsZUIR6NFLHMmPfmBc5oE2nVc
    JapT+VEPO0w3ttwlVTYkEg4pEd7ZsH1JtpytZmjEqxcMJjASF75181VzAaxw8Gwh
    pIyNPKFLNobfH3pqeGoELDdZho+FRI1RRAgibOuXSu2xTlDhI6NFuXdJ/GAZRcB9
    jVH1vYMz9HnDLeupy18AaIdnt9mWNi0OL+cOYB92w9OlvS4ZYVynqbWzhXT2D/NG
    vSBncBRv4zSjoBnoYr4JXm3+qK41gk0ZqhEWiRn6IKPEHxDotZxWRPyzxrKnG46D
    gPnrkMzpqW+9xzHmSWLdms3UD6X3D41A2ddAqUx/ouX9iNkSW5VeltLk6onhH5ip
    mJbbaSfibMQViyggNO/2
    =D/4N
    -----END PGP SIGNATURE----
