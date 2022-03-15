from query.conn import ConnMysql

class Select:
    def __init__(self,table):
        self.table = table
        self.conexao = ConnMysql()

    def sql(self):
        return f'SELECT * FROM {self.table}'

    def all(self):
        conn = self.conexao.connection()
        cursor = conn.cursor()

        cursor.execute(self.sql())

        result = cursor.fetchall()

        cursor.close()
        return  result

    def thisOne(self,id):
        conn = self.conexao.connection()
        cursor = conn.cursor()

        sql = f'{self.sql()} WHERE idPet = {id}'
        cursor.execute(sql)
        result = cursor.fetchone()
        cursor.close()
        return  result


