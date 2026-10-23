from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from ui import Ui_MainWindow
from PyQt5.QtCore import QUrl


class Widget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.configure()
        self.media = QMediaPlayer(self)
        self.media.setVideoOutput(self.ui.video)
        self.get_date()

    def configure(self):
        self.ui.start.clicked.connect(self.media_play)
        self.ui.stop.clicked.connect(self.media_stop)
        self.ui.calendar.selectionChanged.connect(self.get_date)

    def media_play(self):
        self.media.play()

    def media_stop(self):
        self.media.stop()

    def get_date(self):
        date = (self.ui.calendar.selectedDate())
        day = str(date.day())
        self.media.setMedia(QMediaContent(QUrl.fromLocalFile(f'Video\\{day}.avi')))
    def configure(self):
        self.ui.start.clicked.connect(self.media_play)
        self.ui.stop.clicked.connect(self.media_stop)
        self.ui.calendar.selectionChanged.connect(self.get_date)

    def get_date(self):
        date = self.ui.calendar.selectedDate()
        day = str(date.day())

        self.media.stop()
        self.media.setMedia(
            QMediaContent(QUrl.fromLocalFile(f'Video\\{day}.avi'))
        )

        if self.ui.autostart.isChecked():
            self.media.play()
        





app = QApplication([])
win = Widget()
win.show()
app.exec_()
