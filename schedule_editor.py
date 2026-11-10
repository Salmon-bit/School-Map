import sys
import os
import json
from PySide6.QtWidgets import QApplication, QWidget, QInputDialog, QListWidget
from ui.ui_schedule_editor import Ui_ScheduleEdit


class ScheduleEdit(Ui_ScheduleEdit, QWidget):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

        self.schedule = {}
        self.lessons = [0, 0, 0, 0, 0, 0]
        self.lesson_timings = []

        self.addLEssonBtn.clicked.connect(self.add_lesson)
        self.pushButton.clicked.connect(self.exit)

    def count_lesson_times(self):
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
        time = time = time.addSecs(self.lessonDur_6.value() * 60)
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

        print(self.lesson_timings)

    def add_lesson(self):
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

                self.schedule[cur_day.objectName()] = \
                self.schedule.get(cur_day.objectName(), []) + \
                [[lesson_name, str(cab), *self.lesson_timings[self.lessons[day]]]]

                self.lessons[day] += 1

        print(cur_day.objectName())

        print(self.lessons)
        print(self.schedule)

        mn_lw = QListWidget(parent=self.Mn)
        mn_lw.resize(450, 333)
        tu_lw = QListWidget(parent=self.Tu)
        tu_lw.resize(450, 333)
        wd_lw = QListWidget(parent=self.Wd)
        wd_lw.resize(450, 333)
        th_lw = QListWidget(parent=self.Th)
        th_lw.resize(450, 333)
        fr_lw = QListWidget(parent=self.Fr)
        fr_lw.resize(450, 333)
        st_lw = QListWidget(parent=self.St)
        st_lw.resize(450, 333)

        mn_lw.addItems(['; '.join(i) for i in self.schedule.get('Mn', [])])
        tu_lw.addItems(['; '.join(i) for i in self.schedule.get('Tu', [])])
        wd_lw.addItems(['; '.join(i) for i in self.schedule.get('Wd', [])])
        th_lw.addItems(['; '.join(i) for i in self.schedule.get('Th', [])])
        fr_lw.addItems(['; '.join(i) for i in self.schedule.get('Fr', [])])
        st_lw.addItems(['; '.join(i) for i in self.schedule.get('St', [])])

        self.tabWidget.update()

    def exit(self):
        os.makedirs('assets', exist_ok=True)
        with open('assets/schedule.json', 'w', encoding='UTF-8', newline='') as f:
            f.write(json.dumps(self.schedule))

        self.destroy()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    se = ScheduleEdit()
    se.show()
    sys.exit(app.exec())