from mysql.connector import pooling
from mysql.connector import Error

class Conexion:
    host = '127.0.0.1'
    port = 3307
    user = 'root'
    password = 'admin'
    database = 'zona_fit_db'
    pool_size = 5
    pool_name = 'zona_fit_pool'
    pool = None

    @classmethod
    def obtener_pool(cls):
        if cls.pool is None: # Se crea el objeto pool
            try:
                cls.pool = pooling.MySQLConnectionPool(
                    pool_name = cls.pool_name,
                    pool_size = cls.pool_size,
                    host = cls.host,
                    port = cls.port,
                    database = cls.database,
                    user = cls.user,
                    password = cls.password
                )
                return cls.pool
            except Error as e:
                print(f'Ocurrio un error al obtener pool: {e}')
        else:
            return cls.pool

    @classmethod
    def obtener_conexion(cls):
        return cls.obtener_pool().get_connection()

    @classmethod
    def liberar_conexion(cls, conexion):
        conexion.close()


if __name__ == '__main__':
    # Creamos un objeto pool
    pool = Conexion.obtener_pool()
    print(pool)
    conexion1 = pool.get_connection()
    print(conexion1)
    Conexion.liberar_conexion(conexion1)
    print(f'Se ha liberado el objeto conexion1')
