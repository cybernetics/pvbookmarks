
.. index::
   pair: PEX (2014) ; uWSGI 


.. _pex_based_2014:

=======================
PEX based appli (2014)
=======================



I've been thinking about ways to leverage uwsgi for serving PEX-based apps for 
a while. 

Specifically, uwsgi has a few nice features that I think would complement this 
approach really well (and also avoid conflating runtime configuration and code 
to the degree possible).

By leveraging your bootstrapping approach combined with other ideas (e.g. tapping 
uwsgi's ability to import apps from a standard python environment, the ability 
to bootstrap worker environments via --import and the bonus fact that you can 
embed code/content as symbols/data segments), here's what I came up with::

    https://gist.github.com/kwlzn/3d251cf13547ed6bb6f0


This approach gives you a nice single-file uWSGI binary which can import any 
module from a (compressed) pex and run it as a WSGI app, like so:

    $ pex_uwsgi --http :8585 --env UWSGI_PEX=testapp.pex --module 'testapp:app'



This also allows you to pass any arbitrary uWSGI configuration flags to the binary 
at runtime (e.g. # of workers, bind to unix socket vs port, run in uwsgi protocol 
mode vs HTTP, etc), making it perfect for use in mesos. 

uWSGI is very powerful and should make python pex apps significantly more scalable.


