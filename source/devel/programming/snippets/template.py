#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
On a souvent besoin de répéter des séquences de code pour des tableaux.

Une des façons de le faire est d'utiliser Python
"""

from string import Template

def repeat_param(nb_times):
	for i in range(nb_times):
		print "new CParam( ", i, ")"


def repeat_for_calc(nb_times):
	"""
	"""
	for i in range(nb_times):
		data = '=B{0}-C{0}'.format(i)
		print data

def repeat_data(nb_times):
	s = Template('= new ($who, 4, $what)')

if __name__ == "__main__":
	repeat_for_calc(27)
