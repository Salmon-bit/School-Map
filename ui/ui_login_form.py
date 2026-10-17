# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_form.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFormLayout, QFrame,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_LoginForm(object):
    def setupUi(self, LoginForm: QWidget):
        if not LoginForm.objectName():
            LoginForm.setObjectName(u"LoginForm")
        LoginForm.resize(400, 300)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(LoginForm.sizePolicy().hasHeightForWidth())
        LoginForm.setSizePolicy(sizePolicy)
        LoginForm.setMinimumSize(QSize(400, 300))
        LoginForm.setMaximumSize(QSize(400, 300))
        self.verticalLayoutWidget = QWidget(LoginForm)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 10, 381, 281))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.title = QLabel(self.verticalLayoutWidget)
        self.title.setObjectName(u"title")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.title.sizePolicy().hasHeightForWidth())
        self.title.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setFamilies([u"Cantarell"])
        font.setPointSize(13)
        font.setBold(True)
        self.title.setFont(font)
        self.title.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.title)

        self.frame = QFrame(self.verticalLayoutWidget)
        self.frame.setObjectName(u"frame")
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Sunken)
        self.formLayoutWidget = QWidget(self.frame)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(10, 10, 362, 91))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.formLayoutWidget)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label)

        self.account_cred = QLineEdit(self.formLayoutWidget)
        self.account_cred.setObjectName(u"account_cred")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.account_cred)

        self.label_2 = QLabel(self.formLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_2)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.password = QLineEdit(self.formLayoutWidget)
        self.password.setObjectName(u"password")
        sizePolicy.setHeightForWidth(self.password.sizePolicy().hasHeightForWidth())
        self.password.setSizePolicy(sizePolicy)
        self.password.setMinimumSize(QSize(206, 0))
        self.password.setEchoMode(QLineEdit.Password)

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.LabelRole, self.password)

        self.show_password = QPushButton(self.formLayoutWidget)
        self.show_password.setObjectName(u"show_password")
        sizePolicy.setHeightForWidth(self.show_password.sizePolicy().hasHeightForWidth())
        self.show_password.setSizePolicy(sizePolicy)
        icon = QIcon(QIcon.fromTheme(u"dialog-password"))
        self.show_password.setIcon(icon)

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.FieldRole, self.show_password)


        self.formLayout.setLayout(1, QFormLayout.ItemRole.FieldRole, self.formLayout_2)


        self.verticalLayout.addWidget(self.frame)

        self.auto_login = QCheckBox(self.verticalLayoutWidget)
        self.auto_login.setObjectName(u"auto_login")

        self.verticalLayout.addWidget(self.auto_login)

        self.login = QPushButton(self.verticalLayoutWidget)
        self.login.setObjectName(u"login")

        self.verticalLayout.addWidget(self.login)


        self.retranslateUi(LoginForm)

        QMetaObject.connectSlotsByName(LoginForm)
    # setupUi

    def retranslateUi(self, LoginForm):
        LoginForm.setWindowTitle(QCoreApplication.translate("LoginForm", u"Login", None))
        self.title.setText(QCoreApplication.translate("LoginForm", u"\u0412\u043e\u0439\u0442\u0438 \u0432 \u0441\u0438\u0441\u0442\u0435\u043c\u0443", None))
        self.label.setText(QCoreApplication.translate("LoginForm", u"\u0414\u0430\u043d\u043d\u044b\u0435 \u0434\u043b\u044f \u0432\u0445\u043e\u0434\u0430", None))
        self.label_2.setText(QCoreApplication.translate("LoginForm", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.show_password.setText("")
        self.auto_login.setText(QCoreApplication.translate("LoginForm", u"\u0410\u0432\u0442\u043e\u043c\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u0438 \u0432\u0445\u043e\u0434\u0438\u0442\u044c \u0432 \u0441\u0438\u0441\u0442\u0435\u043c\u0443", None))
        self.login.setText(QCoreApplication.translate("LoginForm", u"\u0412\u043e\u0439\u0442\u0438 \u0432 \u0441\u0438\u0441\u0442\u0435\u043c\u0443", None))
    # retranslateUi

