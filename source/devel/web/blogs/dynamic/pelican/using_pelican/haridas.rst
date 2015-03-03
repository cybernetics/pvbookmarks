


.. _pelican_haridas:

========
Haridas
========

.. seealso:: http://haridas.in/wordpress-blog-migrated-to-pelican.html

Initially this blog was a wordpress blog. 

As you know the reasons for that Wordpress is the most successful and feature 
rich blogging engine. 
So I chose it without any doubt. 

I didn't even search for a python alternative blog engine
at that time. But after a while I felt the dificulties while adding some
changes to the wordpress code, bugs with the wordpress plugins and more
importantly the Web UI is very annoying while typing new contents.

If we are considering the technical points, wordpress is a dynamic blog engine,
it is an over killing for blogs and other wiki based sites. Main issue is
with speed of page rendering.The static pages are way faster compared to
the dynamic contents. I know wordpress has caching plugins to make the static
pages out of dynamic one but that are not a very reliable solution.

Actually above points are all come to my mind after seeing the static site
generators and their awesome features and flexibility.

Advantages of static site generators over Dynamic blog engines

- Serve html directly, so very fast.
- Easy maintenance of the site, very less pain with server setup.
- Use your favourite Text editors for blog posting. I use VIM :).
- It use Markdown and Restructured Text Syntaxes for blog entry. So we just
  need to type the post in normal text with simple formating. So don't worry
  about the html formatting while typing the content.
- Host it on Github, and very easy version control and site backup.
- Very easy to customize the Themes or other internals if you want.

ext step was which static site generator I will choose for my site. There are
a lot of them were implemented in Python and Ruby. I went through some of them
and finally chose Pelican a Python based static site generator.


