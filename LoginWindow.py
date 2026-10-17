import json
import hashlib
from PySide6 import QtWidgets
from ui.ui_login_form import Ui_LoginForm


class LoginWindow(QtWidgets.QWidget, Ui_LoginForm):
    def __init__(self, parent):
        super().__init__()

        self.setupUi(self)
        self.p = parent
        self.password_visible = False

        self.login.clicked.connect(self.login_f)
        self.show_password.clicked.connect(self.show_password_f)

    def login_f(self):
        """This method handles login"""
        account_cred = self.account_cred.text()
        password = self.password.text()

        try:
            with open('save.jsonlines', 'r', encoding='UTF-8') as f:
                users = f.readlines()
        except FileNotFoundError:
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
            u = json.loads(u)

            if (u['username'] == account_cred or u['email'] == account_cred)\
                and u['password'] == hashlib.sha256(password.encode()).hexdigest():
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

