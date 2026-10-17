"""This module is the main module of the project.
When you want to run or build the project,
you should use this file as a main module or entrypoint of the programm"""
import sys
from PySide6.QtWidgets import QApplication, QWidget
from ui.ui_welcome_screen import Ui_WelcomeScreen
from register_window import RegisterWindow
from login_window import LoginWindow


class WelcomeScreen(Ui_WelcomeScreen, QWidget):
    """This class provides a Welocme screen window"""
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.rw = None
        self.lw = None

        self.register_btn.clicked.connect(self.open_reg_window)
        self.login_btn.clicked.connect(self.open_log_window)

    def open_reg_window(self):
        """This method opens a registartion window. If login window was open, it will close it."""
        if self.lw is not None:
            self.lw.destroy()
            self.lw = None
        self.rw = RegisterWindow()
        self.rw.show()

    def open_log_window(self):
        """This method opens a login window. If registartion window was open, it will close it."""
        if self.rw is not None:
            self.rw.destroy()
            self.rw = None
        self.lw = LoginWindow(self)
        self.lw.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ws = WelcomeScreen()
    ws.show()
    sys.exit(app.exec())
