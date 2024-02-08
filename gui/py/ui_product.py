# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'productVyzZMB.ui'
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

class Ui_Produto(object):
    def setupUi(self, Produto):
        if not Produto.objectName():
            Produto.setObjectName(u"Produto")
        Produto.resize(700, 350)
        Produto.setMinimumSize(QSize(700, 350))
        Produto.setMaximumSize(QSize(700, 350))
        self.centralwidget = QWidget(Produto)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QMainWindow{\n"
"	border-radius:20px;\n"
"}\n"
"\n"
"QWidget#centralwidget{\n"
"	background-color: #23233D;\n"
"	border-radius:20px;\n"
"}\n"
"\n"
"QPushButton#close_button{\n"
"	background-color: #FF0053;\n"
"	border-radius: 7px;\n"
"}\n"
"\n"
"QFrame#main_frame{\n"
"	margin: 30px;\n"
"}\n"
"\n"
"QLabel{\n"
"	color: rgb(217, 214, 215);\n"
"	max-height: 20px;\n"
"	font-weight: bold;\n"
"	font-size: 12px;\n"
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
"QPushButton#edit_pic{\n"
"	border: none;\n"
"	color:	white;\n"
"}\n"
"\n"
"QPushButton#edit_pic::hover{\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"QPushButton#insert_product_button{\n"
"	color: rgb(217, 214, 215);\n"
"	min-height: 35px;\n"
"	border: 2px solid rgb(126, 128, 128);\n"
"	border"
                        "-radius: 15px;\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"QPushButton#insert_product_button::hover{\n"
"	border: 2px solid rgb(98, 196, 255);\n"
"}")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 30))
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(50, 16777215))
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.close_button = QPushButton(self.frame_4)
        self.close_button.setObjectName(u"close_button")
        self.close_button.setMinimumSize(QSize(15, 15))
        self.close_button.setMaximumSize(QSize(15, 15))

        self.horizontalLayout_2.addWidget(self.close_button)


        self.horizontalLayout.addWidget(self.frame_4)


        self.verticalLayout.addWidget(self.frame)

        self.main_frame = QFrame(self.centralwidget)
        self.main_frame.setObjectName(u"main_frame")
        self.main_frame.setFrameShape(QFrame.NoFrame)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.main_frame)
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.main_frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 107))
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setSpacing(12)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.frame_5)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(120, 16777215))
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 0))

        self.verticalLayout_3.addWidget(self.label)

        self.code_edit = QLineEdit(self.frame_2)
        self.code_edit.setObjectName(u"code_edit")

        self.verticalLayout_3.addWidget(self.code_edit)


        self.horizontalLayout_3.addWidget(self.frame_2)

        self.frame_8 = QFrame(self.frame_5)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(107, 0))
        self.frame_8.setFrameShape(QFrame.NoFrame)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_8)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.frame_8)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 0))

        self.verticalLayout_4.addWidget(self.label_2)

        self.name_edit = QLineEdit(self.frame_8)
        self.name_edit.setObjectName(u"name_edit")

        self.verticalLayout_4.addWidget(self.name_edit)


        self.horizontalLayout_3.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.frame_5)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(107, 0))
        self.frame_9.setFrameShape(QFrame.NoFrame)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.product_pic = QLabel(self.frame_9)
        self.product_pic.setObjectName(u"product_pic")
        self.product_pic.setGeometry(QRect(0, 0, 107, 107))
        self.product_pic.setMinimumSize(QSize(107, 107))
        self.product_pic.setMaximumSize(QSize(16777215, 20))
        self.product_pic.setPixmap(QPixmap(u"../resources/Product/no-image-icon-23492.png"))
        self.product_pic.setScaledContents(True)
        self.edit_pic = QPushButton(self.frame_9)
        self.edit_pic.setObjectName(u"edit_pic")
        self.edit_pic.setGeometry(QRect(-10, 0, 121, 111))

        self.horizontalLayout_3.addWidget(self.frame_9)


        self.verticalLayout_2.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.main_frame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(0, 107))
        self.frame_6.setFrameShape(QFrame.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_4.setSpacing(12)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_10 = QFrame(self.frame_6)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMaximumSize(QSize(150, 16777215))
        self.frame_10.setFrameShape(QFrame.NoFrame)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_10)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.frame_10)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(0, 0))

        self.verticalLayout_6.addWidget(self.label_4)

        self.value_edit = QLineEdit(self.frame_10)
        self.value_edit.setObjectName(u"value_edit")

        self.verticalLayout_6.addWidget(self.value_edit)


        self.horizontalLayout_4.addWidget(self.frame_10)

        self.frame_11 = QFrame(self.frame_6)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMaximumSize(QSize(90, 16777215))
        self.frame_11.setFrameShape(QFrame.NoFrame)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_11)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.frame_11)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(0, 0))

        self.verticalLayout_7.addWidget(self.label_5)

        self.stock_edit = QLineEdit(self.frame_11)
        self.stock_edit.setObjectName(u"stock_edit")

        self.verticalLayout_7.addWidget(self.stock_edit)


        self.horizontalLayout_4.addWidget(self.frame_11)

        self.frame_12 = QFrame(self.frame_6)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.NoFrame)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_12)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.frame_12)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(0, 0))

        self.verticalLayout_8.addWidget(self.label_6)

        self.description_edit = QLineEdit(self.frame_12)
        self.description_edit.setObjectName(u"description_edit")

        self.verticalLayout_8.addWidget(self.description_edit)


        self.horizontalLayout_4.addWidget(self.frame_12)


        self.verticalLayout_2.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.main_frame)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.NoFrame)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_7)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.insert_product_button = QPushButton(self.frame_7)
        self.insert_product_button.setObjectName(u"insert_product_button")

        self.verticalLayout_5.addWidget(self.insert_product_button)


        self.verticalLayout_2.addWidget(self.frame_7)


        self.verticalLayout.addWidget(self.main_frame)

        Produto.setCentralWidget(self.centralwidget)

        self.retranslateUi(Produto)

        QMetaObject.connectSlotsByName(Produto)
    # setupUi

    def retranslateUi(self, Produto):
        Produto.setWindowTitle(QCoreApplication.translate("Produto", u"MainWindow", None))
        self.close_button.setText("")
        self.label.setText(QCoreApplication.translate("Produto", u"*C\u00f3digo:", None))
        self.label_2.setText(QCoreApplication.translate("Produto", u"*Nome do produto:", None))
        self.product_pic.setText("")
        self.edit_pic.setText(QCoreApplication.translate("Produto", u"Inserir Imagem", None))
        self.label_4.setText(QCoreApplication.translate("Produto", u"*Valor:", None))
        self.label_5.setText(QCoreApplication.translate("Produto", u"*Estoque:", None))
        self.label_6.setText(QCoreApplication.translate("Produto", u"Descri\u00e7\u00e3o:", None))
        self.insert_product_button.setText(QCoreApplication.translate("Produto", u"Cadastrar Produto", None))
    # retranslateUi

