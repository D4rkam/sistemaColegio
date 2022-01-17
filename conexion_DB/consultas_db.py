import sqlite3

class Conectar_db():
    nombre_db = 'DB/miSistema_db.db'

    def run_db(self, query, parametros = ()):
        with sqlite3.connect(self.nombre_db) as conexion:
            cursor = conexion.cursor()
            datos = cursor.execute(query, parametros)

            conexion.commit()
        return datos