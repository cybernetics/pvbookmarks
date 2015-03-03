

.. index::
   pair: Exceptions ; C♯


.. _csharp_exceptions_ter:

=======================
C♯ Exceptions
=======================

.. seealso::

   - http://msdn.microsoft.com/fr-fr/library/5whzhsd2%28v=vs.100%29.aspx
   - :ref:`csharp_exceptions`


.. contents::
   :depth: 3


Introduction
============

La classe Exception est la classe de base dont les exceptions héritent.

La plupart des objets exception sont des instances d'une classe dérivée
d'Exception, mais vous pouvez lever n'importe quel objet qui dérive de la classe
Object en tant qu'exception.

Notez que certains langages ne prennent pas en charge la levée et l'interception
d'objets ne dérivant pas de la classe Exception.

**Dans la plupart des cas, il est recommandé de lever et d'intercepter uniquement
des objets Exception**.


Propriétés
===========

La classe Exception possède plusieurs propriétés qui permettent de mieux
comprendre une exception. Il s'agit notamment des propriétés suivantes :

La propriété StackTrace
-----------------------

Cette propriété contient une trace de la pile qui peut être utilisée pour
déterminer l'emplacement où une erreur s'est produite.

La trace de la pile comprend le nom du fichier source et le numéro de ligne du
programme si les informations de débogage sont disponibles.

La propriété InnerException.
----------------------------

Cette propriété peut servir à créer et à conserver une série d'exceptions
pendant la gestion des exceptions.

Vous pouvez utiliser cette propriété pour créer une nouvelle exception qui
contient des exceptions interceptées précédemment.

L'exception d'origine peut être saisie par la deuxième exception dans la
propriété InnerException, permettant ainsi au code qui gère la deuxième exception
d'examiner les informations supplémentaires.

Par exemple, prenons le cas d'une méthode qui lit un fichier et met en forme
les données. Le code essaie de lire le fichier, mais une FileException est levée.
La méthode intercepte FileException et lève une BadFormatException.
En ce cas, FileException peut être enregistrée dans la propriété InnerException
de BadFormatException.

Pour améliorer la capacité de l'appelant à déterminer la raison pour laquelle
une exception a été levée, il est parfois souhaitable qu'une méthode intercepte
une exception levée par le biais d'une routine d'assistance puis lève une
exception plus indicative de l'erreur qui s'est produite.

Une exception nouvelle et plus significative peut être créée, où la référence
d'exception interne peut avoir comme valeur l'exception d'origine.

Cette exception plus significative peut ensuite être levée pour l'appelant.

Notez que cette fonctionnalité permet de créer une série d'exceptions liées
qui se termine par l'exception levée en premier.

La propriété Message
--------------------

Cette propriété fournit des détails sur la cause d'une exception.

Le Message est dans la langue spécifiée par la propriété Thread.CurrentUICulture
du thread qui lève l'exception.

La propriété HelpLink
---------------------

Cette propriété peut contenir une URL (ou une URN) vers un fichier d'aide qui
fournit des informations extensives sur la cause d'une exception.

La propriété Data
------------------

Cette propriété est un IDictionary qui peut conserver des données arbitraires
dans des paires clé/valeur.


Remarques
=========

La plupart des classes qui héritent de la classe Exception n'implémentent pas
de membre supplémentaire et ne fournissent pas de fonctionnalité additionnelle ;
elles héritent simplement de la classe Exception.

Par conséquent, l'information la plus importante concernant une exception se
trouve dans la hiérarchie des exceptions, le nom de l'exception et les
informations contenues dans l'exception.


Création et levée d'exceptions (Guide de programmation C#)
===========================================================

Les programmes peuvent lever une classe d'exception prédéfinie dans l'espace de
noms System (sauf dans les endroits précédemment notés) ou créer leurs propres
classes d'exception en les dérivant de Exception.

Les classes dérivées doivent définir au moins quatre constructeurs:

- un constructeur par défaut,
- un qui définit la propriété du message
- et un qui définit les deux propriétés Message et InnerException.
- Le quatrième constructeur est utilisé pour sérialiser l'exception.

Les nouvelles classes d'exception doivent être sérialisables. Par exemple::


    [Serializable()]
    public class InvalidDepartmentException : System.Exception
    {
        public InvalidDepartmentException() : base() { }
        public InvalidDepartmentException(string message) : base(message) { }
        public InvalidDepartmentException(string message, System.Exception inner) : base(message, inner) { }

        // A constructor is needed for serialization when an
        // exception propagates from a remoting server to the client.
        protected InvalidDepartmentException(System.Runtime.Serialization.SerializationInfo info,
            System.Runtime.Serialization.StreamingContext context) { }
    }


C♯ Exceptions examples
======================


.. toctree::
   :maxdepth: 3
   
   examples/index
   
   
