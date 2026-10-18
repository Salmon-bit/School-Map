"""Login window module"""
import json
import hashlib
from PySide6 import QtWidgets
from ui.ui_login_form import Ui_LoginForm
from database_manager import DatabaseManager

class LoginWindow(QtWidgets.QWidget, Ui_LoginForm):
    """This class provides a login screen window"""
    def __init__(self, parent: QtWidgets.QWidget):
        super().__init__()
        
        self.dm = DatabaseManager()

        self.setupUi(self)
        self.p = parent
        self.password_visible = False

        self.login.clicked.connect(self.login_f)
        self.show_password.clicked.connect(self.show_password_f)

    def login_f(self):
        """This method handles login"""
        account_cred = self.account_cred.text()
        password = self.password.text()

        users = self.dm.get_users()
        if len(users) == 0:
            answer = QtWidgets.QMessageBox.question(
                self,
                'Ошибка',
                'В системе не создано ни одного пользователя.\nСоздать нового пользователя?',
                QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No,
                QtWidgets.QMessageBox.StandardButton.Yes
            )

            if answer == QtWidgets.QMessageBox.StandardButton.Yes:
                self.p.open_reg_window()
                self.destroy()
            else:
                u = []

            return

        for u in users:
            if account_cred in (u[1], u[2])\
                and u[3] == hashlib.sha256(password.encode()).hexdigest():
                # Do something
                QtWidgets.QMessageBox.information(
                    self,
                    'Инфо',
                    'Успешная авторизация!'
                )
                return

        QtWidgets.QMessageBox.critical(
            self,
            'Ошибка',
            'Пользователь с такими учетными данными не найден в системе'
        )

    def show_password_f(self):
        """This methods show or hides password"""
        if self.password_visible:
            self.password.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        else:
            self.password.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)

        self.password_visible = not self.password_visible

    def destroy(self, /, destroyWindow: bool = ..., destroySubWindows: bool = ...) -> None: #pylint: disable=invalid-name
        """Rewrite destroy function to automatically close database connection"""
        self.dm.close_connection()
        return super().destroy(destroyWindow, destroySubWindows)
