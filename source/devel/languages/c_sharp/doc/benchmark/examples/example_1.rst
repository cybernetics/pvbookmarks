



==========================
C♯  Stopwatch.StartNew()
==========================

.. seealso:: http://www.dotnetperls.com/benchmark



::

    using System;
    using System.Diagnostics;

    class Program
    {
        static void Main()
        {
            const int m = 1000000;
            Stopwatch s1 = Stopwatch.StartNew();
            for (int i = 0; i < m; i++)
            {

            }
            s1.Stop();

            Stopwatch s2 = Stopwatch.StartNew();
            for (int i = 0; i < m; i++)
            {

            }
            s2.Stop();

            Stopwatch s3 = Stopwatch.StartNew();
            for (int i = 0; i < m; i++)
            {

            }
            s3.Stop();

            Console.WriteLine("{0},{1},{2}",
                s1.ElapsedMilliseconds,
                s2.ElapsedMilliseconds,
                s3.ElapsedMilliseconds);
            Console.Read();
        }
    }


