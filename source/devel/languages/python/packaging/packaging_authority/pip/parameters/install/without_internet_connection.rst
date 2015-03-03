


========================================
pip Install without internet connection
========================================



1) Save the packages with ``download`` on the connected machine
================================================================

.. seealso::

   - http://stackoverflow.com/questions/7300321/how-to-use-pythons-pip-to-download-and-keep-the-zipped-files-for-a-package



::

    pip install --download=packages -r requirements.txt


2) Install the the packages on the non-connected machine
========================================================


.. seealso::

   - http://stackoverflow.com/questions/7225900/how-to-pip-install-packages-according-to-requirements-txt-from-a-local-directory?rq=1



::

    pip install -r requirements.txt --no-index --find-links file:///C:/projects_id3/P2X238/XLOG2Y057_IHMs_Paban_Eurocopter/0.1.0/Livraison_PC_Encodage_Paban/django_bd_paban/packages


   
