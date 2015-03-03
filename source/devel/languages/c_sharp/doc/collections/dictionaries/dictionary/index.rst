

.. index::
   pair: Dictionary; C♯


.. _csharp_dictionary:

================
c♯ dictionary
================

.. seealso::

   - http://www.dotnetperls.com/dictionary


.. contents::
   :depth: 3



Test de l'appartenance d'une clé à un dictionnaire => ContainsKey
=================================================================


Exemple avec ContainsKey
-------------------------

::

    using System;
    using System.Collections.Generic;

    class Program
    {
        static void Main()
        {
        Dictionary<string, int> dictionary = new Dictionary<string, int>();
        dictionary.Add("apple", 1);
        dictionary.Add("windows", 5);

        // See whether Dictionary contains this string.
        if (dictionary.ContainsKey("apple"))
        {
            int value = dictionary["apple"];
            Console.WriteLine(value);
        }

        // See whether Dictionary contains this string.
        if (!dictionary.ContainsKey("acorn"))
        {
            Console.WriteLine(false);
        }
        }
    }


Exemple avec TryGetValue
-------------------------

.. seealso:: http://www.dotnetperls.com/trygetvalue

::


    using System.Collections.Generic;

    class Program
    {
        static void Main()
        {
            var d = new Dictionary<string, int>();
            d.Add("key", 0);
            // This code does two hash lookups.
            int value;
            if (d.TryGetValue("key", out value))
            {
                d["key"] = value + 1;
            }
        }
    }




Foreach
=======

::

    using System;
    using System.Collections.Generic;

    class Program
    {
        static void Main()
        {
            // Example Dictionary again
            Dictionary<string, int> d = new Dictionary<string, int>()
            {
                {"cat", 2},
                {"dog", 1},
                {"llama", 0},
                {"iguana", -1}
            };
            // Loop over pairs with foreach
            foreach (KeyValuePair<string, int> pair in d)
            {
                Console.WriteLine("{0}, {1}",
                pair.Key,
                pair.Value);
            }
            // Use var keyword to enumerate dictionary
            foreach (var pair in d)
            {
                Console.WriteLine("{0}, {1}",
                pair.Key,
                pair.Value);
            }
        }
    }


Exemples d'initialisation de dictionnaires
==========================================

.. toctree::
   :maxdepth: 3

   init_dictionary






