import psycopg2 as db

conexion = db.connect(user='postgres',
                 password='admin',
                 host='127.0.0.1',
                 port='5432',
                 database= 'test_db')

cursor = conexion.cursor()
sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES (%s, %s, %s)'
valores = (
    ('Cristian', 'Juarez', 'crisjua@mail.com',),
    ('Fernanda', 'Villanueva', 'fervilla@mail.com',),
    ('Julieta', 'rodriguez', 'juliro@mail.com',)
)
cursor.executemany(sentencia, valores)
conexion.commit()
registros_insertados = cursor.rowcount
print(f'Registros insertados: {registros_insertados}')
cursor.close()
conexion.close()