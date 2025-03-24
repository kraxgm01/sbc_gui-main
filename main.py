from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader
from mainwindow import MainWindow
import sys


app = QApplication(sys.argv)
window = MainWindow(app)
# loader = QUiLoader()
# window = loader.load("ui/mission_control.ui", None)
window.resize(1336, 768)
window.show()
app.exec()