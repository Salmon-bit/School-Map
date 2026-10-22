"""This module is the main module of the project.
When you want to run or build the project,
you should use this file as a main module or entrypoint of the program"""
import sys
from PySide6.QtWidgets import QApplication, QWidget
from ui.ui_welcome_screen import Ui_WelcomeScreen
from register_window import RegisterWindow
from login_window import LoginWindow
from main_window import MainWindow


class WelcomeScreen(Ui_WelcomeScreen, QWidget):
    """This class provides a Welcome screen window"""
    def __init__(self, app: QApplication): #pylint: disable=redefined-outer-name
        super().__init__()
        self.app = app

        self.setupUi(self)
        self.rw = None
        self.lw = None
        self.mw = None

        self.register_btn.clicked.connect(self.open_reg_window)
        self.login_btn.clicked.connect(self.open_log_window)

    def open_reg_window(self):
        """This method opens a registration window. If login window was open, it will close it."""
        if self.lw is not None:
            self.lw.destroy()
            self.lw = None
        self.rw = RegisterWindow()
        self.rw.show()

    def open_log_window(self):
        """This method opens a login window. If registration window was open, it will close it."""
        if self.rw is not None:
            self.rw.destroy()
            self.rw = None
        self.lw = LoginWindow(self)
        self.lw.show()

    def open_main_window(
            self,
            username: str,
            email: str,
            school: str):
        """This method opens a main Window. If it already exists, method will reopen it"""
        if self.mw is not None:
            self.mw.destroy()
            self.mw = None
        self.lw.destroy()
        self.lw = None
        self.mw = MainWindow(username, email, school, self, self.app)
        self.mw.show()
        self.hide()

    def quit(self):
        """Quits the program"""
        if self.lw is not None:
            self.lw.destroy()
        if self.rw is not None:
            self.rw.destroy()
        if self.mw is not None:
            self.mw.destroy()
        self.app.quit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ws = WelcomeScreen(app)
    ws.show()
    sys.exit(app.exec())
