"""Provides a Schedule Editor class"""
import json
import sys
from PySide6.QtGui import QCloseEvent
from PySide6.QtWidgets import QApplication, QWidget, QInputDialog, QMessageBox, QListWidget
from ui.ui_schedule_editor import Ui_ScheduleEdit
from database_manager import DatabaseManager


class ScheduleEdit(Ui_ScheduleEdit, QWidget):
    def __init__(self, user_id):
        """Inits the class"""
        super().__init__()

        self.setupUi(self)
        self.user_id = user_id
        self.db = DatabaseManager()

        self.schedule = {}
        self.lessons = [0, 0, 0, 0, 0, 0]
        self.lesson_timings = []

        self.addLEssonBtn.clicked.connect(self.add_lesson)
        self.pushButton.clicked.connect(self.exit)
        self.deleteLesson.clicked.connect(self.delete_last_lesson)
        self.editLesson.clicked.connect(self.edit_lesson)

        self.schedule = json.loads(self.db.get_schedule(self.user_id))
        print(self.schedule)
        self.draw_lessons()
        
        self.count_lessons()

        print(self.lessons)

    def count_lessons(self):
        for key in self.schedule:
            print(key)
            day = 0
            match key:
                case 'Mn':
                    day = 0
                case 'Tu':
                    day = 1
                case 'Wd':
                    day = 2
                case 'Th':
                    day = 3
                case 'Fr':
                    day = 4
                case 'St':
                    day = 5
            self.lessons[day] = len(self.schedule[key])

        print(self.lessons)

    def count_lesson_times(self):
        """Calculates lesson start and lesson end time"""
        time = self.timeEdit_6.dateTime().time()

        self.lesson_timings.append([f'{time.hour()}:{time.minute()}', ''])
        time = time.addSecs(self.lessonDur_6.value() * 60)
        self.lesson_timings[0][1] = f'{time.hour()}:{time.minute()}'

        time = time.addSecs(self.breakDur_6.value() * 60)

        self.lesson_timings.append([f'{time.toString("HH:mm")}', ''])
        time = time.addSecs(self.lessonDur_6.value() * 60)
        self.lesson_timings[1][1] = f'{time.toString("HH:mm")}'

        if self.checkBox.isChecked():
            time = time.addSecs(self.longBreakDur_6.value() * 60)
        else:
            time = time.addSecs(self.breakDur_6.value() * 60)

        self.lesson_timings.append([f'{time.toString("HH:mm")}', ''])
        time = time.addSecs(self.lessonDur_6.value() * 60)
        self.lesson_timings[2][1] = f'{time.toString("HH:mm")}'

        if self.checkBox_2.isChecked():
            time = time.addSecs(self.longBreakDur_6.value() * 60)
        else:
            time = time.addSecs(self.breakDur_6.value() * 60)

        self.lesson_timings.append([f'{time.toString("HH:mm")}', ''])
        time = time.addSecs(self.lessonDur_6.value() * 60)
        self.lesson_timings[3][1] = f'{time.toString("HH:mm")}'

        if self.checkBox_3.isChecked():
            time = time.addSecs(self.longBreakDur_6.value() * 60)
        else:
            time = time.addSecs(self.breakDur_6.value() * 60)

        self.lesson_timings.append([f'{time.toString("HH:mm")}', ''])
        time = time.addSecs(self.lessonDur_6.value() * 60)
        self.lesson_timings[4][1] = f'{time.toString("HH:mm")}'

        if self.checkBox_4.isChecked():
            time = time.addSecs(self.longBreakDur_6.value() * 60)
        else:
            time = time.addSecs(self.breakDur_6.value() * 60)

        self.lesson_timings.append([f'{time.toString("HH:mm")}', ''])
        time = time.addSecs(self.lessonDur_6.value() * 60)
        self.lesson_timings[5][1] = f'{time.toString("HH:mm")}'

        if self.checkBox_5.isChecked():
            time = time.addSecs(self.longBreakDur_6.value() * 60)
        else:
            time = time.addSecs(self.breakDur_6.value() * 60)

        self.lesson_timings.append([f'{time.toString("HH:mm")}', ''])
        time = time.addSecs(self.lessonDur_6.value() * 60)
        self.lesson_timings[6][1] = f'{time.toString("HH:mm")}'

        if self.checkBox_6.isChecked():
            time = time.addSecs(self.longBreakDur_6.value() * 60)
        else:
            time = time.addSecs(self.breakDur_6.value() * 60)

        self.lesson_timings.append([f'{time.toString("HH:mm")}', ''])
        time = time.addSecs(self.lessonDur_6.value() * 60)
        self.lesson_timings[7][1] = f'{time.toString("HH:mm")}'

        time = time.addSecs(self.breakDur_6.value() * 60)

        self.lesson_timings.append([f'{time.toString("HH:mm")}', ''])
        time = time.addSecs(self.lessonDur_6.value() * 60)
        self.lesson_timings[8][1] = f'{time.toString("HH:mm")}'

        # Disable configuration section
        self.breakDur_6.setDisabled(True)
        self.longBreakDur_6.setDisabled(True)
        self.lessonDur_6.setDisabled(True)
        self.timeEdit_6.setDisabled(True)
        # Disable checkboxes
        self.checkBox.setDisabled(True)
        self.checkBox_2.setDisabled(True)
        self.checkBox_3.setDisabled(True)
        self.checkBox_4.setDisabled(True)
        self.checkBox_5.setDisabled(True)
        self.checkBox_6.setDisabled(True)

        print(self.lesson_timings)

    def draw_lessons(self):
        """Shows added lessons"""
        self.mn_lw.clear()
        self.tu_lw.clear()
        self.wd_lw.clear()
        self.th_lw.clear()
        self.fr_lw.clear()
        self.st_lw.clear()

        self.mn_lw.addItems([f'{i[0]} в каб. {i[1]} ({i[2]} - {i[3]})' for i in self.schedule.get('Mn', [])])
        self.tu_lw.addItems([f'{i[0]} в каб. {i[1]} ({i[2]} - {i[3]})' for i in self.schedule.get('Tu', [])])
        self.wd_lw.addItems([f'{i[0]} в каб. {i[1]} ({i[2]} - {i[3]})' for i in self.schedule.get('Wd', [])])
        self.th_lw.addItems([f'{i[0]} в каб. {i[1]} ({i[2]} - {i[3]})' for i in self.schedule.get('Th', [])])
        self.fr_lw.addItems([f'{i[0]} в каб. {i[1]} ({i[2]} - {i[3]})' for i in self.schedule.get('Fr', [])])
        self.st_lw.addItems([f'{i[0]} в каб. {i[1]} ({i[2]} - {i[3]})' for i in self.schedule.get('St', [])])

    def delete_last_lesson(self):
        """Deletes last lesson in selected day of week"""

        day = 0
        match self.tabWidget.currentWidget().objectName():
            case 'Mn':
                day = 0
            case 'Tu':
                day = 1
            case 'Wd':
                day = 2
            case 'Th':
                day = 3
            case 'Fr':
                day = 4
            case 'St':
                day = 5

        if self.lessons[day] == 0:
            return

        self.schedule[self.tabWidget.currentWidget().objectName()] = \
            self.schedule.get(self.tabWidget.currentWidget().objectName(), [])[:-1]

        self.count_lessons()
        self.draw_lessons()

    def edit_lesson(self):
        selected_lesson: QListWidget = self.tabWidget.currentWidget().children()[0]

    def add_lesson(self):
        """Adds new lesson to the schedule"""
        cur_day = self.tabWidget.currentWidget()

        self.count_lesson_times()

        lesson_name, result = QInputDialog.getText(
            self,
            "Добавление урока",
            "Введите название урока"
        )

        if result:
            cab, result_2 = QInputDialog.getInt(
                self,
                "Добавление урока",
                "Введите номер кабинета"
            )
            if result_2:
                day = 0
                match cur_day.objectName():
                    case 'Mn':
                        day = 0
                    case 'Tu':
                        day = 1
                    case 'Wd':
                        day = 2
                    case 'Th':
                        day = 3
                    case 'Fr':
                        day = 4
                    case 'St':
                        day = 5

                if self.lessons[day] >= 9:
                    QMessageBox.critical(
                        self,
                        'Ошибка',
                        'Нелья добавить более 9-ти уроков в один день!'
                    )
                    return

                self.schedule[cur_day.objectName()] = \
                self.schedule.get(cur_day.objectName(), []) + \
                [[lesson_name, str(cab), *self.lesson_timings[self.lessons[day]]]]

                self.lessons[day] += 1


        print(cur_day.objectName())

        print(self.lessons)
        print(self.schedule)

        self.draw_lessons()

    def exit(self):
        """This method is called when the program is closed"""
        self.db.set_schedule(self.user_id, json.dumps(self.schedule))
        self.db.close_connection()

        self.destroy()

    def closeEvent(self, event: QCloseEvent) -> None:
        reply = QMessageBox.question(
            self,
            'Подтверждение',
            'У вас есть не сохраненные данные, вы действительно хотите выйти без сохранения?',
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No,
        )

        if reply == QMessageBox.StandardButton.Yes:
            # Разрешаем закрытие окна
            self.db.close_connection()
            event.accept()
        else:
            # Запрещаем закрытие окна (оставляем его открытым)
            event.ignore()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    se = ScheduleEdit(1)
    se.show()
    sys.exit(app.exec())