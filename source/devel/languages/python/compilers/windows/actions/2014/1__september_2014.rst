


.. _python_windows_compilers_2014:

======================================
Windows compilers for Python 2014
======================================



September 2014
==============


::

    Olivier Grisel wrote:
    > Thank you very Steve for pushing that installer out, this is very appreciated.
    >
    > What is the story for project maintainers who want to also support Python 3.3+
    > (for 32 bit and 64 bit python) for their project with binary wheels for windows?
    > At the moment it's possible to use the Windows SDK as documented here:
    >
    > http://scikit-learn.org/dev/install.html#building-on-windows
    >
    > However getting VC Express + Windows SDK is hard and slow to setup and cannot be
    > scripted in a CI environment.

    It can be, but there are a few tricks involved...

    > In the mean time, it's possible to use CI environments that already feature all
    > the necessary versions of the VC compilers and libraries such as appveyor.com,
    > see this demo project:
    >
    > https://github.com/ogrisel/python-appveyor-demo
    > https://ci.appveyor.com/project/ogrisel/python-appveyor-demo

    This is the best way to have it set up - create a base VM image for your 
    CI environment manually and clone it. I believe all the major cloud providers 
    support this, though using a CI specialist like Appveyor makes it even easier.

    As far as the future story, it will probably be "move to 3.5 on VC14 as soon 
    as possible". Internally, I'll be pushing for a CI-compatible installer for 
    our build tools, which I expect will actually get quite a bit of traction right now.

    Unfortunately, going back in time to do it for both VC9 and VC10 was not an 
    option. We chose VC9 because 2.7 is where people are stuck, while migrating 
    from 3.3->3.5 should not be as big an issue.

    Cheers,
