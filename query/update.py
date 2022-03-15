from query.take_by import TakeBy
from query.conn import ConnMysql
from mysql.connector import Error

class Update:
    def __init__(self,table,data):
        self.table = table
        self.data = data
        self.conn = ConnMysql()
        self.take_by = TakeBy()
        
    def sql(self):
        column = self.take_by.take_by_keys(self.data)
        values = self.take_by.take_by_values(self.data)



        # return f'UPDATE {self.table} SET {column} WHERE  '


data = {'id':'1','nome':'weliton','idade':'36'}
teste = Update('teste',data)
teste.sql()