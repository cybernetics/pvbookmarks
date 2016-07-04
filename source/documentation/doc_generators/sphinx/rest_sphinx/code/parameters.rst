

.. index::
   literalinclude


=======================
Documenting parameters
=======================

.. seealso::

   - http://packages.python.org/an_example_pypi_project/sphinx.html


I'm wondering if people have suggestions on the best way to format
function/method docstrings so it's possible to get Sphinx's fancy
formatting and yet retain nice and readable docstrings from the Python
prompt. I'm especially interested in how to document the function/
method input "parameters".

I know about the :param name: stanza but when there's a relatively
long list of parameters, I don't find it very readable from the Python
prompt. Of course, once processed by Sphinx, it yields great looking
documentation.

I also know about http://packages.python.org/an_example_pypi_project/sphinx.html
and the googley and sphinxey variants. I'm thinking there must be a
good compromise here.

For return values, I often use the following in my docstrings:

:returns:
    :out1: something
    :out2: something else

Indentation and proper alignment make this easy to read *and* it looks
great once processed by Sphinx. But I can't find a similar syntax for
parameters and keywords. I *thought* (and obviously I'm wrong) that
Sphinx accepted :parameters: and :keywords: but those don't look nice
once processed, e.g., to html. In particular, :parameters: is
converted to "Parameters :" (with a space), which often causes the
colon to end on a new line below the word "Parameters".

It would be great to be able to write:

:parameters:
    :in1:  description of in1
    :in2:  description of in2

:keywords:
    :kw1: description of kw1

just the same way we can use :returns:. I'm happy to try and add this
if it sounds like a good idea. I'd like to hear what people think
anyways.

Thanks.



Example documenting parameters
==============================


Constants
---------

.. _cr_success:

COMMAND_SUCCESS
---------------

The CR_S_SUCCESS value is returned when a command is successfull.


+-------------+------------------------+---------------------------------------------------+
| Value       | Name                   | French Message                                    |
+=============+========================+===================================================+
| 0x00000000L | COMMAND_SUCCESS        | Opération réussie.                                |
+-------------+------------------------+---------------------------------------------------+

.. _list_error_codes:

List of error codes
-------------------

+-------------+------------------------+---------------------------------------------------+
| Value       | Name                   | French Message                                    |
+=============+========================+===================================================+
| 0x8130F001L | CR_E_FAILED            | Une vérification de cohérence interne a échoué.   |
+-------------+------------------------+---------------------------------------------------+
| 0x8130F002L | CR_E_TIMEOUT           | Le délai a expiré.                                |
+-------------+------------------------+---------------------------------------------------+
| 0x8130F003L | CR_E_SEND_DATA_FAILED  | L'envoi des données a échoué.                     |
+-------------+------------------------+---------------------------------------------------+
| 0x8130F004L | CR_E_OPEN_PORT_FAILED  | L'ouverture du port COM a échoué.                 |
+-------------+------------------------+---------------------------------------------------+
| 0x8130F005L | CR_E_CLOSE_PORT_FAILED | La fermeture du port COM a échoué.                |
+-------------+------------------------+---------------------------------------------------+
| 0x8130F006L | CR_E_BAD_SYNCHRO       | Erreur de synchronisation avec la base.           |
+-------------+------------------------+---------------------------------------------------+
| 0x8130F007L | CR_E_BAD_ADDRESS       | Mauvaise adresse.                                 |
+-------------+------------------------+---------------------------------------------------+
| 0x8130F008L | CR_E_BAD_SIZE          | Taille incorrecte.                                |
+-------------+------------------------+---------------------------------------------------+
| 0x8130F009L | CR_E_BAD_CHANNEL       | Mauvais canal.                                    |
+-------------+------------------------+---------------------------------------------------+
| 0x8130F00AL | CR_E_BAD_STATUS        | Mauvais statut retourné par la base.              |
+-------------+------------------------+---------------------------------------------------+
| 0x8130F00BL | CR_E_OPEN_FILE_FAILED  | Ouverture du fichier a échoué.                    |
+-------------+------------------------+---------------------------------------------------+



::


    .. c:function:: DWORD CR_RFID_VerifierPIN(ST_CODE_PIN *pCodePIN)

        Le code PIN permet d'autoriser l'utilisation des clés de chiffrement et de
        signature dans le lecteur RFID.

        :Paramètres:
            :entree:
                :pCodePIN: le code PIN à présenter au lecteur RFID.

        :Returns:
           :error:  :ref:`see the error codes <list_error_codes>`
           :success:  :ref:`COMMAND_SUCCESS <cr_success>`

.. _CR_RFID_VerifierPIN:


CR_RFID_VerifierPIN
--------------------

.. c:function:: DWORD CR_RFID_VerifierPIN(ST_CODE_PIN *pCodePIN)

    Le code PIN permet d'autoriser l'utilisation des clés de chiffrement et de
    signature dans le lecteur RFID.

    :Paramètres:
        :entree:
            :pCodePIN: le code PIN à présenter au lecteur RFID.

    :Returns:
       :error:  :ref:`see the error codes <list_error_codes>`
       :success:  :ref:`COMMAND_SUCCESS <cr_success>`

