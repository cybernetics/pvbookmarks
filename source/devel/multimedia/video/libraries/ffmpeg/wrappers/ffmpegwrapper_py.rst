

.. index::
   triple:  Multimedia; ffmpeg; wrapper


.. _pyffmpegwrapper:

=====================
python ffmpegwrapper
=====================

.. seealso::

   - http://pypi.python.org/pypi/ffmpegwrapper/
   - http://github.com/interrupted/ffmpegwrapper

A simple wrapper for ffmpeg-cli

FFmpegWrapper is a small wrapper for the ffmpeg encoder.

You can append Codec, Filters and other OptionStores to the FFmpeg class and
then run the resulting command::

    >>> from ffmpegwrapper import FFmpeg, Input, Output, VideoCodec, VideoFilter
    >>> codec = VideoCodec('webm')
    >>> input_video = Input('old')
    >>> output_video = Output('new', videofilter, codec)
    >>> FFmpeg('ffmpeg', input_video, output_video)
    <FFmpeg ['ffmpeg', '-i', 'old', '-vcodec', 'webm', 'new']>


