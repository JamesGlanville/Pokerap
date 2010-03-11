#!/usr/bin/python

# home(x,y,z,all) move(+-(0.1,1,10)mm) extrude (on, off, 1cm)

import glob # wtf is glob?
from random import choice
import re
import sys,os # don't need these
from PyQt4 import QtGui, QtCore # could probably import as * to save typing

class Curry: # I /think/ there's a reason for the name curry. Solves a hard to articulate problem.
	
	
  #keep a reference to all curried instances
  #or they are immediately garbage collected
  instances = []
  def __init__(self, func, *args, **kwargs):
	self.func = func
	self.pending = args[:]
	self.kwargs = kwargs.copy()
	self.instances.append(self)
 
  def __call__(self, *args, **kwargs):
	kw = self.kwargs
	kw.update(kwargs)
	funcArgs = self.pending + args
	#sometimes we want to limit the number of arguments that get passed,
	#calling the constructor with the option __max_args__ = n will limit
	#the function call args to the first n items
	maxArgs = kw.get("__max_args__", -1)
	if maxArgs != -1:
		funcArgs = funcArgs[:maxArgs]
		del kw["__max_args__"]
	return self.func(*funcArgs, **kw)

class Jogger(QtGui.QMainWindow):
	def __init__(self, parent=None):
		QtGui.QMainWindow.__init__(self, parent)

		self.setGeometry(50, 50,350, 420)
		self.setWindowTitle('Jogger')

		self.statusbar = self.statusBar()
		self.connect(self, QtCore.SIGNAL("messageToStatusbar(QString)"), 
		self.statusbar, QtCore.SLOT("showMessage(QString)"))
		
		Bhomeall = QtGui.QPushButton("Home All",self)
		Bhomeall.setGeometry(110,360,90,30)
		self.connect(Bhomeall, QtCore.SIGNAL('clicked()'), self.homeall )
		
		Bhomex = QtGui.QPushButton("Home X",self)
		Bhomex.setGeometry(110,320,90,30)
		self.connect(Bhomex, QtCore.SIGNAL('clicked()'), self.homex )
		
		Bhomey = QtGui.QPushButton("Home Y",self)
		Bhomey.setGeometry(110,280,90,30)
		self.connect(Bhomey, QtCore.SIGNAL('clicked()'), self.homey )
		
		Bhomez = QtGui.QPushButton("Home Z",self)
		Bhomez.setGeometry(110,240,90,30)
		self.connect(Bhomez, QtCore.SIGNAL('clicked()'), self.homez )

		exit = QtGui.QAction(QtGui.QIcon('icons/exit.png'), 'Exit', self)
		exit.setShortcut('Ctrl+Q')
		exit.setStatusTip('Exit application')
		self.connect(exit, QtCore.SIGNAL('triggered()'), QtCore.SLOT('close()'))


		menubar = self.menuBar()	
		file = menubar.addMenu('&File')
		file.addAction(exit)
	
	def homeall(self):
		print "homeall"
	def homex(self):
		print "homex"
	def homey(self):
		print "homey"
	def homez(self):
		print "homez"

	def keyPressEvent(self, event):
		if event.key() == QtCore.Qt.Key_Escape:
			self.close()
		if event.key() == QtCore.Qt.Key_S:
			self.skip()



app = QtGui.QApplication(sys.argv)

va = Jogger()
va.show()

sys.exit(app.exec_())
