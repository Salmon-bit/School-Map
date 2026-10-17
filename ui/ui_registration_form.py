# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'registration_form.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Registration(object):
    def setupUi(self, Registration: QWidget):
        if not Registration.objectName():
            Registration.setObjectName(u"Registration")
        Registration.resize(400, 300)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Registration.sizePolicy().hasHeightForWidth())
        Registration.setSizePolicy(sizePolicy)
        Registration.setMinimumSize(QSize(400, 300))
        Registration.setMaximumSize(QSize(400, 300))
        self.verticalLayoutWidget = QWidget(Registration)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 10, 385, 281))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setFamilies([u"Cantarell"])
        font.setPointSize(13)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_2)

        self.username = QLineEdit(self.verticalLayoutWidget)
        self.username.setObjectName(u"username")
        self.username.setMaxLength(32)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.username)

        self.label_3 = QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_3)

        self.email = QLineEdit(self.verticalLayoutWidget)
        self.email.setObjectName(u"email")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.email)

        self.label_4 = QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_4)

        self.label_5 = QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_5)

        self.label_6 = QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.label_6)

        self.school_select = QComboBox(self.verticalLayoutWidget)
        self.school_select.addItem("")
        self.school_select.addItem("")
        self.school_select.setObjectName(u"school_select")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.school_select)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.password = QLineEdit(self.verticalLayoutWidget)
        self.password.setObjectName(u"password")
        sizePolicy.setHeightForWidth(self.password.sizePolicy().hasHeightForWidth())
        self.password.setSizePolicy(sizePolicy)
        self.password.setMinimumSize(QSize(220, 0))
        self.password.setInputMethodHints(Qt.ImhHiddenText|Qt.ImhNoAutoUppercase|Qt.ImhNoPredictiveText|Qt.ImhSensitiveData)
        self.password.setMaxLength(16000)
        self.password.setEchoMode(QLineEdit.Password)

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.LabelRole, self.password)

        self.show_password = QPushButton(self.verticalLayoutWidget)
        self.show_password.setObjectName(u"show_password")
        sizePolicy.setHeightForWidth(self.show_password.sizePolicy().hasHeightForWidth())
        self.show_password.setSizePolicy(sizePolicy)
        icon = QIcon(QIcon.fromTheme(u"dialog-password"))
        self.show_password.setIcon(icon)
        self.show_password.setFlat(False)

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.FieldRole, self.show_password)


        self.horizontalLayout.addLayout(self.formLayout_2)


        self.formLayout.setLayout(2, QFormLayout.ItemRole.FieldRole, self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.password_repeat = QLineEdit(self.verticalLayoutWidget)
        self.password_repeat.setObjectName(u"password_repeat")
        sizePolicy.setHeightForWidth(self.password_repeat.sizePolicy().hasHeightForWidth())
        self.password_repeat.setSizePolicy(sizePolicy)
        self.password_repeat.setMinimumSize(QSize(220, 0))
        self.password_repeat.setInputMethodHints(Qt.ImhHiddenText|Qt.ImhNoAutoUppercase|Qt.ImhNoPredictiveText|Qt.ImhSensitiveData)
        self.password_repeat.setEchoMode(QLineEdit.Password)

        self.formLayout_3.setWidget(0, QFormLayout.ItemRole.LabelRole, self.password_repeat)

        self.show_password_rep = QPushButton(self.verticalLayoutWidget)
        self.show_password_rep.setObjectName(u"show_password_rep")
        sizePolicy.setHeightForWidth(self.show_password_rep.sizePolicy().hasHeightForWidth())
        self.show_password_rep.setSizePolicy(sizePolicy)
        self.show_password_rep.setIcon(icon)

        self.formLayout_3.setWidget(0, QFormLayout.ItemRole.FieldRole, self.show_password_rep)


        self.horizontalLayout_2.addLayout(self.formLayout_3)


        self.formLayout.setLayout(3, QFormLayout.ItemRole.FieldRole, self.horizontalLayout_2)


        self.verticalLayout.addLayout(self.formLayout)

        self.register_2 = QPushButton(self.verticalLayoutWidget)
        self.register_2.setObjectName(u"register_2")

        self.verticalLayout.addWidget(self.register_2)


        self.retranslateUi(Registration)

        QMetaObject.connectSlotsByName(Registration)
    # setupUi

    def retranslateUi(self, Registration):
        Registration.setWindowTitle(QCoreApplication.translate("Registration", u"Registration", None))
        self.label.setText(QCoreApplication.translate("Registration", u"\u0420\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u044f \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f", None))
        self.label_2.setText(QCoreApplication.translate("Registration", u"\u0418\u043c\u044f \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f", None))
        self.username.setPlaceholderText(QCoreApplication.translate("Registration", u"\u0412\u0430\u0448\u0435 \u0438\u043c\u044f \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f", None))
        self.label_3.setText(QCoreApplication.translate("Registration", u"\u042d\u043b\u0435\u043a\u0442\u0440\u043e\u043d\u043d\u0430\u044f \u043f\u043e\u0447\u0442\u0430", None))
        self.email.setPlaceholderText(QCoreApplication.translate("Registration", u"your@email.com", None))
        self.label_4.setText(QCoreApplication.translate("Registration", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.label_5.setText(QCoreApplication.translate("Registration", u"\u041f\u043e\u0432\u0442\u043e\u0440 \u043f\u0430\u0440\u043e\u043b\u044f", None))
        self.label_6.setText(QCoreApplication.translate("Registration", u"\u0428\u043a\u043e\u043b\u0430", None))
        self.school_select.setItemText(0, QCoreApplication.translate("Registration", u"\u0428\u043a\u043e\u043b\u0430", None))
        self.school_select.setItemText(1, QCoreApplication.translate("Registration", u"\u0428\u043a\u043e\u043b\u0430 \u21162070", None))

        self.password.setInputMask("")
        self.password.setPlaceholderText(QCoreApplication.translate("Registration", u"\u0412\u0430\u0448 \u043f\u0430\u0440\u043e\u043b\u044c", None))
        self.show_password.setText("")
        self.password_repeat.setInputMask("")
        self.password_repeat.setPlaceholderText(QCoreApplication.translate("Registration", u"\u041f\u043e\u0432\u0442\u043e\u0440\u0438\u0442\u0435 \u0432\u0430\u0448 \u043f\u0430\u0440\u043e\u043b\u044c", None))
        self.show_password_rep.setText("")
        self.register_2.setText(QCoreApplication.translate("Registration", u"\u0417\u0430\u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0438\u0440\u043e\u0432\u0430\u0442\u044c\u0441\u044f", None))
    # retranslateUi

