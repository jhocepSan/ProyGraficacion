#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PySide.QtGui import *
from PySide.QtCore import *
import sys,time,AreaDibujo
class VentanaPrincipal(QMainWindow):
	def __init__(self):
		super(VentanaPrincipal,self).__init__()
		self.setGeometry(50,60,700,500)
		self.setWindowTitle("Proyecto Graficacion")
		self.sectorGr=AreaDibujo.EspacioDbj(self)
		self.menu()
		self.statusBar().showMessage("Este es la parte de Informacion")
		self.setCentralWidget(self.sectorGr)
	def menu(self):
		self.toolsMenu = self.menuBar().addMenu("&Herramientas")
		limpiar=QAction("&Limpiar",self,shortcut="Ctrl+L",
			statusTip="Limpiar el area de Dibujo",triggered=lambda:self.sectorGr.limpiar())
		self.toolsMenu.addAction(limpiar)
		self.drawMenu=self.menuBar().addMenu("&Dibujar")
		self.drawBrMenu=self.menuBar().addMenu("&Bresenham")
		rectabr=QAction("&Recta", self,shortcut="Ctrl+R",
			statusTip="Recta Bresenham",triggered=lambda:self.rectaBr())
		cirbr=QAction("&Circulo",self,shortcut="Ctrl+C",
			statusTip="Circunferencia Bresenham",triggered=lambda:self.circBr())
		self.drawBrMenu.addAction(rectabr)
		self.drawBrMenu.addAction(cirbr)
	def rectaBr(self):
		for x in range(200):
			self.sectorGr.setCordenada([x,2*x])
			self.sectorGr.update()

def main():
	app=QApplication(sys.argv)
	ventana=VentanaPrincipal()
	ventana.show()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()