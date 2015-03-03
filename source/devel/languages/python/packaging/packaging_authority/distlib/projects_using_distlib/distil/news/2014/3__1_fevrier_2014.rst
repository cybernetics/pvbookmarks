

.. _distil_news_1_fevrier_2014_3:

==============================
3) Distil news 1 fevrier 2014
==============================

::

    Sujet: Re: [Distutils] PEX at Twitter (re: PEX - Twitter's multi-platform executable archive format for Python)
    Date : Sat, 1 Feb 2014 12:03:34 +0000 (GMT)
    De : Vinay Sajip <vinay_sajip@yahoo.co.uk>
    Pour : Paul Moore <p.f.moore@gmail.com>
    Copie à : DistUtils mailing list <distutils-sig@python.org>

On Sat, 1/2/14, Paul Moore <p.f.moore@gmail.com> wrote:

::

    > I would like it if pip worked the same way (even though the
    > tide of installing pip into each virtualenv may be unstoppable
    > by now). Would you be interested in writing a patch to do this?
    > I don't have the time to commit to it and nobody else seems
    > particularly interested in doing it, which is one reason it's not
    > happened, I suspect. It's certainly not a fundamental limitation
    > of pip.

It's not, and virtualenv does it with -p, right ? Here's the distil code
that does it::

    ARG_RE = re.compile(r'-[ep](=?.*)?')
    # Use encode rather than br'' to avoid syntax error in 2.5, so we can
    # print a more helpful message.
    PYTHON_RE = re.compile(r'Python \d(\.\d+)+'.encode('utf-8'))

    def find_python(env_or_python, is_env):
        result = None
        if not is_env:
            result = env_or_python
        else:
            env = os.path.abspath(env_or_python)
            if os.path.isdir(env):
                from distutils import sysconfig
                exe = 'python%s' % sysconfig.get_config_var('EXE')
                for subdir in ('bin', 'Scripts'):
                    p = os.path.join(env, subdir, exe)
                    if os.path.isfile(p) and os.access(p, os.X_OK):
                        result = p
                        break
        if result:
            import subprocess

            try:
                cmd = [result, '--version']
                p = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                                     stderr=subprocess.STDOUT)
                out, _ = p.communicate()
                if p.returncode:
                    logger.error('Command %r returned non-zero status: %d',
                                 ' '.join(cmd), p.returncode)
                    result = None
                elif not PYTHON_RE.match(out):
                    logger.error('Command %r - unexpected output: %r',
                                 ' '.join(cmd), out)
                    result = None
            except Exception as e:
                logger.exception('Command %r - unexpected exception: %r',
                             ' '.join(cmd), e)
                result = None
        return result

    def find_env_or_python(args=None):
        result = None
        args = (args or sys.argv)[1:]
        nargs = len(args)
        for i, arg in enumerate(args):
            m = ARG_RE.match(arg)
            if m:
                value = m.groups()[0]
                start = i + 1
                if value:
                    if value[0] in '=:':
                        argval = value[1:]
                    else:
                        argval = value
                    end = i + 2
                elif i < (nargs - 1):
                    argval = args[i + 1]
                    end = i + 3
                # if result is set, then start and end indicate the slice to lose
                # from sys.argv. First, validate the env.
                result = find_python(argval, arg[1] =='e')
                if result:
                    del sys.argv[start:end]
                else:
                    if arg[1] == 'e':
                        msg = 'No such environment: %r' % argval
                    else:
                        msg = 'No such Python interpreter: %r' % argval
                    raise ValueError(msg)
        return result

    def main(args=None):
        python = find_env_or_python()
        if python:
            cmd = [python] + sys.argv
            import subprocess
            return subprocess.call(cmd)
        # the rest of the main() logic goes here as normal


::

    > If you'd rather have this as a selling point for distil, then that's
    > fair. But the vast weight of existing pip users and
    > documentation, plus the core support for pip as the preferred
    > default installer encapsulated in PEP 453, is going to make
    > this much less useful to people in practice.

I'm not trying to "sell" distil versus pip, as I've said before, though I do
want it to be better than pip, by trying out different ideas on how to
do things. In my admittedly biased opinion it already is better in numerous
respects, but if people won't see for lack of looking, that's not my loss :-)

The reasons I wouldn't volunteer to add this to pip are:

1. I don't believe I really need to, since the code above is pretty self-
    contained and shouldn't take too long to adapt. So, any obstacles to
    adding it would surely not be technical. Anyone can feel free to add
    the above to pip.

2. I find working on pip painful because of how it works. I have no
    animus against pip; I have overcome this pain in the past and
    did a fair chunk of the work in getting it to work on 2.x and 3.x in
    a single code-base. But that was when I thought it was important
    for 3.x adoption to get pip and virtualenv working under 3.x in a
    low-maintenance fashion (i.e. no 2to3). Of course, I now have the
    use of distil, so I seldom need to use pip :-)

3. I try to avoid "politics" and "religion" in software development when
    I can, and I feel their presence more in the pip project than I'm
    comfortable with. I don't really want to fight non-technical battles.

Re. PEP 453, I voiced my reservations at the time, but if "that ship
has sailed", then so be it - "nobody ever got fired for recommending
pip". The Python community will get the packaging infrastructure that
it deserves, just like a populace does with elections :-)

Regards,

Vinay Sajip
