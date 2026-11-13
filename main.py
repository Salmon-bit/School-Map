"""This module is the main module of the project.
When you want to run or build the project,
you should use this file as a main module or entrypoint of the program"""
import sys
import os
import json
from PySide6.QtWidgets import QApplication, QWidget
from ui.ui_welcome_screen import Ui_WelcomeScreen
from register_window import RegisterWindow
from login_window import LoginWindow
from main_window import MainWindow
from database_manager import DatabaseManager


# pylint: disable=too-many-instance-attributes
class WelcomeScreen(Ui_WelcomeScreen, QWidget):
    """This class provides a Welcome screen window"""
    def __init__(self, app: QApplication): #pylint: disable=redefined-outer-name
        super().__init__()
        self.app = app

        self.setupUi(self)
        self.dm = DatabaseManager()
        self.rw = None
        self.lw = None
        self.mw = None

        self.username = ''
        self.email = ''
        self.school = ''

        self.register_btn.clicked.connect(self.open_reg_window)
        self.login_btn.clicked.connect(self.open_log_window)
        self.show_on_start.clicked.connect(self.toggle_checkbox)

        self.show_on_start.setChecked(not os.path.exists('assets/hide_on_start'))

        try:
            os.makedirs('assets', exist_ok=True)
            with open('assets/userdata.json', 'r', encoding='UTF-8', newline='') as f:
                data = json.load(f)
        except FileNotFoundError:
            return

        if os.path.exists('assets/hide_on_start'):
            self.open_main_window(data['username'], data['email'])

    def toggle_checkbox(self):
        """Handles checkbox"""
        os.makedirs('assets', exist_ok=True)
        if not self.show_on_start.isChecked():
            with open('assets/hide_on_start', 'w', encoding='UTF-8'):
                pass
        else:
            try:
                os.remove('assets/hide_on_start')
            except FileNotFoundError:
                pass

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
            email: str):
        """This method opens a main Window. If it already exists, method will reopen it"""
        if self.mw is not None:
            self.mw.destroy()
            self.mw = None
        if self.lw is not None:
            self.lw.destroy()
            self.lw = None
        if self.rw is not None:
            self.rw.destroy()
            self.rw = None
        self.hide()
        self.mw = MainWindow(username, email, self, self.app)
        self.mw.show()

    def quit(self):
        """Quits the program"""
        if self.lw is not None:
            self.lw.destroy()
        if self.rw is not None:
            self.rw.destroy()
        if self.mw is not None:
            self.mw.destroy()
        self.dm.close_connection()
        self.destroy()
        self.app.quit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ws = WelcomeScreen(app)
    if ws.mw is None:
        ws.show()
    sys.exit(app.exec())
