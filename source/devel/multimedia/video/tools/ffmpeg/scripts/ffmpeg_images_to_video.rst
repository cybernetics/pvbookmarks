

============================
Video ffmpeg images to video
============================

.. seealso::

   - http://mediaintro.teeks99.com/Video/Video-3-Quality.html
   - http://www.freesoftwaremagazine.com/articles/assembling_video_png_stream_ffmpeg



Here is the command that takes the stream of PNGs and strips off the
letterboxing, then packs it up as raw video, 24fps::

    ffmpeg -i 1080/sintel_trailer_2k_%04d.png -vf crop=1920:816:0:132 -vcodec rawvideo -r 24 -pix_fmt yuv444p sintel_trailer.y4m



From there its easy to convert into theora::

    ffmpeg2theora -v 10 -K 24 sintel_trailer.y4m


Personally I've never gotten comfortable with specifying the video quality, I
always like to try out different bit-rates and then look at different results
to figure out what is "good enough" (to just try it on part of the video without
encoding the whole thing use -ss to specify a staring point and -t to specify a
duration). Without the video quality parameter (which I don't think ffmpeg
supports), I can do it all at once::

    ffmpeg -i 1080/sintel_trailer_2k_%04d.png -vf crop=1920:816:0:132 -vcodec libtheora -b 9000k -r 24 -pix_fmt yuv444p sintel_trailer.ogv


You could also go to the VP8 codec, and knock about 55% off the file size with
about the same quality::

    ffmpeg -i 1080/sintel_trailer_2k_%04d.png -vf crop=1920:816:0:132 -vcodec libvpx -b 4000k -r 24 -pix_fmt yuv444p sintel_trailer.ogv


Or if you really want quality, you could do either of those with 2-pass::

    ffmpeg -i 1080/sintel_trailer_2k_%04d.png -pass 1 -vf crop=1920:816:0:132 -vcodec libtheora -b 6000k -bt 6000k -r 24 -pix_fmt yuv444p -f rawvideo -y /dev/null
    ffmpeg -i 1080/sintel_trailer_2k_%04d.png -pass 2 -vf crop=1920:816:0:132 -vcodec libtheora -b 6000k -bt 6000k -r 24 -pix_fmt yuv444p sintel_trailer.ogv

    ffmpeg -i 1080/sintel_trailer_2k_%04d.png -pass 1 -vf crop=1920:816:0:132 -vcodec libvpx -b 3000k -bt 3000k -r 24 -pix_fmt yuv444p -f rawvideo -y /dev/null
    ffmpeg -i 1080/sintel_trailer_2k_%04d.png -pass 2 -vf crop=1920:816:0:132 -vcodec libvpx -b 3000k -bt 3000k -r 24 -pix_fmt yuv444p sintel_trailer.ogv

If you really want the letterboxing, (sigh) you can add::

    -padtop 131 -padbottom 131 -padcolor 000000 to the ffmpeg commands.

To see the results for the entire video quality demo I did for my class, check
out this site: http://mediaintro.teeks99.com/Video/Video-3-Quality.html

