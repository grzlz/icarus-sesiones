import pandas as pd
import psycopg2

class ETL:
    def __init__(self, db_host, db_port, db_name, db_user, db_password):
        self.db_host = db_host
        self.db_port = db_port
        self.db_name = db_name
        self.db_user = db_user
        self.db_password = db_password
    
    def extraccion(self, table_name):
        # Establecer la conexión con la base de datos
        conn = psycopg2.connect(
            host=self.db_host,
            port=self.db_port,
            database=self.db_name,
            user=self.db_user,
            password=self.db_password
        )
        
        # Extraer los datos de la tabla específica
        query = f"SELECT * FROM {table_name}"
        df = pd.read_sql_query(query, conn)
        
        # Cerrar la conexión
        conn.close()
        
        return df
    
    def transformacion(self, df):
        # Realizar alguna operación de transformación en los datos
        # Por ejemplo, filtrar filas basándote en alguna condición. Todos los usuarios llamados Pedro
        transformed_df = df[df['nombre'] == "Pedro"]
         
        return transformed_df
    
    def carga(self, transformed_df, new_table_name):
        # Establecer una nueva conexión con la base de datos
        conn = psycopg2.connect(
            host=self.db_host,
            port=self.db_port,
            database=self.db_name,
            user=self.db_user,
            password=self.db_password
        )
        
        # Crear una nueva tabla en la base de datos
        cursor = conn.cursor()
        cursor.execute(f"CREATE TABLE {new_table_name} (user_id serial, role_id serial, nombre varchar, correo varchar)")
        
        # Insertar los datos transformados en la nueva tabla
        for row in transformed_df.itertuples(index=False):
            cursor.execute(f"INSERT INTO {new_table_name} VALUES %s", (row,))
        
        # Confirmar los cambios y cerrar la conexión
        conn.commit()
        conn.close()

etl = ETL(db_host='54.67.75.40', db_port=5432, db_name='portos', db_user='myuser', db_password='test')

# Extracción
df_extracted = etl.extraccion('tabla_1')

# Transformación
df_transformed = etl.transformacion(df_extracted)

# Carga
etl.carga(df_transformed, 'tabla_2')
#