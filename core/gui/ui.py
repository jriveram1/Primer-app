from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel
)

class interface_download_youtube(Qwidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def list_components(self):
        self.setWindowTitle("Download Video from Youtube")
        self.resize(500, 500)

app = QApplication([])
window = interface_download_youtube()
window.show()
app.exec()