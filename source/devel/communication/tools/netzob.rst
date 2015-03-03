
.. index::
   communication tools (netzob)


.. _netzob:

=============================================================
netzob (NETwork protocol modeliZatiOn By reverse engineering)
=============================================================

NETZOB : NETwork protocol modeliZatiOn By reverse engineering

.. seealso:: 

   - https://code.google.com/p/netzob/
   - :ref:`python_netzob`

Netzob simplifies the work for security auditors by providing a complete 
framework for the reverse engineering of communication protocols. It handles 
different types of protocols : text protocols (like HTTP and IRC), fixed 
fields protocols (like IP and TCP) and variable fields protocols 
(like ASN.1 based formats). 

Netzob is therefore suitable for reversing network protocols, stuctured files 
and system and process flows (IPC and communication with drivers). 

Netzob is provided with modules dedicated to capture data in multiple contexts 
(network, file, process and kernel data acquisition).

Description of the functionalities
==================================

- Handle the following inputs as initial data:

	* PCAP
	* Network capturing (with Scapy)
	* Structured files with unknown format
	* Intra Processus communication (API calls)
	* Inter Processus Communication (pipes, shared memory and sockets)
	* Kernel Memory (with a dedicacted module) 
	
- Metadata representation of inputs

- Clustering : Regroups equivalent messages using:

	* an UPGMA Algorithm to regroup similar messages
	* an openMP and MPI implementation 

- Sequencing, Alignment : Identification of fields in messages:

	* Needleman & Wunsch Implementation 

- Fields dependencies identification:

	* length fields and associated payloads
	* encapsulated messages identifications 

- Fields type identification:

	* Primary types : binary, ascii, num, base64...
	* Definition domain, unique elements and intervals
	* Data carving (tar gz, png, jpg, ...)
	* Semantic data identification (emails, IP ...) 
	
- Fuzzing :

	* Live instrumentation through a dedicated proxy
	* Possibilities of variations:
	
		* Data and types
		* Length
		* Fields dependencies 
		
- Results exports:
	
	* XML meta representations of infered protocol,
	* Dedicated New Wireshark Disector 

