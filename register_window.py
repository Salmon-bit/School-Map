"""Register window module"""
import json
import hashlib
from PySide6 import QtWidgets
from ui.ui_registration_form import Ui_Registration


class RegisterWindow(QtWidgets.QWidget, Ui_Registration):
    """This class provides a register screen window"""
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.show_pswd = False
        self.show_pswd_rep = False

        self.show_password.clicked.connect(self.show_password_f)
        self.show_password_rep.clicked.connect(self.show_password_rep_f)

        self.register_2.clicked.connect(self.register)

    def show_password_f(self):
        """This method shows or hides password"""
        if self.show_pswd:
            self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        else:
            self.password.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.show_pswd = not self.show_pswd

    def show_password_rep_f(self):
        """This method shows or hides password"""
        if self.show_pswd_rep:
            self.password_repeat.setEchoMode(QtWidgets.QLineEdit.Password)
        else:
            self.password_repeat.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.show_pswd_rep = not self.show_pswd_rep

    def register(self): # pylint: disable=too-many-return-statements
        """This method handles user registration"""
        username = self.username.text()
        email = self.email.text()
        pswd = self.password.text()
        pswd_rep = self.password_repeat.text()
        school = self.school_select.currentText()

        try:
            with open('save.jsonlines', 'r', encoding='UTF-8') as f:
                users = f.readlines()
        except FileNotFoundError:
            users = []

        if len(username) < 3 or len(username) > 32:
            QtWidgets.QMessageBox.critical(
                self,
                'Ошибка',
                'Длина имени пользователя должна быть от 3 до 32 символов!'
            )
            return
        if "@" not in email:
            QtWidgets.QMessageBox.critical(
                self,
                'Ошибка',
                'Введённый адрес электронной почты не действителен!'
            )
            return
        if pswd != pswd_rep:
            QtWidgets.QMessageBox.critical(
                self,
                'Ошибка',
                'Пароли не совпадают!'
            )
            return
        if len(pswd) < 8:
            QtWidgets.QMessageBox.critical(
                self,
                'Ошибка',
                'Длина пароля должна быть не менее 8 символов!'
            )
            return
        if school == "Школа":
            QtWidgets.QMessageBox.critical(
                self,
                'Ошибка',
                'Выберите какую-нибудь школу!'
            )
            return

        for u in users:
            u = json.loads(u)
            if u['username'] == username:
                QtWidgets.QMessageBox.critical(
                    self,
                    'Ошибка',
                    'Такой пользователь уже существует!'
                )
                return
            if u['email'] == email:
                QtWidgets.QMessageBox.critical(
                    self,
                    'Ошибка',
                    'Пользователь с такой электронной почтой уже существует!'
                )
                return

        with open('save.jsonlines', 'a', encoding='UTF-8') as f:
            dc = {
                'username': username,
                'email': email,
                'password': hashlib.sha256(pswd.encode()).hexdigest(),
                'school': school
            }
            json.dump(dc, f)
            f.write('\n')

        QtWidgets.QMessageBox.information(self, 'Инфо', 'Успешная регистрация!')
