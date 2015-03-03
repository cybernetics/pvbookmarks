#! /usr/bin/python
# A small script, which checks Sphinx reStructured Text (.rst) files for various inconsistencies and errors so as to save
# bandwidth by catching some of the most obvious problems before the document is sent off for review.

import glob
import sys

class RestructuredTextChecker:

    def __init__(self):
        pass

    def load(self, filename, stderr=sys.stdout):
        stream = open(filename, "rt")
        number = 0                      # line number
        last   = ""                     # last/previous line
        while 1:
            # read yet another line
            line = stream.readline()

            # if None, we're at the end of the input
            if not line:
                break

            # increment line number
            number += 1

            # drop trailing newline, if any
            if line[-1] == '\n':
                line = line[:-1]

            # check for trailing whitespace
            if line.rstrip() != line:
                stderr.write("(%s %d) Warning: Trailing whitespace detected\n" % ( filename, number ))
                line = line.rstrip()   # make comparisons of marker text possible

            # check for too short or too long section marker
            if len(line) > 0 and line[0] in "=-^":
                if last != "" and len(line) < len(last):
                    stderr.write("(%s %d) Warning: Marker line too short\n" % ( filename, number ))
                elif last != "" and len(line) > len(last):
                    stderr.write("(%s %d) Warning: Marker line too long\n" % ( filename, number ))
                last = ""             # disable line-too-long check of section headers
                continue

            # check for too long lines (in excess of 79 characters)
            if len(last) > 79:
                stderr.write("(%s %d) Warning: Line exceeds 79 characters\n" % ( filename, number - 1 ))

            # todo: add other checks as they are discovered and deemed usable

            # save this line for possible future marker comparison
            last = line

        stream.close()


def main(args):
     # redirect all output to stdout (stderr belongs to the `yes` family of utterly insane inventions).
     output = sys.stdout

     # if no args given, show help
     if len(args) == 0:
         output.write("reStructured Text Checker v0.03\n")
         output.write("Copyright (C) 2012 The LLVM Team.  All Rights Reserved.\n")
         output.write("\n")
         output.write("Syntax: \"chkrst\" source-file(s)\n")
         output.write("\n")
         output.write("Scans and checks .rst files for obvious yet embarrassing errors.\n")
         return 0

     # expand wildcards in arguments
     files = []
     for arg in args:
         found = glob.glob(arg)
         if found == []:
             output.write("Warning: Pattern '%s' not matched\n" % arg)
         files += found

     # process each file in turn
     for file in files:
         checker = RestructuredTextChecker()
         checker.load(file, output)
         del checker

     return 0
         

if __name__ == "__main__":
    result = main(sys.argv[1:])
    sys.exit(result)
