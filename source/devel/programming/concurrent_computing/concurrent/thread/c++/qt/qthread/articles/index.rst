

.. index::
   pair: Articles; QThread


.. _qthread_articles:

=========================================================
QThread articles
=========================================================


.. seealso::

   - http://doc-snapshot.qt-project.org/qt5-stable/threads-technologies.html
   - http://labs.qt.nokia.com/2010/06/17/youre-doing-it-wrong/
   - http://labs.trolltech.com/blogs/2006/12/04/threading-without-the-headache/
   - http://doc-snapshot.qt-project.org/qt5-stable/qthread.html
   - :ref:`nzmqt_library`


.. contents::
   :depth: 3

Introduction
============

We use IRC extensively to communicate amongst ourselves as well as with the
community. I hang out on the #qt channel on the Freenode network and help
people with questions when I can.

A common question that I see (and that makes me cringe at the same time) has to
do with understanding threading with Qt and how to make some code they’ve
written work.

People show their code, or examples based on their code, and I often end up
thinking::


    You’re doing it wrong


I know this is a bit of a bold thing to say, perhaps a bit provocative, but at
the same time, I can’t help but think that the (hypothetical) class below is an
incorrect application of object-oriented principles as well as incorrect usage of Qt.

::

    class MyThread : public QThread
    {
    public:
        MyThread()
        {
            moveToThread(this);
        }

        void run();

    signals:
        void progress(int);
        void dataReady(QByteArray);

    public slots:
        void doWork();
        void timeoutHandler();
    };


My #1 biggest gripe with this code is moveToThread(this); I see so many people
using this without understanding what it does.

What does it do, you ask? The moveToThread() function tells Qt to ensure that
event handlers, and by extension signals and slots, are called from the
specified thread context. QThread is the thread interface, so we’re telling the
thread to run code “in itself”.

We’re also doing this before the thread is running as well.
Even though this seems to work, it’s confusing, and not how QThread was designed
to be used (all of the functions in QThread were written and intended to be
called from the creating thread, not the thread that QThread starts).

My impression is that moveToThread(this); creeps into people’s code because they
saw some blog somewhere that used it. A quick web search turns up several of
these blogs, all of which follow the pattern in the class above:

- subclass QThread
- add signals and slots to do work
- test code, see that the slots aren’t called “from the right thread”
- ask google, find moveToThread(this); and comments that “it seems to work when
  I add this”

In my opinion, the problems started at step 1. QThread was designed and is
intended to be used as an interface or a control point to an operating system
thread, not as a place to put code that you want to run in a thread.

We object-oriented programmers subclass because we want to extend or specialize
the base class functionality. The only valid reasons I can think of for
subclassing QThread is to add functionality that QThread doesn’t have, e.g.
perhaps providing a pointer to memory to use as the thread’s stack, or possibly
adding real-time interfaces/support.
Code to download a file, or to query a database, or to do any other kind of
processing should not be added to a subclass of QThread; it should be
encapsulated in an object of it’s own.

Usually, this means simply changing your class to inherit from QObject instead
of QThread and, possibly, changing the class name. QThread has a started()
signal that you can connect to when you need to perform some initialization.


To actually have your code run in the new thread context, you need to
instantiate a QThread and assign your object to that thread using the
moveToThread() function.
Even though you are still using moveToThread() to tell Qt to run your code in a
specific thread context, we are keeping the thread interface separate.
If necessary, it is now possible to have multiple instances of your class
assigned to a single thread, or multiple instances of many different classes
assigned to a single thread. In other words, it’s unnecessary to tie a single
instance of a class to a single thread.



I take much of the blame for the confusion that comes with writing threaded
Qt code. The original QThread class was abstract, so subclassing was necessary.
It wasn’t until Qt 4.4 that QThread::run() gained a default implementation.

Previously, the only way to use QThread was to subclass. With the addition of
thread affinity and support for signal and slot connections between objects of
different affinity, suddenly we have a convenient way of working with threads.

We like convenience, we want to use it. Unfortunately, I realized to late that
forcing people to subclass QThread actually made it harder than it needed to be.

I also take the blame for not getting up-to-date examples and documentation made
to show people how to get the convenience with the minimum amount of headaches.

For now, the best resource I can point at is a blog I wrote several years ago.



Disclaimer: everything you see above is of course opinion. I’ve worked a lot on
these classes, and have a fairly clear idea of how to use them and how not to
use them.


Threading without the headache with QThread
===========================================

.. seealso::

   - http://labs.trolltech.com/blogs/2006/12/04/threading-without-the-headache/
   - :ref:`nzmqt_library`


A couple of weeks ago, I started trying to find out if a pure virtual function
can be made impure without breaking binary compatibility.

“Why ?” you ask ? Because I want to make QThread::run() call QThread::exec() by
default. We all know that threading is difficult to do, mostly because of the
need to lock data, synchronize threads (with a QWaitCondition or QSemaphore,
for example). However, it doesn’t have to be.

Consider the following code snippet::

    // create the producer and consumer and plug them together
    Producer producer;
    Consumer consumer;
    producer.connect(&consumer, SIGNAL(consumed()), SLOT(produce()));
    consumer.connect(&producer, SIGNAL(produced(QByteArray *)), SLOT(consume(QByteArray *)));

    // they both get their own thread
    QThread producerThread;
    producer.moveToThread(&producerThread);
    QThread consumerThread;
    consumer.moveToThread(&consumerThread);

    // go!
    producerThread.start();
    consumerThread.start();



Wouldn’t life be wonderful if it were that easy? The good news is, it already
is, if you do just a small amount of work: subclass QThread and reimplement
run() to simply call exec(). The code snippet above comes from an example [1]
where I’ve done this.

The end result is a solution to the Producer/Consumer problem without the need
for a lock, a condition variable, or a semaphore. Hell, I don’t even have to
write a thread. I can do everything in a nice object oriented way; the Producer
code goes in one place, the Consumer code in another, and then I move these into
the wonderful black boxed thread object that does what I expect.

So what’s the point of all this? I hope to be able to answer my original
question: can a pure virtual function be made impure without breaking binary
compabitlity? If so, I hope to make QThread::run() call exec() in Qt 4.3.


- http://chaos.troll.no/~bhughes/producerconsumer.tar.gz
