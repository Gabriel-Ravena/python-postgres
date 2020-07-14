import psycopg2 as db

conexion = db.connect(user='postgres',
                 password='admin',
                 host='127.0.0.1',
                 port='5432',
                 database= 'test_db')

cursor = conexion.cursor()
sentencia = 'UPDATE persona SET nombre = %s, apellido = %s, email = %s WHERE id_persona = %s'
valores = (('Noelia', 'Gaitan', 'noega@mail.com', 7),
           ('Macarena', 'Martinez', 'maca@mail.com', 8),
           ('Mariana', 'Gonzales', 'margon@mail.com', 14)
           )
cursor.executemany(sentencia, valores)
conexion.commit()
registros_actualizados = cursor.rowcount
print(f'Registros actualizados: {registros_actualizados}')
cursor.close()
conexion.close()