"""Module Show Friends UI"""
import sys
from PySide6.QtWidgets import QWidget, QApplication, QListWidget, QLabel


class ListWidget(QWidget):
    """Creates UI to show users friends"""
    def __init__(self, label_text: str, items: list[str], title: str):
        """Creates UI to show users friends
        
        :param username: Username
        :type username: str
        :param friends: All user friends
        :type friends: list[str]
        :param title: The window title
        :type title: str
        """
        super().__init__()
        self.label_text = label_text
        self.items = items
        self.title = title

        self.setup_ui()

    def setup_ui(self):
        """Setups user interface"""
        self.setGeometry(300, 300, 300, 405)
        self.setMaximumSize(300, 405)
        self.setMinimumSize(300, 405)
        self.setWindowTitle(self.title)

        l = QLabel(self.label_text, self)
        l.setGeometry(5, 5, 290, 20)

        self.lv = QListWidget(self)
        self.lv.setGeometry(5, 30, 290, 370)

        self.lv.addItems(self.items)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    sf = ListWidget('Олѣгъ', ["Salmon228", 'Wrait_araIt'], "Friends")
    sf.show()
    sys.exit(app.exec())
