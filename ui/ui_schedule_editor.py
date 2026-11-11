# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'schedule_editor.ui'
##
## Created by: Qt User Interface Compiler version 6.12.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject, QRect,
                            QSize, QTime, Qt)
from PySide6.QtGui import (QFont)
from PySide6.QtWidgets import (QCheckBox, QFormLayout, QHBoxLayout,
                               QLabel, QListWidget, QPushButton,
                               QSizePolicy, QSpacerItem, QSpinBox, QTabWidget,
                               QTimeEdit, QVBoxLayout, QWidget)

class Ui_ScheduleEdit(object):
    def setupUi(self, ScheduleEdit):
        if not ScheduleEdit.objectName():
            ScheduleEdit.setObjectName(u"ScheduleEdit")
        ScheduleEdit.resize(800, 450)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ScheduleEdit.sizePolicy().hasHeightForWidth())
        ScheduleEdit.setSizePolicy(sizePolicy)
        ScheduleEdit.setMinimumSize(QSize(800, 450))
        ScheduleEdit.setMaximumSize(QSize(800, 450))
        self.horizontalLayoutWidget = QWidget(ScheduleEdit)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 0, 820, 401))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.tabWidget = QTabWidget(self.horizontalLayoutWidget)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy2)
        self.tabWidget.setMinimumSize(QSize(450, 0))
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setElideMode(Qt.ElideLeft)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.Mn = QWidget()
        self.Mn.setObjectName(u"Mn")
        self.mn_lw = QListWidget(self.Mn)
        self.mn_lw.setObjectName(u"mn_lw")
        self.mn_lw.setGeometry(QRect(-5, 1, 451, 341))
        self.tabWidget.addTab(self.Mn, "")
        self.Tu = QWidget()
        self.Tu.setObjectName(u"Tu")
        self.tu_lw = QListWidget(self.Tu)
        self.tu_lw.setObjectName(u"tu_lw")
        self.tu_lw.setGeometry(QRect(0, 0, 451, 311))
        self.tabWidget.addTab(self.Tu, "")
        self.Wd = QWidget()
        self.Wd.setObjectName(u"Wd")
        self.wd_lw = QListWidget(self.Wd)
        self.wd_lw.setObjectName(u"wd_lw")
        self.wd_lw.setGeometry(QRect(0, 0, 451, 321))
        self.tabWidget.addTab(self.Wd, "")
        self.Th = QWidget()
        self.Th.setObjectName(u"Th")
        self.th_lw = QListWidget(self.Th)
        self.th_lw.setObjectName(u"th_lw")
        self.th_lw.setGeometry(QRect(0, 0, 451, 311))
        self.tabWidget.addTab(self.Th, "")
        self.Fr = QWidget()
        self.Fr.setObjectName(u"Fr")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.Fr.sizePolicy().hasHeightForWidth())
        self.Fr.setSizePolicy(sizePolicy3)
        self.fr_lw = QListWidget(self.Fr)
        self.fr_lw.setObjectName(u"fr_lw")
        self.fr_lw.setGeometry(QRect(0, 0, 451, 311))
        self.tabWidget.addTab(self.Fr, "")
        self.St = QWidget()
        self.St.setObjectName(u"St")
        self.st_lw = QListWidget(self.St)
        self.st_lw.setObjectName(u"st_lw")
        self.st_lw.setGeometry(QRect(0, 0, 451, 311))
        self.tabWidget.addTab(self.St, "")

        self.verticalLayout.addWidget(self.tabWidget)

        self.addLEssonBtn = QPushButton(self.horizontalLayoutWidget)
        self.addLEssonBtn.setObjectName(u"addLEssonBtn")
        self.addLEssonBtn.setMinimumSize(QSize(0, 30))

        self.verticalLayout.addWidget(self.addLEssonBtn)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer = QSpacerItem(20, 46, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.formLayout_7 = QFormLayout()
        self.formLayout_7.setObjectName(u"formLayout_7")
        self.formLayout_7.setLabelAlignment(Qt.AlignLeading)
        self.formLayout_7.setFormAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.formLayout_7.setVerticalSpacing(10)
        self.lessonDur_6 = QSpinBox(self.horizontalLayoutWidget)
        self.lessonDur_6.setObjectName(u"lessonDur_6")
        self.lessonDur_6.setValue(40)

        self.formLayout_7.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lessonDur_6)

        self.label_22 = QLabel(self.horizontalLayoutWidget)
        self.label_22.setObjectName(u"label_22")

        self.formLayout_7.setWidget(0, QFormLayout.ItemRole.FieldRole, self.label_22)

        self.breakDur_6 = QSpinBox(self.horizontalLayoutWidget)
        self.breakDur_6.setObjectName(u"breakDur_6")
        self.breakDur_6.setValue(10)

        self.formLayout_7.setWidget(1, QFormLayout.ItemRole.LabelRole, self.breakDur_6)

        self.label_23 = QLabel(self.horizontalLayoutWidget)
        self.label_23.setObjectName(u"label_23")

        self.formLayout_7.setWidget(1, QFormLayout.ItemRole.FieldRole, self.label_23)

        self.longBreakDur_6 = QSpinBox(self.horizontalLayoutWidget)
        self.longBreakDur_6.setObjectName(u"longBreakDur_6")
        self.longBreakDur_6.setValue(20)

        self.formLayout_7.setWidget(2, QFormLayout.ItemRole.LabelRole, self.longBreakDur_6)

        self.label_24 = QLabel(self.horizontalLayoutWidget)
        self.label_24.setObjectName(u"label_24")

        self.formLayout_7.setWidget(2, QFormLayout.ItemRole.FieldRole, self.label_24)

        self.timeEdit_6 = QTimeEdit(self.horizontalLayoutWidget)
        self.timeEdit_6.setObjectName(u"timeEdit_6")
        self.timeEdit_6.setDateTime(QDateTime(QDate(2000, 1, 1), QTime(8, 30, 0)))
        self.timeEdit_6.setCalendarPopup(True)
        self.timeEdit_6.setTimeSpec(Qt.LocalTime)

        self.formLayout_7.setWidget(3, QFormLayout.ItemRole.LabelRole, self.timeEdit_6)

        self.label_25 = QLabel(self.horizontalLayoutWidget)
        self.label_25.setObjectName(u"label_25")

        self.formLayout_7.setWidget(3, QFormLayout.ItemRole.FieldRole, self.label_25)

        self.checkBox = QCheckBox(self.horizontalLayoutWidget)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setChecked(True)

        self.formLayout_7.setWidget(4, QFormLayout.ItemRole.LabelRole, self.checkBox)

        self.checkBox_2 = QCheckBox(self.horizontalLayoutWidget)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setChecked(False)

        self.formLayout_7.setWidget(5, QFormLayout.ItemRole.LabelRole, self.checkBox_2)

        self.checkBox_3 = QCheckBox(self.horizontalLayoutWidget)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.formLayout_7.setWidget(6, QFormLayout.ItemRole.LabelRole, self.checkBox_3)

        self.checkBox_4 = QCheckBox(self.horizontalLayoutWidget)
        self.checkBox_4.setObjectName(u"checkBox_4")

        self.formLayout_7.setWidget(7, QFormLayout.ItemRole.LabelRole, self.checkBox_4)

        self.checkBox_5 = QCheckBox(self.horizontalLayoutWidget)
        self.checkBox_5.setObjectName(u"checkBox_5")
        self.checkBox_5.setChecked(True)

        self.formLayout_7.setWidget(8, QFormLayout.ItemRole.LabelRole, self.checkBox_5)

        self.checkBox_6 = QCheckBox(self.horizontalLayoutWidget)
        self.checkBox_6.setObjectName(u"checkBox_6")

        self.formLayout_7.setWidget(9, QFormLayout.ItemRole.LabelRole, self.checkBox_6)

        self.label_2 = QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout_7.setWidget(6, QFormLayout.ItemRole.FieldRole, self.label_2)

        self.label_3 = QLabel(self.horizontalLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.formLayout_7.setWidget(7, QFormLayout.ItemRole.FieldRole, self.label_3)


        self.verticalLayout_2.addLayout(self.formLayout_7)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.pushButton = QPushButton(ScheduleEdit)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 410, 781, 31))

        self.retranslateUi(ScheduleEdit)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(ScheduleEdit)
    # setupUi

    def retranslateUi(self, ScheduleEdit):
        ScheduleEdit.setWindowTitle(QCoreApplication.translate("ScheduleEdit", u"Schedule Editor", None))
        self.label.setText(QCoreApplication.translate("ScheduleEdit", u"\u0423\u0440\u043e\u043a\u0438", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Mn), QCoreApplication.translate("ScheduleEdit", u"\u041f\u043d", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Tu), QCoreApplication.translate("ScheduleEdit", u"\u0412\u0442", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Wd), QCoreApplication.translate("ScheduleEdit", u"\u0421\u0440", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Th), QCoreApplication.translate("ScheduleEdit", u"\u0427\u0442", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Fr), QCoreApplication.translate("ScheduleEdit", u"\u041f\u0442", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.St), QCoreApplication.translate("ScheduleEdit", u"\u0421\u0431", None))
        self.addLEssonBtn.setText(QCoreApplication.translate("ScheduleEdit", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0443\u0440\u043e\u043a", None))
        self.label_22.setText(QCoreApplication.translate("ScheduleEdit", u"\u0414\u043b\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u044c \u0443\u0440\u043e\u043a\u0430 (\u043c\u0438\u043d)", None))
        self.label_23.setText(QCoreApplication.translate("ScheduleEdit", u"\u0414\u043b\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u044c \u043f\u0435\u0440\u0435\u043c\u0435\u043d\u044b (\u043c\u0438\u043d)", None))
        self.label_24.setText(QCoreApplication.translate("ScheduleEdit", u"\u0414\u043b\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u044c \u0431\u043e\u043b\u044c\u0448\u043e\u0439 \u043f\u0435\u0440\u0435\u043c\u0435\u043d\u044b (\u043c\u0438\u043d)", None))
        self.label_25.setText(QCoreApplication.translate("ScheduleEdit", u"\u041d\u0430\u0447\u0430\u043b\u043e \u0443\u0440\u043e\u043a\u043e\u0432 (\u0427\u0427:\u041c\u041c)", None))
        self.checkBox.setText(QCoreApplication.translate("ScheduleEdit", u"2", None))
        self.checkBox_2.setText(QCoreApplication.translate("ScheduleEdit", u"3", None))
        self.checkBox_3.setText(QCoreApplication.translate("ScheduleEdit", u"4", None))
        self.checkBox_4.setText(QCoreApplication.translate("ScheduleEdit", u"5", None))
        self.checkBox_5.setText(QCoreApplication.translate("ScheduleEdit", u"6", None))
        self.checkBox_6.setText(QCoreApplication.translate("ScheduleEdit", u"7", None))
        self.label_2.setText(QCoreApplication.translate("ScheduleEdit", u"\u041e\u0442\u043c\u0435\u0442\u044c\u0442\u0435 \u0443\u0440\u043e\u043a\u0438, \u043f\u043e\u0441\u043b\u0435 \u043a\u043e\u0442\u043e\u0440\u044b\u0445 \u0443 \u0432\u0430\u0441 ", None))
        self.label_3.setText(QCoreApplication.translate("ScheduleEdit", u"\u0431\u043e\u043b\u044c\u0448\u0430\u044f \u043f\u0435\u0440\u0435\u043c\u0435\u043d\u0430", None))
        self.pushButton.setText(QCoreApplication.translate("ScheduleEdit", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0438 \u0432\u044b\u0439\u0442\u0438", None))
    # retranslateUi

