


.. index::
   pair: Windows ; Media
   pair: C# ; Media namespace
   pair: C# ; Image


.. _csharp_windows_media:

==================================
C# System.Windows.Media Namespace
==================================


.. seealso::

   - http://msdn.microsoft.com/en-us/library/ms608873.aspx
   - http://msdn.microsoft.com/fr-fr/library/system.windows.media.imaging.bitmapsource.aspx

.. contents::
   :depth: 3


Introduction
============

Provides types that enable integration of rich media, including drawings, text,
and audio/video content in Windows Presentation Foundation (WPF) applications.


Bitmapsource
============

.. seealso::

   - http://msdn.microsoft.com/fr-fr/library/system.windows.media.imaging.bitmapsource.aspx


:Espace de noms:  :file:`System.Windows.Media.Imaging`
:Assembly:  :file:`PresentationCore` (dans PresentationCore.dll)

Représente un seul jeu constant de pixels à une certaine taille et à une
certaine résolution.



Bitmapsource example code
----------------------------


L'exemple de code suivant utilise une classe dérivée BitmapSource, BitmapImage,
pour créer une bitmap à partir d'un fichier image et pour l'utiliser comme source
d'un contrôle Image.

::

    // Create the image element.
    Image simpleImage = new Image();
    simpleImage.Width = 200;
    simpleImage.Margin = new Thickness(5);

    // Create source.
    BitmapImage bi = new BitmapImage();
    // BitmapImage.UriSource must be in a BeginInit/EndInit block.
    bi.BeginInit();
    bi.UriSource = new Uri(@"/sampleImages/cherries_larger.jpg",UriKind.RelativeOrAbsolute);
    bi.EndInit();
    // Set the image source.
    simpleImage.Source = bi;

Bitmapencoder
=============

.. seealso::

   - http://msdn.microsoft.com/fr-fr/library/system.windows.media.imaging.bitmapencoder.aspx


Encode une collection d'objets BitmapFrame en un flux d'image.


Bitmapencoder example code
---------------------------

L'exemple suivant montre comment utiliser la classe TiffBitmapEncoder dérivée
pour encoder une image.


::

    FileStream stream = new FileStream("empty.tif", FileMode.Create);
    TiffBitmapEncoder encoder = new TiffBitmapEncoder();
    TextBlock myTextBlock = new TextBlock();
    myTextBlock.Text = "Codec Author is: " + encoder.CodecInfo.Author.ToString();
    encoder.Frames.Add(BitmapFrame.Create(image));
    MessageBox.Show(myPalette.Colors.Count.ToString());
    encoder.Save(stream);


Bitmap
======

.. seealso::

   - http://msdn.microsoft.com/fr-fr/library/system.drawing.bitmap




Encapsule une bitmap GDI+, composée des données de pixels d'une image graphique
et de ses attributs.

**Bitmap est un objet utilisé pour manipuler des images définies par des
données de pixels.**

Bitmap Notes
------------

Une bitmap est composée des données de pixels d'une image graphique et de ses
attributs. Vous pouvez enregistrer un bitmap dans un fichier selon plusieurs
formats standard.

GDI+ prend en charge les formats de fichiers suivants : BMP, GIF, EXIF, JPG, PNG
et TIFF. Pour plus d'informations sur les formats pris en charge,
consultez la page Types de bitmaps.

Vous pouvez créer des images à partir de fichiers, de flux de données et d'autres
sources en utilisant l'un des constructeurs Bitmap et vous pouvez les enregistrer
dans un flux de données ou dans le système de fichiers à l'aide de la
méthode Save.

Pour dessiner des images à l'écran ou dans la mémoire, utilisez la méthode
DrawImage de l'objet Graphics. Pour une liste de rubriques sur l'utilisation de
fichiers image, consultez la page Utilisation des images, bitmaps, icônes et
métafichiers.


Bitmap example
---------------

::

    Bitmap image1;
    private void Button1_Click(System.Object sender, System.EventArgs e)
    {

        try
        {
            // Retrieve the image.
            image1 = new Bitmap(@"C:\Documents and Settings\All Users\"
                              + @"Documents\My Music\music.bmp", true);

            int x, y;

            // Loop through the images pixels to reset color.
            for(x=0; x<image1.Width; x++)
            {
                for(y=0; y<image1.Height; y++)
                {
                    Color pixelColor = image1.GetPixel(x, y);
                    Color newColor = Color.FromArgb(pixelColor.R, 0, 0);
                    image1.SetPixel(x, y, newColor);
                }
            }

            // Set the PictureBox to display the image.
            PictureBox1.Image = image1;

            // Display the pixel format in Label1.
            Label1.Text = "Pixel format: "+image1.PixelFormat.ToString();

        }
        catch(ArgumentException)
        {
            MessageBox.Show("There was an error." +
                "Check the path to the image file.");
        }
    }

PictureBox
==========

.. seealso::

   - http://msdn.microsoft.com/en-us/library/system.windows.forms.picturebox.aspx


Represents a Windows picture box control for displaying an image.

:Namespace:  :file:`System.Windows.Forms`
:Assembly:  :file:`System.Windows.Forms` (in System.Windows.Forms.dll)

Remarks
-------

Typically the PictureBox is used to display graphics from a bitmap, metafile,
icon, JPEG, GIF, or PNG file.

Set the Image property to the Image you want to display, either at design time
or at run time. You can alternatively specify the image by setting the
ImageLocation property and load the image synchronously using the Load method
or asynchronously using the LoadAsync method.

PictureBox example
------------------

The following code example illustrates how you can set an image and resize the
display area of the picture box. This example requires that ShowMyImage is
called in an existing form, and that the System.Drawing namespace has been
added to the source code for your form.

::

    private Bitmap MyImage ;
    public void ShowMyImage(String fileToDisplay, int xSize, int ySize)
    {
       // Sets up an image object to be displayed.
       if (MyImage != null)
       {
          MyImage.Dispose();
       }

       // Stretches the image to fit the pictureBox.
       pictureBox1.SizeMode = PictureBoxSizeMode.StretchImage ;
       MyImage = new Bitmap(fileToDisplay);
       pictureBox1.ClientSize = new Size(xSize, ySize);
       pictureBox1.Image = (Image) MyImage ;
    }





Other tools in other languages
==============================

.. seealso::

   - :ref:`python_pil_module`



C# media example code 1
=======================

.. literalinclude::  MediaImage.cs
   :linenos:
   :encoding: latin-1






