.. module:: smartcard_FAQ
    :synopsis: FAQ smartcard

==============
Smartcard FAQ
==============

.. seealso:: Source: http://www.smartcardalliance.org/pages/smart-cards-faq

What is a smart card ?
======================

A smart card is a device that includes an embedded integrated circuit that can 
be either a secure microcontroller or equivalent intelligence with internal 
memory or a memory chip alone. The card connects to a reader with direct
physical contact or with a remote contactless radio frequency interface. 

With an embedded microcontroller, smart cards have the unique ability to store 
large amounts of data, carry out their own on-card functions (e.g., encryption
and mutual authentication) and interact intelligently with a smart card reader. 

Smart card technology conforms to international standards (ISO/IEC 7816 and 
ISO/IEC 14443) and is available in a variety of form factors, including
plastic cards, key fobs, watches, subscriber identification modules used 
in GSM mobile phones, and USB-based tokens.

For the purposes of this FAQ, “card” is used as the generic term to 
describe any device in which smart card technology is used.

What are the ISO/IEC 14443 and ISO/IEC 7816 standards?
======================================================

ISO/IEC 14443 is the international standard for contactless smart chips and 
cards that operate (i.e., can be read from or written to) at a distance of 
less than 10 centimeters (4 inches). This standard operates at 13.56 MHz 
and includes specifications for the physical characteristics, radio frequency 
power and signal interface, initialization and anticollision protocols 
and transmission protocol.


ISO/IEC 7816 is the international standard for contact smart cards. 
ISO/IEC 7816 Parts 4 and above are used by both contact and contactless 
smart card applications for security operations and commands for interchange.

What is a contactless smart card ?
----------------------------------

A contactless smart card includes an embedded smart card secure microcontroller 
or equivalent intelligence, internal memory and a small antenna and communicates 
with a reader through a contactless radio frequency (RF) interface. Contactless 
smart card technology is used in applications that need to protect personal 
information and/or deliver fast, secure transactions, such as transit fare 
payment cards, government and corporate identification cards,
documents such as electronic passports and visas, and financial payment cards.


Contactless smart cards have the ability to securely manage, store and provide 
access to data on the card, perform on-card functions (e.g., encryption and 
mutual authentication) and interact intelligently with a contactless smart
card reader. Contactless smart card technology and applications conform to 
international standards (ISO/IEC 14443 and ISO/IEC 7816). 

Contactless smart card technology is available in a variety of forms - 
in plastic cards, watches, key fobs, documents and other handheld devices 
(e.g., built into mobile phones).


How do contactless smart cards work ?
=====================================

Contactless smart card systems are closely related to contact smart card 
systems. Like contact smart card systems, information is stored on a chip 
embedded within the contactless smart card. However, unlike the contact 
smart card, the power supplied to the card as well as the data exchanged 
between the card and the reader are achieved without the use of contacts, 
using magnetic or electromagnetic fields to both power the card as well 
as to exchange data with the reader.

The contactless smart card contains an antenna embedded within the plastic
body of the card (or within a key fob, watch or other document). When the 
card is brought into the electromagnetic field of the reader, the chip in 
the card is powered on. Once the chip is powered on, a wireless communication
protocol is initiated and established between the card and the reader for 
data transfer.

The following four functions describe at a high level the sequence of events 
that happen when a contactless smart card is brought near a card reader:

* Energy transfer to the card for powering the integrated circuit (chip)
* Clock signal transfer
* Data transfer to the contactless smart card
* Data transfer from the contactless smart card

Hence, once the card is brought within range of an electromagnetic field of 
the required frequency, the card will be powered up, ready to communicate 
with the reader. Since the contactless smart cards described in this FAQ are
based on the ISO/IEC 14443 standard, this frequency is 13.56 MHz and a reader
that complies with the standard would have an activation field (range) of 
about 4 inches (approximately 10 centimeters). In other words, the card 
needs to be within 10 centimeters of a reader for it to be effectively powered; 
however, the effective range for communications for the card to be read 
will depend on a number of factors like the power of the reader, the
antenna of the reader and the antenna of the card.

Is contactless smart card technology the same as RFID technology ?
==================================================================

No. There is significant confusion in discussions of RF-enabled applications, 
with contactless smart card technology often incorrectly categorized as ‘RFID.’ 
There are a wide range of RF technologies used for a variety of applications 
– each with different operational parameters, frequencies, read ranges and
capabilities to support security and privacy features. For example, the RFID
technologies that are used to add value in manufacturing, shipping and 
object-related tracking operate over long ranges (e.g., 25 feet), were designed
for that purpose alone and have minimal built-in support for security and privacy.

Contactless smart cards, on the other hand, use RF technology, but, by design, 
operate at a short range (less than 4 inches) and can support the equivalent 
security capabilities of a contact smart card chip.

What security capabilities do contactless smart cards support ?
===============================================================

Contactless smart cards use RF technology, but, by design, operate at a short 
range (less than 4 inches) and can support the equivalent security capabilities
of a contact smart card chip (see below). Contactless smart cards and readers 
conform to international standards, ISO/IEC 14443 and ISO/IEC 7816, and can 
implement a variety of industry-standard cryptographic protocols (e.g., AES, 3DES, RSA, ECC).


The contactless smart chip includes a smart card secure microcontroller and
internal memory and has unique attributes RFID tags lack – i.e., the ability
to securely manage, store and provide access to data on the card, perform
complex functions (for example, encryption and mutual authentication) and 
interact intelligently via RF with a contactless reader. Applications using 
contactless smart cards support many security features that ensure the integrity,
confidentiality and privacy of information stored or transmitted, including 
the following:

- Mutual authentication. For applications requiring secure card access, the 
  contactless smart card-based device can verify that the reader is authentic 
  and can prove its own authenticity to the reader before starting a secure transaction.
- Strong information security. For applications requiring complete data protection,
  information stored on cards or documents using contactless smart card technology 
  can be encrypted and communication between the contactless smart card-based 
  device and the reader can be encrypted to prevent eavesdropping. Hashes and/or 
  digital signatures can be used to ensure data integrity and to authenticate 
  the card and the credentials it contains.
  

Cryptographically strong random number generators can be used to enable 
dynamic cryptographic keys, preventing replay attacks:

- Strong contactless device security. Like contact smart cards, contactless
  smart card technology is extremely difficult to duplicate or forge and has 
  built-in tamper-resistance. Smart card chips include a variety of hardware 
  and software capabilities that detect and react to tampering attempts and 
  help counter possible attacks. For example, the chips are manufactured with
  features such as extra metal layers, sensors to detect thermal and UV light 
  attacks, and additional software and hardware circuitry to thwart differential
  power analysis.
  
- Authenticated and authorized information access. The contactless smart card’s 
  ability to process information and react to its environment allows it to 
  uniquely provide authenticated information access and protect the privacy of 
  personal information. The contactless smart card can verify the authority 
  of the information requestor and then allow access only to the information 
  required. Access to stored information can also be further protected by a personal 
  identification number (PIN) or biometric to protect privacy and counter unauthorized access.
  
- Support for biometric authentication. For human identification systems that 
  require the highest degree of security and privacy, smart cards can be 
  implemented in combination with biometric technology. Biometrics are measurable 
  physical characteristics or personal behavioral traits that can be used to 
  recognize the identity or verify the claimed identity of an individual. 
  Smart cards and biometrics are a natural fit to provide two- or multi-factor 
  authentication. A smart card is the logical secure storage medium for biometric 
  information. During the enrollment process, the biometric template can be 
  stored on the smart card chip for later verification. Only the authorized user 
  with a biometric matching the stored enrollment template receives access and privileges.
  
- Strong support for information privacy. The use of smart card technology 
  strengthens the ability of a system to protect individual privacy. 
  Unlike other technologies, smart card-based devices can implement a 
  personal firewall for an individual, releasing only the information 
  required and only when it is required. The ability to support authenticated 
  and authorized information access and the strong contactless device and 
  data security make contactless smart cards excellent guardians of 
  personal information and individual privacy.


It is important to note that information privacy and security must be designed 
into an application at the system level by the organization issuing the 
contactless device, card or document. It is critical that issuing organizations 
have the appropriate policies in place to support the security and privacy 
requirements of the application being deployed and then implement the 
appropriate technology that delivers those features. The ability of
contactless smart card technology to support a wide array of security 
features provides organizations with the flexibility to implement the 
level of security that is commensurate with the risk expected in the application.


