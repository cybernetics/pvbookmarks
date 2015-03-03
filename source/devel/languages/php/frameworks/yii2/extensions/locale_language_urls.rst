
.. index::
   pair: Pretty URLs ; Yii2


.. _yii2_locale_urls:

==========================================
Yii 2.0: yii2-localeurls
==========================================
 
 
.. seealso::

   - http://www.yiiframework.com/extension/yii2-localeurls/
   - https://github.com/codemix/yii2-localeurls
   - http://www.yiiframework.com/doc-2.0/yii-base-application.html#%24language-detail
  

.. contents::
   :depth: 3    

Yii2 Locale URLs
=================

Automatic locale/language management through URLs for Yii 2.

Features
========

With this extension you can use URLs that contain a language code like::

    /en/some/page
    /de/some/page
    http://www.example.com/en/some/page
    http://www.example.com/de/some/page


You can also configure friendly names if you want::

- http://www.example.com/english/some/page
- http://www.example.com/deutsch/some/page

The language code is automatically added whenever you create a URL, and read 
back when a URL is parsed. 

For best user experience the language is autodetected from the browser settings 
but the user can still access other languages simply by calling a URL with 
another language code.

The last requested language is also persisted in the user session and in a 
cookie. 
So if the user tries to access your site without a language code in the URL, 
he'll get redirected to the language he had used on his last visit.

All the above (and more) is configurable of course.

For more details check out the project on github:


