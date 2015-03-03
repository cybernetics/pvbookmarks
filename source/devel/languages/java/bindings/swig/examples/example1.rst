



.. _java_swig_example_1:

==================
Java swig example1
==================


.. seealso::

   - http://www.swig.org/tutorial.html


Building a Java module
======================

So you want to get going in a hurry? To illustrate the use of SWIG, suppose you
have some C functions you want added to Tcl, Perl, Python, Java and C#.

Specifically, let's say you have them in a file 'example.c'::

    /* File : example.c */

    #include <time.h>
    double My_variable = 3.0;

    int fact(int n) {
     if (n <= 1) return 1;
     else return n*fact(n-1);
    }

    int my_mod(int x, int y) {
     return (x%y);
    }

    char *get_time()
    {
     time_t ltime;
     time(&ltime);
     return ctime(&ltime);
    }



(swig) Interface file
=====================

Now, in order to add these files to your favorite language, you need to write
an "interface file" which is the input to SWIG. An interface file for these
C functions might look like this::

    /* example.i */
    %module example
    %{
    /* Put header files here or function declarations like below */
    extern double My_variable;
    extern int fact(int n);
    extern int my_mod(int x, int y);
    extern char *get_time();
    %}

    extern double My_variable;
    extern int fact(int n);
    extern int my_mod(int x, int y);
    extern char *get_time();


SWIG will also generate JNI code for accessing C/C++ code from Java. Here is
an example building a Java module (shown for Cygwin, see the SWIG Wiki Shared
Libraries page for help with other operating systems)::

    $ swig -java example.i
    $ gcc -c example.c example_wrap.c -I/c/jdk1.3.1/include -I/c/jdk1.3.1/include/win32
    $ gcc -shared example.o  example_wrap.o -mno-cygwin -Wl,--add-stdcall-alias  -o example.dll
    $ cat main.java
    public class main {
    public static void main(String argv[]) {
     System.loadLibrary("example");
     System.out.println(example.getMy_variable());
     System.out.println(example.fact(5));
     System.out.println(example.get_time());
    }
    }
    $ javac main.java
    $ java main
    3.0
    120
    Mon Mar  4 18:20:31  2002
    $



