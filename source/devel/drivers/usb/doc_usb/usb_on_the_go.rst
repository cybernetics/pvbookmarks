.. module:: USB_on_the_go_OTG
    :synopsis: USB on the go



.. index::
   pair: USB; on the go (OTG)


===================
USB on the go (OTG)
===================


.. seealso::

   - http://en.wikipedia.org/wiki/USB_On-The-Go
   - http://fr.wikipedia.org/wiki/USB_On-The-Go
   - http://de.wikipedia.org/wiki/Universal_Serial_Bus


.. contents::
   :depth: 3


Architecture
============


Standard USB uses a master/slave architecture; a USB host acts as the
protocol master, and a USB 'Device' acts as the slave. Only the Host
can schedule the configuration and data transfers over the link.

The Devices cannot initiate data transfers, they only respond to
requests given by a host. OTG introduces the concept that a 'Device'
can perform both the master and slave roles, and so subtly changes
the terminology.

Now a 'Device' can be either a 'Host' (acting as the link master)
or a 'Peripheral' (acting as the link slave). The Device connected
to the 'A' end of the cable at start-up acts as the Default Host,
while the 'B' end acts as the Default Peripheral.

USB On-The-Go does not preclude using a USB hub, but it describes
Host/Peripheral role swapping only for the case of a one-to-one
connection where two OTG devices are directly connected.

Role swapping does not work through a standard hub, and one device
will act as the Host and the other as the Peripheral until the hub
is disconnected.


Principe
========

Le standard USB (USB 1.1/2.0) utilise une architecture maître/esclave
un concentrateur USB (en anglais host USB) agit comme un Maître USB et
un périphérique USB agit comme un Esclave.

**Seuls les concentrateurs USB  peuvent gérer la configuration et le transfert
des données lors de  la connexion.**

La norme USB-OTG change cette situation. Les périphériques compatibles avec
la norme USB-OTG sont capables d'ouvrir une session, contrôler la connexion
et, échanger les rôles maître / périphérique.

Pour ce faire, USB-OTG introduit deux nouveaux protocoles : SRP
(Session Request Protocol) et HNP (Host Negotiation Protocol).

Les périphériques USB ON-The-Go sont compatibles avec les normes USB 1.1/2.0
et se comportent comme un périphérique USB standard lorsqu'ils sont connectés
avec des périphériques USB traditionnels (non OTG).

