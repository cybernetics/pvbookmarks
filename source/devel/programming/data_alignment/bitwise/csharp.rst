

.. index::
   pair: Bitwise ; C#


.. _csharp_bitwise_io:

==================================
C# Bitwise IO
==================================


.. seealso::

   - http://rosettacode.org/wiki/Bitwise_IO#C.23
   - :ref:`csharp_language`


.. contents::
   :depth: 3


Code C♯
========


.. code-block:: c

    /// <summary>
    /// Classe pour lire les bits
    /// </summary>
    public class BitReader
    {
        uint readData = 0;
        int startPosition = 0;
        int endPosition = 0;

        public int InBuffer
        {
            get { return endPosition - startPosition; }
        }

        private Stream stream;

        public Stream BaseStream
        {
            get { return stream; }
        }

        public BitReader(Stream stream)
        {
            this.stream = stream;
        }

        void EnsureData(int bitCount)
        {
            int readBits = bitCount - InBuffer;
            while (readBits > 0)
            {
                int b = BaseStream.ReadByte();

                if (b < 0) throw new InvalidOperationException("Unexpected end of stream");

                readData |= checked((uint)b << endPosition);
                endPosition += 8;
                readBits -= 8;
            }
        }

        public bool ReadBit()
        {
            return Read(1) > 0;
        }

        public int Read(int bitCount)
        {
            EnsureData(bitCount);

            int result = (int)(readData >> startPosition) & ((1 << bitCount) - 1);
            startPosition += bitCount;
            if (endPosition == startPosition)
            {
                endPosition = startPosition = 0;
                readData = 0;
            }
            else if (startPosition >= 8)
            {
                readData >>= startPosition;
                endPosition -= startPosition;
                startPosition = 0;
            }

            return result;
        }

        public void Align()
        {
            endPosition = startPosition = 0;
            readData = 0;
        }
    }

    /// <summary>
    /// Classe pour écrire les bits
    /// </summary>
    public class BitWriter
    {
        uint data = 0;
        int dataLength = 0;
        Stream stream;

        public Stream BaseStream
        {
            get { return stream; }
        }

        public int BitsToAligment
        {
            get { return (32 - dataLength) % 8; }
        }

        public BitWriter(Stream stream)
        {
            this.stream = stream;
        }

        public void WriteBit(bool value)
        {
            Write(value ? 1 : 0, 1);
        }

        public void Write(int value, int length)
        {
            uint currentData = data | checked((uint)value << dataLength);
            int currentLength = dataLength + length;
            while (currentLength >= 8)
            {
                BaseStream.WriteByte((byte)currentData);
                currentData >>= 8;
                currentLength -= 8;
            }
            data = currentData;
            dataLength = currentLength;
        }

        public void Align()
        {
            if (dataLength > 0)
            {
                BaseStream.WriteByte((byte)data);

                data = 0;
                dataLength = 0;
            }
        }
    }


Exemple d'appel C♯
==================

::

    /// <summary>
    /// Ecriture des informations issues de la base dans la mémoire EPC private
    /// </summary>
    public static void EcrireECSMemoryPrivate(CPotPeinture pot_de_peinture)
    {
        MemoryStream memory_stream = new MemoryStream();
        BitWriter bit_writer = new BitWriter(memory_stream);

        // Ecriture des longueurs de champs
        // ================================
        // 1) Longueur champ NomProduit
        bit_writer.Write(pot_de_peinture.NomProduit.Length, 4);
        // 2) Longueur champ ReferenceProduit
        bit_writer.Write(pot_de_peinture.ReferenceProduit.Length, 4);
        // 3) Longueur champ Fournisseur
        bit_writer.Write(pot_de_peinture.Fournisseur.Length, 4);
        // 4) Longueur champ NumeroLot
        bit_writer.Write(pot_de_peinture.NumeroLot.Length, 5);
        // 5) Longueur champ Teinte
        bit_writer.Write(pot_de_peinture.Teinte.Length, 4);

        // Ecriture des champs Nom, ReferenceProduit, Fournisseur, NumeroLot et Teinte
        // ===========================================================================
        // 1) Ecriture du champ NomProduit
        Compression.CompressData(bit_writer, pot_de_peinture.NomProduit);
        // 2) Ecriture du champ ReferenceProduit
        Compression.CompressData(bit_writer, pot_de_peinture.ReferenceProduit);
        // 3) Ecriture du champ Fournisseur
        Compression.CompressData(bit_writer, pot_de_peinture.Fournisseur);
        // 4) Ecriture du champ NumeroLot
        Compression.CompressData(bit_writer, pot_de_peinture.NumeroLot);
        // 5) Ecriture du champ Teinte
        Compression.CompressData(bit_writer, pot_de_peinture.Teinte);


        // Fin ecriture
        bit_writer.Align();

        memory_stream.Position = 0;
        BitReader bit_reader = new BitReader(memory_stream);

        // Lecture des longueurs de champs
        // ===============================
        // 1) Longueur champ NomProduit
        int longueur_nom = bit_reader.Read(4);
        string message = string.Format("Longueur NomProduit({0})={1}", pot_de_peinture.NomProduit, longueur_nom);
        Console.WriteLine(message);

        // 2) Longueur champ ReferenceProduit
        int longueur_reference_produit = bit_reader.Read(4);
        message = string.Format("Longueur ReferenceProduit({0})={1}", pot_de_peinture.ReferenceProduit, longueur_reference_produit);
        Console.WriteLine(message);

        // 3) Longueur champ Fournisseur
        int longueur_fournisseur = bit_reader.Read(4);
        message = string.Format("Longueur Fournisseur({0})={1}", pot_de_peinture.Fournisseur, longueur_fournisseur);
        Console.WriteLine(message);

        // 4) Longueur champ NumeroLot
        int longueur_numero_lot = bit_reader.Read(5);
        message = string.Format("Longueur NumeroLot({0})={1}", pot_de_peinture.NumeroLot, longueur_numero_lot);
        Console.WriteLine(message);

        // 5) Longueur champ Teinte
        int longueur_teinte = bit_reader.Read(4);
        message = string.Format("Longueur Teinte({0})={1}", pot_de_peinture.Teinte, longueur_teinte);
        Console.WriteLine(message);

        // Lecture des champs Nom, ReferenceProduit, Fournisseur, NumeroLot et Teinte
        // ===========================================================================
        // 1) Lecture du champ NomProduit
        string dataNomProduit = "";
        Compression.DecompressData(bit_reader, longueur_nom, ref dataNomProduit);
        message = string.Format("NomProduit={0}", dataNomProduit);
        Console.WriteLine(message);
        // 2) Lecture champ  ReferenceProduit
        string dataReferenceProduit = "";
        Compression.DecompressData(bit_reader, longueur_reference_produit, ref dataReferenceProduit);
        message = string.Format("ReferenceProduit={0}", dataReferenceProduit);
        Console.WriteLine(message);
        // 3) Lecture champ Fournisseur
        string dataFournisseur = "";
        Compression.DecompressData(bit_reader, longueur_fournisseur, ref dataFournisseur);
        message = string.Format("Fournisseur={0}", dataFournisseur);
        Console.WriteLine(message);
        // 4) Lecture champ NumeroLot
        string dataNumeroLot = "";
        Compression.DecompressData(bit_reader, longueur_numero_lot, ref dataNumeroLot);
        message = string.Format("NumeroLot={0}", dataNumeroLot);
        Console.WriteLine(message);
        // 5) Lecture champ Teinte
        string dataTeinte = "";
        Compression.DecompressData(bit_reader, longueur_teinte, ref dataTeinte);
        message = string.Format("Teinte={0}", dataTeinte);
        Console.WriteLine(message);


        bit_reader.Align();
    }
