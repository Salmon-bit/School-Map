"""Provides a Schedule Editor class"""
import json
import sys
from PySide6.QtWidgets import QApplication, QWidget, QInputDialog, QMessageBox
from ui.ui_schedule_editor import Ui_ScheduleEdit
from database_manager import DatabaseManager


class ScheduleEdit(Ui_ScheduleEdit, QWidget):
    def __init__(self, user_id):
        """Inits the class"""
        super().__init__()

        self.setupUi(self)
        self.user_id = user_id

        self.schedule = {}
        self.lessons = [0, 0, 0, 0, 0, 0]
        self.lesson_timings = []

        self.addLEssonBtn.clicked.connect(self.add_lesson)
        self.pushButton.clicked.connect(self.exit)

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

        print(self.lesson_timings)

    def add_lesson(self):
        """Adds new lesson to the schedule"""
        cur_day = self.tabWidget.currentWidget()

        if self.lessons == [0, 0, 0, 0, 0, 0]:
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

    def exit(self):
        """This method is called when the program is closed"""
        db = DatabaseManager()
        db.set_schedule(self.user_id, json.dumps(self.schedule))
        db.close_connection()

        self.destroy()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    se = ScheduleEdit(1)
    se.show()
    sys.exit(app.exec())