import pymysql

# Establecer la conexión a la base de datos
conexion = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    db='emprendimiento'
)


try:
    with conexion.cursor() as cursor:
        # Agregar una nueva imagen (debe ser PNG o JPG)
        with open('ruta/a/tu/imagen.png', 'rb') as archivo:
            datos_imagen = archivo.read()
            agregar_imagen = "INSERT INTO mi_tabla (nombre, imagen) VALUES (%s, %s)"
            cursor.execute(agregar_imagen, ('Nombre de la imagen', datos_imagen))
        conexion.commit()

        # ... (El resto del código permanece igual)

except Exception as e:
    print(f"Error: {e}")
    conexion.rollback()

finally:
    conexion.close()