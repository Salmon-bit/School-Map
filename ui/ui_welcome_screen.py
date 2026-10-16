# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'welcome_screen.ui'
##
## Created by: Qt User Interface Compiler version 6.12.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_WelcomeScreen(object):
    def setupUi(self, WelcomeScreen):
        if not WelcomeScreen.objectName():
            WelcomeScreen.setObjectName(u"WelcomeScreen")
        WelcomeScreen.resize(400, 300)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(WelcomeScreen.sizePolicy().hasHeightForWidth())
        WelcomeScreen.setSizePolicy(sizePolicy)
        WelcomeScreen.setMinimumSize(QSize(400, 300))
        WelcomeScreen.setMaximumSize(QSize(400, 300))
        self.title = QLabel(WelcomeScreen)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(10, 10, 381, 71))
        font = QFont()
        font.setFamilies([u"Cantarell"])
        font.setPointSize(13)
        font.setBold(True)
        self.title.setFont(font)
        self.title.setScaledContents(False)
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setWordWrap(True)
        self.show_on_start = QCheckBox(WelcomeScreen)
        self.show_on_start.setObjectName(u"show_on_start")
        self.show_on_start.setGeometry(QRect(90, 270, 221, 21))
        self.show_on_start.setChecked(True)
        self.frame = QFrame(WelcomeScreen)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 90, 381, 171))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayoutWidget = QWidget(self.frame)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 10, 361, 151))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setItalic(True)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setWordWrap(True)

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.login_btn = QPushButton(self.verticalLayoutWidget)
        self.login_btn.setObjectName(u"login_btn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.login_btn.sizePolicy().hasHeightForWidth())
        self.login_btn.setSizePolicy(sizePolicy2)

        self.horizontalLayout.addWidget(self.login_btn)

        self.register_btn = QPushButton(self.verticalLayoutWidget)
        self.register_btn.setObjectName(u"register_btn")
        sizePolicy2.setHeightForWidth(self.register_btn.sizePolicy().hasHeightForWidth())
        self.register_btn.setSizePolicy(sizePolicy2)

        self.horizontalLayout.addWidget(self.register_btn)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(WelcomeScreen)

        QMetaObject.connectSlotsByName(WelcomeScreen)
    # setupUi

    def retranslateUi(self, WelcomeScreen):
        WelcomeScreen.setWindowTitle(QCoreApplication.translate("WelcomeScreen", u"Welcome", None))
        self.title.setText(QCoreApplication.translate("WelcomeScreen", u"\u0414\u043e\u0431\u0440\u043e \u043f\u043e\u0436\u0430\u043b\u0432\u0430\u0442\u044c! \u042d\u0442\u043e \u043f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u0435 \u043f\u043e\u0437\u0432\u043e\u043b\u044f\u0435\u0442 \u043f\u0440\u043e\u0441\u043c\u0430\u0442\u0440\u0438\u0432\u0430\u0442\u044c \u0438\u043d\u0442\u0435\u0440\u0430\u043a\u0442\u0438\u0432\u043d\u044b\u0435 \u043a\u0430\u0440\u0442\u044b \u0440\u0430\u0437\u043b\u0438\u0447\u043d\u044b\u0445 \u0448\u043a\u043e\u043b \u043c\u043e\u0441\u043a\u0432\u044b.", None))
        self.show_on_start.setText(QCoreApplication.translate("WelcomeScreen", u"\u041f\u043e\u043a\u0430\u0437\u044b\u0432\u0430\u0442\u044c \u044d\u0442\u043e \u043e\u043a\u043d\u043e \u043f\u0440\u0438 \u0441\u0442\u0430\u0440\u0442\u0435", None))
        self.label.setText(QCoreApplication.translate("WelcomeScreen", u"\u0427\u0442\u043e\u0431\u044b \u043f\u0440\u043e\u0434\u043e\u043b\u0436\u0438\u0442\u044c, \u0432\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043e\u0434\u043d\u043e \u0438\u0437 \u0441\u043b\u0443\u0434\u0443\u044e\u0449\u0438\u0445 \u0434\u0435\u0439\u0441\u0442\u0432\u0438\u0439:", None))
        self.login_btn.setText(QCoreApplication.translate("WelcomeScreen", u"\u0412\u0445\u043e\u0434", None))
        self.register_btn.setText(QCoreApplication.translate("WelcomeScreen", u"\u0420\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u044f", None))
    # retranslateUi

