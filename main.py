import os
import sys
import webbrowser
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit
from PyQt5.QtGui import QPixmap, QIcon

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        btn1 = QPushButton('23층')
        btn1.setCheckable(True)
        self.check = False
        btn1.clicked.connect(self.btn1_clicked)

        self.lbl_img = QLabel()
        self.pixmap = QPixmap(resource_path('23.png'))
        self.lbl_img.setPixmap(self.pixmap)

        btn2 = QPushButton('24층')
        btn2.clicked.connect(lambda: webbrowser.open('https://www.youtube.com/watch?v=tvBfW1m6DiM&t=128s'))

        btn3 = QPushButton('39층')
        btn3.clicked.connect(lambda: webbrowser.open('http://39.theseed.ze.am/'))

        memo = QLineEdit(self)

        vbox = QVBoxLayout()
        hbox = QHBoxLayout()
        hbox.addWidget(btn1)
        hbox.addWidget(btn2)
        hbox.addWidget(btn3)
        vbox.addLayout(hbox)
        vbox.addWidget(self.lbl_img)
        vbox.addWidget(memo)
        self.lbl_img.hide()

        self.setLayout(vbox)
        self.setWindowTitle('더 시드')
        self.setWindowIcon(QIcon(resource_path('seed.ico')))
        self.move(300, 300)
        self.show()

    def btn1_clicked(self):
        if self.check:
            self.lbl_img.hide()
            self.resize(self.minimumSizeHint())
            self.adjustSize()
            self.check = False
        elif not self.check:
            self.lbl_img.show()
            self.check = True


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
