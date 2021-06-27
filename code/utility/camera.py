import cv2
import sys
from PyQt5.QtCore import QThread
from PyQt5.QtGui import QImage, QPixmap

class Camera(QThread):
	__instance = None

	@staticmethod
	def get_instance():
		if Camera.__instance == None :
			Camera()
		return Camera.__instance

	def run(self):
		self.capture()

	def __init__(self):
		super(Camera, self).__init__()
		if Camera.__instance != None:
			raise Exception("this is singleton dude")
		else:
			self.image = None
			self.ready = False
			self.converter = ConverterPixmap()
			self.converter.start()
			self.init_cvcamera()
			self.start()
			Camera.__instance = self

	def init_cvcamera(self):
		self.camera = cv2.VideoCapture(0)
		self.camera.set(3, 1920)
		self.camera.set(4, 1080)

	def capture(self):
		while True:
			ret, im = self.camera.read()
			self.image = im
			self.converter.setImageInput(im)
			if not self.ready:
				self.ready = True		

class ConverterPixmap(QThread):
	def __init__(self):
		super(ConverterPixmap, self).__init__()
		self.ready = False

	def run(self):
		while(True):
			if(self.ready==False):
				continue
			height, width, channel = self.image.shape
			bytesPerLine = 3 * width
			cvRGBImg = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
			qImg = QImage(cvRGBImg.data, width , height, bytesPerLine, QImage.Format_RGB888)
			pixmap = QPixmap.fromImage(qImg)
			self.pixmap = pixmap

	def setImageInput(self,image):
		self.image = image
		self.ready = True

