
.. index::
   pair: GnuPG; Signing
   pair: Signature; gpg
   pair: gpg ; sign
   pair: gpg ; detach-sign
   pair: gpg ; clearsign
   pair: gpg ; verify
   pair: gpg ; edit-key
   pair: Digital; Signature
   pair: Verify; Signature
   
      
.. _gnupg_sign:

=================================================================
``gpg`` sign commands
=================================================================


.. seealso::

   - :ref:`signature_de_logiciels`
   - :ref:`signature_numerique`
   - https://fr.wikibooks.org/wiki/GPG#Avec_un_fichier_joint

   
.. contents::
   :depth: 3   


Signing (``gpg`` [--options] ``--sign`` file)
==============================================

You can sign files with the ``--sign`` command. 

``gpg`` will prompt you for the passphrase for your secret key (private key)::

    ``gpg`` --armor --sign my_file.txt

    dir my*
    09/01/2014  09:51               548 my_file.txt
    09/01/2014  09:51               855 my_file.txt.asc
    
    

Note: if you have multiple secret keys that you can use to sign, then you'll 
have to indicate which of those secret keys you want to use to produce a 
signature.  

To designate the secret key, you can either use the --local-user option with 
the --sign command, or you can use the default-key option in your Options file.

In the example above, we used the --armor option to produce ASCII Armored output 
(though we could have dropped the --armor option and produced a binary .``gpg`` file). 

When we open the encrypted, ASCII Armored file, the ciphertext contents look 
just like a file that we encrypted.

::    
    
    type my_file.txt.asc
    

::
    
    -----BEGIN PGP MESSAGE-----
    Version: GnuPG v2.0.17 (MingW32)

    owGbwMvMwMTYNVHg36LaLQsY1zKZJnHnVsanZeak6pVUlASdS5bj5dLTU8jMS0mt
    sLLi5VJQUChIzCyyUnDPKw1wt1ZwzUsuqiwoyczPQ5JzzshMSytKTE/FIe8Y7Ozp
    qWCt4FiUm1+EJJ5ekA4UTYVowRAvSk3OLMhMzcOUScRqTn5pSUEpRDGYgACwd+LT
    80oL0uOTczIN46HWAf3Gy2VLKeDlAoeLgnN+bm5iXoqCT2ZeqoJnXklqUVpicqoC
    SnBQwTKo54A+Ss4HWpJXUgyNI6uU1IKSDCsFY7A8CCJsVtAAhU+0rm4+mFscq6Cr
    Cw0EBVDEa5LmNJDhnYwyLAyMTAxsrEygJMPAxSkAS1PnFnEwLA8QZ/htNu9IbLfQ
    YZGkXV3XncPkH7C8u3q9vtozyuLMXyOpJXNubbfn3PA/cM4bhjn3PqtGRZx2Plqz
    51oNp19ChCuH1i5jfz32iTtm9cz7fFf7StXK7H0s0zO/uAdyFrlxidpdWiXC02iq
    PoEzVbB4ys2aS+Vqb2+dDOzSLNR0czj7ZJf4RcHzge4ZUecaUjb/X/nvw4GO35N2
    8M9VnX3vf+iX1N1CR4r+zltcPFfOP1e4UdX5dsLFpZXSwR8Wmx9Nlp0kqiB/17zb
    N0p+gv8b7+grhYVHwoT+cAWKbGU9/PgM1/vzDRxPfO3eaCzUWanSsV3/a9Ba9i+6
    k3PFVlwNi4w1/9jzVH97hs0vAA==
    =MDJI
    -----END PGP MESSAGE-----
    

In fact, we have encrypted the original file, but we encrypted it with our own 
secret key (as opposed to someone else's public key). 

In fact, signing is sometimes known as "encrypting to the private key." 

The recipient will decrypt the with our public key and verify the signature. 

The problem here, of course, is that we may want to sign the file, but leave 
the contents in plaintext form so that the contents are still readable. 

To do this, we'll **clearsign** the file with the ``--clearsign`` command 
instead of signing it with the --sign command.

(For more information on signing messages and files, see the `GNU Privacy Handbook`_.)


.. _`GNU Privacy Handbook`:  http://www.gnupg.org/gph/en/manual.html



Clearsigning (``gpg`` [ --options] ``--clearsign`` file)
=========================================================

To sign a message or file but leave the actual text or contents unencrypted 
(in plaintext), you can clearsign the file or message with the 
``--clearsign`` command::

    ``gpg`` --clearsign my_file.txt


::

    dir my*
    09/01/2014  09:51               548 my_file.txt
    09/01/2014  10:05             1 097 my_file.txt.asc


::

    type my_file.txt.asc
    
    
::

    
    -----BEGIN PGP SIGNED MESSAGE-----
    Hash: SHA1


    .. index::
       pair: GnuPG; Encryption
       pair: Chiffrage; Encryption
       pair: ASCII ; Armor
       pair: ``gpg`` ; encrypt
       pair: ``gpg`` ; recipient
       pair: ``gpg`` ; armor
       pair: ``gpg`` ; output


    .. _gnupg_cli1_encrypt:

    =================================================================
    GnuPG Command Line Interface  Encryption
    =================================================================


    .. contents::
       :depth: 3


    Encryption (``gpg`` [--options] --encrypt file)
    ============================================

    -----BEGIN PGP SIGNATURE-----
    Version: GnuPG v2.0.17 (MingW32)

    iQEcBAEBAgAGBQJSzmZwAAoJEIqREP6ifbSgFyoH/3VlI5vTBOSKXLZ4opEOfTh0
    gk5OO339YChR46n5mgYCd+uKh0x79tnal5NA5+0SB4vThDYPQz/rrxTkTKsTvNSv
    TmTo06n1xK9zA9Uxa2nq+IETbK3b4QosCdp5AtysdLCZDMQBR+lFS15VLWOPxHLF
    I/UgOfgoKtOCy67D6cikcqr+XUl3FppPduR/klm9UM2jpT2lKoxNCoFgN6Qs6Y5y
    QjlM/5NUDqSbwZ3Z0H4vvE2aXnN1uljfIH9v0jo2JsVjXdv+LXmfTm1eTA63X0/d
    mHGwV2MVylk68khik82RtCaDxSeXV3DIeE1/XWgq46B4rCBMB5ENIBwD1q/kfCM=
    =0Pxs
    -----END PGP SIGNATURE-----
        


When you open the clearsigned output file, you'll see that ``gpg`` has left the 
original contents in **plaintext** and appended a signature for the contents 
at the bottom.


When clearsigning files, it is not necessary to use the ``--armor`` option. 

``gpg`` automatically uses ASCII Armor for the clear signature it appends to the 
bottom of the encrypted contents (ciphertext). 

Of course, it only makes sense to clearsign simple text files. If you clearsign 
binary files, ``gpg`` will produce an ASCII Armored signature, but the original 
contents will still be binary gobbledygook.

(For more information on clearsigning messages and files, see the `GNU Privacy Handbook`_)

.. _`GNU Privacy Handbook`:  http://www.gnupg.org/gph/en/manual.html


Detached Signatures (``gpg`` [ --options] ``--detach-sign`` file)
==================================================================


You can also produce a signature as a **detached signature file**. 

When creating **detached signatures**, ``gpg`` leaves the original file **as is** and 
creates a separate file that contains only the **digital signature**. 

To sign a file and produce a detached signature, use the -``-detach-sign`` command::

    ``gpg`` --detach-sign my_file.txt


::

    dir my*
    09/01/2014  09:51               548 my_file.txt
    09/01/2014  10:15               287 my_file.txt.sig

	

Once you enter your passphrase, ``gpg`` creates a detached signature file 
(:file:`my_file.txt.sig`) that is named similar to the file being signed 
(:file:`my_file.txt`). 

- .SIG files are binary files like .``gpg`` files::

    type my_file.txt.sig
    
::
    
    ë☺∟♦ ☺☻ ♠♣☻R╬h╚
            ►èæ►■ó}┤áï ì«!+E¢ßfzª¢╣ø³W
    ¥ìvTmx8┼Å§├▀╗ÒE╚µ╬├4#‼§♠├ `╠6å╝┬À▄+Å⌂éE.‗╚ï>>♣êvÎ`áém∟ë§h»♠ö°áõ/¢└ÈD╚ó╠←%Õ×RGYg☺]#╠ë▓ÁÇNI■Ccm&ÿ6ÑNb     *£>┌◄/‗ı‗ÒµÃ←░


If you prefer ``gpg`` to produce detached signature files in ASCII Armor format, 
use the ``--armor`` option::


    ``gpg`` --armor --detach-sign my_file.txt


::

    dir my*

    
::
    
    09/01/2014  09:51               548 my_file.txt
    09/01/2014  10:20               499 my_file.txt.asc


As you might expect, you can open the **ASCII Armored detached signature** file 
(which has the ``.asc`` extension) and view the contents::


    type my_file.txt.asc
    

::
    
    -----BEGIN PGP SIGNATURE-----
    Version: GnuPG v2.0.17 (MingW32)

    iQEcBAABAgAGBQJSzmnLAAoJEIqREP6ifbSgQH0H/iPyuH4uTAFLG5nzfNZFzR77
    0VQ4o+AB6i0GVYHT6Ve+io2J2oGako1uTOYsEupmx+jmP1URGr00nOol0LVu2FUH
    vHtdsIEyxYNugKLOn55Z2z2ahAIKXGJi+AtDdW/oBQzBvZxCu+dgphyj4yfxcXM8
    DYcObLyVz/StzS37TIzXimIZMLtsG+e6Pk/+B9ZEkxckJaMS9KcHRiJRaNlb8TdZ
    G+bE4d1jwBvfmSVlgQjW0I90a/gz8pMk79HACk5aAXZH+ZdrV7LnwaF0x+/N5QZD
    wbS3EzEFCP3STvdhOzL4g1E9kFZcVpj+LkQe1/j6pbnjkHbEGW1mCrgn3yy7LmY=
    =eYwV
    -----END PGP SIGNATURE-----


Verifying Detached Signatures (``gpg`` [ --options] ``--verify`` sigfile signed_files)
=======================================================================================


To verify files with detached signatures, use the ``--verify`` command and specify 
the detached signature file as well as the files that were signed::

    ``gpg`` --verify my_file.txt.sig my_file.txt

::

    ``gpg``: Signature faite le 01/09/14 10:15:52 Paris, Madrid avec la clé RSA ID A27DB4A0
    ``gpg``: Bonne signature de  pvergain (``gpg``) <pvergain@gmail.com> 
    ``gpg``:                 alias  Patrick (Adresse professionnelle) <patrick.vergain@id3.eu> 



