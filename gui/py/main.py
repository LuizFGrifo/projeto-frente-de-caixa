from ui_login import Ui_Login
from ui_main import Ui_MainWindow
from ui_product import Ui_Produto
from pyside_imports import *


class UiPrduct(QMainWindow, Ui_Produto):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.q = QSqlQuery()

        # Removendo a toolbar e a cor das bordas
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.close_button.clicked.connect(self.close)
        self.insert_product_button.clicked.connect(self.insert_product)

        self.picture = "../../resources/Product/no-product.png"
        self.product_pic.setPixmap(QPixmap(self.picture))

        self.edit_pic.clicked.connect(self.update_pic)

        self.code_edit.setValidator(QIntValidator())
        self.stock_edit.setValidator(QIntValidator())
        self.value_edit.setValidator(QDoubleValidator())

    def insert_product(self):
        code = self.code_edit.text()
        name = self.name_edit.text()
        value = self.value_edit.text()
        stock = self.stock_edit.text()
        description = self.description_edit.text()

        if code == "" or name == "" or value == "" or stock == "":
            QMessageBox.warning(self, "Error", "Preencha todos os campos obrigatórios")

        self.q.prepare(INSERT_PRODUCT_QUERY)
        self.q.bindValue(0, code)
        self.q.bindValue(1, name)
        self.q.bindValue(2, value)
        self.q.bindValue(3, stock)
        self.q.bindValue(4, description)

        if self.picture != "../../resources/Product/no-product.png":
            extension = self.picture.split(".")[-1]
            self.q.bindValue(5, "../../resources/Product/" + code + "." + extension)
        else:
            self.q.bindValue(5, self.picture)

        self.q.exec()

        if self.q.lastError().isValid():
            QMessageBox.warning(self, "Error", self.q.lastError().text())
        else:
            QMessageBox.information(self, "Sucesso", "Produto cadastrado com sucesso!")

            if self.picture != "../../resources/Product/no-product.png":
                extension = self.picture.split(".")[-1]
                shutil.copy(self.picture, "../../resources/Product/" + code + "." + extension)

            self.close()

    def update_pic(self):
        options = QFileDialog.DontUseNativeDialog

        # Para pegar apenas o path do arquivo, usamos o "_"
        file, _ = QFileDialog.getOpenFileName(self, "Selecione a imagem do produto!", "",
                                              "Arquivos de imagem(*.png *.jpg *.jpeg *.webp)", options=options)

        if file:
            self.picture = file
            self.product_pic.setPixmap(QPixmap(self.picture))

    # Para poder mover a tela sem toolbar
    def mousePressEvent(self, event):
        self.dragPos = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event):
        self.move(self.pos() + event.globalPosition().toPoint() - self.dragPos)
        self.dragPos = event.globalPosition().toPoint()
        event.accept()


class UiMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.product_window = None
        self.setupUi(self)

        self.q = QSqlQuery()

        self.product_edit.textChanged.connect(self.search_product)
        self.cancel_item_button.clicked.connect(self.remove_product)
        self.discount_button.clicked.connect(self.give_discount)
        self.centralwidget.installEventFilter(self)

        self.product_pic.setPixmap(QPixmap("../../resources/Product/no-product.png"))

    def eventFilter(self, obj, event):  # Lógica da tecla de atalho F5
        if event.type() == QEvent.KeyPress:
            if event.key() == Qt.Key_F5:
                self.remove_product()
            if event.key() == Qt.Key_F6:
                self.give_discount()
            if event.key() == Qt.Key_F10:
                self.product_window = UiPrduct()
                self.product_window.show()

        return False

    def update_info(self):
        self.product_edit.setText('')

        itens = self.tableWidget.rowCount()
        quant = 0
        discount = 0.0

        for item in range(itens):
            item = self.tableWidget.item(item, 2)
            item_discount = float(self.tableWidget.item(item.row(), 4).text().replace(',', '.'))
            quant = float(quant + int(item.text()))
            discount += (float(item.text()) * item_discount)

        self.items_label.setText(
            '<html><head/><body><p><span style=\" font-weight:700; color:#27acff;\">Itens: </span><span style=\" '
            'font-weight:700; color:#8f8f8f;\">{}</span></p></body></html>'.format(
                itens))
        self.quant_label.setText(
            '<html><head/><body><p><span style=\" font-weight:700; color:#27acff;\">Quantidade: </span><span style=\" '
            'font-weight:700; color:#8f8f8f;\">{}</span></p></body></html>'.format(
                quant))
        self.discount_label.setText('<html><head/><body><p><span style=\" font-weight:700; '
                                    'color:#27acff;\">Devolu\u00e7\u00e3o/Desconto: </span><span style=\" '
                                    'font-weight:700; color:#a5a5a5;\">{}</span></p></body></html>'.format(discount))

        if itens == 0:
            self.product_label.setText("")
            self.stock_edit.setText("")
            self.value_edit.setText("")
            self.product_pic.setPixmap(QPixmap("../../resources/Product/no-product.png"))

    def remove_product(self):
        product = self.tableWidget.selectedItems()

        if int(product[2].text()) > 1:
            self.tableWidget.setItem(product[0].row(), 2, QTableWidgetItem(str(int(product[2].text()) - 1)))
        else:
            self.tableWidget.removeRow(product[0].row())

        self.update_info()

    def give_discount(self):
        discount, ok = QInputDialog.getDouble(self, "Desconto", "Digite o valor de desconto")

        product_value = self.tableWidget.item(self.tableWidget.currentRow(), 3)

        if discount > 0 and discount <= float(product_value.text().replace(',', '.')):
            self.tableWidget.setItem(product_value.row(), 4, QTableWidgetItem(str(discount)))

        self.update_info()

    def search_product(self):
        code = self.product_edit.text()
        self.q.prepare(SELECT_PRODUCT_QUERY)
        self.q.addBindValue(code)

        self.q.exec()

        if self.q.first():
            self.product_label.setText(self.q.value("name"))
            self.stock_edit.setText(str(self.q.value('stock')))
            self.value_edit.setText(str(self.q.value('value')))
            self.product_pic.setPixmap(QPixmap(self.q.value('pic')))

            self.add_products_to_table(self.q)

    def add_products_to_table(self, product):
        item = self.tableWidget.findItems(product.value('code'), Qt.MatchExactly)

        if item:
            row_table = item[0].row()
            quant = int(self.tableWidget.item(row_table, 2).text())

            if product.value('stock') > quant:
                self.tableWidget.setItem(row_table, 2, QTableWidgetItem(str(quant + 1)))
            else:
                QMessageBox.warning(self, 'Estoque insuficiente', 'O estoque atingiu o limite!')
        else:
            row = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row)
            self.tableWidget.setItem(row, 0, QTableWidgetItem(product.value('code')))
            self.tableWidget.setItem(row, 1, QTableWidgetItem(product.value('name')))
            self.tableWidget.setItem(row, 2, QTableWidgetItem('1'))
            self.tableWidget.setItem(row, 3, QTableWidgetItem(str(product.value('value'))))
            self.tableWidget.setItem(row, 4, QTableWidgetItem('0,0'))

        self.update_info()


class UiLogin(QMainWindow, Ui_Login):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.q = QSqlQuery()  # Para executar a query nesta janela

        # Removendo a toolbar e a cor das bordas
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # Mover a tela para o centro
        self.move(self.screen().availableGeometry().center() - self.frameGeometry().center())

        # Adicionando funções minimizar e fechar dos botões
        self.minimize_button.clicked.connect(self.showMinimized)
        self.close_button.clicked.connect(self.close)

        # Função para realizar login
        self.login_button.clicked.connect(self.login)
        self.username_edit.returnPressed.connect(self.login)
        self.password_edit.returnPressed.connect(self.login)

    # Para poder mover a tela sem toolbar
    def mousePressEvent(self, event):
        self.dragPos = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event):
        self.move(self.pos() + event.globalPosition().toPoint() - self.dragPos)
        self.dragPos = event.globalPosition().toPoint()
        event.accept()

    def login(self):
        userName = self.username_edit.text()  # Para pegar o texto
        password = self.password_edit.text()

        if userName == "" or password == "":
            self.error_label.setText('ERROR: Preencha todos os campos!')
        else:
            self.error_label.setText("")

            self.q.prepare(SELECT_USER_QUERY)
            self.q.addBindValue(userName)  # Substitui o "?" para o valor do userName

            self.q.exec()

            if self.q.first():
                if self.q.value("password") == password:
                    self.close()  # Para fechar a janela
                    main_window.show()
                else:
                    self.error_label.setText("Senha incorreta!")
            else:
                self.error_label.setText("Usuário não encontrado!")
            self.q.finish()  # Finaliza a query quando terminarmos o login


if __name__ == "__main__":
    app = QApplication([])
    conn = create_connection()
    main_window = UiMainWindow()
    window = UiLogin()
    window.show()
    app.exec()
