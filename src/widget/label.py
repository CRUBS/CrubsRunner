#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# © 2022 Tremaudant Axel
# axel.tremaudant@gmail.com

# This software is a computer program whose purpose is to easily and precisely generate sequential file for robots
# used in the Coupe de France de robotique.

# This software is governed by the CeCILL license under French law and abiding by the rules of distribution of free
# software. You can use, modify and/ or redistribute the software under the terms of the CeCILL license as circulated
# by CEA, CNRS and INRIA at the following URL "http://www.cecill.info".
# As a counterpart to the access to the source code and rights to copy, modify and redistribute granted by the license,
# users are provided only with a limited warranty and the software's author, the holder of the economic rights,
# and the successive licensors have only limited liability.
# In this respect, the user's attention is drawn to the risks associated with loading, using, modifying
# and/or developing or reproducing the software by the user in light of its specific status of free software,
# that may mean that it is complicated to manipulate, and that also
# therefore means that it is reserved for developers and experienced professionals having in-depth computer knowledge.
# Users are therefore encouraged to load and test the software's suitability as regards their requirements in conditions
# enabling the security of their systems and/or data to be ensured and, more generally, to use and operate it
# in the same conditions as regards security.
# The fact that you are presently reading this means that you have had knowledge of the CeCILL license
# and that you accept its terms.


"""
Fichier contenant la classe Label.
"""

from PyQt5 import QtWidgets


class Label(QtWidgets.QLabel):
    """
    Redefinition de QtWidgets.QLabel.
    """
    def __init__(self, text=""):
        """
        Constructeur de Label.
        :param text: str: Texte a ecrire dans le label.
        """
        super(Label, self).__init__(text)
        self.key = None

    def set_key(self, key):
        """
        Definition de la touche correspondant au label.
        :param key: any: Touche
        :return: None
        """
        self.key = key

    def get_key(self):
        """
        Renvoie la touche associee au label
        :return: any: Touche
        """
        return self.key
