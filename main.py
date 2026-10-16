import sys
from PySide6.QtWidgets import QApplication, QWidget
from ui.ui_welcome_screen import Ui_WelcomeScreen
from RegisterWindow import RegisterWindow
from LoginWindow import LoginWindow


class WelcomeScreen(Ui_WelcomeScreen, QWidget):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.rw = None
        self.lw = None

        self.register_btn.clicked.connect(self.open_reg_window)
        self.login_btn.clicked.connect(self.open_log_window)

    def open_reg_window(self):
        if self.lw != None:
            self.lw.destroy()
            self.lw = None
        self.rw = RegisterWindow()
        self.rw.show()

    def open_log_window(self):
        if self.rw != None:
            self.rw.destroy()
            self.rw = None
        self.lw = LoginWindow(self)
        self.lw.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ws = WelcomeScreen()
    ws.show()
    sys.exit(app.exec())
