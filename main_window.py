"""Creates Main Window Class"""
import sys
from PySide6.QtWidgets import QMainWindow, QApplication
from ui.ui_main_window import Ui_MainWindow
from database_manager import DatabaseManager
from school_draw import Drawer


class MainWindow(QMainWindow, Ui_MainWindow):
    """Main Window class. The main window of the programm."""
    def __init__(self):
        super().__init__()
        self.dm = DatabaseManager()

        self.setupUi(self)

        parent = self.school_veiw_floor_1.parentWidget()
        geometry = self.school_veiw_floor_1.geometry()

        # 2. Уничтожаем старый пустой QWidget
        self.school_veiw_floor_1.deleteLater()

        # 3. Создаем наш кастомный Drawer на том же месте с тем же родителем
        self.school_veiw_floor_1 = Drawer(parent)
        self.school_veiw_floor_1.setGeometry(geometry)

        # 4. Активируем отрисовку
        self.school_veiw_floor_1.trigger_paint()

    def destroy(self):
        """Rewrite destroy function to automatically close database connection"""
        self.dm.close_connection()
        return super().destroy(True, True)


if __name__  == "__main__":
    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec())
