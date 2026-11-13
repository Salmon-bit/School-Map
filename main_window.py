"""Creates Main Window Class"""
import os
import sys
import webbrowser
from PySide6.QtCore import QSize # pylint: disable=no-name-in-module
from PySide6.QtWidgets import QMainWindow, QApplication, QWidget, QMessageBox
from PySide6.QtWidgets import QInputDialog
import web
from ui.ui_main_window import Ui_MainWindow
from ui.ui_list_widget import ListWidget
from database_manager import DatabaseManager
from school_draw import Drawer
from schedule_editor import ScheduleEdit


class MainWindow(QMainWindow, Ui_MainWindow): # pylint:disable=too-many-instance-attributes
    """Main Window class. The main window of the program."""
    def __init__(self, # pylint: disable=too-many-statements
                 username: str = "",
                 email: str = "",
                 parent: QWidget | None = None,
                 app: QApplication | None = None): #pylint: disable=redefined-outer-name
        super().__init__()

        # Window
        self.sf = None
        self.ss = None
        self.cr = None
        self.ui = None
        self.se = None

        self.dm = DatabaseManager()
        self.parent = parent
        self.username = username
        self.email = email
        self.school = self.dm.get_school_by_username(self.username)

        self.setupUi(self)
        self.setMaximumSize(QSize(800, 600))
        self.setMinimumSize(QSize(800, 600))

        parent = self.school_view_floor_1.parentWidget()
        geometry = self.school_view_floor_1.geometry()

        self.school_view_floor_1.deleteLater()

        self.school_view_floor_1 = Drawer(self.school, 1, parent)
        self.school_view_floor_1.setGeometry(geometry)

        self.school_view_floor_1.trigger_paint()

        if self.parent is not None:
            self.actionExit.triggered.connect(self.parent.quit)
        else:
            if app is not None:
                self.actionExit.triggered.connect(exit)
            else:
                sys.exit(1)

        # Status bar update
        self.actionExit.setStatusTip('Выйти из программы')
        self.actionAddFriendByEmail.setStatusTip('Добавить нового друга используя его почту')
        self.actionAddFriendById.setStatusTip(
            'Добавить нового друга используя его уникальный идентификатор'
        )
        self.actionAddFriendByUsername.setStatusTip(
            'Добавить нового друга используя его имя пользователя'
        )
        self.actionAddSchedule.setStatusTip('Добавить новое расписание в Ваш профиль')
        self.actionChangeSchool.setStatusTip('Изменить Вашу школу на новую из списка')
        self.actionCredits.setStatusTip('Посмотреть информацию о создателях программы')
        self.actionEditSchedule.setStatusTip('Изменить Ваше расписание в профиле')
        self.actionEULA.setStatusTip('Посмотреть пользовательское соглашение')
        self.actionHelp.setStatusTip(
            'Перейти на WEB-страницу с документацией по использованию программы'
        )
        self.actionLicense.setStatusTip(
            'Перейти на WEB-страницу с лицензией, которую использует данный продукт'
        )
        self.actionRemoveSchedule.setStatusTip('Удалить Ваше расписание из профиля')
        self.actionUserInfo.setStatusTip('Посмотреть информацию о Вас')
        self.actionViewFriends.setStatusTip('Посмотреть Ваших друзей')
        self.actionViewStudents.setStatusTip('Посмотреть учеников, которые учатся в Вашей школе')
        self.floor_1.setStatusTip('Схема первого этажа Вашей школы')
        self.floor_2.setStatusTip('Схема второго этажа Вашей школы')
        self.smallerView.setStatusTip('Увеличить масштаб схемы выбранного Вами этажа')
        self.biggerView.setStatusTip('Уменьшить масштаб схемы выбранного Вами этажа')
        self.resetView.setStatusTip(
            'Вернуть масштаб схемы выбранного Вами этажа к значению по умолчанию'
        )

        # Friends section
        self.actionAddFriendById.triggered.connect(self.add_friend_by_id)
        self.actionAddFriendByEmail.triggered.connect(self.add_friend_by_email)
        self.actionAddFriendByUsername.triggered.connect(self.add_friend_by_username)
        self.actionViewFriends.triggered.connect(self.view_friends)

        # School section
        self.actionViewStudents.triggered.connect(self.view_students)

        # Schedule section
        self.actionAddSchedule.triggered.connect(self.add_schedule)

        # Program section
        self.actionHelp.triggered.connect(self.open_help)
        self.actionCredits.triggered.connect(self.open_credits)
        self.actionUserInfo.triggered.connect(self.view_user_info)
        self.actionLicense.triggered.connect(self.view_license)
        self.actionEULA.triggered.connect(self.view_eula)

    def add_schedule(self):
        """Opens schedule editor window"""
        if self.se is not None:
            self.se.destroy()
            self.se = None

        self.se = ScheduleEdit(self.dm.get_id_by_username(self.username))
        self.se.show()

    @staticmethod
    def view_eula():
        """Opens a new tab in browser with EULA"""
        webbrowser.open(
            url='https://github.com/Salmon-bit/School-Map/blob/main/EULA.md',
            new=2
        )

    @staticmethod
    def view_license():
        """Opens a new tab in browser with License"""
        webbrowser.open(
            url='https://github.com/Salmon-bit/School-Map?tab=MIT-1-ov-file',
            new=2
        )

    def view_user_info(self):
        """Opens a new window that shows user info"""
        if self.ui is not None:
            self.ui = None

        self.ui = ListWidget(
            'Пользователь',
            [
                f"ID: {self.dm.get_id_by_username(self.username)}",
                f"Имя пользователя: {self.username}",
                f"E-Mail: {self.dm.get_email_by_username(self.username)}",
                f"Школа: {self.dm.get_school_by_username(self.username)}"
            ],
            'User'
        )
        self.ui.show()

    def open_credits(self):
        """Opens a new window that shows developers"""
        if self.cr is not None:
            self.cr = None

        web.get_devs()
        try:
            os.makedirs('assets', exist_ok=True)
            with open('assets/devs.txt', 'r', encoding='UTF-8', newline='') as f:
                devs = [l.strip() for l in f.readlines()]
        except FileNotFoundError:
            devs = [
                "Не удалось получить список разработчиков.\n\
Проверьте своё интернет-подключение."
            ]
        self.cr = ListWidget(
            "Создатели:",
            devs,
            "Developers"
        )
        self.cr.show()

    @staticmethod
    def open_help():
        """Opens a GitHub Readme"""
        webbrowser.open("https://github.com/Salmon-bit/School-Map/blob/main/README.md", 2)

    def view_friends(self):
        """Opens window that shows user friends"""
        f = self.dm.get_user_friends(self.dm.get_id_by_username(self.username))
        f = list(map(self.dm.get_username_by_id, f))
        self.sf = ListWidget(self.username, f, 'Friends')
        self.sf.show()

    def view_students(self):
        """Opens a new window that shows students in school"""
        print(self.username)
        f = self.dm.get_students(self.dm.get_school_by_username(self.username))
        f = list(map(self.dm.get_username_by_id, f))
        self.school = self.dm.get_school_by_username(self.username)
        self.ss = ListWidget(f'Ученики школы \"{self.school}\"', f, "Students")
        self.ss.show()

    def destroy(self):
        """Rewrite destroy function to automatically close database connection"""
        self.dm.close_connection()
        return super().destroy(True, True)

    def add_friend_by_id(self):
        """Adds friend by id"""
        uid_2, result = QInputDialog.getInt(
            self,
            'Добавить друга по ID',
            'Введите ID пользователя, которого хотите добавить  друзья:',
            1,
            1
        )
        if result:
            try:
                uid_1 = self.dm.get_id_by_username(self.username)
                self.dm.add_friends(uid_1, uid_2)
            except ValueError as e:
                QMessageBox.critical(self, 'Ошибка!', e.args[0])
                return

            QMessageBox.information(
                self,
                'Инфо',
                f'Вы с {self.dm.get_username_by_id(uid_2)} успешно стали друзьями!'
            )

    def add_friend_by_email(self):
        """Adds friend by email"""
        email_2, result = QInputDialog.getText(
            self,
            'Добавить друга по E-Mail',
            'Введите E-Mail друга, которого хотите добавить в друзья:'
        )
        if result:
            uid_2 = self.dm.get_id_by_email(email_2)
            print(uid_2)
            if uid_2 == '':
                QMessageBox.critical(
                    self,
                    'Ошибка!',
                    'Пользователя с таким E-Mail не существует в системе!'
                )
                return
            uid_1 = self.dm.get_id_by_email(self.email)
            print(uid_1, uid_2)
            try:
                self.dm.add_friends(uid_1, uid_2)
            except ValueError as e:
                QMessageBox.critical(self, 'Ошибка!', e.args[0])
                return

            QMessageBox.information(
                self,
                'Инфо',
                f'Вы с {self.dm.get_username_by_email(email_2)} успешно стали друзьями!'
            )

    def add_friend_by_username(self):
        """Adds friend by username"""
        us_2, result = QInputDialog.getText(
            self,
            'Добавить друга по имени пользователя',
            'Введите имя пользователя человека, с которым вы хотите стать друзьями:'
        )
        if result:
            uid_2 = self.dm.get_id_by_username(us_2)
            if uid_2 == '':
                QMessageBox.critical(
                    self,
                    'Ошибка!',
                    'Пользователя с таким именем пользователя не существует в системе!'
                )
                return
            uid_1 = self.dm.get_id_by_username(self.username)
            try:
                self.dm.add_friends(uid_1, uid_2)
            except ValueError as e:
                QMessageBox.critical(self, 'Ошибка!', e.args[0])
                return

            QMessageBox.information(
                self,
                'Инфо',
                f'Вы с {us_2} успешно стали друзьями!'
            )


if __name__  == "__main__":
    app = QApplication(sys.argv)
    mw = MainWindow('Salmon228', app=app)
    mw.show()
    sys.exit(app.exec())
