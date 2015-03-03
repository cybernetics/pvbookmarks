#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_xml.py
~~~~~~~~~~~~

Test the xml format


"""

from bs4 import BeautifulSoup
	
def parseLog(filename):
    handler = open(filename).read()
    soup = BeautifulSoup(handler)
    print soup.prettify()


if __name__ == '__main__':
    parseLog('file1.xml')
