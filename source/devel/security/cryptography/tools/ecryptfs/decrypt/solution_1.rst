

=================================
Recovering Your Mount Passphrase
=================================

In the event that you did not write down your mount passphrase, you may 
be able to recover it by decrypting the file  
/home/username/.ecryptfs/wrapped-passphrase using your **login passphrase**::

    ecryptfs-unwrap-passphrase /home/username/.ecryptfs/wrapped-passphrase
    
Type your login passphrase to reveal the mount passphrase 

If your login passphrase matches the passphrase used to encrypt the 
wrapped-passphrase file, your mount passphrase will be written to screen. 

Record and protect this data accordingly.

If you have lost your wrapped-passphrase file, and you did not record 
your mount passphrase, it is impossible to access your encrypted data. 



