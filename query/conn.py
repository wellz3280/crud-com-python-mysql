import mysql.connector

class ConnMysql:
    def _data_conn(self):
        data = {'host':'localhost','database':'testeApi','user':'root','password':''}
        return data

    def connection(self):
        data = self._data_conn()
        conn = mysql.connector.connect(
            host = data['host'],
            database = data['database'],
            user = data['user'],
            password = data['password']
        )

        return conn