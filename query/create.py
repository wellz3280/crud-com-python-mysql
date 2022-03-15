from query.take_by import TakeBy
from query.conn import ConnMysql
from mysql.connector import Error

class Create:
    def __init__(self,table,data):
        self.data = data
        self.table = table
        self.conn = ConnMysql()

    def _sql(self):
        takeby = TakeBy()

        colls = takeby.take_by_keys(self.data)
        vals = takeby.take_by_values(self.data)

        columns = ",".join(colls)
        values = "','".join(vals)

        sql = "INSERT INTO " + self.table + " (" + columns + ") VALUES ('" + values + "');"

        return sql

    def get(self):
        try:
            sql = self._sql()
            conn = self.conn.connection()
            cursor = conn.cursor()
            cursor.execute(sql)
            conn.commit()

            print(f'{cursor.rowcount} linhas afetadas')

        except Error as erro:

            print(f'Falha ao inserir dados ao banco {erro}')
            cursor.close()
        finally:
            if (conn.is_connected()):
                conn.close()
                print("conexao finalizada")