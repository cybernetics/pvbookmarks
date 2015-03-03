

.. index::
   pair: Password; stockage

.. _stockage_mots_de_passe_2014:

===================================
Stockage des mots de passe en 2014
===================================


.. contents::
   :depth: 3


Articles
========

.. seealso:: 

   - http://linuxfr.org/users/elyotna/journaux/l-art-de-stocker-des-mots-de-passe


Bonjour à tous,

Je vous propose un enième article sur un sujet bien connu : comment sécuriser des mots de passe dans une base de données. Et au passage, comment éviter de se taper la honte si votre BDD est leakée.

Après une longue réflexion, j'ai décidé de présenter ce journal sous forme de niveaux. Deux négatifs (-2 et -1) qui correspondent à des solutions (trop) souvent mises en place mais pas sécurisées du tout.
Puis, un niveau 0 qui devrait être la norme, et un niveau 1 pour les grosses BDD qui recèlent des millions d'informations critiques.
Préambule

Dans ce journal, il est question de fonctions de hachage. Elles permettent de convertir un message de taille arbitraire en une empreinte de taille fixe qui semble aléatoire. Exemple :

SHA1('Mon Super Message De La Mort Qui Tue') = 26e5f8bbf9e0e74a862c292f1eb181dfedc06261

Une telle fonction est qualifiée de fonction à sens unique, puisque le but est de rendre (calculatoirement) impossible la récupération du message original à partir d'une empreinte.
La seconde propriété d'une fonction de hachage, c'est qu'il doit être infaisable pour un attaquant de trouver deux messages différents qui donnent la même empreinte - on parle alors de collision.
Parmi les plus connues, on notera MD5, SHA1, SHA2 et SHA3.
Niveau -2 : MD5($pwd)

Une solution que vous avez tous du rencontrer une fois dans votre vie, c'est ça :

<?php

$query = mysql_query('select * from account where login = '.$login.' and pwd = MD5('.$password.')');

?>

Sans parler du fait que MD5 est une fonction de hash obsolète et cassée, c'est surtout la méthode ici qui n'est pas sécurisée.
Car croyez-moi, même avec un SHA2-256 ou même un SHA-3, je vous pète 95% de vos mots de passe en moins d'une journée.

Pour cela, rien de plus simple : je récupère une Rainbow Table, et je la fais correspondre avec votre base de données. Une Rainbow Table, c'est une table précalculée de valeurs en clair et leurs hash associés :

RainbowTable
Niveau -1 : SHA1($salt + $pwd)

Avec cette méthode, on sent que la personne qui a essayé de sécuriser ses mots de passe y a mis un peu plus de volonté en rajoutant un sel, c'est-à-dire une valeur constante qu'il concatène aux mots de passe avant de les hasher.
Ca a pour avantage d'invalider les Rainbow Table existantes, mais ce n'est malheureusement pas suffisant.

Pour casser ça, on part d'un utilisateur dont on connaît déjà le mot de passe en clair (un ami ou nous-même qui avons crée un compte sur la plateforme).
On lance alors une attaque brute-force pour déterminer le sel global. Ca peut prendre jusqu'à une semaine selon la force du sel.

Une fois le sel trouvé, on retrouve à nouveaux 95% des mots de passe en calculant une nouvelle Rainbow Table basée sur ce sel.

A noter aussi que si l'attaquant a un accès plus important que la BDD (code source de la plateforme), il peut directement trouver le fichier dans lequel est stocké le sel.. Dans ce cas, on retrouve le même niveau de sécurité qu'en -2.
Niveau 0 : bcrypt($perUserSalt, $pwd)

Là, on arrive enfin à quelque chose de convenable. Par rapport au niveau -1, deux choses changent :

    Au lieu d'utiliser une fonction de hash classique, on utilise des procédures dédiée aux mots de passe. bcrypt (basé sur l'algorithme de chiffrement Blowfish) et scrypt sont les deux plus connues, et ont comme avantage d'être lentes à calculer. Pour un attaquant, ça rend le procédé de brute-force beaucoup plus long. Pour la plateforme, la perte en performances est négligeable (un utilisateur se connecte une fois et point barre).
    Le sel global devient un sel généré aléatoirement pour chaque utilisateur. Ainsi, même si l'on retrouve le mot de passe d'un utilisateur - ce qui peut prendre plusieurs semaines à cause de la lenteur de bcrypt/scrypt -, cela ne compromet pas ceux des autres.

Voici à quoi peut ressembler une BDD basée sur bcrypt :

Bcrypt
======

On peut voir ici que le champ "password" contient plus que le hash des mots de 
passe. 

Il contient ces informations :

    $2a : Algorithme utilisé (en l'occurence Bcrypt avec un mot de passe UTF-8)
    $10 : niveau de difficulté choisi pour l'algorithme (parce que oui, c'est configurable selon la puissance de la plateforme)
    $NOLgNI4iSzHbxYj3/CNW3OAf9/dmuOOCMsF1oPNjhThyG6eaDnB0e : le sel (16 octets) et le hash (24 octets) codés en Base64 puis concaténés

Niveau 1 : AES(bcrypt($perUserSalt, $pwd), $secretKey)

Fiou, là c'est du haut de gamme ! De la haute voltige de la protection de mot de passe.

Pour les grosses plateformes remplies de millions d'informations utilisateurs, le top du top consiste à rajouter une couche de chiffrement sur le hash - avec AES par exemple -, associée à une clé constante.
Attention cependant, tout dépend de la sécurité du stockage de cette clé secrète. C'est pourquoi il est conseillé d'utiliser un HSM.
Un HSM, pour faire court, est un serveur cryptographique qui possède des protections physiques : Il "tilt" (effacement des données) si l'on tente de l'ouvrir ou de le déplacer, et ses composants électroniques sont coulés dans un mélange qui les rend physiquement inaccessibles.
Logiciellement, il agit comme une boîte noire de chiffrement/déchiffrement et autres primitives cryptographiques, requêtables par réseau.

Pour le coup, si vous avez une implémentation rigoureuse de ça, avec en plus l'utilisation d'un HSM, la probabilité qu'un attaquant arrive à ne casser ne serait-ce qu'un seul mot de passe est minime.

Et vous, vous utilisez quoi ? :>





