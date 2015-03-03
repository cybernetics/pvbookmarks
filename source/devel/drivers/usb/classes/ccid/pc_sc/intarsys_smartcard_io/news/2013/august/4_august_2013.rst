

.. _smartcard_io_4_august_2013:

===========================================
Intarsys smartcard.io August 4th 2013
===========================================


::

    MUSCLE <muscle@lists.musclecard.com>
    à:	 MUSCLE <muscle@lists.musclecard.com>
    date:	 4 août 2013 17:47
    objet:	 Re: [Muscle] Alternate javax.smartcardio provider   


Hello,

this is only a small add-on to your appreciated work in the PCSC domain. 
We have to thank you.

We have been new to git with this release, so we missed the "best practice tip" 
to create eclipse projects one level below the git module. 

That said - after a clone you can import the the root directory directly via 
File->Import->General->Existing projects. 
With a current eclipse and Java 7 it should compile immediately. 

If you want to compile *everything* from source, you should also clone the 
"intarsys/runtime" and "intarsys/native-c" respositories and treat them the 
same way. 

The dependencies into "runtime" are quite small but to much to get rid of 
(at least for this release).

For the deployment, we wanted to create a deliverable that is able to compile 
without much effort. 
We will have a look if we can manage this in a more standard way.

To get your code running, don't forget to add the new provider before the 
standard Sun one. 

One way to do this is in the working examples in the "examples" folder.

Regards, Michael

