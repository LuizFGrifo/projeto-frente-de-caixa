# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loginjCYBKB.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
                               QLineEdit, QMainWindow, QPushButton, QSizePolicy,
                               QVBoxLayout, QWidget)
import resource


class Ui_Login(object):
    def setupUi(self, Login):
        if not Login.objectName():
            Login.setObjectName(u"Login")
        Login.resize(530, 430)
        Login.setMinimumSize(QSize(530, 430))
        Login.setMaximumSize(QSize(530, 430))
        self.centralwidget = QWidget(Login)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QWidget#centralwidget{\n"
                                         "	background-image: url(:/images/resources/images/login-background.png);\n"
                                         "	border-radius: 20px;\n"
                                         "}\n"
                                         "\n"
                                         "QFrame#main_frame{\n"
                                         "	background-color: #23233B;\n"
                                         "	border-radius: 20px;\n"
                                         "	margin: 80px;\n"
                                         "	padding-top: 20px;\n"
                                         "	padding-left: 30px;\n"
                                         "	padding-right: 30px;\n"
                                         "}\n"
                                         "\n"
                                         "QLabel{\n"
                                         "	color: rgb(217, 214, 215);\n"
                                         "	max-height: 10px;\n"
                                         "}\n"
                                         "\n"
                                         "QLineEdit {\n"
                                         "	padding-left: 20px;\n"
                                         "	min-height: 40px;\n"
                                         "	border-radius: 15px;\n"
                                         "	background-color: #434459;\n"
                                         "	color: rgb(217, 214, 215);\n"
                                         "}\n"
                                         "\n"
                                         "QLineEdit::focus{\n"
                                         "	border: 2px solid rgb(98, 131, 255);\n"
                                         "}\n"
                                         "\n"
                                         "QLineEdit::hover{\n"
                                         "	border: 2px solid rgb(98, 196, 255);\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton#login_button{\n"
                                         "	color: rgb(217, 214, 215);\n"
                                         "	min-height: 35px;\n"
                                         "	border: 2px solid rgb(126, 128, 128);\n"
                                         "	border-radius: 15px;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton#login_button::hover{\n"
                                         "	border: 2px solid rgb(98, 196, 255);\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton#minimize_button{\n"
                                         "	background-color:"
                                         " rgb(255, 251, 0);\n"
                                         "	border-radius: 7px;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton#close_button{\n"
                                         "	background-color: rgb(255, 38, 0);\n"
                                         "	border-radius: 7px;\n"
                                         "}\n"
                                         "\n"
                                         "QLabel#error_label {\n"
                                         "	color: red;\n"
                                         "}")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.topbar_frame = QFrame(self.centralwidget)
        self.topbar_frame.setObjectName(u"topbar_frame")
        self.topbar_frame.setMaximumSize(QSize(16777215, 30))
        self.topbar_frame.setFrameShape(QFrame.NoFrame)
        self.topbar_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.topbar_frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 12, 0, 0)
        self.frame_2 = QFrame(self.topbar_frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.frame_2)

        self.frame = QFrame(self.topbar_frame)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(70, 16777215))
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 20, 0)
        self.minimize_button = QPushButton(self.frame)
        self.minimize_button.setObjectName(u"minimize_button")
        self.minimize_button.setMaximumSize(QSize(15, 15))

        self.horizontalLayout_2.addWidget(self.minimize_button)

        self.close_button = QPushButton(self.frame)
        self.close_button.setObjectName(u"close_button")
        self.close_button.setMaximumSize(QSize(15, 15))

        self.horizontalLayout_2.addWidget(self.close_button)

        self.horizontalLayout.addWidget(self.frame)

        self.verticalLayout.addWidget(self.topbar_frame)

        self.main_frame = QFrame(self.centralwidget)
        self.main_frame.setObjectName(u"main_frame")
        self.main_frame.setFrameShape(QFrame.NoFrame)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.main_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.username_label = QLabel(self.main_frame)
        self.username_label.setObjectName(u"username_label")

        self.verticalLayout_2.addWidget(self.username_label)

        self.username_edit = QLineEdit(self.main_frame)
        self.username_edit.setObjectName(u"username_edit")

        self.verticalLayout_2.addWidget(self.username_edit)

        self.password_label = QLabel(self.main_frame)
        self.password_label.setObjectName(u"password_label")

        self.verticalLayout_2.addWidget(self.password_label)

        self.password_edit = QLineEdit(self.main_frame)
        self.password_edit.setObjectName(u"password_edit")
        self.password_edit.setEchoMode(QLineEdit.Password)

        self.verticalLayout_2.addWidget(self.password_edit)

        self.login_button = QPushButton(self.main_frame)
        self.login_button.setObjectName(u"login_button")

        self.verticalLayout_2.addWidget(self.login_button)

        self.error_label = QLabel(self.main_frame)
        self.error_label.setObjectName(u"error_label")
        self.error_label.setMinimumSize(QSize(0, 20))

        self.verticalLayout_2.addWidget(self.error_label)

        self.verticalLayout.addWidget(self.main_frame)

        Login.setCentralWidget(self.centralwidget)

        self.retranslateUi(Login)

        QMetaObject.connectSlotsByName(Login)

    # setupUi

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("Login", u"MainWindow", None))
        # if QT_CONFIG(tooltip)
        self.minimize_button.setToolTip(QCoreApplication.translate("Login", u"Minimizar", None))
        # endif // QT_CONFIG(tooltip)
        self.minimize_button.setText("")
        # if QT_CONFIG(tooltip)
        self.close_button.setToolTip(QCoreApplication.translate("Login", u"Fechar", None))
        # endif // QT_CONFIG(tooltip)
        self.close_button.setText("")
        self.username_label.setText(QCoreApplication.translate("Login", u"Usu\u00e1rio", None))
        self.username_edit.setText("")
        self.password_label.setText(QCoreApplication.translate("Login", u"Senha", None))
        self.password_edit.setText("")
        self.login_button.setText(QCoreApplication.translate("Login", u"Login", None))
        self.error_label.setText("")
    # retranslateUi
