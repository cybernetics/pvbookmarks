# -*- coding: utf-8 -*-
#
# @file       calc_distance.py
# @author     $Author: pvergain $
# @version    $Revision: 369 $
# @date       $Date: 2011-11-24 09:59:35 +0100 (Thu, 24 Nov 2011) $
#
"""
Sort un tableau de valeurs en fonction de la distance entre le capteur
et un obstacle.

"""

FACTEUR = (4.9 * 1024) / 5000.0
FACTEUR_INV = 5000.0 / (4.9 * 1024)

def calc_puissance(distance):
    """This pin outputs analog voltage with a scaling factor of (Vcc/**1024**) per cm.
       A supply of **5000 mV** yields **~4.9mV/cm.**, and 3.3V yields ~3.2mV/cm.

       FACTEUR = (4.9 * 1024)/5000

       p = d * FACTEUR
    """
    puissance = (distance * FACTEUR)
    return puissance

def calc_distance(puissance):
    """Calcul de la distance en fonction de la puissance.

    d = p * FACTEUR_INV
    """
    distance = (puissance * FACTEUR_INV)
    return puissance

def output_table():
    for distance in range(20,100,1):
        print('distance=', distance, 'puissance=', calc_puissance(distance))

    for puissance in range(20,100,1):
        print('puissance=', puissance, 'distance=', calc_distance(puissance))

if __name__ == '__main__':
    output_table()


