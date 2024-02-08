import sqlite3

conn = sqlite3.connect('myDB.db')  # Cria uma conexão com o BD
c = conn.cursor()  # Cria um cursor para interagir com o BD

c.execute('''
    CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
    username TEXT NOT NULL, 
    password TEXT NOT NULL, 
    email TEXT NOT NULL) ''')

c.execute('''INSERT INTO users (username, password, email) VALUES ('admin', 'admin', 'admin@gmail.com')''')

c.execute('''
    CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    code TEXT NOT NULL,
    name TEXT NOT NULL,
    value FLOAT NOT NULL,
    stock INTEGER NOT NULL,
    pic VARCHAR(40) NOT NULL,
    description TEXT NOT NULL
);
''')

c.execute('''INSERT INTO products (code, name, value, stock, pic, description) VALUES ('001', 'Cyberpunk 2077', '200,00', '15', '../../resources/Product/001.jpg', 'Jogo de Ação e Aventura')
''')
c.execute('''INSERT INTO products (code, name, value, stock, pic, description) VALUES ('002', '7 Days to Die', '75,79', '80', '../../resources/Product/002.jpg', 'Jogo de Ação e sobrevivência em apocalipse zumbi')
''')

conn.commit()  # Executa o código SQLite
