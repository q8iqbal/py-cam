from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from code.modul.main.main_view import MainWidget
import sys

class Ui(QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('resource/ui/main_window.ui',self)
        self._init_ui()
    
    def _init_ui(self):
        widget = MainWidget()
        self.setCentralWidget(widget)
        self.show()

def main():
    app = QApplication(sys.argv)
    view = Ui()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()