
.. index::
   pair: Linux; Password Cracking
   

.. _artduweb_john:

=====================================================================================
Linux Password Cracking: Explain unshadow and john commands ( john the ripper tool ) 
=====================================================================================

.. seealso::

   - http://www.artduweb.com/tutoriels/jtr

.. contents::
   :depth: 3   

john --test
===========

::

    assr38@vercors:/tmp$ john --test
    Benchmarking: Traditional DES [128/128 BS SSE2]... DONE
    Many salts: 2050K c/s real, 2162K c/s virtual
    Only one salt:  1675K c/s real, 1817K c/s virtual

    Benchmarking: BSDI DES (x725) [128/128 BS SSE2]... DONE
    Many salts: 65536 c/s real, 69719 c/s virtual
    Only one salt:  61598 c/s real, 67677 c/s virtual

    Benchmarking: FreeBSD MD5 [32/32]... DONE
    Raw:    5474 c/s real, 6380 c/s virtual

    Benchmarking: OpenBSD Blowfish (x32) [32/32]... DONE
    Raw:    273 c/s real, 392 c/s virtual

    Benchmarking: Kerberos AFS DES [48/64 4K MMX]... DONE
    Short:  141260 c/s real, 315314 c/s virtual
    Long:   531968 c/s real, 858012 c/s virtual

    Benchmarking: LM DES [128/128 BS SSE2]... DONE
    Raw:    6467K c/s real, 10520K c/s virtual

    Benchmarking: generic crypt(3) [?/32]... DONE
    Many salts: 66950 c/s real, 145836 c/s virtual
    Only one salt:  65875 c/s real, 145741 c/s virtual

    Benchmarking: dummy [N/A]... DONE
    Raw:    46127K c/s real, 65709K c/s virtual
