

.. index::
   pair: Exceptions ; C♯


.. _csharp_exception_1:

=========================
C♯  Exceptions example 1
=========================

.. seealso::

   - http://msdn.microsoft.com/fr-fr/library/5whzhsd2%28v=vs.100%29.aspx
   - :ref:`csharp_exceptions`


.. contents::
   :depth: 3


Introduction
============


::

    /// <summary>
    /// Ajout d'une ouverture dans le tag RFID "Melange"
    /// </summary>
    public void AjoutOuvertureTagRFIDMelange_EtEcrireBacsMelange(TagRFIDMelange tagRFIDMelange
                                            , List<string> ordresDeFabrication
                                            , int numero_melange
                                            , ref string newCodeEPC)
    {
        Id3Tag id3Tag = Id3Tag.LireTagUnique(LecteurUHF_ID3);
        if (id3Tag == null)
        {
            labelMessage.Text = "Aucun tag trouvé";
            labelMessage.Visible = true;
            return;
        }

        // Mise à jour du tag mélange
        // ==========================
        try
        {
            CBacMelange bac_melange = new CBacMelange(tagRFIDMelange);

            try
            {
                // On débute une transaction qui peut être annulée
                DB_Eurocopter.Database.BeginTransaction();

                // Même date d'ouverture pour tous les OF
                DateTime date_saisie = DateTime.Now;
                foreach (string ordre_fabrication in ordresDeFabrication)
                {
                    try
                    {
                        // On écrit autant d'enregistrements BacMelange qu'il y a 
                        // d'ordres de fabrication
                        COrdreFabrication ouverture_bac = new COrdreFabrication(BacMelange.id
                                                                      , ordre_fabrication
                                                                      , numero_melange
                                                                      , OperateurCourant.id
                                                                      , date_saisie);

                        // Création de l'ouverture
                        DB_Eurocopter.Database.Insert(ouverture_bac);

                        Log.Write("DB_Eurocopter.Database.Insert Ouverture bac=>OK", false);

                        Log.Write("COrdreFabrication=..." + Environment.NewLine
                             + "bac_melange_id:" + ouverture_bac.bac_melange_id + Environment.NewLine
                             + "date_saisie:" + ouverture_bac.date_saisie.ToString("yyyy-MM-dd HH:mm:ss") + Environment.NewLine
                             + "id:" + ouverture_bac.id + Environment.NewLine
                             + "numero:" + ouverture_bac.numero + Environment.NewLine
                             + "ordre_fabrication:" + ouverture_bac.ordre_fabrication + Environment.NewLine
                             , false);
                    }
                    catch (Exception ex)
                    {
                        string message = string.Format("DB_Eurocopter.Database.Insert():{0}", ex.Message);
                        Log.Write(message + Environment.NewLine + ex.StackTrace, false);
                        labelMessage.Text = "Erreur d'insertion dans la base de données";
                        labelMessage.Visible = true;
                        throw new Exception("CBacMelange_ouvertures", ex);
                    }
                }

                try
                {
                    // on tente l'écriture dans le tag
                    tagRFIDMelange.EcrireTagMelange(id3Tag
                                                    , bac_melange
                                                    , tagRFIDMelange.DeltaOuverturesMelange
                                                    , tagRFIDMelange.CodeEPC
                                                    , ref newCodeEPC);
                }
                catch (Exception ex)
                {
                    // On fait un roolback de la transaction
                    //DB_Eurocopter.Database.Rollback();
                    string message = string.Format(" tagRFIDMelange.EcrireTag():{0}", ex.Message);
                    Log.Write(message + Environment.NewLine + ex.StackTrace, false);
                    //labelError.Text = "Echec de l'écriture du tag";
                    //labelError.Visible = true;
                    //throw new Exception("EcrireTag", ex);
                }
            
                // On incrémente le compteur d'ouverture de la vacation courante
                IncrementerOuverturePotVacationCourante();

                // Tout s'est bien passé, la transaction est bonne
                DB_Eurocopter.Database.Commit();
            }
            catch (Exception ex)
            {
                // On fait un roolback de la transaction
                DB_Eurocopter.Database.Rollback();

                bac_melange = null;
                string message = string.Format("Transaction annulée (Rollback) :{0}", ex.Message);
                Log.Write(message + Environment.NewLine + ex.StackTrace, false);
                throw new Exception("Apres rollback ", ex);
            }
        }
        catch (Exception ex)
        {
            string message = string.Format("AjoutOuvertureTagRFIDMelange_EtEcrireBacsMelange() tagMelange.EcrireTag() exception={0}", ex.Message);
            Log.Write(message + Environment.NewLine + ex.StackTrace, false);
            throw new Exception(message, ex);
        }

    } // public void AjoutOuvertureTagRFIDMelange_EtEcrireBacsMelange()
