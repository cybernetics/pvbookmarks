
.. index::
   opencv tree sources


.. _opencv_tree_sources:


===================
Opencv tree sources
===================

::

    |   CMakeLists.txt
    |   cmake_uninstall.cmake.in
    |   cvconfig.h.cmake
    |   index.rst
    |   OpenCV.mk.in
    |   opencv.pc.cmake.in
    |   OpenCVConfig.cmake.in
    |   OpenCVFindIPP.cmake
    |   OpenCVFindLATEX.cmake
    |   OpenCVFindOpenEXR.cmake
    |   OpenCVFindOpenNI.cmake
    |   OpenCVFindPkgConfig.cmake
    |   OpenCVModule.cmake
    |   OpenCVPCHSupport.cmake
    |   Package.cmake.in
    |   README
    |
    +---3rdparty
    |   |   CMakeLists.txt
    |   |   readme.txt
    |   |
    |   +---ffmpeg
    |   |       CMakeLists.txt
    |   |       ffopencv.c
    |   |       make.bat
    |   |       opencv_ffmpeg.dll
    |   |       opencv_ffmpeg_64.dll
    |   |       readme.txt
    |   |
    |   +---ilmimf
    |   |       LICENSE
    |   |       README
    |   |
    |   +---include
    |   |   |   msc_inttypes.h
    |   |   |   msc_stdint.h
    |   |   |
    |   |   +---dshow
    |   |   |       amvideo.h
    |   |   |       audevcod.h
    |   |   |       bdatypes.h
    |   |   |       control.h
    |   |   |       ddraw.h
    |   |   |       dshow.h
    |   |   |       dsound.h
    |   |   |       dvdmedia.h
    |   |   |       errors.h
    |   |   |       evcode.h
    |   |   |       ksuuids.h
    |   |   |       strmif.h
    |   |   |       uuids.h
    |   |   |       _mingw_dxhelper.h
    |   |   |       _mingw_unicode.h
    |   |   |
    |   |   \---ffmpeg_
    |   |       +---libavcodec
    |   |       |       avcodec.h
    |   |       |       avfft.h
    |   |       |       dxva2.h
    |   |       |       opt.h
    |   |       |       vaapi.h
    |   |       |       vdpau.h
    |   |       |       xvmc.h
    |   |       |
    |   |       +---libavdevice
    |   |       |       avdevice.h
    |   |       |
    |   |       +---libavformat
    |   |       |       avformat.h
    |   |       |       avio.h
    |   |       |
    |   |       +---libavutil
    |   |       |       adler32.h
    |   |       |       attributes.h
    |   |       |       avconfig.h
    |   |       |       avstring.h
    |   |       |       avutil.h
    |   |       |       base64.h
    |   |       |       common.h
    |   |       |       crc.h
    |   |       |       error.h
    |   |       |       fifo.h
    |   |       |       intfloat_readwrite.h
    |   |       |       log.h
    |   |       |       lzo.h
    |   |       |       mathematics.h
    |   |       |       md5.h
    |   |       |       mem.h
    |   |       |       pixdesc.h
    |   |       |       pixfmt.h
    |   |       |       rational.h
    |   |       |       sha1.h
    |   |       |
    |   |       \---libswscale
    |   |               swscale.h
    |   |
    |   +---lib
    |   |       libavcodec.a
    |   |       libavcodec64.a
    |   |       libavcore64.a
    |   |       libavdevice.a
    |   |       libavdevice64.a
    |   |       libavformat.a
    |   |       libavformat64.a
    |   |       libavutil.a
    |   |       libavutil64.a
    |   |       libcoldname_.a
    |   |       libgcc64.a
    |   |       libgcc_.a
    |   |       libmingwex64.a
    |   |       libmingwex_.a
    |   |       libnative_camera_r2.2.2.so
    |   |       libnative_camera_r2.3.3.so
    |   |       libswscale.a
    |   |       libswscale64.a
    |   |       libwsock3264.a
    |   |       libwsock32_.a
    |   |
    |   +---libjasper
    |   |   |   CMakeLists.txt
    |   |   |   jas_cm.c
    |   |   |   jas_debug.c
    |   |   |   jas_getopt.c
    |   |   |   jas_icc.c
    |   |   |   jas_iccdata.c
    |   |   |   jas_image.c
    |   |   |   jas_init.c
    |   |   |   jas_malloc.c
    |   |   |   jas_seq.c
    |   |   |   jas_stream.c
    |   |   |   jas_string.c
    |   |   |   jas_tmr.c
    |   |   |   jas_tvp.c
    |   |   |   jas_version.c
    |   |   |   jp2_cod.c
    |   |   |   jp2_cod.h
    |   |   |   jp2_dec.c
    |   |   |   jp2_dec.h
    |   |   |   jp2_enc.c
    |   |   |   jpc_bs.c
    |   |   |   jpc_bs.h
    |   |   |   jpc_cod.h
    |   |   |   jpc_cs.c
    |   |   |   jpc_cs.h
    |   |   |   jpc_dec.c
    |   |   |   jpc_dec.h
    |   |   |   jpc_enc.c
    |   |   |   jpc_enc.h
    |   |   |   jpc_fix.h
    |   |   |   jpc_flt.h
    |   |   |   jpc_math.c
    |   |   |   jpc_math.h
    |   |   |   jpc_mct.c
    |   |   |   jpc_mct.h
    |   |   |   jpc_mqcod.c
    |   |   |   jpc_mqcod.h
    |   |   |   jpc_mqdec.c
    |   |   |   jpc_mqdec.h
    |   |   |   jpc_mqenc.c
    |   |   |   jpc_mqenc.h
    |   |   |   jpc_qmfb.c
    |   |   |   jpc_qmfb.h
    |   |   |   jpc_t1cod.c
    |   |   |   jpc_t1cod.h
    |   |   |   jpc_t1dec.c
    |   |   |   jpc_t1dec.h
    |   |   |   jpc_t1enc.c
    |   |   |   jpc_t1enc.h
    |   |   |   jpc_t2cod.c
    |   |   |   jpc_t2cod.h
    |   |   |   jpc_t2dec.c
    |   |   |   jpc_t2dec.h
    |   |   |   jpc_t2enc.c
    |   |   |   jpc_t2enc.h
    |   |   |   jpc_tagtree.c
    |   |   |   jpc_tagtree.h
    |   |   |   jpc_tsfb.c
    |   |   |   jpc_tsfb.h
    |   |   |   jpc_util.c
    |   |   |   jpc_util.h
    |   |   |   LICENSE
    |   |   |   README
    |   |   |
    |   |   \---jasper
    |   |           jasper.h
    |   |           jas_cm.h
    |   |           jas_config.h
    |   |           jas_config.h.in
    |   |           jas_config2.h
    |   |           jas_debug.h
    |   |           jas_fix.h
    |   |           jas_getopt.h
    |   |           jas_icc.h
    |   |           jas_image.h
    |   |           jas_init.h
    |   |           jas_malloc.h
    |   |           jas_math.h
    |   |           jas_seq.h
    |   |           jas_stream.h
    |   |           jas_string.h
    |   |           jas_tmr.h
    |   |           jas_tvp.h
    |   |           jas_types.h
    |   |           jas_version.h
    |   |
    |   +---libjpeg
    |   |       CMakeLists.txt
    |   |       jcapimin.c
    |   |       jcapistd.c
    |   |       jccoefct.c
    |   |       jccolor.c
    |   |       jcdctmgr.c
    |   |       jchuff.c
    |   |       jchuff.h
    |   |       jcinit.c
    |   |       jcmainct.c
    |   |       jcmarker.c
    |   |       jcmaster.c
    |   |       jcomapi.c
    |   |       jconfig.h
    |   |       jcparam.c
    |   |       jcphuff.c
    |   |       jcprepct.c
    |   |       jcsample.c
    |   |       jctrans.c
    |   |       jdapimin.c
    |   |       jdapistd.c
    |   |       jdatadst.c
    |   |       jdatasrc.c
    |   |       jdcoefct.c
    |   |       jdcolor.c
    |   |       jdct.h
    |   |       jddctmgr.c
    |   |       jdhuff.c
    |   |       jdhuff.h
    |   |       jdinput.c
    |   |       jdmainct.c
    |   |       jdmarker.c
    |   |       jdmaster.c
    |   |       jdmerge.c
    |   |       jdphuff.c
    |   |       jdpostct.c
    |   |       jdsample.c
    |   |       jdtrans.c
    |   |       jerror.c
    |   |       jerror.h
    |   |       jfdctflt.c
    |   |       jfdctfst.c
    |   |       jfdctint.c
    |   |       jidctflt.c
    |   |       jidctfst.c
    |   |       jidctint.c
    |   |       jidctred.c
    |   |       jinclude.h
    |   |       jmemansi.c
    |   |       jmemmgr.c
    |   |       jmemsys.h
    |   |       jmorecfg.h
    |   |       jpegint.h
    |   |       jpeglib.h
    |   |       jquant1.c
    |   |       jquant2.c
    |   |       jutils.c
    |   |       jversion.h
    |   |       README
    |   |       transupp.c
    |   |       transupp.h
    |   |
    |   +---libpng
    |   |       CMakeLists.txt
    |   |       png.c
    |   |       png.h
    |   |       pngconf.h
    |   |       pngerror.c
    |   |       pngget.c
    |   |       pngmem.c
    |   |       pngpread.c
    |   |       pngpriv.h
    |   |       pngread.c
    |   |       pngrio.c
    |   |       pngrtran.c
    |   |       pngrutil.c
    |   |       pngset.c
    |   |       pngtest.c
    |   |       pngtest.png
    |   |       pngtrans.c
    |   |       pngwio.c
    |   |       pngwrite.c
    |   |       pngwtran.c
    |   |       pngwutil.c
    |   |       README
    |   |
    |   +---libtiff
    |   |       CMakeLists.txt
    |   |       t4.h
    |   |       tiff.h
    |   |       tiffconf.h
    |   |       tiffio.h
    |   |       tiffio.hxx
    |   |       tiffiop.h
    |   |       tiffvers.h
    |   |       tif_apple.c
    |   |       tif_aux.c
    |   |       tif_close.c
    |   |       tif_codec.c
    |   |       tif_color.c
    |   |       tif_compress.c
    |   |       tif_config.h
    |   |       tif_dir.c
    |   |       tif_dir.h
    |   |       tif_dirinfo.c
    |   |       tif_dirread.c
    |   |       tif_dirwrite.c
    |   |       tif_dumpmode.c
    |   |       tif_error.c
    |   |       tif_extension.c
    |   |       tif_fax3.c
    |   |       tif_fax3.h
    |   |       tif_fax3sm.c
    |   |       tif_flush.c
    |   |       tif_getimage.c
    |   |       tif_jbig.c
    |   |       tif_jpeg.c
    |   |       tif_luv.c
    |   |       tif_lzw.c
    |   |       tif_next.c
    |   |       tif_ojpeg.c
    |   |       tif_open.c
    |   |       tif_packbits.c
    |   |       tif_pixarlog.c
    |   |       tif_predict.c
    |   |       tif_predict.h
    |   |       tif_print.c
    |   |       tif_read.c
    |   |       tif_stream.cxx
    |   |       tif_strip.c
    |   |       tif_swab.c
    |   |       tif_thunder.c
    |   |       tif_tile.c
    |   |       tif_unix.c
    |   |       tif_version.c
    |   |       tif_warning.c
    |   |       tif_win32.c
    |   |       tif_write.c
    |   |       tif_zip.c
    |   |       uvcode.h
    |   |
    |   \---zlib
    |           .cvsignore
    |           adler32.c
    |           CMakeLists.txt
    |           compress.c
    |           crc32.c
    |           crc32.h
    |           deflate.c
    |           deflate.h
    |           gzclose.c
    |           gzguts.h
    |           gzlib.c
    |           gzread.c
    |           gzwrite.c
    |           infback.c
    |           inffast.c
    |           inffast.h
    |           inffixed.h
    |           inflate.c
    |           inflate.h
    |           inftrees.c
    |           inftrees.h
    |           README
    |           trees.c
    |           trees.h
    |           uncompr.c
    |           zconf.h
    |           zlib.h
    |           zutil.c
    |           zutil.h
    |
    +---android
    |   |   android.toolchain.cmake
    |   |   CMakeCache.android.initial.cmake
    |   |   README.android
    |   |
    |   +---android-opencv
    |   |   |   AndroidManifest.xml
    |   |   |   AndroidOpenCVConfig.cmake.in
    |   |   |   CMakeLists.txt
    |   |   |   cmake_android.cmd
    |   |   |   cmake_android.sh
    |   |   |   cmake_android_neon.sh
    |   |   |   default.properties
    |   |   |   project_create.sh
    |   |   |   README.txt
    |   |   |
    |   |   +---jni
    |   |   |   |   android-cv-typemaps.i
    |   |   |   |   android-cv.i
    |   |   |   |   buffers.i
    |   |   |   |   Calibration.cpp
    |   |   |   |   Calibration.i
    |   |   |   |   CMakeLists.txt
    |   |   |   |   cv.i
    |   |   |   |   glcamera.i
    |   |   |   |   gl_code.cpp
    |   |   |   |   image_pool.cpp
    |   |   |   |   image_pool.i
    |   |   |   |   nocopy.i
    |   |   |   |   yuv2rgb16tab.c
    |   |   |   |   yuv2rgb_neon.c
    |   |   |   |   yuv420rgb888.s
    |   |   |   |   yuv420rgb888c.c
    |   |   |   |   yuv420sp2rgb.c
    |   |   |   |
    |   |   |   \---include
    |   |   |           android_logger.h
    |   |   |           Calibration.h
    |   |   |           glcamera.h
    |   |   |           image_pool.h
    |   |   |           yuv2rgb.h
    |   |   |           yuv420sp2rgb.h
    |   |   |
    |   |   +---res
    |   |   |   +---drawable-mdpi
    |   |   |   |       cameraback.jpg
    |   |   |   |
    |   |   |   +---layout
    |   |   |   |       calibrationviewer.xml
    |   |   |   |       camera.xml
    |   |   |   |       camerasettings.xml
    |   |   |   |       chesssizer.xml
    |   |   |   |
    |   |   |   \---values
    |   |   |           attrs.xml
    |   |   |           chessnumbers.xml
    |   |   |           settingnumbers.xml
    |   |   |           strings.xml
    |   |   |
    |   |   \---src
    |   |       \---com
    |   |           \---opencv
    |   |               |   OpenCV.java
    |   |               |
    |   |               +---calibration
    |   |               |   |   CalibrationViewer.java
    |   |               |   |   Calibrator.java
    |   |               |   |   ChessBoardChooser.java
    |   |               |   |
    |   |               |   \---services
    |   |               |           CalibrationService.java
    |   |               |
    |   |               +---camera
    |   |               |       CameraActivity.java
    |   |               |       CameraButtonsHandler.java
    |   |               |       CameraConfig.java
    |   |               |       NativePreviewer.java
    |   |               |       NativeProcessor.java
    |   |               |
    |   |               +---opengl
    |   |               |       GL2CameraViewer.java
    |   |               |
    |   |               \---utils
    |   |                       BitmapBridge.java
    |   |
    |   +---apps
    |   |   +---Calibration
    |   |   |   |   AndroidManifest.xml
    |   |   |   |   default.properties
    |   |   |   |   project_create.sh
    |   |   |   |   README.txt
    |   |   |   |
    |   |   |   +---artwork
    |   |   |   |       icon.xcf
    |   |   |   |
    |   |   |   +---res
    |   |   |   |   +---drawable-hdpi
    |   |   |   |   |       icon.png
    |   |   |   |   |
    |   |   |   |   +---drawable-ldpi
    |   |   |   |   |       icon.png
    |   |   |   |   |
    |   |   |   |   +---drawable-mdpi
    |   |   |   |   |       cameraback.jpg
    |   |   |   |   |       icon.png
    |   |   |   |   |       patternicon.png
    |   |   |   |   |
    |   |   |   |   +---layout
    |   |   |   |   |       calib_camera.xml
    |   |   |   |   |
    |   |   |   |   +---menu
    |   |   |   |   |       calibrationmenu.xml
    |   |   |   |   |
    |   |   |   |   \---values
    |   |   |   |           color.xml
    |   |   |   |           strings.xml
    |   |   |   |
    |   |   |   \---src
    |   |   |       \---com
    |   |   |           \---opencv
    |   |   |               +---calibration
    |   |   |               |       Calibration.java
    |   |   |               |
    |   |   |               \---misc
    |   |   |                       SDCardChecker.java
    |   |   |
    |   |   +---camera_template
    |   |   |   |   AndroidManifest.xml
    |   |   |   |   build.sh
    |   |   |   |   clean.sh
    |   |   |   |   default.properties
    |   |   |   |   Makefile
    |   |   |   |   README.txt
    |   |   |   |   sample.local.env.mk
    |   |   |   |
    |   |   |   +---jni
    |   |   |   |       Android.mk
    |   |   |   |       Application.mk
    |   |   |   |       foobar.i
    |   |   |   |       TestBar.cpp
    |   |   |   |       TestBar.h
    |   |   |   |
    |   |   |   +---res
    |   |   |   |   +---drawable-hdpi
    |   |   |   |   |       icon.png
    |   |   |   |   |
    |   |   |   |   +---drawable-ldpi
    |   |   |   |   |       icon.png
    |   |   |   |   |
    |   |   |   |   +---drawable-mdpi
    |   |   |   |   |       icon.png
    |   |   |   |   |
    |   |   |   |   \---values
    |   |   |   |           strings.xml
    |   |   |   |
    |   |   |   \---src
    |   |   |       \---com
    |   |   |           \---foo
    |   |   |               \---bar
    |   |   |                       FooBar.java
    |   |   |
    |   |   +---CVCamera
    |   |   |   |   AndroidManifest.xml
    |   |   |   |   CMakeLists.txt
    |   |   |   |   default.properties
    |   |   |   |   project_create.sh
    |   |   |   |   README.txt
    |   |   |   |   uninstall.phone.sh
    |   |   |   |
    |   |   |   +---jni
    |   |   |   |       CMakeLists.txt
    |   |   |   |       cvcamera.i
    |   |   |   |       Processor.cpp
    |   |   |   |       Processor.h
    |   |   |   |       Processor.i
    |   |   |   |
    |   |   |   +---res
    |   |   |   |   +---drawable-hdpi
    |   |   |   |   |       icon.png
    |   |   |   |   |
    |   |   |   |   +---drawable-ldpi
    |   |   |   |   |       icon.png
    |   |   |   |   |
    |   |   |   |   +---drawable-mdpi
    |   |   |   |   |       icon.png
    |   |   |   |   |
    |   |   |   |   +---layout
    |   |   |   |   |       main.xml
    |   |   |   |   |
    |   |   |   |   \---values
    |   |   |   |           strings.xml
    |   |   |   |
    |   |   |   \---src
    |   |   |       \---com
    |   |   |           \---theveganrobot
    |   |   |               \---cvcamera
    |   |   |                       CVCamera.java
    |   |   |
    |   |   +---HelloAndroid
    |   |   |       CMakeLists.txt
    |   |   |       cmake_android.cmd
    |   |   |       cmake_android.sh
    |   |   |       main.cpp
    |   |   |       run.cmd
    |   |   |       run.sh
    |   |   |
    |   |   \---OpenCV_SAMPLE
    |   |       |   AndroidManifest.xml
    |   |       |   CMakeLists.txt
    |   |       |   cmake_android.cmd
    |   |       |   cmake_android_neon.sh
    |   |       |   default.properties
    |   |       |   project_create.sh
    |   |       |
    |   |       +---jni
    |   |       |       CMakeLists.txt
    |   |       |       cvsample.cpp
    |   |       |       cvsample.h
    |   |       |       OpenCV_SAMPLE.i
    |   |       |
    |   |       +---res
    |   |       |   +---drawable-hdpi
    |   |       |   |       icon.png
    |   |       |   |
    |   |       |   +---drawable-ldpi
    |   |       |   |       icon.png
    |   |       |   |
    |   |       |   +---drawable-mdpi
    |   |       |   |       icon.png
    |   |       |   |
    |   |       |   +---layout
    |   |       |   |       main.xml
    |   |       |   |
    |   |       |   +---menu
    |   |       |   |       sample_menu.xml
    |   |       |   |
    |   |       |   \---values
    |   |       |           strings.xml
    |   |       |
    |   |       \---src
    |   |           \---com
    |   |               \---OpenCV_SAMPLE
    |   |                       OpenCV_SAMPLE.java
    |   |
    |   \---scripts
    |           build.cmd
    |           cmake_android.cmd
    |           cmake_android.sh
    |           cmake_android_armeabi.sh
    |           cmake_android_neon.sh
    |           wincfg.cmd.tmpl
    |
    +---data
    |   |   CMakeLists.txt
    |   |   readme.txt
    |   |
    |   +---haarcascades
    |   |       haarcascade_eye.xml
    |   |       haarcascade_eye_tree_eyeglasses.xml
    |   |       haarcascade_frontalface_alt.xml
    |   |       haarcascade_frontalface_alt2.xml
    |   |       haarcascade_frontalface_alt_tree.xml
    |   |       haarcascade_frontalface_default.xml
    |   |       haarcascade_fullbody.xml
    |   |       haarcascade_lefteye_2splits.xml
    |   |       haarcascade_lowerbody.xml
    |   |       haarcascade_mcs_eyepair_big.xml
    |   |       haarcascade_mcs_eyepair_small.xml
    |   |       haarcascade_mcs_lefteye.xml
    |   |       haarcascade_mcs_mouth.xml
    |   |       haarcascade_mcs_nose.xml
    |   |       haarcascade_mcs_righteye.xml
    |   |       haarcascade_mcs_upperbody.xml
    |   |       haarcascade_profileface.xml
    |   |       haarcascade_righteye_2splits.xml
    |   |       haarcascade_upperbody.xml
    |   |
    |   \---lbpcascades
    |           lbpcascade_frontalface.xml
    |
    +---doc
    |   |   acircles_pattern.png
    |   |   check_docs.py
    |   |   check_docs_whitelist.txt
    |   |   CMakeLists.txt
    |   |   conf.py
    |   |   Doxyfile.in
    |   |   haartraining.htm
    |   |   license.txt
    |   |   mymath.sty
    |   |   ocv.py
    |   |   opencv-logo.png
    |   |   opencv-logo2.png
    |   |   opencv.bib
    |   |   opencv.ico
    |   |   opencv.jpg
    |   |   opencv2refman.pdf
    |   |   opencv_cheatsheet.pdf
    |   |   opencv_cheatsheet.tex
    |   |   opencv_tutorials.pdf
    |   |   opencv_user.pdf
    |   |   packaging.txt
    |   |   pattern.png
    |   |   reformat.py
    |   |
    |   +---pattern_tools
    |   |       gen_pattern.py
    |   |       README.txt
    |   |       svgfig.py
    |   |
    |   +---tutorials
    |   |   |   tutorials.rst
    |   |   |
    |   |   +---calib3d
    |   |   |   \---table_of_content_calib3d
    |   |   |           table_of_content_calib3d.rst
    |   |   |
    |   |   +---core
    |   |   |   +---adding_images
    |   |   |   |   |   adding_images.rst
    |   |   |   |   |
    |   |   |   |   \---images
    |   |   |   |           Adding_Images_Tutorial_Result_0.png
    |   |   |   |
    |   |   |   +---basic_geometric_drawing
    |   |   |   |   |   basic_geometric_drawing.rst
    |   |   |   |   |
    |   |   |   |   \---images
    |   |   |   |           Drawing_1_Tutorial_Result_0.png
    |   |   |   |           Drawing_1_Tutorial_Result_0a.png
    |   |   |   |           Drawing_1_Tutorial_Result_0b.png
    |   |   |   |
    |   |   |   +---basic_linear_transform
    |   |   |   |   |   basic_linear_transform.rst
    |   |   |   |   |
    |   |   |   |   \---images
    |   |   |   |           Basic_Linear_Transform_a.png
    |   |   |   |           Basic_Linear_Transform_b.png
    |   |   |   |           Basic_Linear_Transform_Tutorial_Result_0.png
    |   |   |   |
    |   |   |   +---random_generator_and_text
    |   |   |   |   |   random_generator_and_text.rst
    |   |   |   |   |
    |   |   |   |   \---images
    |   |   |   |           Drawing_2_Tutorial_Result_0.png
    |   |   |   |           Drawing_2_Tutorial_Result_1.png
    |   |   |   |           Drawing_2_Tutorial_Result_2.png
    |   |   |   |           Drawing_2_Tutorial_Result_3.png
    |   |   |   |           Drawing_2_Tutorial_Result_4.png
    |   |   |   |           Drawing_2_Tutorial_Result_5.png
    |   |   |   |           Drawing_2_Tutorial_Result_6.png
    |   |   |   |           Drawing_2_Tutorial_Result_7.png
    |   |   |   |
    |   |   |   \---table_of_content_core
    |   |   |       |   table_of_content_core.rst
    |   |   |       |
    |   |   |       \---images
    |   |   |               Adding_Images_Tutorial_Result_0.png
    |   |   |               Basic_Linear_Transform_Tutorial_Result_0.png
    |   |   |               Drawing_1_Tutorial_Result_0.png
    |   |   |               Drawing_2_Tutorial_Result_7.png
    |   |   |               Morphology_1_Tutorial_Cover.png
    |   |   |               Smoothing_Tutorial_Cover.png
    |   |   |
    |   |   +---definitions
    |   |   |       noContent.rst
    |   |   |       README.txt
    |   |   |
    |   |   +---features2d
    |   |   |   \---table_of_content_features2d
    |   |   |           table_of_content_features2d.rst
    |   |   |
    |   |   +---general
    |   |   |   \---table_of_content_general
    |   |   |           table_of_content_general.rst
    |   |   |
    |   |   +---gpu
    |   |   |   \---table_of_content_gpu
    |   |   |           table_of_content_gpu.rst
    |   |   |
    |   |   +---highgui
    |   |   |   +---table_of_content_highgui
    |   |   |   |   |   table_of_content_highgui.rst
    |   |   |   |   |
    |   |   |   |   \---images
    |   |   |   |           Adding_Trackbars_Tutorial_Cover.png
    |   |   |   |
    |   |   |   \---trackbar
    |   |   |       |   trackbar.rst
    |   |   |       |
    |   |   |       \---images
    |   |   |               Adding_Trackbars_Tutorial_Cover.png
    |   |   |               Adding_Trackbars_Tutorial_Result_0.png
    |   |   |               Adding_Trackbars_Tutorial_Result_1.png
    |   |   |               Adding_Trackbars_Tutorial_Result_1a.png
    |   |   |               Adding_Trackbars_Tutorial_Result_1b.png
    |   |   |               Adding_Trackbars_Tutorial_Trackbar.png
    |   |   |
    |   |   +---images
    |   |   |       calib3d.png
    |   |   |       core.png
    |   |   |       feature2D.png
    |   |   |       general.png
    |   |   |       gpu.png
    |   |   |       highgui.png
    |   |   |       imgproc.png
    |   |   |       introduction.png
    |   |   |       ml.png
    |   |   |       objdetect.png
    |   |   |       video.png
    |   |   |
    |   |   +---imgproc
    |   |   |   +---erosion_dilatation
    |   |   |   |   |   erosion_dilatation.rst
    |   |   |   |   |
    |   |   |   |   \---images
    |   |   |   |           Morphology_1_Tutorial_Cover.png
    |   |   |   |           Morphology_1_Tutorial_Dilation_Result.png
    |   |   |   |           Morphology_1_Tutorial_Erosion_Result.png
    |   |   |   |           Morphology_1_Tutorial_Original_Image.png
    |   |   |   |           Morphology_1_Tutorial_Theory_Dilation.png
    |   |   |   |           Morphology_1_Tutorial_Theory_Erosion.png
    |   |   |   |           Morphology_1_Tutorial_Theory_Original_Image.png
    |   |   |   |
    |   |   |   +---gausian_median_blur_bilateral_filter
    |   |   |   |   |   gausian_median_blur_bilateral_filter.rst
    |   |   |   |   |
    |   |   |   |   \---images
    |   |   |   |           Smoothing_Tutorial_Cover.png
    |   |   |   |           Smoothing_Tutorial_Result_Median_Filter.png
    |   |   |   |           Smoothing_Tutorial_theory_gaussian_0.jpg
    |   |   |   |
    |   |   |   +---imgtrans
    |   |   |   |   +---canny_detector
    |   |   |   |   |   |   canny_detector.rst
    |   |   |   |   |   |
    |   |   |   |   |   \---images
    |   |   |   |   |           Canny_Detector_Tutorial_Original_Image.jpg
    |   |   |   |   |           Canny_Detector_Tutorial_Result.jpg
    |   |   |   |   |
    |   |   |   |   +---copyMakeBorder
    |   |   |   |   |   |   copyMakeBorder.rst
    |   |   |   |   |   |
    |   |   |   |   |   \---images
    |   |   |   |   |           CopyMakeBorder_Tutorial_Results.jpg
    |   |   |   |   |
    |   |   |   |   +---filter_2d
    |   |   |   |   |   |   filter_2d.rst
    |   |   |   |   |   |
    |   |   |   |   |   \---images
    |   |   |   |   |           filter_2d_tutorial_kernel_theory.png
    |   |   |   |   |           filter_2d_tutorial_result.png
    |   |   |   |   |
    |   |   |   |   +---hough_circle
    |   |   |   |   |   |   hough_circle.rst
    |   |   |   |   |   |
    |   |   |   |   |   \---images
    |   |   |   |   |           Hough_Circle_Tutorial_Result.jpg
    |   |   |   |   |           Hough_Circle_Tutorial_Theory_0.jpg
    |   |   |   |   |
    |   |   |   |   +---hough_lines
    |   |   |   |   |   |   hough_lines.rst
    |   |   |   |   |   |
    |   |   |   |   |   \---images
    |   |   |   |   |           Hough_Lines_Tutorial_Original_Image.jpg
    |   |   |   |   |           Hough_Lines_Tutorial_Result.jpg
    |   |   |   |   |           Hough_Lines_Tutorial_Theory_0.jpg
    |   |   |   |   |           Hough_Lines_Tutorial_Theory_1.jpg
    |   |   |   |   |           Hough_Lines_Tutorial_Theory_2.jpg
    |   |   |   |   |
    |   |   |   |   +---laplace_operator
    |   |   |   |   |   |   laplace_operator.rst
    |   |   |   |   |   |
    |   |   |   |   |   \---images
    |   |   |   |   |           Laplace_Operator_Tutorial_Original_Image.jpg
    |   |   |   |   |           Laplace_Operator_Tutorial_Result.jpg
    |   |   |   |   |           Laplace_Operator_Tutorial_Theory_ddIntensity.jpg
    |   |   |   |   |           Laplace_Operator_Tutorial_Theory_Previous.jpg
    |   |   |   |   |
    |   |   |   |   \---sobel_derivatives
    |   |   |   |       |   sobel_derivatives.rst
    |   |   |   |       |
    |   |   |   |       \---images
    |   |   |   |               Sobel_Derivatives_Tutorial_Result.jpg
    |   |   |   |               Sobel_Derivatives_Tutorial_Theory_0.jpg
    |   |   |   |               Sobel_Derivatives_Tutorial_Theory_ddIntensity_Function.jpg
    |   |   |   |               Sobel_Derivatives_Tutorial_Theory_dIntensity_Function.jpg
    |   |   |   |               Sobel_Derivatives_Tutorial_Theory_Intensity_Function.jpg
    |   |   |   |
    |   |   |   +---opening_closing_hats
    |   |   |   |   |   opening_closing_hats.rst
    |   |   |   |   |
    |   |   |   |   \---images
    |   |   |   |           Morphology_2_Tutorial_Cover.png
    |   |   |   |           Morphology_2_Tutorial_Original_Image.jpg
    |   |   |   |           Morphology_2_Tutorial_Theory_BlackHat.png
    |   |   |   |           Morphology_2_Tutorial_Theory_Closing.png
    |   |   |   |           Morphology_2_Tutorial_Theory_Gradient.png
    |   |   |   |           Morphology_2_Tutorial_Theory_Opening.png
    |   |   |   |           Morphology_2_Tutorial_Theory_TopHat.png
    |   |   |   |
    |   |   |   +---pyramids
    |   |   |   |   |   pyramids.rst
    |   |   |   |   |
    |   |   |   |   \---images
    |   |   |   |           Pyramids_Tutorial_Cover.png
    |   |   |   |           Pyramids_Tutorial_Original_Image.png
    |   |   |   |           Pyramids_Tutorial_Pyramid_Theory.png
    |   |   |   |           Pyramids_Tutorial_PyrDown_Result.png
    |   |   |   |           Pyramids_Tutorial_PyrUp_Result.png
    |   |   |   |
    |   |   |   +---table_of_content_imgproc
    |   |   |   |   |   table_of_content_imgproc.rst
    |   |   |   |   |
    |   |   |   |   \---images
    |   |   |   |       |   Morphology_1_Tutorial_Cover.png
    |   |   |   |       |   Morphology_2_Tutorial_Cover.png
    |   |   |   |       |   Pyramids_Tutorial_Cover.png
    |   |   |   |       |   Smoothing_Tutorial_Cover.png
    |   |   |   |       |   Threshold_Tutorial_Cover.png
    |   |   |   |       |
    |   |   |   |       \---imgtrans
    |   |   |   |               Canny_Detector_Tutorial_Cover.jpg
    |   |   |   |               CopyMakeBorder_Tutorial_Cover.jpg
    |   |   |   |               Filter_2D_Tutorial_Cover.jpg
    |   |   |   |               Hough_Circle_Tutorial_Cover.jpg
    |   |   |   |               Hough_Lines_Tutorial_Cover.jpg
    |   |   |   |               Laplace_Operator_Tutorial_Cover.jpg
    |   |   |   |               Sobel_Derivatives_Tutorial_Cover.jpg
    |   |   |   |
    |   |   |   \---threshold
    |   |   |       |   threshold.rst
    |   |   |       |
    |   |   |       \---images
    |   |   |               Threshold_Tutorial_Cover.png
    |   |   |               Threshold_Tutorial_Original_Image.png
    |   |   |               Threshold_Tutorial_Result_Binary_Inverted.png
    |   |   |               Threshold_Tutorial_Result_Zero.png
    |   |   |               Threshold_Tutorial_Theory_Base_Figure.png
    |   |   |               Threshold_Tutorial_Theory_Binary.png
    |   |   |               Threshold_Tutorial_Theory_Binary_Inverted.png
    |   |   |               Threshold_Tutorial_Theory_Example.png
    |   |   |               Threshold_Tutorial_Theory_Truncate.png
    |   |   |               Threshold_Tutorial_Theory_Zero.png
    |   |   |               Threshold_Tutorial_Theory_Zero_Inverted.png
    |   |   |
    |   |   +---introduction
    |   |   |   +---display_image
    |   |   |   |   |   display_image.rst
    |   |   |   |   |
    |   |   |   |   \---images
    |   |   |   |           Display_Image_Tutorial_Result.png
    |   |   |   |
    |   |   |   +---linux_eclipse
    |   |   |   |   |   linux_eclipse.rst
    |   |   |   |   |
    |   |   |   |   \---images
    |   |   |   |           eclipse_cpp_logo.jpeg
    |   |   |   |           Eclipse_Tutorial_Screenshot-0.png
    |   |   |   |           Eclipse_Tutorial_Screenshot-1.png
    |   |   |   |           Eclipse_Tutorial_Screenshot-10.png
    |   |   |   |           Eclipse_Tutorial_Screenshot-11.png
    |   |   |   |           Eclipse_Tutorial_Screenshot-12.png
    |   |   |   |           Eclipse_Tutorial_Screenshot-13.png
    |   |   |   |           Eclipse_Tutorial_Screenshot-14.png
    |   |   |   |           Eclipse_Tutorial_Screenshot-15.png
    |   |   |   |           Eclipse_Tutorial_Screenshot-2.png
    |   |   |   |           Eclipse_Tutorial_Screenshot-3.png
    |   |   |   |           Eclipse_Tutorial_Screenshot-4.png
    |   |   |   |           Eclipse_Tutorial_Screenshot-5.png
    |   |   |   |           Eclipse_Tutorial_Screenshot-6.png
    |   |   |   |           Eclipse_Tutorial_Screenshot-7.png
    |   |   |   |           Eclipse_Tutorial_Screenshot-8.png
    |   |   |   |           Eclipse_Tutorial_Screenshot-9.png
    |   |   |   |
    |   |   |   +---linux_gcc_cmake
    |   |   |   |   |   linux_gcc_cmake.rst
    |   |   |   |   |
    |   |   |   |   \---images
    |   |   |   |           gccegg-65.png
    |   |   |   |           GCC_CMake_Example_Tutorial.png
    |   |   |   |
    |   |   |   +---linux_install
    |   |   |   |   |   linux_install.rst
    |   |   |   |   |
    |   |   |   |   \---images
    |   |   |   |           ubuntu_logo.jpeg
    |   |   |   |
    |   |   |   +---load_save_image
    |   |   |   |   |   load_save_image.rst
    |   |   |   |   |
    |   |   |   |   \---images
    |   |   |   |           Load_Save_Image_Result_1.png
    |   |   |   |           Load_Save_Image_Result_2.png
    |   |   |   |           Load_Save_Image_Result_a.png
    |   |   |   |           Load_Save_Image_Result_b.png
    |   |   |   |
    |   |   |   +---table_of_content_introduction
    |   |   |   |   |   table_of_content_introduction.rst
    |   |   |   |   |
    |   |   |   |   \---images
    |   |   |   |           Display_Image_Tutorial_Result.png
    |   |   |   |           eclipse_cpp_logo.jpeg
    |   |   |   |           gccegg-65.png
    |   |   |   |           Load_Save_Image_Result_1.png
    |   |   |   |           ubuntu_logo.jpeg
    |   |   |   |           windows_logo.jpg
    |   |   |   |
    |   |   |   \---windows_install
    |   |   |       |   windows_install.rst
    |   |   |       |
    |   |   |       \---images
    |   |   |               windows_logo.jpg
    |   |   |
    |   |   +---ml
    |   |   |   \---table_of_content_ml
    |   |   |           table_of_content_ml.rst
    |   |   |
    |   |   +---objdetect
    |   |   |   \---table_of_content_objdetect
    |   |   |           table_of_content_objdetect.rst
    |   |   |
    |   |   \---video
    |   |       \---table_of_content_video
    |   |               table_of_content_video.rst
    |   |
    |   +---user_guide
    |   |       ug_features2d.rst
    |   |       ug_highgui.rst
    |   |       ug_mat.rst
    |   |       user_guide.rst
    |   |
    |   +---vidsurv
    |   |       Blob_Tracking_Modules.doc
    |   |       Blob_Tracking_Tests.doc
    |   |       TestSeq.doc
    |   |
    |   +---_static
    |   |       insertIframe.js
    |   |
    |   \---_themes
    |       \---blue
    |           |   layout.html
    |           |   theme.conf
    |           |
    |           \---static
    |                   default.css_t
    |
    +---include
    |   |   CMakeLists.txt
    |   |
    |   +---opencv
    |   |       cv.h
    |   |       cv.hpp
    |   |       cvaux.h
    |   |       cvaux.hpp
    |   |       cvwimage.h
    |   |       cxcore.h
    |   |       cxcore.hpp
    |   |       cxeigen.hpp
    |   |       cxmisc.h
    |   |       highgui.h
    |   |       ml.h
    |   |
    |   \---opencv2
    |           opencv.hpp
    |
    +---modules
    |   |   CMakeLists.txt
    |   |   refman.rst
    |   |
    |   +---androidcamera
    |   |   |   CMakeLists.txt
    |   |   |
    |   |   +---camera_wrapper
    |   |   |       camera_wrapper.cpp
    |   |   |       camera_wrapper.h
    |   |   |       CMakeLists.txt
    |   |   |
    |   |   +---include
    |   |   |       camera_activity.hpp
    |   |   |       camera_properties.h
    |   |   |
    |   |   \---src
    |   |           camera_activity.cpp
    |   |
    |   +---calib3d
    |   |   |   CMakeLists.txt
    |   |   |
    |   |   +---doc
    |   |   |   |   calib3d.rst
    |   |   |   |   camera_calibration_and_3d_reconstruction.rst
    |   |   |   |
    |   |   |   \---pics
    |   |   |           stereo_undistort.jpg
    |   |   |
    |   |   +---include
    |   |   |   \---opencv2
    |   |   |       \---calib3d
    |   |   |               calib3d.hpp
    |   |   |
    |   |   +---src
    |   |   |       calibinit.cpp
    |   |   |       calibration.cpp
    |   |   |       checkchessboard.cpp
    |   |   |       circlesgrid.cpp
    |   |   |       circlesgrid.hpp
    |   |   |       fundam.cpp
    |   |   |       modelest.cpp
    |   |   |       posit.cpp
    |   |   |       precomp.cpp
    |   |   |       precomp.hpp
    |   |   |       quadsubpix.cpp
    |   |   |       solvepnp.cpp
    |   |   |       stereobm.cpp
    |   |   |       stereogc.cpp
    |   |   |       stereosgbm.cpp
    |   |   |       triangulate.cpp
    |   |   |       _modelest.h
    |   |   |
    |   |   \---test
    |   |           test_affine3d_estimator.cpp
    |   |           test_cameracalibration.cpp
    |   |           test_cameracalibration_artificial.cpp
    |   |           test_cameracalibration_badarg.cpp
    |   |           test_chessboardgenerator.cpp
    |   |           test_chessboardgenerator.hpp
    |   |           test_chesscorners.cpp
    |   |           test_chesscorners_badarg.cpp
    |   |           test_chesscorners_timing.cpp
    |   |           test_compose_rt.cpp
    |   |           test_cornerssubpix.cpp
    |   |           test_fundam.cpp
    |   |           test_main.cpp
    |   |           test_posit.cpp
    |   |           test_precomp.cpp
    |   |           test_precomp.hpp
    |   |           test_reproject_image_to_3d.cpp
    |   |           test_solvepnp_ransac.cpp
    |   |           test_stereomatching.cpp
    |   |           test_undistort.cpp
    |   |           test_undistort_badarg.cpp
    |   |
    |   +---contrib
    |   |   |   CMakeLists.txt
    |   |   |
    |   |   +---include
    |   |   |   \---opencv2
    |   |   |       \---contrib
    |   |   |               contrib.hpp
    |   |   |
    |   |   \---src
    |   |           adaptiveskindetector.cpp
    |   |           ba.cpp
    |   |           chamfermatching.cpp
    |   |           fuzzymeanshifttracker.cpp
    |   |           octree.cpp
    |   |           polyfit.cpp
    |   |           precomp.cpp
    |   |           precomp.hpp
    |   |           selfsimilarity.cpp
    |   |           spinimages.cpp
    |   |           stereovar.cpp
    |   |
    |   +---core
    |   |   |   CMakeLists.txt
    |   |   |
    |   |   +---doc
    |   |   |   |   basic_structures.rst
    |   |   |   |   clustering.rst
    |   |   |   |   core.rst
    |   |   |   |   drawing_functions.rst
    |   |   |   |   dynamic_structures.rst
    |   |   |   |   intro.rst
    |   |   |   |   old_basic_structures.rst
    |   |   |   |   old_xml_yaml_persistence.rst
    |   |   |   |   operations_on_arrays.rst
    |   |   |   |   utility_and_system_functions_and_macros.rst
    |   |   |   |   xml_yaml_persistence.rst
    |   |   |   |
    |   |   |   \---pics
    |   |   |           ellipse.png
    |   |   |           memstorage1.png
    |   |   |           memstorage2.png
    |   |   |
    |   |   +---include
    |   |   |   \---opencv2
    |   |   |       \---core
    |   |   |               core.hpp
    |   |   |               core_c.h
    |   |   |               eigen.hpp
    |   |   |               internal.hpp
    |   |   |               mat.hpp
    |   |   |               operations.hpp
    |   |   |               types_c.h
    |   |   |               version.hpp
    |   |   |               wimage.hpp
    |   |   |
    |   |   +---src
    |   |   |       alloc.cpp
    |   |   |       arithm.cpp
    |   |   |       array.cpp
    |   |   |       cmdparser.cpp
    |   |   |       convert.cpp
    |   |   |       copy.cpp
    |   |   |       datastructs.cpp
    |   |   |       drawing.cpp
    |   |   |       dxt.cpp
    |   |   |       lapack.cpp
    |   |   |       mathfuncs.cpp
    |   |   |       matmul.cpp
    |   |   |       matop.cpp
    |   |   |       matrix.cpp
    |   |   |       out.cpp
    |   |   |       persistence.cpp
    |   |   |       precomp.cpp
    |   |   |       precomp.hpp
    |   |   |       rand.cpp
    |   |   |       stat.cpp
    |   |   |       system.cpp
    |   |   |       tables.cpp
    |   |   |
    |   |   \---test
    |   |           test_arithm.cpp
    |   |           test_ds.cpp
    |   |           test_dxt.cpp
    |   |           test_io.cpp
    |   |           test_main.cpp
    |   |           test_mat.cpp
    |   |           test_math.cpp
    |   |           test_operations.cpp
    |   |           test_precomp.cpp
    |   |           test_precomp.hpp
    |   |           test_rand.cpp
    |   |
    |   +---features2d
    |   |   |   CMakeLists.txt
    |   |   |
    |   |   +---doc
    |   |   |       common_interfaces_of_descriptor_extractors.rst
    |   |   |       common_interfaces_of_descriptor_matchers.rst
    |   |   |       common_interfaces_of_feature_detectors.rst
    |   |   |       common_interfaces_of_generic_descriptor_matchers.rst
    |   |   |       drawing_function_of_keypoints_and_matches.rst
    |   |   |       features2d.rst
    |   |   |       feature_detection_and_description.rst
    |   |   |       object_categorization.rst
    |   |   |
    |   |   +---include
    |   |   |   \---opencv2
    |   |   |       \---features2d
    |   |   |               features2d.hpp
    |   |   |
    |   |   +---src
    |   |   |       bagofwords.cpp
    |   |   |       blobdetector.cpp
    |   |   |       brief.cpp
    |   |   |       calonder.cpp
    |   |   |       descriptors.cpp
    |   |   |       detectors.cpp
    |   |   |       draw.cpp
    |   |   |       dynamic.cpp
    |   |   |       evaluation.cpp
    |   |   |       fast.cpp
    |   |   |       generated_16.i
    |   |   |       generated_32.i
    |   |   |       generated_64.i
    |   |   |       keypoint.cpp
    |   |   |       matchers.cpp
    |   |   |       mser.cpp
    |   |   |       oneway.cpp
    |   |   |       orb.cpp
    |   |   |       orb_pattern.hpp
    |   |   |       planardetect.cpp
    |   |   |       precomp.cpp
    |   |   |       precomp.hpp
    |   |   |       sift.cpp
    |   |   |       stardetector.cpp
    |   |   |       surf.cpp
    |   |   |       test_pairs.txt
    |   |   |
    |   |   \---test
    |   |           test_bruteforcematcher.cpp
    |   |           test_detectors.cpp
    |   |           test_fast.cpp
    |   |           test_features2d.cpp
    |   |           test_main.cpp
    |   |           test_mser.cpp
    |   |           test_nearestneighbors.cpp
    |   |           test_precomp.cpp
    |   |           test_precomp.hpp
    |   |
    |   +---flann
    |   |   |   CMakeLists.txt
    |   |   |
    |   |   +---include
    |   |   |   \---opencv2
    |   |   |       \---flann
    |   |   |               allocator.h
    |   |   |               all_indices.h
    |   |   |               autotuned_index.h
    |   |   |               composite_index.h
    |   |   |               dist.h
    |   |   |               flann.hpp
    |   |   |               flann_base.hpp
    |   |   |               general.h
    |   |   |               ground_truth.h
    |   |   |               hdf5.h
    |   |   |               heap.h
    |   |   |               index_testing.h
    |   |   |               kdtree_index.h
    |   |   |               kmeans_index.h
    |   |   |               linear_index.h
    |   |   |               logger.h
    |   |   |               matrix.h
    |   |   |               nn_index.h
    |   |   |               object_factory.h
    |   |   |               random.h
    |   |   |               result_set.h
    |   |   |               sampling.h
    |   |   |               saving.h
    |   |   |               simplex_downhill.h
    |   |   |               timer.h
    |   |   |
    |   |   \---src
    |   |           flann.cpp
    |   |           precomp.cpp
    |   |           precomp.hpp
    |   |
    |   +---gpu
    |   |   |   CMakeLists.txt
    |   |   |
    |   |   +---doc
    |   |   |       camera_calibration_and_3d_reconstruction.rst
    |   |   |       data_structures.rst
    |   |   |       feature_detection_and_description.rst
    |   |   |       gpu.rst
    |   |   |       image_filtering.rst
    |   |   |       image_processing.rst
    |   |   |       initalization_and_information.rst
    |   |   |       introduction.rst
    |   |   |       matrix_reductions.rst
    |   |   |       object_detection.rst
    |   |   |       operations_on_matrices.rst
    |   |   |       per_element_operations.rst
    |   |   |
    |   |   +---include
    |   |   |   \---opencv2
    |   |   |       \---gpu
    |   |   |               devmem2d.hpp
    |   |   |               gpu.hpp
    |   |   |               matrix_operations.hpp
    |   |   |               stream_accessor.hpp
    |   |   |
    |   |   +---src
    |   |   |   |   arithm.cpp
    |   |   |   |   bilateral_filter.cpp
    |   |   |   |   blend.cpp
    |   |   |   |   brute_force_matcher.cpp
    |   |   |   |   calib3d.cpp
    |   |   |   |   cascadeclassifier.cpp
    |   |   |   |   color.cpp
    |   |   |   |   cudastream.cpp
    |   |   |   |   element_operations.cpp
    |   |   |   |   error.cpp
    |   |   |   |   filtering.cpp
    |   |   |   |   graphcuts.cpp
    |   |   |   |   hog.cpp
    |   |   |   |   imgproc_gpu.cpp
    |   |   |   |   initialization.cpp
    |   |   |   |   match_template.cpp
    |   |   |   |   matrix_operations.cpp
    |   |   |   |   matrix_reductions.cpp
    |   |   |   |   mssegmentation.cpp
    |   |   |   |   precomp.cpp
    |   |   |   |   precomp.hpp
    |   |   |   |   speckle_filtering.cpp
    |   |   |   |   split_merge.cpp
    |   |   |   |   stereobm.cpp
    |   |   |   |   stereobp.cpp
    |   |   |   |   stereocsbp.cpp
    |   |   |   |   surf.cpp
    |   |   |   |
    |   |   |   +---cuda
    |   |   |   |       blend.cu
    |   |   |   |       brute_force_matcher.cu
    |   |   |   |       calib3d.cu
    |   |   |   |       color.cu
    |   |   |   |       element_operations.cu
    |   |   |   |       filters.cu
    |   |   |   |       hog.cu
    |   |   |   |       imgproc.cu
    |   |   |   |       internal_shared.hpp
    |   |   |   |       match_template.cu
    |   |   |   |       mathfunc.cu
    |   |   |   |       matrix_operations.cu
    |   |   |   |       matrix_reductions.cu
    |   |   |   |       safe_call.hpp
    |   |   |   |       split_merge.cu
    |   |   |   |       stereobm.cu
    |   |   |   |       stereobp.cu
    |   |   |   |       stereocsbp.cu
    |   |   |   |       surf.cu
    |   |   |   |
    |   |   |   +---nvidia
    |   |   |   |   |   NCVHaarObjectDetection.cu
    |   |   |   |   |   NCVHaarObjectDetection.hpp
    |   |   |   |   |
    |   |   |   |   +---core
    |   |   |   |   |       NCV.cu
    |   |   |   |   |       NCV.hpp
    |   |   |   |   |       NCVRuntimeTemplates.hpp
    |   |   |   |   |
    |   |   |   |   \---NPP_staging
    |   |   |   |           NPP_staging.cu
    |   |   |   |           NPP_staging.hpp
    |   |   |   |
    |   |   |   \---opencv2
    |   |   |       \---gpu
    |   |   |           \---device
    |   |   |                   border_interpolate.hpp
    |   |   |                   datamov_utils.hpp
    |   |   |                   dynamic_smem.hpp
    |   |   |                   limits_gpu.hpp
    |   |   |                   saturate_cast.hpp
    |   |   |                   transform.hpp
    |   |   |                   vecmath.hpp
    |   |   |
    |   |   \---test
    |   |       |   test_arithm.cpp
    |   |       |   test_bitwise_oper.cpp
    |   |       |   test_blend.cpp
    |   |       |   test_brute_force_matcher.cpp
    |   |       |   test_calib3d.cpp
    |   |       |   test_dft_routines.cpp
    |   |       |   test_features2d.cpp
    |   |       |   test_filters.cpp
    |   |       |   test_hog.cpp
    |   |       |   test_imgproc_gpu.cpp
    |   |       |   test_main.cpp
    |   |       |   test_match_template.cpp
    |   |       |   test_meanshift.cpp
    |   |       |   test_mssegmentation.cpp
    |   |       |   test_nvidia.cpp
    |   |       |   test_operator_async_call.cpp
    |   |       |   test_operator_convert_to.cpp
    |   |       |   test_operator_copy_to.cpp
    |   |       |   test_operator_set_to.cpp
    |   |       |   test_precomp.cpp
    |   |       |   test_precomp.hpp
    |   |       |   test_split_merge.cpp
    |   |       |   test_stereo_bm.cpp
    |   |       |   test_stereo_bm_async.cpp
    |   |       |   test_stereo_bp.cpp
    |   |       |   test_stereo_csbp.cpp
    |   |       |
    |   |       \---nvidia
    |   |               main_nvidia.cpp
    |   |               NCVAutoTestLister.hpp
    |   |               NCVTest.hpp
    |   |               NCVTestSourceProvider.hpp
    |   |               TestCompact.cpp
    |   |               TestCompact.h
    |   |               TestDrawRects.cpp
    |   |               TestDrawRects.h
    |   |               TestHaarCascadeApplication.cpp
    |   |               TestHaarCascadeApplication.h
    |   |               TestHaarCascadeLoader.cpp
    |   |               TestHaarCascadeLoader.h
    |   |               TestHypothesesFilter.cpp
    |   |               TestHypothesesFilter.h
    |   |               TestHypothesesGrow.cpp
    |   |               TestHypothesesGrow.h
    |   |               TestIntegralImage.cpp
    |   |               TestIntegralImage.h
    |   |               TestIntegralImageSquared.cpp
    |   |               TestIntegralImageSquared.h
    |   |               TestRectStdDev.cpp
    |   |               TestRectStdDev.h
    |   |               TestResize.cpp
    |   |               TestResize.h
    |   |               TestTranspose.cpp
    |   |               TestTranspose.h
    |   |
    |   +---haartraining
    |   |       CMakeLists.txt
    |   |       createsamples.cpp
    |   |       cvboost.cpp
    |   |       cvclassifier.h
    |   |       cvcommon.cpp
    |   |       cvhaarclassifier.cpp
    |   |       cvhaartraining.cpp
    |   |       cvhaartraining.h
    |   |       cvsamples.cpp
    |   |       haartraining.cpp
    |   |       performance.cpp
    |   |       _cvcommon.h
    |   |       _cvhaartraining.h
    |   |
    |   +---highgui
    |   |   |   CMakeLists.txt
    |   |   |
    |   |   +---doc
    |   |   |   |   highgui.rst
    |   |   |   |   qt_new_functions.rst
    |   |   |   |   reading_and_writing_images_and_video.rst
    |   |   |   |   user_interface.rst
    |   |   |   |
    |   |   |   \---pics
    |   |   |           qtgui.png
    |   |   |
    |   |   +---include
    |   |   |   \---opencv2
    |   |   |       \---highgui
    |   |   |               highgui.hpp
    |   |   |               highgui_c.h
    |   |   |
    |   |   +---src
    |   |   |   |   bitstrm.cpp
    |   |   |   |   bitstrm.hpp
    |   |   |   |   cap.cpp
    |   |   |   |   cap_android.cpp
    |   |   |   |   cap_cmu.cpp
    |   |   |   |   cap_dc1394.cpp
    |   |   |   |   cap_dc1394_v2.cpp
    |   |   |   |   cap_dshow.cpp
    |   |   |   |   cap_ffmpeg.cpp
    |   |   |   |   cap_ffmpeg_api.hpp
    |   |   |   |   cap_ffmpeg_impl.hpp
    |   |   |   |   cap_gstreamer.cpp
    |   |   |   |   cap_images.cpp
    |   |   |   |   cap_libv4l.cpp
    |   |   |   |   cap_mil.cpp
    |   |   |   |   cap_openni.cpp
    |   |   |   |   cap_pvapi.cpp
    |   |   |   |   cap_qt.cpp
    |   |   |   |   cap_qtkit.mm
    |   |   |   |   cap_tyzx.cpp
    |   |   |   |   cap_unicap.cpp
    |   |   |   |   cap_v4l.cpp
    |   |   |   |   cap_vfw.cpp
    |   |   |   |   cap_xine.cpp
    |   |   |   |   grfmts.hpp
    |   |   |   |   grfmt_base.cpp
    |   |   |   |   grfmt_base.hpp
    |   |   |   |   grfmt_bmp.cpp
    |   |   |   |   grfmt_bmp.hpp
    |   |   |   |   grfmt_exr.cpp
    |   |   |   |   grfmt_exr.hpp
    |   |   |   |   grfmt_imageio.cpp
    |   |   |   |   grfmt_imageio.hpp
    |   |   |   |   grfmt_jpeg.cpp
    |   |   |   |   grfmt_jpeg.hpp
    |   |   |   |   grfmt_jpeg2000.cpp
    |   |   |   |   grfmt_jpeg2000.hpp
    |   |   |   |   grfmt_png.cpp
    |   |   |   |   grfmt_png.hpp
    |   |   |   |   grfmt_pxm.cpp
    |   |   |   |   grfmt_pxm.hpp
    |   |   |   |   grfmt_sunras.cpp
    |   |   |   |   grfmt_sunras.hpp
    |   |   |   |   grfmt_tiff.cpp
    |   |   |   |   grfmt_tiff.hpp
    |   |   |   |   loadsave.cpp
    |   |   |   |   makeswig.sh
    |   |   |   |   precomp.cpp
    |   |   |   |   precomp.hpp
    |   |   |   |   utils.cpp
    |   |   |   |   utils.hpp
    |   |   |   |   window.cpp
    |   |   |   |   window_carbon.cpp
    |   |   |   |   window_cocoa.mm
    |   |   |   |   window_gtk.cpp
    |   |   |   |   window_QT.cpp
    |   |   |   |   window_QT.h
    |   |   |   |   window_QT.qrc
    |   |   |   |   window_w32.cpp
    |   |   |   |
    |   |   |   \---files_Qt
    |   |   |       |   stylesheet_trackbar.qss
    |   |   |       |
    |   |   |       \---Milky
    |   |   |           |   README.txt
    |   |   |           |
    |   |   |           +---48
    |   |   |           |       1.png
    |   |   |           |       10.png
    |   |   |           |       100.png
    |   |   |           |       101.png
    |   |   |           |       102.png
    |   |   |           |       103.png
    |   |   |           |       104.png
    |   |   |           |       105.png
    |   |   |           |       106.png
    |   |   |           |       107.png
    |   |   |           |       108.png
    |   |   |           |       109.png
    |   |   |           |       11.png
    |   |   |           |       110.png
    |   |   |           |       111.png
    |   |   |           |       112.png
    |   |   |           |       113.png
    |   |   |           |       114.png
    |   |   |           |       115.png
    |   |   |           |       116.png
    |   |   |           |       117.png
    |   |   |           |       118.png
    |   |   |           |       119.png
    |   |   |           |       12.png
    |   |   |           |       120.png
    |   |   |           |       121.png
    |   |   |           |       122.png
    |   |   |           |       123.png
    |   |   |           |       124.png
    |   |   |           |       125.png
    |   |   |           |       126.png
    |   |   |           |       127.png
    |   |   |           |       128.png
    |   |   |           |       129.png
    |   |   |           |       13.png
    |   |   |           |       130.png
    |   |   |           |       131.png
    |   |   |           |       14.png
    |   |   |           |       15.png
    |   |   |           |       16.png
    |   |   |           |       17.png
    |   |   |           |       18.png
    |   |   |           |       19.png
    |   |   |           |       2.png
    |   |   |           |       20.png
    |   |   |           |       21.png
    |   |   |           |       22.png
    |   |   |           |       23.png
    |   |   |           |       24.png
    |   |   |           |       25.png
    |   |   |           |       26.png
    |   |   |           |       27.png
    |   |   |           |       28.png
    |   |   |           |       29.png
    |   |   |           |       3.png
    |   |   |           |       30.png
    |   |   |           |       31.png
    |   |   |           |       32.png
    |   |   |           |       33.png
    |   |   |           |       34.png
    |   |   |           |       35.png
    |   |   |           |       36.png
    |   |   |           |       37.png
    |   |   |           |       38.png
    |   |   |           |       39.png
    |   |   |           |       4.png
    |   |   |           |       40.png
    |   |   |           |       41.png
    |   |   |           |       42.png
    |   |   |           |       43.png
    |   |   |           |       44.png
    |   |   |           |       45.png
    |   |   |           |       46.png
    |   |   |           |       47.png
    |   |   |           |       48.png
    |   |   |           |       49.png
    |   |   |           |       5.png
    |   |   |           |       50.png
    |   |   |           |       51.png
    |   |   |           |       52.png
    |   |   |           |       53.png
    |   |   |           |       54.png
    |   |   |           |       55.png
    |   |   |           |       56.png
    |   |   |           |       57.png
    |   |   |           |       58.png
    |   |   |           |       59.png
    |   |   |           |       6.png
    |   |   |           |       60.png
    |   |   |           |       61.png
    |   |   |           |       62.png
    |   |   |           |       63.png
    |   |   |           |       64.png
    |   |   |           |       65.png
    |   |   |           |       66.png
    |   |   |           |       67.png
    |   |   |           |       68.png
    |   |   |           |       69.png
    |   |   |           |       7.png
    |   |   |           |       70.png
    |   |   |           |       71.png
    |   |   |           |       72.png
    |   |   |           |       73.png
    |   |   |           |       74.png
    |   |   |           |       75.png
    |   |   |           |       76.png
    |   |   |           |       77.png
    |   |   |           |       78.png
    |   |   |           |       79.png
    |   |   |           |       8.png
    |   |   |           |       80.png
    |   |   |           |       81.png
    |   |   |           |       82.png
    |   |   |           |       83.png
    |   |   |           |       84.png
    |   |   |           |       85.png
    |   |   |           |       86.png
    |   |   |           |       87.png
    |   |   |           |       88.png
    |   |   |           |       89.png
    |   |   |           |       9.png
    |   |   |           |       90.png
    |   |   |           |       91.png
    |   |   |           |       92.png
    |   |   |           |       93.png
    |   |   |           |       94.png
    |   |   |           |       95.png
    |   |   |           |       96.png
    |   |   |           |       97.png
    |   |   |           |       98.png
    |   |   |           |       99.png
    |   |   |           |
    |   |   |           \---64
    |   |   |                   1.png
    |   |   |                   10.png
    |   |   |                   100.png
    |   |   |                   101.png
    |   |   |                   102.png
    |   |   |                   103.png
    |   |   |                   104.png
    |   |   |                   105.png
    |   |   |                   106.png
    |   |   |                   107.png
    |   |   |                   108.png
    |   |   |                   109.png
    |   |   |                   11.png
    |   |   |                   110.png
    |   |   |                   111.png
    |   |   |                   112.png
    |   |   |                   113.png
    |   |   |                   114.png
    |   |   |                   115.png
    |   |   |                   116.png
    |   |   |                   117.png
    |   |   |                   118.png
    |   |   |                   119.png
    |   |   |                   12.png
    |   |   |                   120.png
    |   |   |                   121.png
    |   |   |                   122.png
    |   |   |                   123.png
    |   |   |                   124.png
    |   |   |                   125.png
    |   |   |                   126.png
    |   |   |                   127.png
    |   |   |                   128.png
    |   |   |                   129.png
    |   |   |                   13.png
    |   |   |                   130.png
    |   |   |                   131.png
    |   |   |                   14.png
    |   |   |                   15.png
    |   |   |                   16.png
    |   |   |                   17.png
    |   |   |                   18.png
    |   |   |                   19.png
    |   |   |                   2.png
    |   |   |                   20.png
    |   |   |                   21.png
    |   |   |                   22.png
    |   |   |                   23.png
    |   |   |                   24.png
    |   |   |                   25.png
    |   |   |                   26.png
    |   |   |                   27.png
    |   |   |                   28.png
    |   |   |                   29.png
    |   |   |                   3.png
    |   |   |                   30.png
    |   |   |                   31.png
    |   |   |                   32.png
    |   |   |                   33.png
    |   |   |                   34.png
    |   |   |                   35.png
    |   |   |                   36.png
    |   |   |                   37.png
    |   |   |                   38.png
    |   |   |                   39.png
    |   |   |                   4.png
    |   |   |                   40.png
    |   |   |                   41.png
    |   |   |                   42.png
    |   |   |                   43.png
    |   |   |                   44.png
    |   |   |                   45.png
    |   |   |                   46.png
    |   |   |                   47.png
    |   |   |                   48.png
    |   |   |                   49.png
    |   |   |                   5.png
    |   |   |                   50.png
    |   |   |                   51.png
    |   |   |                   52.png
    |   |   |                   53.png
    |   |   |                   54.png
    |   |   |                   55.png
    |   |   |                   56.png
    |   |   |                   57.png
    |   |   |                   58.png
    |   |   |                   59.png
    |   |   |                   6.png
    |   |   |                   60.png
    |   |   |                   61.png
    |   |   |                   62.png
    |   |   |                   63.png
    |   |   |                   64.png
    |   |   |                   65.png
    |   |   |                   66.png
    |   |   |                   67.png
    |   |   |                   68.png
    |   |   |                   69.png
    |   |   |                   7.png
    |   |   |                   70.png
    |   |   |                   71.png
    |   |   |                   72.png
    |   |   |                   73.png
    |   |   |                   74.png
    |   |   |                   75.png
    |   |   |                   76.png
    |   |   |                   77.png
    |   |   |                   78.png
    |   |   |                   79.png
    |   |   |                   8.png
    |   |   |                   80.png
    |   |   |                   81.png
    |   |   |                   82.png
    |   |   |                   83.png
    |   |   |                   84.png
    |   |   |                   85.png
    |   |   |                   86.png
    |   |   |                   87.png
    |   |   |                   88.png
    |   |   |                   89.png
    |   |   |                   9.png
    |   |   |                   90.png
    |   |   |                   91.png
    |   |   |                   92.png
    |   |   |                   93.png
    |   |   |                   94.png
    |   |   |                   95.png
    |   |   |                   96.png
    |   |   |                   97.png
    |   |   |                   98.png
    |   |   |                   99.png
    |   |   |
    |   |   \---test
    |   |           test_drawing.cpp
    |   |           test_ffmpeg.cpp
    |   |           test_gui.cpp
    |   |           test_main.cpp
    |   |           test_precomp.cpp
    |   |           test_precomp.hpp
    |   |           test_video_io.cpp
    |   |
    |   +---imgproc
    |   |   |   CMakeLists.txt
    |   |   |
    |   |   +---doc
    |   |   |   |   feature_detection.rst
    |   |   |   |   filtering.rst
    |   |   |   |   geometric_transformations.rst
    |   |   |   |   histograms.rst
    |   |   |   |   imgproc.rst
    |   |   |   |   miscellaneous_transformations.rst
    |   |   |   |   motion_analysis_and_object_tracking.rst
    |   |   |   |   object_detection.rst
    |   |   |   |   planar_subdivisions.rst
    |   |   |   |   structural_analysis_and_shape_descriptors.rst
    |   |   |   |
    |   |   |   \---pics
    |   |   |           backprojectpatch.png
    |   |   |           bayer.png
    |   |   |           boundingrect.png
    |   |   |           building.jpg
    |   |   |           contoursecarea.png
    |   |   |           cornersubpix.png
    |   |   |           defects.png
    |   |   |           houghp.png
    |   |   |           integral.png
    |   |   |           inv_logpolar.jpg
    |   |   |           logpolar.jpg
    |   |   |           minareabox.png
    |   |   |           pointpolygon.png
    |   |   |           quadedge.png
    |   |   |           subdiv.png
    |   |   |           threshold.png
    |   |   |
    |   |   +---include
    |   |   |   \---opencv2
    |   |   |       \---imgproc
    |   |   |               imgproc.hpp
    |   |   |               imgproc_c.h
    |   |   |               types_c.h
    |   |   |
    |   |   +---src
    |   |   |       accum.cpp
    |   |   |       approx.cpp
    |   |   |       canny.cpp
    |   |   |       color.cpp
    |   |   |       contours.cpp
    |   |   |       convhull.cpp
    |   |   |       corner.cpp
    |   |   |       cornersubpix.cpp
    |   |   |       deriv.cpp
    |   |   |       distransform.cpp
    |   |   |       emd.cpp
    |   |   |       featureselect.cpp
    |   |   |       featuretree.cpp
    |   |   |       filter.cpp
    |   |   |       floodfill.cpp
    |   |   |       gcgraph.hpp
    |   |   |       geometry.cpp
    |   |   |       grabcut.cpp
    |   |   |       histogram.cpp
    |   |   |       hough.cpp
    |   |   |       imgwarp.cpp
    |   |   |       inpaint.cpp
    |   |   |       kdtree.cpp
    |   |   |       linefit.cpp
    |   |   |       lsh.cpp
    |   |   |       matchcontours.cpp
    |   |   |       moments.cpp
    |   |   |       morph.cpp
    |   |   |       precomp.cpp
    |   |   |       precomp.hpp
    |   |   |       pyramids.cpp
    |   |   |       pyrsegmentation.cpp
    |   |   |       rotcalipers.cpp
    |   |   |       samplers.cpp
    |   |   |       segmentation.cpp
    |   |   |       shapedescr.cpp
    |   |   |       smooth.cpp
    |   |   |       spilltree.cpp
    |   |   |       subdivision2d.cpp
    |   |   |       sumpixels.cpp
    |   |   |       tables.cpp
    |   |   |       templmatch.cpp
    |   |   |       thresh.cpp
    |   |   |       undistort.cpp
    |   |   |       utils.cpp
    |   |   |       _featuretree.h
    |   |   |       _geom.h
    |   |   |       _imgproc.h
    |   |   |       _kdtree.hpp
    |   |   |       _list.h
    |   |   |
    |   |   \---test
    |   |           test_approxpoly.cpp
    |   |           test_canny.cpp
    |   |           test_color.cpp
    |   |           test_contours.cpp
    |   |           test_convhull.cpp
    |   |           test_distancetransform.cpp
    |   |           test_emd.cpp
    |   |           test_filter.cpp
    |   |           test_floodfill.cpp
    |   |           test_grabcut.cpp
    |   |           test_histograms.cpp
    |   |           test_imgwarp.cpp
    |   |           test_inpaint.cpp
    |   |           test_main.cpp
    |   |           test_moments.cpp
    |   |           test_precomp.cpp
    |   |           test_precomp.hpp
    |   |           test_pyrsegmentation.cpp
    |   |           test_subdivisions.cpp
    |   |           test_templmatch.cpp
    |   |           test_thresh.cpp
    |   |           test_watershed.cpp
    |   |
    |   +---legacy
    |   |   |   CMakeLists.txt
    |   |   |
    |   |   +---include
    |   |   |   \---opencv2
    |   |   |       \---legacy
    |   |   |               blobtrack.hpp
    |   |   |               compat.hpp
    |   |   |               legacy.hpp
    |   |   |               streams.hpp
    |   |   |
    |   |   \---src
    |   |           3dtracker.cpp
    |   |           auxutils.cpp
    |   |           bgfg_estimation.cpp
    |   |           blobtrack.cpp
    |   |           blobtrackanalysis.cpp
    |   |           blobtrackanalysishist.cpp
    |   |           blobtrackanalysisior.cpp
    |   |           blobtrackanalysistrackdist.cpp
    |   |           blobtrackgen1.cpp
    |   |           blobtrackgenyml.cpp
    |   |           blobtrackingauto.cpp
    |   |           blobtrackingcc.cpp
    |   |           blobtrackingccwithcr.cpp
    |   |           blobtrackingkalman.cpp
    |   |           blobtrackinglist.cpp
    |   |           blobtrackingmsfg.cpp
    |   |           blobtrackingmsfgs.cpp
    |   |           blobtrackpostprockalman.cpp
    |   |           blobtrackpostproclinear.cpp
    |   |           blobtrackpostproclist.cpp
    |   |           calcimagehomography.cpp
    |   |           calibfilter.cpp
    |   |           camshift.cpp
    |   |           clique.cpp
    |   |           compat.cpp
    |   |           condens.cpp
    |   |           contourtree.cpp
    |   |           correspond.cpp
    |   |           corrimages.cpp
    |   |           createhandmask.cpp
    |   |           decomppoly.cpp
    |   |           dominants.cpp
    |   |           dpstereo.cpp
    |   |           eigenobjects.cpp
    |   |           enmin.cpp
    |   |           enteringblobdetection.cpp
    |   |           enteringblobdetectionreal.cpp
    |   |           epilines.cpp
    |   |           extendededges.cpp
    |   |           face.cpp
    |   |           face.h
    |   |           facedetection.cpp
    |   |           facedetection.h
    |   |           facetemplate.cpp
    |   |           facetemplate.h
    |   |           findface.cpp
    |   |           findhandregion.cpp
    |   |           hmm.cpp
    |   |           hmm1d.cpp
    |   |           hmmobs.cpp
    |   |           image.cpp
    |   |           lcm.cpp
    |   |           lee.cpp
    |   |           levmar.cpp
    |   |           levmarprojbandle.cpp
    |   |           levmartrif.cpp
    |   |           lines.cpp
    |   |           lmeds.cpp
    |   |           morphcontours.cpp
    |   |           morphing.cpp
    |   |           pgh.cpp
    |   |           precomp.cpp
    |   |           precomp.hpp
    |   |           prewarp.cpp
    |   |           scanlines.cpp
    |   |           segment.cpp
    |   |           snakes.cpp
    |   |           subdiv2.cpp
    |   |           testseq.cpp
    |   |           texture.cpp
    |   |           trifocal.cpp
    |   |           vecfacetracking.cpp
    |   |           video.cpp
    |   |           _facedetection.h
    |   |           _matrix.h
    |   |           _vectrack.h
    |   |           _vm.h
    |   |
    |   +---ml
    |   |   |   CMakeLists.txt
    |   |   |
    |   |   +---doc
    |   |   |   |   boosting.rst
    |   |   |   |   decision_trees.rst
    |   |   |   |   expectation_maximization.rst
    |   |   |   |   gradient_boosted_trees.rst
    |   |   |   |   k_nearest_neighbors.rst
    |   |   |   |   ml.rst
    |   |   |   |   mldata.rst
    |   |   |   |   neural_networks.rst
    |   |   |   |   normal_bayes_classifier.rst
    |   |   |   |   random_trees.rst
    |   |   |   |   statistical_models.rst
    |   |   |   |   support_vector_machines.rst
    |   |   |   |
    |   |   |   \---pics
    |   |   |           mlp.png
    |   |   |           neuron_model.png
    |   |   |           sigmoid_bipolar.png
    |   |   |
    |   |   +---include
    |   |   |   \---opencv2
    |   |   |       \---ml
    |   |   |               ml.hpp
    |   |   |
    |   |   +---src
    |   |   |       ann_mlp.cpp
    |   |   |       boost.cpp
    |   |   |       cnn.cpp
    |   |   |       data.cpp
    |   |   |       em.cpp
    |   |   |       ertrees.cpp
    |   |   |       estimate.cpp
    |   |   |       gbt.cpp
    |   |   |       inner_functions.cpp
    |   |   |       knearest.cpp
    |   |   |       nbayes.cpp
    |   |   |       precomp.cpp
    |   |   |       precomp.hpp
    |   |   |       rtrees.cpp
    |   |   |       svm.cpp
    |   |   |       testset.cpp
    |   |   |       tree.cpp
    |   |   |
    |   |   \---test
    |   |           test_emknearestkmeans.cpp
    |   |           test_gbttest.cpp
    |   |           test_main.cpp
    |   |           test_mltests.cpp
    |   |           test_mltests2.cpp
    |   |           test_precomp.cpp
    |   |           test_precomp.hpp
    |   |           test_save_load.cpp
    |   |
    |   +---objdetect
    |   |   |   CMakeLists.txt
    |   |   |
    |   |   +---doc
    |   |   |   |   cascade_classification.rst
    |   |   |   |   objdetect.rst
    |   |   |   |
    |   |   |   \---pics
    |   |   |           haarfeatures.png
    |   |   |
    |   |   +---include
    |   |   |   \---opencv2
    |   |   |       \---objdetect
    |   |   |               objdetect.hpp
    |   |   |
    |   |   +---src
    |   |   |       cascadedetect.cpp
    |   |   |       datamatrix.cpp
    |   |   |       distancetransform.cpp
    |   |   |       featurepyramid.cpp
    |   |   |       fft.cpp
    |   |   |       haar.cpp
    |   |   |       hog.cpp
    |   |   |       latentsvm.cpp
    |   |   |       latentsvmdetector.cpp
    |   |   |       lsvmparser.cpp
    |   |   |       lsvmtbbversion.cpp
    |   |   |       matching.cpp
    |   |   |       planardetect.cpp
    |   |   |       precomp.cpp
    |   |   |       precomp.hpp
    |   |   |       resizeimg.cpp
    |   |   |       routine.cpp
    |   |   |       _latentsvm.h
    |   |   |       _lsvmparser.h
    |   |   |       _lsvm_distancetransform.h
    |   |   |       _lsvm_error.h
    |   |   |       _lsvm_fft.h
    |   |   |       _lsvm_matching.h
    |   |   |       _lsvm_resizeimg.h
    |   |   |       _lsvm_routine.h
    |   |   |       _lsvm_tbbversion.h
    |   |   |       _lsvm_types.h
    |   |   |
    |   |   \---test
    |   |           test_cascadeandhog.cpp
    |   |           test_latentsvmdetector.cpp
    |   |           test_main.cpp
    |   |           test_precomp.cpp
    |   |           test_precomp.hpp
    |   |
    |   +---python
    |   |   |   CMakeLists.txt
    |   |   |
    |   |   +---src1
    |   |   |       api
    |   |   |       cv.cpp
    |   |   |       defs
    |   |   |       gen.py
    |   |   |
    |   |   +---src2
    |   |   |       cv2.cpp
    |   |   |       gen2.py
    |   |   |       hdr_parser.py
    |   |   |       opencv_extra_api.hpp
    |   |   |
    |   |   \---test
    |   |           calchist.py
    |   |           camera_calibration.py
    |   |           findstereocorrespondence.py
    |   |           goodfeatures.py
    |   |           leak1.py
    |   |           leak2.py
    |   |           leak3.py
    |   |           leak4.py
    |   |           precornerdetect.py
    |   |           test.py
    |   |           tickets.py
    |   |           ticket_6.py
    |   |           transformations.py
    |   |
    |   +---stitching
    |   |       autocalib.cpp
    |   |       autocalib.hpp
    |   |       blenders.cpp
    |   |       blenders.hpp
    |   |       CMakeLists.txt
    |   |       exposure_compensate.cpp
    |   |       exposure_compensate.hpp
    |   |       main.cpp
    |   |       matchers.cpp
    |   |       matchers.hpp
    |   |       motion_estimators.cpp
    |   |       motion_estimators.hpp
    |   |       precomp.cpp
    |   |       precomp.hpp
    |   |       seam_finders.cpp
    |   |       seam_finders.hpp
    |   |       util.cpp
    |   |       util.hpp
    |   |       util_inl.hpp
    |   |       warpers.cpp
    |   |       warpers.hpp
    |   |       warpers_inl.hpp
    |   |
    |   +---traincascade
    |   |       boost.cpp
    |   |       boost.h
    |   |       cascadeclassifier.cpp
    |   |       cascadeclassifier.h
    |   |       CMakeLists.txt
    |   |       features.cpp
    |   |       haarfeatures.cpp
    |   |       haarfeatures.h
    |   |       imagestorage.cpp
    |   |       imagestorage.h
    |   |       lbpfeatures.cpp
    |   |       lbpfeatures.h
    |   |       traincascade.cpp
    |   |       traincascade_features.h
    |   |
    |   +---ts
    |   |   |   CMakeLists.txt
    |   |   |
    |   |   +---include
    |   |   |   \---opencv2
    |   |   |       \---ts
    |   |   |               ts.hpp
    |   |   |               ts_gtest.h
    |   |   |
    |   |   \---src
    |   |           precomp.cpp
    |   |           precomp.hpp
    |   |           ts.cpp
    |   |           ts_arrtest.cpp
    |   |           ts_func.cpp
    |   |           ts_gtest.cpp
    |   |
    |   \---video
    |       |   CMakeLists.txt
    |       |
    |       +---doc
    |       |       motion_analysis_and_object_tracking.rst
    |       |       video.rst
    |       |
    |       +---include
    |       |   \---opencv2
    |       |       \---video
    |       |               background_segm.hpp
    |       |               tracking.hpp
    |       |
    |       +---src
    |       |       bgfg_acmmm2003.cpp
    |       |       bgfg_codebook.cpp
    |       |       bgfg_common.cpp
    |       |       bgfg_gaussmix.cpp
    |       |       bgfg_gaussmix2.cpp
    |       |       camshift.cpp
    |       |       kalman.cpp
    |       |       lkpyramid.cpp
    |       |       motempl.cpp
    |       |       optflowbm.cpp
    |       |       optflowgf.cpp
    |       |       optflowhs.cpp
    |       |       optflowlk.cpp
    |       |       precomp.cpp
    |       |       precomp.hpp
    |       |
    |       \---test
    |               test_accum.cpp
    |               test_camshift.cpp
    |               test_estimaterigid.cpp
    |               test_kalman.cpp
    |               test_main.cpp
    |               test_motiontemplates.cpp
    |               test_optflow.cpp
    |               test_optflowpyrlk.cpp
    |               test_precomp.cpp
    |               test_precomp.hpp
    |
    \---samples
        |   CMakeLists.txt
        |
        +---c
        |   |   adaptiveskindetector.cpp
        |   |   agaricus-lepiota.data
        |   |   airplane.jpg
        |   |   baboon.jpg
        |   |   baboon200.jpg
        |   |   baboon200_rotated.jpg
        |   |   bgfg_codebook.cpp
        |   |   blobtrack_sample.cpp
        |   |   box.png
        |   |   box_in_scene.png
        |   |   build_all.sh
        |   |   calonder_params.xml
        |   |   cat.jpg
        |   |   cat.xml
        |   |   CMakeLists.txt
        |   |   contours.c
        |   |   convert_cascade.c
        |   |   cvsample.dsp
        |   |   delaunay.c
        |   |   facedetect.cmd
        |   |   facedetect.cpp
        |   |   fback_c.c
        |   |   find_obj.cpp
        |   |   find_obj_calonder.cpp
        |   |   find_obj_ferns.cpp
        |   |   fruits.jpg
        |   |   intrinsics.yml
        |   |   JCB.png
        |   |   latentsvmdetect.cpp
        |   |   lena.jpg
        |   |   morphology.c
        |   |   motempl.c
        |   |   mser_sample.cpp
        |   |   mushroom.cpp
        |   |   one_way_sample.cpp
        |   |   one_way_train_0000.jpg
        |   |   one_way_train_0001.jpg
        |   |   one_way_train_images.txt
        |   |   polar_transforms.c
        |   |   puzzle.png
        |   |   pyramid_segmentation.c
        |   |   scene_l.bmp
        |   |   scene_r.bmp
        |   |   stuff.jpg
        |   |   tree.avi
        |   |   tree_engine.cpp
        |   |   waveform.data
        |   |
        |   \---example_cmake
        |           CMakeLists.txt
        |           minarea.c
        |           README.txt
        |
        +---cpp
        |   |   3calibration.cpp
        |   |   baboon.jpg
        |   |   bagofwords_classification.cpp
        |   |   bgfg_segm.cpp
        |   |   brief_match_test.cpp
        |   |   build3dmodel.cpp
        |   |   building.jpg
        |   |   calibration.cpp
        |   |   calibration_artificial.cpp
        |   |   camshiftdemo.cpp
        |   |   chamfer.cpp
        |   |   CMakeLists.txt
        |   |   connected_components.cpp
        |   |   contours2.cpp
        |   |   convexhull.cpp
        |   |   cout_mat.cpp
        |   |   demhist.cpp
        |   |   descriptor_extractor_matcher.cpp
        |   |   detector_descriptor_evaluation.cpp
        |   |   dft.cpp
        |   |   distrans.cpp
        |   |   drawing.cpp
        |   |   edge.cpp
        |   |   em.cpp
        |   |   fback.cpp
        |   |   fern_params.xml
        |   |   ffilldemo.cpp
        |   |   filestorage.cpp
        |   |   fitellipse.cpp
        |   |   fruits.jpg
        |   |   generic_descriptor_match.cpp
        |   |   grabcut.cpp
        |   |   houghlines.cpp
        |   |   image.cpp
        |   |   imagelist_creator.cpp
        |   |   inpaint.cpp
        |   |   kalman.cpp
        |   |   kinect_maps.cpp
        |   |   kmeans.cpp
        |   |   laplace.cpp
        |   |   left01.jpg
        |   |   left02.jpg
        |   |   left03.jpg
        |   |   left04.jpg
        |   |   left05.jpg
        |   |   left06.jpg
        |   |   left07.jpg
        |   |   left08.jpg
        |   |   left09.jpg
        |   |   left11.jpg
        |   |   left12.jpg
        |   |   left13.jpg
        |   |   left14.jpg
        |   |   lena.jpg
        |   |   letter-recognition.data
        |   |   letter_recog.cpp
        |   |   lkdemo.cpp
        |   |   logo.png
        |   |   logo_in_clutter.png
        |   |   matcher_simple.cpp
        |   |   matching_to_many_images.cpp
        |   |   meanshift_segmentation.cpp
        |   |   minarea.cpp
        |   |   morphology2.cpp
        |   |   multicascadeclassifier.cpp
        |   |   peopledetect.cpp
        |   |   pic1.png
        |   |   pic2.png
        |   |   pic3.png
        |   |   pic4.png
        |   |   pic5.png
        |   |   pic6.png
        |   |   points_classifier.cpp
        |   |   right01.jpg
        |   |   right02.jpg
        |   |   right03.jpg
        |   |   right04.jpg
        |   |   right05.jpg
        |   |   right06.jpg
        |   |   right07.jpg
        |   |   right08.jpg
        |   |   right09.jpg
        |   |   right11.jpg
        |   |   right12.jpg
        |   |   right13.jpg
        |   |   right14.jpg
        |   |   segment_objects.cpp
        |   |   select3dobj.cpp
        |   |   squares.cpp
        |   |   starter_imagelist.cpp
        |   |   starter_video.cpp
        |   |   stereo_calib.cpp
        |   |   stereo_calib.xml
        |   |   stereo_match.cpp
        |   |   stuff.jpg
        |   |   tsukuba_l.png
        |   |   tsukuba_r.png
        |   |   video_dmtx.cpp
        |   |   video_homography.cpp
        |   |   watershed.cpp
        |   |
        |   +---matching_to_many_images
        |   |   |   query.png
        |   |   |
        |   |   \---train
        |   |           1.png
        |   |           2.png
        |   |           3.png
        |   |           trainImages.txt
        |   |
        |   +---Qt_sample
        |   |       CMakeLists.txt
        |   |       cube4.avi
        |   |       main.cpp
        |   |
        |   \---tutorial_code
        |       +---Basic
        |       |       AddingImages.cpp
        |       |       AddingImagesTrackbar.cpp
        |       |       BasicLinearTransforms.cpp
        |       |       BasicLinearTransformsTrackbar.cpp
        |       |       DisplayImage.cpp
        |       |       Drawing_1.cpp
        |       |       Drawing_2.cpp
        |       |       LoadSaveImage.cpp
        |       |
        |       +---images
        |       |       cat.jpg
        |       |       HappyFish.jpg
        |       |       lena.png
        |       |       LinuxLogo.jpg
        |       |       WindowsLogo.jpg
        |       |
        |       \---Image_Processing
        |               Morphology_1.cpp
        |               Smoothing.cpp
        |
        +---gpu
        |   |   aloeL.jpg
        |   |   aloeR.jpg
        |   |   cascadeclassifier.cpp
        |   |   cascadeclassifier_nvidia_api.cpp
        |   |   CMakeLists.txt
        |   |   driver_api_multi.cpp
        |   |   driver_api_stereo_multi.cpp
        |   |   hog.cpp
        |   |   morfology.cpp
        |   |   multi.cpp
        |   |   road.png
        |   |   stereo_match.cpp
        |   |   stereo_multi.cpp
        |   |   surf_keypoint_matcher.cpp
        |   |   tsucuba_left.png
        |   |   tsucuba_right.png
        |   |
        |   \---performance
        |           CMakeLists.txt
        |           performance.cpp
        |           performance.h
        |           tests.cpp
        |
        +---MacOSX
        |   \---FaceTracker
        |       |   FaceTracker-Info.plist
        |       |   FaceTracker.cpp
        |       |   README.txt
        |       |
        |       \---FaceTracker.xcodeproj
        |               project.pbxproj
        |
        +---python
        |       camera.py
        |       camshift.py
        |       chessboard.py
        |       contours.py
        |       convexhull.py
        |       cv20squares.py
        |       cvutils.py
        |       delaunay.py
        |       demhist.py
        |       dft.py
        |       distrans.py
        |       dmtx.py
        |       drawing.py
        |       edge.py
        |       facedetect.py
        |       fback.py
        |       ffilldemo.py
        |       fitellipse.py
        |       houghlines.py
        |       inpaint.py
        |       kalman.py
        |       kmeans.py
        |       laplace.py
        |       lkdemo.py
        |       logpolar.py
        |       minarea.py
        |       minidemo.py
        |       morphology.py
        |       motempl.py
        |       numpy_array.py
        |       numpy_warhol.py
        |       peopledetect.py
        |       pyramid_segmentation.py
        |       squares.py
        |       watershed.py
        |
        \---python2
                browse.py
                calibrate.py
                coherence.py
                color_histogram.py
                common.py
                edge.py
                gaussian_mix.py
                letter_recog.py
                obj_detect.py
                video.py
                _coverage.py

