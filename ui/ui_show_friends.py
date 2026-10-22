"""Module Show Friends UI"""
import sys
from PySide6.QtWidgets import QWidget, QApplication, QListWidget, QLabel


class ShowFriends(QWidget):
    """Creates UI to show users friends"""
    def __init__(self, username: str, friends: list[str]):
        """Creates UI to show users friends
        
        :param username: Username
        :type username: str
        :param friends: All user friends
        :type friends: list[str]
        """
        super().__init__()
        self.username = username
        self.friends = friends

        self.setup_ui()

    def setup_ui(self):
        """Setups user interface"""
        self.setGeometry(300, 300, 300, 405)
        self.setMaximumSize(300, 405)
        self.setMinimumSize(300, 405)
        self.setWindowTitle("Friends")

        l = QLabel(f'Друзья {self.username}', self)
        l.setGeometry(5, 5, 290, 20)

        self.lv = QListWidget(self)
        self.lv.setGeometry(5, 30, 290, 370)

        self.lv.addItems(self.friends)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    sf = ShowFriends('Олѣгъ', ["Salmon228", 'Wrait_araIt'])
    sf.show()
    sys.exit(app.exec())
