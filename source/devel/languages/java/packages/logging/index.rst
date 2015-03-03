

.. index::
   pair: Java ; Logging

.. _java_logging:

=======================
Java logging package
=======================

.. seealso::

   - http://docs.oracle.com/javase/7/docs/technotes/guides/logging/overview.html
   - http://www.vogella.com/articles/Logging/article.html



Example 1
===========

The following is a small program that performs logging using the default configuration.

This program relies on the root handlers that were established by the LogManager 
based on the configuration file. 

It creates its own Logger object and then makes calls to that Logger object to 
report various events.

::


    package com.wombat;
    import java.util.logging.*;

    public class Nose{
        // Obtain a suitable logger.
        private static Logger logger = Logger.getLogger("com.wombat.nose");
        public static void main(String argv[]) {
            // Log a FINE tracing message
            logger.fine("doing stuff");
            try{
                Wombat.sneeze();
            } catch (Exception ex) {
                // Log the exception
                logger.log(Level.WARNING, "trouble sneezing", ex);
            }
            logger.fine("done");
        }
    }

Example 2
===========

Changing the Configuration
---------------------------

Here's a small program that dynamically adjusts the logging configuration to 
send output to a specific file and to get lots of information on wombats. 

The pattern "%t" means the system temporary directory.

::

    public static void main(String[] args) {
        Handler fh = new FileHandler("%t/wombat.log");
        Logger.getLogger("").addHandler(fh);
        Logger.getLogger("com.wombat").setLevel(Level.FINEST);
        ...
    }

Example 3
===========

2.3 Simple Use, Ignoring Global Configuration
----------------------------------------------

Here's a small program that sets up its own logging Handler and ignores the 
global configuration.


::


    package com.wombat;

    import java.util.logging.*;

    public class Nose {
        private static Logger logger = Logger.getLogger("com.wombat.nose");
        private static FileHandler fh = new FileHandler("mylog.txt");
        public static void main(String argv[]) {
            // Send logger output to our FileHandler.
            logger.addHandler(fh);
            // Request that every detail gets logged.
            logger.setLevel(Level.ALL);
            // Log a simple INFO message.
            logger.info("doing stuff");
            try {
                Wombat.sneeze();
            } catch (Exception ex) {
                logger.log(Level.WARNING, "trouble sneezing", ex);
            }
            logger.fine("done");
        }
    }

