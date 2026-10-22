"""Creates Main Window Class"""
import sys
from PySide6.QtWidgets import QMainWindow, QApplication, QWidget
from ui.ui_main_window import Ui_MainWindow
from ui.ui_show_friends import ShowFriends
from database_manager import DatabaseManager
from school_draw import Drawer


class MainWindow(QMainWindow, Ui_MainWindow):
    """Main Window class. The main window of the program."""
    def __init__(self,
                 username: str = "",
                 email: str = "",
                 school: str = "",
                 parent: QWidget | None = None,
                 app: QApplication | None = None): #pylint: disable=redefined-outer-name
        super().__init__()

        # Window
        self.sf = None

        self.dm = DatabaseManager()
        self.parent = parent
        self.username = username
        self.email = email
        self.school = school

        self.setupUi(self)

        parent = self.school_view_floor_1.parentWidget()
        geometry = self.school_view_floor_1.geometry()

        self.school_view_floor_1.deleteLater()

        self.school_veiw_floor_1 = Drawer(parent)
        self.school_veiw_floor_1.setGeometry(geometry)

        self.school_veiw_floor_1.trigger_paint()

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

        self.actionViewFriends.triggered.connect(self.veiw_friends)

    def veiw_friends(self):
        """Opens window that shows user friends"""
        f = self.dm.get_user_friends(self.dm.get_id_by_username(self.username))
        f = list(map(self.dm.get_username_by_id, f))
        self.sf = ShowFriends(self.username, f)
        self.sf.show()

    def destroy(self):
        """Rewrite destroy function to automatically close database connection"""
        self.dm.close_connection()
        return super().destroy(True, True)

if __name__  == "__main__":
    app = QApplication(sys.argv)
    mw = MainWindow('Salmon228', app=app)
    mw.show()
    sys.exit(app.exec())
