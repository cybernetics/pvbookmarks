

.. index::
   pair: cli ; Example1

.. _python_cli_example1:

=======================
Python cli exxample1
=======================


::

    """
    This gist is a one-click pip setup for windows:

     1. installs distribute if needed
     2. installs pip
     3. (On windows) sets the path environment variable so "pip" is always runnable from cmd.

    Tested on Windows 7 with python2.7
    """

    import subprocess
    try:
        from urllib import urlopen
    except ImportError:
        # py3k
        from urllib.request import urlopen
    import os
    import tarfile
    import platform
    import sys

    distribute_url = 'http://pypi.python.org/packages/source/d/distribute/distribute-0.6.32.tar.gz'
    get_pip_url = 'https://raw.github.com/pypa/pip/master/contrib/get-pip.py'

    python = sys.executable

    def download(url):
        print('downloading %s' % url)
        fname = os.path.basename(url)
        with open(fname, 'wb') as f:
            data = urlopen(url).read()
            f.write(data)
            
        return fname

    def run(line):
        return subprocess.check_output(line, shell=True)

    def add_path_env_windows(new_path):
        # checks both user and system path
        path_str = os.environ['path']
        if new_path.lower() in path_str.lower():
            return
        else:
            print('Adding pip to user path')
            # Add to user path
            # The system path "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Environment"
            # may not be writable using setx /m because of permissions.
            output = run('reg query "HKEY_CURRENT_USER\Environment" /v path')
            output = output.decode(sys.stdout.encoding)
            previous_path = output.split('    ')[3].strip(';\r\n')
            total_path_str = previous_path + ';' + new_path
            execline = 'setx path "%s"' % total_path_str
            if hasattr(execline, 'decode'):
                # python 2
                run(execline.encode(sys.getfilesystemencoding()))
            else:
                # python 3
                run(execline)

    def main():
        try:
            import setuptools
        except ImportError:
            # install distribute
            fname = download(distribute_url)
            
            with tarfile.open(fname) as tar:
                dirname = tar.getnames()[0]
                tar.extractall()
            run(python + ' %s/setup.py install' % dirname)
        
        try:
            import pip
        except ImportError:
            pipf = download(get_pip_url)
            run(python + ' %s' % pipf)
        
        if platform.system() == 'Windows':
            # add to environment path e.g. "C:\python27\Scripts" so you can run "pip"
            # in the command line
            add_path_env_windows(os.path.join(sys.exec_prefix, 'Scripts'))

    main()

