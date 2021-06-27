from PyQt5 import uic
from PyQt5.QtWidgets import QWidget
from code.modul.main.main_controller import MainController

class MainWidget(QWidget):
    def __init__(self):
        super(MainWidget,self).__init__()
        self._page_ctrl = MainController(self)
        self._init_ui()
        self._init_listener()
        
    def _init_ui(self):
        uic.loadUi('resource/ui/main_widget.ui',self)

    def _init_listener(self):
        self.capture_pb.clicked.connect(self._action_capture)
        self.start_pb.clicked.connect(self._action_start)

    def _action_start(self):
        self._page_ctrl.start_camera()

    def _action_capture(self):
        self._page_ctrl.capture_image()

    def set_camera_preview(self, pixmap):
        self.camera_preview.setPixmap(pixmap)
     