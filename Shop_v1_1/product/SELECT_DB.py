import sqlite3
from sqlite3 import Error

__all__ = ["product_all" , "ProDataList" , "products"]


class _DataClass:
    """ класс для хранения строк из базы данных
    (WARNING) используеться для класса DATALIST
              применение из вне не желательно
    """
    def __init__(self, db_data , rowid_key : bool = False):
        shift = 0
        if rowid_key:
            self.rowid = db_data[0]
            shift = 1
        self.category_id = db_data[0 + shift]
        self.title = db_data[1 + shift]
        self.description = db_data[2+shift]
        self.url_photo = db_data[3 + shift]
        self.rowid_key = rowid_key

    def __str__(self) -> str:
        if self.rowid_key:
            return f'{self.rowid} | {self.category_id} | {self.title} | {self.description} | {self.url_photo}'
        else:
            return f'{self.category_id} | {self.title} | {self.description} | {self.url_photo}'
        

class ProDataList:
    """ класс для хранения таблицы из базы данных """
    data_list = []

    def __init__(self, L_data , rowid_key : bool = False):
        print(L_data)
        for i in L_data:
            self.data_list.append(_DataClass(i, rowid_key))
            
    def __str__(self) -> str:
        dataListStr = """"""

        for i in self.data_list:
            dataListStr += str(i) + "\n"
        
        return dataListStr


def product_all(db_file : str = "./database/shop.sqlite" , rowid : bool = False):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(conn)
        c = conn.cursor()
        if rowid:
            c.execute('''
            SELECT rowid, * FROM product;
            ''')
        else:
            c.execute('''
            SELECT * FROM product;
            ''')
        return c.fetchall()
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

def product_id(sid , db_file : str = "./database/shop.sqlite" , rowid : bool = False ):
    """ create a database connection to a SQLite database """
    conn = None
    
    try:
        conn = sqlite3.connect(db_file)
        print(conn)
        c = conn.cursor()
        if rowid:
            c.execute(f'''
            SELECT rowid, * FROM product WHERE rowid = {sid};
            ''')
        else:
            c.execute(f'''
            SELECT * FROM product WHERE  = {sid};
            ''')
        return c.fetchall()
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

def product_title(title , db_file : str = "./database/shop.sqlite" , rowid : bool = False ):
    """ create a database connection to a SQLite database """
    conn = None
    
    try:
        conn = sqlite3.connect(db_file)
        print(conn)
        c = conn.cursor()
        if rowid:
            c.execute(f'''
            SELECT rowid, * FROM product WHERE title = '{title}';
            ''')
        else:
            c.execute(f'''
            SELECT * FROM product WHERE title = '{title}';
            ''')
        return c.fetchall()
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

def product_cat(cat_id , db_file : str = "./database/shop.sqlite" , rowid : bool = False):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(conn)
        c = conn.cursor()
        if rowid:
            c.execute(f'''
            SELECT rowid, * FROM product WHERE category_id = {cat_id};
            ''')
        else:
            c.execute(f'''
            SELECT * , rowid FROM product WHERE category_id = {cat_id};
            ''')
        return c.fetchall()
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()



def products( title = "" , sid : int = -1 , cat_id : int = -1):
    if sid == -1 and cat_id == -1 and title == "":
        return ProDataList(product_all())
    elif sid >= 0:
        return ProDataList(product_id(sid))
    elif cat_id >= 0:
        return ProDataList(product_cat( cat_id))
    elif title != "":
        return ProDataList(product_title(title))