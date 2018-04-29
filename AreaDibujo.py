#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PySide.QtCore import *
from PySide.QtGui import *
import sys

class EspacioDbj(QWidget):
	def __init__(self):
		super(EspacioDbj,self).__init__()
		self.setGeometry(0,0,700,500)
		self.imgc=QLabel(self)
		self.imgc.setGeometry(0,0,700,500)
		self.img=QImage(700,500,QImage.Format_RGB32)
		self.color= qRgb(189, 149, 39)  # 0xffbd9527
	def pintar(self,x,y):
		self.img.setPixel(x, y, self.color)
		self.img.save("imagen.jpg","jpg")
		self.imgc.setPixmap(QPixmap('imagen.jpg'))
		self.imgc.show()