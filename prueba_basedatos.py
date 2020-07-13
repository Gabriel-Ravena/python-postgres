import psycopg2
#Declaramos la variable con los datos de la conexión de nuestra base de datos en postgres
conexion = psycopg2.connect(user='postgres',
                 password='admin',
                 host='127.0.0.1',
                 port='5432',
                 database= 'test_db')

cursor = conexion.cursor()
sql = 'SELECT * FROM persona ORDER BY id_persona'
cursor.execute(sql)
registros = cursor.fetchall()
print(registros)

cursor.close()
conexion.close()

