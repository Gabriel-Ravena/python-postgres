import psycopg2 as db

conexion = db.connect(user='postgres',
                 password='admin',
                 host='127.0.0.1',
                 port='5432',
                 database= 'test_db')

cursor = conexion.cursor()
sql = 'SELECT * FROM persona WHERE id_persona IN %s'
entrada = input("Proporciona pks a ver(separados por coma):")
tupla = tuple(entrada.split(','))
#print(tupla)
llaves_primarias = (tupla,)
cursor.execute(sql, llaves_primarias)
registros = cursor.fetchall()
for registro in registros:
    print(registros)

cursor.close()
conexion.close()
