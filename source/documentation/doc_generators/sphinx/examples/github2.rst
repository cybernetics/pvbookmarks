
.. index::
   pair: projects using sphinx ; github2
   pair: documentation; paramètres
   pair: python very good exemples;  github2


.. _github2_example:

=============================
github2 using sphinx
=============================


.. seealso::

   - http://packages.python.org/github2/
   - seealso:: :ref:`github2`



This is a Python library implementing all of the features available in
version 2 of the `Github API`_.


.. _`Github API`:  http://develop.github.com/


Example
=======


::

        class Github(object):

            def __init__(self, username=None, api_token=None, requests_per_second=None,
                         access_token=None, cache=None, proxy_host=None,
                         proxy_port=8080):
                """
                An interface to GitHub's API:
                http://develop.github.com/

                .. versionadded:: 0.2.0
                The ``requests_per_second`` parameter
                .. versionadded:: 0.3.0
                The ``cache`` and ``access_token`` parameters
                .. versionadded:: 0.4.0
                The ``proxy_host`` and ``proxy_port`` parameters

                :param str username: your own GitHub username.
                :param str api_token: can be found at https://github.com/account
                (while logged in as that user):
                :param str access_token: can be used when no ``username`` and/or
                ``api_token`` is used. The ``access_token`` is the OAuth access
                token that is received after successful OAuth authentication.
                :param float requests_per_second: indicate the API rate limit you're
                operating under (1 per second per GitHub at the moment),
                or None to disable delays. The default is to disable delays (for
                backwards compatibility).
                :param str cache: a directory for caching GitHub responses.
                :param str proxy_host: the hostname for the HTTP proxy, if needed.
                :param str proxy_port: the hostname for the HTTP proxy, if needed (will
                default to 8080 if a proxy_host is set and no port is set).
                """

            self.request = GithubRequest(username=username, api_token=api_token,
                                         requests_per_second=requests_per_second,
                                         access_token=access_token, cache=cache,
                                         proxy_host=proxy_host,
                                         proxy_port=proxy_port)
            self.issues = Issues(self.request)
            self.users = Users(self.request)
            self.repos = Repositories(self.request)
            self.commits = Commits(self.request)
            self.organizations = Organizations(self.request)
            self.teams = Teams(self.request)
            self.pull_requests = PullRequests(self.request)


    def get_network_meta(self, project):
        """Get Github metadata associated with a project

        :param str project: GitHub project
        """
         return self.request.raw_request("/".join([self.request.github_url,
                                                  project,
                                                  "network_meta"]), {})

    def get_network_data(self, project, nethash, start=None, end=None):
        """Get chunk of Github network data

        :param str project: GitHub project
        :param str nethash: identifier provided by ``get_network_meta``
        :param int start: optional start point for data
        :param int stop: optional end point for data
        """
        data = {"nethash": nethash}
        if start:
            data["start"] = start
        if end:
            data["end"] = end

        return self.request.raw_request("/".join([self.request.github_url,
                                                  project,
                                                  "network_data_chunk"]),
                                                  data)

    def _handle_naive_datetimes(f):
        """Decorator to make datetime arguments use GitHub timezone

        :param func f: Function to wrap
        """
        def wrapper(datetime_):
            if not datetime_.tzinfo:
                datetime_ = datetime_.replace(tzinfo=GITHUB_TZ)
            else:
                datetime_ = datetime_.astimezone(GITHUB_TZ)
            return f(datetime_)
        wrapped = wrapper
        wrapped.__name__ = f.__name__
        wrapped.__doc__ = (
            f.__doc__
            + """\n    .. note:: Supports naive and timezone-aware datetimes"""
        )
        return wrapped


    @_handle_naive_datetimes
    def datetime_to_ghdate(datetime_):
        """Convert Python datetime to Github date string

        :param datetime datetime_: datetime object to convert
        """
        return datetime_.strftime(GITHUB_DATE_FORMAT)
