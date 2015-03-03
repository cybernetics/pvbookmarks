

.. index::
   pair: CRC ; CRC32
   pair: C♯ ; CRC32


.. _crc32_csharp:

======================
CRC32 C♯
======================


.. seealso::

   - http://damieng.com/blog/2006/08/08/calculating_crc32_in_c_and_net
   - https://github.com/damieng/DamienGKit/blob/master/CSharp/DamienG.Library/Security/Cryptography/Crc32.cs
   


To compute the hash for a file simply::

    Crc32 crc32 = new Crc32();
    String hash = String.Empty;

    using (FileStream fs = File.Open("c:\\myfile.txt", FileMode.Open))
        foreach (byte b in crc32.ComputeHash(fs)) hash += b.ToString("x2").ToLower();

    Console.WriteLine("CRC-32 is {0}", hash)



