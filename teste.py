from query.select import Select
from query.create import Create

data = {'name':'Malvadão','raca':'pintcher','idade':'18'}
insert = Create('pets',data).get()



# print(f'id: {thisOne[0]} ')
# print(f'nome: {thisOne[1]} ')
# print(f'raça: {thisOne[2]} ')
# print(f'idade: {thisOne[3]} ')
# import mysql.connector

# conexao = ConnMysql()
# conn = conexao.connection()
# cursor = conn.cursor()


# CREATE
# sql =  'INSERT INTO pets (name,raca,idade) VALUES ("teste","gato do sul",6)'
#
# cursor.execute(sql)
#
# conn.commit()

# READ

# sql = 'SELECT * FROM pets'
#
# cursor.execute(sql)
# result = cursor.fetchall()
#
# pets = []
# for data in result:
#    name,raca,idade = data[1],data[2],data[3]
#    print(f'nome:{name},raça:{raca},idade:{idade}')
# UPDATE
# sql = f'UPDATE pets SET name = "petisco" WHERE idPet = 2 '
# cursor.execute(sql)
# conn.commit()
#
# cursor.close()
#
# # DELETE
# sql = f'DELETE FROM pets WHERE idPet = 4'
# cursor.execute(sql)
# conn.commit()
# cursor.close()