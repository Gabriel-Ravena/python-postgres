import psycopg2 as db

conexion = db.connect(user='postgres',
                 password='admin',
                 host='127.0.0.1',
                 port='5432',
                 database= 'test_db')
try:
    #conexion.autocommit = True
    cursor = conexion.cursor()
    sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES (%s, %s, %s)'
    valores = ['Sergio2', 'Maydana12345', 'smaydana@mail.com']
    cursor.execute(sentencia, valores)

    sentencia = 'UPDATE persona SET nombre = %s, apellido = %s, email = %s WHERE id_persona = %s'
    valores = ['Beto1', 'Ifran2', 'beto3@mail.com', 12]
    cursor.execute(sentencia, valores)

    conexion.commit()
except Exception as e:
    conexion.rollback()
    print(f"Ocurrió un error en la transacción: {e}")
finally:
    cursor.close()
    conexion.close()
