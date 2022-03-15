from query.conn import ConnMysql
from mysql.connector import Error

class Delete:
    def __init__(self,table,column,id):
        self.table = table
        self.id = id
        self.column = column
        self.conn = ConnMysql()

    def _sql(self):
        return f'DELETE FROM {self.table} WHERE {self.column} = {self.id} '

    def get(self):
        try:
            sql = self._sql()
            conn = self.conn.connection()
            cursor = conn.cursor()
            cursor.execute(sql)

            conn.commit()

            print(f'{cursor.rowcount} linha(s) deletada(s)')
        except Error as erro:
            print(f'Falha ao inserir dados ao banco {erro}')
        finally:
            if (conn.is_connected()):
                conn.close()
                print("conexao finalizada")

