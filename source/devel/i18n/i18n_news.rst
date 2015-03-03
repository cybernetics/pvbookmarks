

.. index::
   pair: i18n ; News
   pair: i18n ; LCID

.. _i18n_news:

=========
i18n news
=========

.. contents::
   :depth: 3

On Aug 18, 2010, at 9:01 [Libusb-devel] Strings and Languages
=============================================================

- http://usb.org/developers/docs/USB_LANGIDs.pdf
- http://msdn.microsoft.com/en-us/library/0h88fahh%28VS.85%29.aspx

::

    On Aug 18, 2010, at 9:01 PM, Peter Stuge wrote:
    > Alan Ott wrote:
    >>>> mapping from locale names (like en_US) to USB language IDs
    >>>> (eg: 0x0409).
    >>>
    >>> http://usb.org/developers/docs/USB_LANGIDs.pdf
    >>
    >> I assume you're suggesting that I make my own mapping. That seems
    >> quite error prone.
    >
    > ?!
    >
    >
    >> I'm looking for a "right" way to do it, something like "check out the
    >> source code for...." or "use libXYZ" or "the USB language codes
    >> correspond to .... which is the same as Y and so you can use...."
    >
    > How about "write the source code for it" ?
    >
    >
    >> Doing it myself seems like a bad idea.
    >
    > I think it's a great idea. Have someone review it if you're anxious
    > about getting it right. It should be a quick matter, and a very
    > straightforward struct [].

    Ok, you convinced me. The reason I was hesitant is because I'm kind of
    new to i18n, and it seems like the kind of thing it's easy to have a
    simplified understanding of.

    It turns out that the USB language IDs are the same as Microsoft LCID
    codes (best I could tell without examining each and every one).
    There's a table matching those LCIDs with string language codes here:

    - http://msdn.microsoft.com/en-us/library/0h88fahh%28VS.85%29.aspx

    I did a little regex work and turned that table into something usable.

    The code is at:

    - http://github.com/signal11/hidapi/blob/master/linux/hid-libusb.c

    beginning at line 806

    I'd appreciate some review of it, as it seems like there's plenty of
    places where I could have made incorrect assumptions.




