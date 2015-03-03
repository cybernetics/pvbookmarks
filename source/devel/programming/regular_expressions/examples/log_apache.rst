

.. index::
   pair: python examples; namedtuple



=======================
parses Apache logs
=======================

.. seealso::

   - http://slott-softwarearchitect.blogspot.com/2012/01/apache-log-parsing.html


How much do I love Python?  Consider this little snippet that parses Apache logs.


::

    import re
    from collections import defaultdict, namedtuple

    format_pat= re.compile(
        r"(?P<host>[\d\.]+)\s"
        r"(?P<identity>\S*)\s"
        r"(?P<user>\S*)\s"
        r"\[(?P<time>.*?)\]\s"
        r'"(?P<request>.*?)"\s'
        r"(?P<status>\d+)\s"
        r"(?P<bytes>\S*)\s"
        r'"(?P<referer>.*?)"\s' # [SIC]
        r'"(?P<user_agent>.*?)"\s*'
    )

    Access = namedtuple('Access',
        ['host', 'identity', 'user', 'time', 'request',
        'status', 'bytes', 'referer', 'user_agent'] )

    def access_iter( source_iter ):
        for log in source_iter:
            for line in (l.rstrip() for l in log):
                match= format_pat.match(line)
                if match:
                    yield Access( **match.groupdict() )



That's about it.  The access log rows are now first-class Access-class objects
that can be processed pleasantly by high-level Python applications.


Cool things
===========

- The adjacent string concatenation means that the regular expression can be
  broken up into bits to make it readable.
- When the named tuple attributes match the regular expression names, we can
  trivially turn the match.groupdict() into a named tuple.
- By using a generator, the other parts of the application can simply loop
  through the results without tying up memory to create vast intermediate structures.

A couple of years back, a sysadmin was trying to justify spending money on a
log analyzer product.  I suggested they (at the very least) get an open source
log analyzer.

I also suggested that they learn Python and save themselves the pain of working
with a (potentially) complex tool.  Given this as a common library module,
log analysis applications are remarkably easy to write.



