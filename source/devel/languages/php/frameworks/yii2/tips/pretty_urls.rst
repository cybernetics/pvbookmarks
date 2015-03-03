
.. index::
   pair: Pretty URLs ; Yii2


.. _yii2_pretty_urls:

==========================================
Yii2 pretty urls
==========================================
 
 
.. seealso::

   - http://code.tutsplus.com/tutorials/programming-with-yii2-getting-started--cms-22440
    

Turning on Pretty URLs
=======================

First, **let's enable Yii2's pretty URLs with mod_rewrite**. 

On the Yii home page, if you click on the About menu option, the URL will be s
omething like http://localhost:8888/hello/web/index.php?r=site%2Fabout. 

We'd like to change that to http://localhost:8888/hello/web/site/about.

The config subdirectory includes environment configurations for your web and 
console applications as well as the future database settings. 

Edit /config/web.php to add urlManagement to the current web application. 

Add the following urlManager section within the components array:

.. code-block:: php

    <? php
    'components' => [
    //...
      'urlManager' => [
              'showScriptName' => false,
              'enablePrettyUrl' => true
                      ],   
    //...
    'request' => [

Then, create an .htaccess file within /web where the primary index.php file 
exists

Then, create an .htaccess file within /web where the primary index.php file exists:

.. code-block:: apacheconf

    RewriteEngine on
     
    # If a directory or a file exists, use it directly
    RewriteCond %{REQUEST_FILENAME} !-f
    RewriteCond %{REQUEST_FILENAME} !-d
    # Otherwise forward it to <span class="skimlinks-unlinked">index.php</span>
    RewriteRule . <span class="skimlinks-unlinked">index.php</span>

Make sure mod_rewrite is running locally on MAMP; if not, check out this Stack 
Overflow guide.

In your browser, visit this URL: http://localhost:8888/hello/web/site/about. 

You should see the Yii application About page and clicking on other menu 
options should bring up pretty URLs.




