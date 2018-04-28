#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PySide.QtCore import *
from PySide.QtGui import *
import sys

class EspacioDbj(QWidget):
	def __init__(self,parent=None):
		super(EspacioDbj,self).__init__(parent=parent)
		self.cordenada=None
		self.setGeometry(0,0,200,100)
		self.update()
	def paintEvent(self,even):
		if self.cordenada:
			self.scene=QPainter(self)
			self.scene.begin(self)
			self.scene.setBackground(Qt.blue)
			self.scene.setPen(Qt.blue)
			self.scene.drawPoint(self.cordenada[0],self.cordenada[1])
			self.scene.end()
		#parent.paintEvent(self,even)
	def setCordenada(self,dato):
		self.cordenada=dato