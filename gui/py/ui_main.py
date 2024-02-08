from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize, Qt)
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QFrame,
                               QHBoxLayout, QLabel, QLineEdit,
                               QPushButton, QSizePolicy, QSpacerItem,
                               QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 600)
        MainWindow.setMinimumSize(QSize(1000, 600))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QFrame#topbar_frame {\n"
                                         "	background-color: #0F102E\n"
                                         "}\n"
                                         "\n"
                                         "QFrame#bottom_frame {\n"
                                         "	background-color: white;\n"
                                         "}\n"
                                         "\n"
                                         "QLabel#product_label{\n"
                                         "	font-size: 25px;\n"
                                         "	color: white;\n"
                                         "}\n"
                                         "\n"
                                         "QLineEdit{\n"
                                         "	background-color: white;\n"
                                         "	min-height: 35px;\n"
                                         "	border-radius: 15px;\n"
                                         "	padding-left: 20px;\n"
                                         "	font-weight: bold;\n"
                                         "	font-size: 15px;\n"
                                         "}\n"
                                         "\n"
                                         "QLineEdit#product_edit::focus{\n"
                                         "	border: 2px solid #36AFFF;\n"
                                         "}\n"
                                         "\n"
                                         "QLineEdit#product_edit::hover{\n"
                                         "	border: 2px solid #36AFFF;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton#discount_button {\n"
                                         "	border: none;\n"
                                         "	font-weight: bold;\n"
                                         "	color: #00D400\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton#cancel_item_button {\n"
                                         "	border: none;\n"
                                         "	font-weight: bold;\n"
                                         "	color: #F20000\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton#finish_button {\n"
                                         "	background-color: #27ACFF;\n"
                                         "	color: white;\n"
                                         "	font-size: 20px;\n"
                                         "	min-height: 40px;\n"
                                         "	border: none\n"
                                         "}\n"
                                         "\n"
                                         "QTableWidget {\n"
                                         "	background-color: white;\n"
                                         "	color: black;\n"
                                         "}")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.topbar_frame = QFrame(self.centralwidget)
        self.topbar_frame.setObjectName(u"topbar_frame")
        self.topbar_frame.setMinimumSize(QSize(0, 50))
        self.topbar_frame.setMaximumSize(QSize(16777215, 50))
        self.topbar_frame.setFrameShape(QFrame.NoFrame)
        self.topbar_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.topbar_frame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.product_label = QLabel(self.topbar_frame)
        self.product_label.setObjectName(u"product_label")
        self.product_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.product_label)

        self.verticalLayout.addWidget(self.topbar_frame)

        self.main_frame = QFrame(self.centralwidget)
        self.main_frame.setObjectName(u"main_frame")
        self.main_frame.setFrameShape(QFrame.NoFrame)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.main_frame)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(50, 0, 50, 12)
        self.left_frame = QFrame(self.main_frame)
        self.left_frame.setObjectName(u"left_frame")
        self.left_frame.setMinimumSize(QSize(400, 0))
        self.left_frame.setFrameShape(QFrame.NoFrame)
        self.left_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.left_frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 20, 0, 0)
        self.product_edit = QLineEdit(self.left_frame)
        self.product_edit.setObjectName(u"product_edit")

        self.verticalLayout_2.addWidget(self.product_edit)

        self.frame = QFrame(self.left_frame)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 50))
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.stock_edit = QLineEdit(self.frame)
        self.stock_edit.setObjectName(u"stock_edit")
        self.stock_edit.setEnabled(False)

        self.horizontalLayout_2.addWidget(self.stock_edit)

        self.value_edit = QLineEdit(self.frame)
        self.value_edit.setObjectName(u"value_edit")
        self.value_edit.setEnabled(False)

        self.horizontalLayout_2.addWidget(self.value_edit)

        self.verticalLayout_2.addWidget(self.frame)

        self.frame_2 = QFrame(self.left_frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.product_pic = QLabel(self.frame_2)
        self.product_pic.setObjectName(u"product_pic")
        self.product_pic.setMinimumSize(QSize(200, 300))
        self.product_pic.setMaximumSize(QSize(200, 300))
        self.product_pic.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.product_pic)

        self.verticalLayout_2.addWidget(self.frame_2)

        self.horizontalLayout.addWidget(self.left_frame)

        self.right_frame = QFrame(self.main_frame)
        self.right_frame.setObjectName(u"right_frame")
        self.right_frame.setMinimumSize(QSize(400, 0))
        self.right_frame.setFrameShape(QFrame.NoFrame)
        self.right_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.right_frame)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 20, 0, 0)
        self.frame_3 = QFrame(self.right_frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 0))
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_5.setSpacing(20)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)

        self.discount_button = QPushButton(self.frame_3)
        self.discount_button.setObjectName(u"discount_button")

        self.horizontalLayout_5.addWidget(self.discount_button)

        self.cancel_item_button = QPushButton(self.frame_3)
        self.cancel_item_button.setObjectName(u"cancel_item_button")

        self.horizontalLayout_5.addWidget(self.cancel_item_button)

        self.verticalLayout_3.addWidget(self.frame_3)

        self.tableWidget = QTableWidget(self.right_frame)
        if (self.tableWidget.columnCount() < 5):
            self.tableWidget.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setShowGrid(False)
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setProperty("showSortIndicator", False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_3.addWidget(self.tableWidget)

        self.frame_4 = QFrame(self.right_frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 30))
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.items_label = QLabel(self.frame_4)
        self.items_label.setObjectName(u"items_label")

        self.horizontalLayout_6.addWidget(self.items_label)

        self.quant_label = QLabel(self.frame_4)
        self.quant_label.setObjectName(u"quant_label")

        self.horizontalLayout_6.addWidget(self.quant_label)

        self.discount_label = QLabel(self.frame_4)
        self.discount_label.setObjectName(u"discount_label")

        self.horizontalLayout_6.addWidget(self.discount_label)

        self.verticalLayout_3.addWidget(self.frame_4)

        self.finish_button = QPushButton(self.right_frame)
        self.finish_button.setObjectName(u"finish_button")

        self.verticalLayout_3.addWidget(self.finish_button)

        self.horizontalLayout.addWidget(self.right_frame)

        self.verticalLayout.addWidget(self.main_frame)

        self.bottom_frame = QFrame(self.centralwidget)
        self.bottom_frame.setObjectName(u"bottom_frame")
        self.bottom_frame.setMinimumSize(QSize(0, 50))
        self.bottom_frame.setMaximumSize(QSize(16777215, 50))
        self.bottom_frame.setFrameShape(QFrame.NoFrame)
        self.bottom_frame.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.bottom_frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Frente de Caixa V.1.0", None))
        self.product_label.setText("")
        self.product_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Produto", None))
        self.stock_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Estoque", None))
        self.value_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Valor Unit.", None))
        self.product_pic.setText("")
        self.discount_button.setText(QCoreApplication.translate("MainWindow", u"Desconto (F6)", None))
        self.cancel_item_button.setText(QCoreApplication.translate("MainWindow", u"Cancelar Item (F5)", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"COD", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"PRODUTO", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"QUANT", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"VALOR UNIT", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"DESCONTO", None));
        self.items_label.setText(QCoreApplication.translate("MainWindow",
                                                            u"<html><head/><body><p><span style=\" font-weight:700; color:#27acff;\">Itens: </span><span style=\" font-weight:700; color:#a5a5a5;\">000</span></p></body></html>",
                                                            None))
        self.quant_label.setText(QCoreApplication.translate("MainWindow",
                                                            u"<html><head/><body><p><span style=\" font-weight:700; color:#27acff;\">Quantidade: </span><span style=\" font-weight:700; color:#a5a5a5;\">000</span></p></body></html>",
                                                            None))
        self.discount_label.setText(QCoreApplication.translate("MainWindow",
                                                               u"<html><head/><body><p><span style=\" font-weight:700; color:#27acff;\">Devolu\u00e7\u00e3o/Desconto: </span><span style=\" font-weight:700; color:#a5a5a5;\">000</span></p></body></html>",
                                                               None))
        self.finish_button.setText(QCoreApplication.translate("MainWindow", u"Finalizar Venda (F3)", None))
    # retranslateUi
