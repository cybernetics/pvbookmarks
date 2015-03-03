/**
@file       MediaImage.cs
@author     $Author: pvergain $
@version    $Revision: 751 $
@date       $Date: 2012-09-26 09:48:17 +0200 (Wed, 26 Sep 2012) $
@brief      Gestion des images.
@details
 *
*/

/** @addtogroup MediaImage
 *  @{
 */


using System;
using System.Collections; // ArrayList
using System.Collections.Generic;  // SortedDictionary
using System.Globalization;
using System.Threading;
using System.Windows.Forms;
using System.Resources;
using System.Reflection; // Assembly
using System.ComponentModel; // BackgroundWorker
using System.IO; // File
using System.Drawing; // Image
using System.Drawing.Imaging;  // ImageFormat
using System.Windows.Media.Imaging;  // http://msdn.microsoft.com/fr-fr/library/system.windows.media.imaging.bitmapsource.aspx
// http://msdn.microsoft.com/fr-fr/library/system.windows.media.imaging.bitmapencoder.aspx
// Encode une collection d'objets BitmapFrame en un flux d'image.
using System.Windows.Media; // http://msdn.microsoft.com/en-us/library/system.windows.media.pixelformats.aspx

namespace VideoCell
{
    /// <summary>
    /// Gestion des media image.
    /// </summary>
    public static class CMediaImage
    {
        /// <summary>
        /// Création d'une image à partir d'une bitmap
        /// </summary>
        public static BitmapEncoder CreateImageFromRawData(int ImageWidth, int ImageLength, byte[] ImageData, VideoCellImage.Format videoCellFormat, ref string file_name)
        {
            BitmapEncoder encoder = null;

            int ImageSize = (ImageWidth * ImageLength);

            byte[] RawData = new byte[ImageSize];
            Buffer.BlockCopy(ImageData, ImageWidth * 2, RawData, 0, ImageSize);


            int bitsPerPixel = 8;
            int stride = (ImageWidth * bitsPerPixel + 7) / 8;
            BitmapSource bmps = BitmapSource.Create(ImageWidth, ImageLength
                                                   , 96, 96
                                                   , PixelFormats.Gray8
                                                   , null
                                                   , RawData
                                                   , stride);

            switch (videoCellFormat)
            {
                case VideoCellImage.Format.JPG:
                    encoder = new JpegBitmapEncoder();
                    JpegBitmapEncoder encodjpeg = (JpegBitmapEncoder)encoder;
                    encodjpeg.QualityLevel = 10;  // Permet de produire des fichiers de taille identique à celle produite par PIL
                    file_name = file_name + ".jpg";
                    break;
                case VideoCellImage.Format.TIFF:
                    encoder = new TiffBitmapEncoder();
                    file_name = file_name + ".tiff";
                    break;
                case VideoCellImage.Format.BMP:
                    encoder = new BmpBitmapEncoder();
                    file_name = file_name + ".bmp";
                    break;
                default:
                    break;
            }

            encoder.Frames.Add(BitmapFrame.Create(bmps));

            return encoder;

        } // public BitmapEncoder CreateImageFromRawData()



    }  // public class CMediaImage


} // VideoCell

/**
    fin VideoCellCommands

@}

*/
