from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QFileDialog
from code.utility.camera import Camera
import cv2

class MainController:
    def __init__(self,widget):
        self.widget = widget
        self.main_timer = QTimer()
        self._camera = Camera.get_instance()

    def start_camera(self):
        self.main_timer.timeout.connect(self.main_loop)
        self.main_timer.setInterval(1)
        self.main_timer.start()

    def capture_image(self):
        self.widget.camera_preview.setText('oppai capture')
        image = self._camera.image
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        filename, _ = QFileDialog.getSaveFileName(self.widget,"Save Image","","Image (*.jpg)", options=options)
        if filename:
            print(filename)
            cv2.imwrite(filename+'.jpg',image)
           
    def main_loop(self):
        if not self._camera.ready:
            return
        self.widget.set_camera_preview(self._camera.converter.pixmap)