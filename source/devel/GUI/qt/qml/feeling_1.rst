


================
QML and Qt Quick
================

.. seealso:: http://labs.qt.nokia.com/2011/02/18/buckets-of-cold-water/



L.MCH February 19, 2011 at 3:57 am
==================================

@David & Will Stokes

**QML & Qt Quick are a lot more relevant for desktop applications than it seems.**
Once you start mastering Qt Quick and getting the mindset behind its design, it
simplifies app development not just for smartphones, but on desktops an embedded
devices too.

QML has very basic components but they are a lot more flexible than QWidgets
coded in C++.

For example: a QML Listview is not “something like a listview”, instead is
“something like a listview and much more” that you can use as a listview, but
also as a multipage panel, or turn it into a “versatile treeview” by using the
proper models and delegates.

QML UI items look more spartan than QWidgets, but they are easier and faster
to compose into new UI elements you can reuse and extend further.

I’m using Qt to develop “simple” SCADA/DCS applications running on windows
desktops and windows ce devices and it simply rocks (*really* simple and basic,
not the really big SCADA stuff, my applications are more like distributed HMIs
on steroids).

Low-level I/O and synchronization on serial links, tcp/ip and CAN bus is handled
by a reusable “SCADA engine framework” coded in Qt/C++ and using C++ coded
QWidgets for the fixed parts of the UI, while all the higher level and
customized interactive visualization and instrumentation is handled by QML.

In other words it makes a lot easier to develop a “base application” written
in Qt/C++ and adapt and extend it by scripting in QML/Javascript parts of its
user interface and most of its higher level logic.

The best part is that I’m **the C++ guy that handles the weird and complex stuff**
while the (boring) customized SCADA/DCS/HMI UIs for the final customers are
coded in QML by the same guys that usually develop the plc programs on the
remote devices, this way THEY write the UI as they like it (and of course they
test it too) and they really like it too, because they feel they have full
control of the system and development cycle is faster.

Of course some things need to be improved and there are problems (i.e. using
Qt 4.7.1 there are some memory leaks that are really troublesome on
memory-constrained Windows CE devices, but most of them are already fixed in
the git repository so i just had to download a commit with the relevant patches)
but it is a lot better than coding everything in C++ or using Python/”pure
javascript”/Lua/ecc. for the scriptable parts (because in my humble opinion
QML integrates a lot better the lower level Qt/C++ parts with the higher level
UI coding and application logic).

Mine may seem a very peculiar situation, but almost every application that grows
beyound a certain size/complexity ends up needing what Qt Quick provides
(i.e. high level scripting and “flexible UI modding”).


Curt February 19, 2011 at 5:09 pm
==================================
@vohi

Thanks to you and the whole Troll team for great software and documentation over
the years and for strong, helpful communication right now. I agree with the
statement that QML will improve the desktop. In fact, we are currently involved
in a project utilizing Qt Quick widgets as part of a desktop application and it
is working well for us. We will keep working in Qt for the coming years.

Thanks again for addressing questions from the community, the Qt “love” team,
as one of the earlier posts mentioned.  Take care.


