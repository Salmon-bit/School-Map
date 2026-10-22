# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.12.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLayout,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QTabWidget, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.actionAddFriendById = QAction(MainWindow)
        self.actionAddFriendById.setObjectName(u"actionAddFriendById")
        self.actionAddFriendByUsername = QAction(MainWindow)
        self.actionAddFriendByUsername.setObjectName(u"actionAddFriendByUsername")
        self.actionAddFriendByEmail = QAction(MainWindow)
        self.actionAddFriendByEmail.setObjectName(u"actionAddFriendByEmail")
        icon = QIcon()
        iconThemeName = u"mail-unread"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u".", QSize(), QIcon.Mode.Normal, QIcon.State.Off)

        self.actionAddFriendByEmail.setIcon(icon)
        self.actionViewFriends = QAction(MainWindow)
        self.actionViewFriends.setObjectName(u"actionViewFriends")
        self.actionViewStudents = QAction(MainWindow)
        self.actionViewStudents.setObjectName(u"actionViewStudents")
        icon1 = QIcon()
        iconThemeName = u"edit-find"
        if QIcon.hasThemeIcon(iconThemeName):
            icon1 = QIcon.fromTheme(iconThemeName)
        else:
            icon1.addFile(u".", QSize(), QIcon.Mode.Normal, QIcon.State.Off)

        self.actionViewStudents.setIcon(icon1)
        self.actionChangeSchool = QAction(MainWindow)
        self.actionChangeSchool.setObjectName(u"actionChangeSchool")
        self.actionAddSchedule = QAction(MainWindow)
        self.actionAddSchedule.setObjectName(u"actionAddSchedule")
        self.actionEditSchedule = QAction(MainWindow)
        self.actionEditSchedule.setObjectName(u"actionEditSchedule")
        self.actionRemoveSchedule = QAction(MainWindow)
        self.actionRemoveSchedule.setObjectName(u"actionRemoveSchedule")
        self.actionHelp = QAction(MainWindow)
        self.actionHelp.setObjectName(u"actionHelp")
        icon2 = QIcon()
        iconThemeName = u"dialog-information"
        if QIcon.hasThemeIcon(iconThemeName):
            icon2 = QIcon.fromTheme(iconThemeName)
        else:
            icon2.addFile(u".", QSize(), QIcon.Mode.Normal, QIcon.State.Off)

        self.actionHelp.setIcon(icon2)
        self.actionCredits = QAction(MainWindow)
        self.actionCredits.setObjectName(u"actionCredits")
        self.actionUserInfo = QAction(MainWindow)
        self.actionUserInfo.setObjectName(u"actionUserInfo")
        self.actionEULA = QAction(MainWindow)
        self.actionEULA.setObjectName(u"actionEULA")
        self.actionLicense = QAction(MainWindow)
        self.actionLicense.setObjectName(u"actionLicense")
        icon3 = QIcon()
        iconThemeName = u"document-new"
        if QIcon.hasThemeIcon(iconThemeName):
            icon3 = QIcon.fromTheme(iconThemeName)
        else:
            icon3.addFile(u".", QSize(), QIcon.Mode.Normal, QIcon.State.Off)

        self.actionLicense.setIcon(icon3)
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        icon4 = QIcon()
        iconThemeName = u"application-exit"
        if QIcon.hasThemeIcon(iconThemeName):
            icon4 = QIcon.fromTheme(iconThemeName)
        else:
            icon4.addFile(u".", QSize(), QIcon.Mode.Normal, QIcon.State.Off)

        self.actionExit.setIcon(icon4)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy1)
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 0, 781, 551))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.floor_veiw = QTabWidget(self.verticalLayoutWidget)
        self.floor_veiw.setObjectName(u"floor_veiw")
        self.floor_1 = QWidget()
        self.floor_1.setObjectName(u"floor_1")
        self.school_view_floor_1 = QWidget(self.floor_1)
        self.school_view_floor_1.setObjectName(u"school_view_floor_1")
        self.school_view_floor_1.setGeometry(QRect(20, 20, 741, 421))
        sizePolicy1.setHeightForWidth(self.school_view_floor_1.sizePolicy().hasHeightForWidth())
        self.school_view_floor_1.setSizePolicy(sizePolicy1)
        self.floor_veiw.addTab(self.floor_1, "")
        self.floor_2 = QWidget()
        self.floor_2.setObjectName(u"floor_2")
        self.floor_veiw.addTab(self.floor_2, "")

        self.verticalLayout.addWidget(self.floor_veiw)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.biggerView = QPushButton(self.verticalLayoutWidget)
        self.biggerView.setObjectName(u"biggerView")

        self.horizontalLayout.addWidget(self.biggerView)

        self.resetView = QPushButton(self.verticalLayoutWidget)
        self.resetView.setObjectName(u"resetView")

        self.horizontalLayout.addWidget(self.resetView)

        self.smallerView = QPushButton(self.verticalLayoutWidget)
        self.smallerView.setObjectName(u"smallerView")

        self.horizontalLayout.addWidget(self.smallerView)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.currentSize = QLabel(self.verticalLayoutWidget)
        self.currentSize.setObjectName(u"currentSize")
        self.currentSize.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.currentSize)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 20))
        self.menuFriends = QMenu(self.menubar)
        self.menuFriends.setObjectName(u"menuFriends")
        self.menuAddFriend = QMenu(self.menuFriends)
        self.menuAddFriend.setObjectName(u"menuAddFriend")
        self.menuSchool = QMenu(self.menubar)
        self.menuSchool.setObjectName(u"menuSchool")
        self.menuSchedule = QMenu(self.menubar)
        self.menuSchedule.setObjectName(u"menuSchedule")
        self.menuProgramm = QMenu(self.menubar)
        self.menuProgramm.setObjectName(u"menuProgramm")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFriends.menuAction())
        self.menubar.addAction(self.menuSchool.menuAction())
        self.menubar.addAction(self.menuSchedule.menuAction())
        self.menubar.addAction(self.menuProgramm.menuAction())
        self.menuFriends.addAction(self.menuAddFriend.menuAction())
        self.menuFriends.addAction(self.actionViewFriends)
        self.menuAddFriend.addAction(self.actionAddFriendById)
        self.menuAddFriend.addAction(self.actionAddFriendByUsername)
        self.menuAddFriend.addAction(self.actionAddFriendByEmail)
        self.menuSchool.addAction(self.actionViewStudents)
        self.menuSchool.addSeparator()
        self.menuSchool.addAction(self.actionChangeSchool)
        self.menuSchedule.addAction(self.actionAddSchedule)
        self.menuSchedule.addAction(self.actionEditSchedule)
        self.menuSchedule.addAction(self.actionRemoveSchedule)
        self.menuProgramm.addAction(self.actionHelp)
        self.menuProgramm.addAction(self.actionCredits)
        self.menuProgramm.addAction(self.actionUserInfo)
        self.menuProgramm.addAction(self.actionEULA)
        self.menuProgramm.addAction(self.actionLicense)
        self.menuProgramm.addSeparator()
        self.menuProgramm.addAction(self.actionExit)

        self.retranslateUi(MainWindow)

        self.floor_veiw.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"School Map", None))
        self.actionAddFriendById.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e \u0438\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440\u0443", None))
#if QT_CONFIG(shortcut)
        self.actionAddFriendById.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+I", None))
#endif // QT_CONFIG(shortcut)
        self.actionAddFriendByUsername.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e \u0438\u043c\u0435\u043d\u0438 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f", None))
        self.actionAddFriendByEmail.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e \u043f\u043e\u0447\u0442\u0435", None))
        self.actionViewFriends.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u043c\u043e\u0442\u0440\u0435\u0442\u044c \u0434\u0440\u0443\u0437\u0435\u0439", None))
#if QT_CONFIG(shortcut)
        self.actionViewFriends.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+F", None))
#endif // QT_CONFIG(shortcut)
        self.actionViewStudents.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u043c\u043e\u0442\u0440\u0435\u0442\u044c \u0443\u0447\u0435\u043d\u0438\u043a\u043e\u0432", None))
#if QT_CONFIG(shortcut)
        self.actionViewStudents.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionChangeSchool.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043c\u0435\u043d\u0438\u0442\u044c \u0448\u043a\u043e\u043b\u0443", None))
#if QT_CONFIG(shortcut)
        self.actionChangeSchool.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Alt+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionAddSchedule.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0440\u0430\u0441\u043f\u0438\u0441\u0430\u043d\u0438\u0435", None))
#if QT_CONFIG(shortcut)
        self.actionAddSchedule.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionEditSchedule.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c \u0440\u0430\u0441\u043f\u0438\u0441\u0430\u043d\u0438\u0435", None))
        self.actionRemoveSchedule.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u043c\u043e\u0442\u0440\u0435\u0442\u044c \u0440\u0430\u0441\u043f\u0438\u0441\u0430\u043d\u0438\u0435", None))
        self.actionHelp.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0440\u0430\u0432\u043a\u0430", None))
#if QT_CONFIG(shortcut)
        self.actionHelp.setShortcut(QCoreApplication.translate("MainWindow", u"F1", None))
#endif // QT_CONFIG(shortcut)
        self.actionCredits.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u0435\u043b\u0438", None))
        self.actionUserInfo.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043e \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u0435", None))
        self.actionEULA.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c\u0441\u043a\u043e\u0435 \u0441\u043e\u0433\u043b\u0430\u0448\u0435\u043d\u0438\u0435", None))
        self.actionLicense.setText(QCoreApplication.translate("MainWindow", u"\u041b\u0438\u0446\u0435\u043d\u0437\u0438\u044f", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0445\u043e\u0434", None))
#if QT_CONFIG(shortcut)
        self.actionExit.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Q", None))
#endif // QT_CONFIG(shortcut)
        self.floor_veiw.setTabText(self.floor_veiw.indexOf(self.floor_1), QCoreApplication.translate("MainWindow", u"Этаж 1", None))
        self.floor_veiw.setTabText(self.floor_veiw.indexOf(self.floor_2), QCoreApplication.translate("MainWindow", u"Этаж 2", None))
        self.biggerView.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.resetView.setText(QCoreApplication.translate("MainWindow", u"1x", None))
        self.smallerView.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u0431\u043b\u0438\u0437\u0438\u0442\u044c", None))
        self.currentSize.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0430\u0441\u0448\u0442\u0430\u0431: 1x", None))
        self.menuFriends.setTitle(QCoreApplication.translate("MainWindow", u"\u0414\u0440\u0443\u0437\u044c\u044f", None))
        self.menuAddFriend.setTitle(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0434\u0440\u0443\u0433\u0430", None))
        self.menuSchool.setTitle(QCoreApplication.translate("MainWindow", u"\u0428\u043a\u043e\u043b\u0430", None))
        self.menuSchedule.setTitle(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u043f\u0438\u0441\u0430\u043d\u0438\u0435", None))
        self.menuProgramm.setTitle(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0430", None))
    # retranslateUi

