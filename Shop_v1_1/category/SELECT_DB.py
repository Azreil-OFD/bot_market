import sqlite3
from sqlite3 import Error


__all__ = ["CatDataList" , "category_all" , "category"]

class _DataClass:
    """ класс для хранения строк из базы данных
    (WARNING) используеться для класса DATALIST
              применение из вне не желательно
    """
    def __init__(self, db_data):

        self.id = db_data[0]
        self.title = db_data[1]
        self.description = db_data[2]

    def __str__(self) -> str:
        return f'{self.id} | {self.title} | {self.description}'
        
        

class CatDataList:
    """ класс для хранения таблицы из базы данных """
    data_list = []

    def __init__(self, L_data):
        for i in L_data:
            self.data_list.append(_DataClass(i))

    def __str__(self) -> str:
        dataListStr = """"""

        for i in self.data_list:
            dataListStr += str(i) + "\n"
        
        return dataListStr

def category_all(db_file : str = "./database/shop.sqlite"):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(conn)
        c = conn.cursor()

        c.execute('''
            SELECT * FROM category;
            ''')
        return c.fetchall()
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


def category():
    return CatDataList(category_all())