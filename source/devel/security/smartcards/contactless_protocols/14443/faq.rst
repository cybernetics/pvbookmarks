.. module:: 14443Faq 
    :synopsis: 14443 FAQ annexes 

.. index::
   14443
   15693
   APDU
   T=CL   

===============    
Protocol issues
===============

Protocol issue CL1356A, 14443 / 15693 protocol
==============================================

Question from jncabarrou@ateis-eu.com
-------------------------------------

:: 

      -----Message d'origine-----
      De : jn Cabarrou / ATEIS [mailto:jncabarrou@ateis-eu.com]
      Envoyé : vendredi 11 décembre 2009 15:06
      À : Philippe BOURGAULT
      Objet : Re: RE : RE : Utilisation CL1356A avc le framework .NET

      Bonjour M. Bourgault,

      APDUResponse apduResp;

      CardNative iCard = new CardNative();

      string[] readers = iCard.ListReaders();

      iCard.Connect(readers[0], SHARE.Exclusive, PROTOCOL.T1);
      Console.WriteLine("Connects card on reader: " + readers[0]);

      APDUParam apduParam = new APDUParam();
  
      apduParam.Data = new byte[] { 0xFF, 0xCA, 0x00, 0x00, 0x00 };
      apduSelectFile.Update(apduParam);    //  {apduParam  :  Class=A0 Ins=A4 P1=00 P2=00 P3=05 Data=FFCA000000}
      apduResp = iCard.Transmit(apduSelectFile);                      <-----------------   ici erreur   1112

      Merci pour votre aide


Response from PB
----------------

:: 

    Vous passez un APDU "Select File" adressable uniquement à une carte supportant
    le T=CL (level 14443-4) alors que votre carte est une 15693.
    
    Vous devez passer un APDU comme suit :
        APDUCommand apduGetData_ID = new APDUCommand(0xFF , 0xCA, 0, 0, null, 0)
        apduResp = iCard.Transmit(apduGetData);
 