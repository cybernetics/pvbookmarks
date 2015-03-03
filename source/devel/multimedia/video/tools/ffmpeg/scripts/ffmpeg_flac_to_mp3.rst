
=================================================================
Convert all FLAC files in a directory into MP3 files with FFmpeg
=================================================================

.. seealso::

   - http://blogs.fsfe.org/marklindhout/2012/11/converting-flac-files-to-mp3-with-ffmpeg-and-bash/


::

    $ (for FILE in *.flac ; do ffmpeg -i "$FILE" -f mp3 -ab 192000 "`basename "$FILE" .flac`.mp3" || break; done)


A little explanation; The brackets around the command allow for a nice interrupt
when the user presses CTRL+C. This is practical especially when you’re processing
many files.

Seeing as we’re processing an album here, 15 files is no exception, and who wants
to be pressing CTRL+C 15 times, right ?


The basename part makes sure the extension is changed from .flac to .mp3.

If you would just drop the $FILE variable in there, you’d end up with files named
cool-songtitle.flac.mp3.

