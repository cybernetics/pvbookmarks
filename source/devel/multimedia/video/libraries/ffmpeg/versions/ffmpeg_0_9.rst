


.. _ffmpeg_version_0_9:

====================================
ffmpeg 0.9.0 "Harmony" (2011-12-11)
====================================

.. seealso:: http://ffmpeg.org/download.html#release_0.9


0.9 was released on 2011-12-11.

It is the latest stable FFmpeg release from the 0.9 release branch, which was
cut from master on 2011-12-11.

Amongst lots of other changes, it includes all changes from:

- ffmpeg-mt,
- libav master of 2011-12-11
- libav 0.7.2 as of 2011-12-11


We have made a **new major release (0.9)** It contains all features and bugfixes of
the git master branch. A partial list of new stuff is below:

- native dirac decoder
- mmsh seeking
- more accurate rgb->rgb in swscale
- MPO file format reading support
- mandelbrot fraktal video source
- libass filter
- export quarter_sample & divx_packed from decoders
- VBLE decoder
- libopenjpeg encoder
- alpha opaqueness fixes in many codecs
- 8bit palette dynamic range fixes in many codecs
- AVIOInterruptCB
- OS/2 threads support
- cbr mp3 muxing fix
- sample rate change support in flv (nellymoser decoder)
- mov/mp4 chunking support (equivalent to mp4boxs -inter)
- mov/mp4 fragment support (equivalent to mp4boxs -frag)
- rgba tiffs
- x264rgb bugfix
- cljrencoder with dither
- escape130 decoder
- many new ARM optimizations
- report
- Dxtory capture format decoder
- life video source
- wtv, sox, utvideo and many other new regression tests
- gcc coverage support
- callauto video source
- planar rgb input support in sws
- libmodplug & bintext output
- g723.1 encoder
- g723.1 muxer
- random() function for the expression evaluator
- persistent variables for the expression evaluator
- pulseaudio input support
- h264 422 inter decoding support
- prores encoder
- native utvideo decoder
- libutvideo support
- deshake filter
- aevalsrc filter
- segment muxer
- mkv timecode v2 muxer
- cache urlprotocol
- libaacplus support
- ACT/BIT demuxers
- AMV video encoder
- g729 decoder
- stdin control of drawtext
- 2bpp, 4bpp png support
- interlaced 1bpp and PAETH png fixes
- libspeex encoding support
- hardened h264 decoder that wont overread the bitstream
- wtv muxer
- H/W Accelerated H.264 Decoding on Android
- stereo3d filter from libmpcodecs works now
- an experimental jpeg2000 encoder
- many bugfixes
- libswresample

