from PySide6.QtSql import QSqlDatabase, QSqlQuery

SELECT_USER_QUERY = "SELECT * FROM users WHERE username = ?"

INSERT_PRODUCT_QUERY = "INSERT INTO products (code, name, value, stock, description, pic) VALUES (?, ?, ?, ?, ?, ?)"

SELECT_PRODUCT_QUERY = "SELECT * FROM products WHERE code = ?"


def create_connection():
    conn = QSqlDatabase.addDatabase('QSQLITE')
    conn.setDatabaseName('myDB.db')

    if not conn.open():
        print('Database error: %s' % conn.lastError().text())
        return False
    else:
        print("Database connection established")
        return True
