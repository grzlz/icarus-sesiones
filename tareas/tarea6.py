import sys 
import psycopg2
import pandas as pd
from sqlalchemy import create_engine

class Procesadordedatos():
    def __init__(self, conexion, usuario, contraseña, basededatos, tabla_fuente, tabla_destino, puerto):
        self.conexion = conexion
        self.usuario = usuario
        self.contraseña = contraseña
        self.basededatos = basededatos
        self.tabla_fuente = tabla_fuente
        self.tabla_destino = tabla_destino
        self.puerto = puerto
    def conectar(self):
        connection = psycopg2.connect(
            database= self.basededatos,
            user= self.usuario,
            password=self.contraseña,
            host=self.conexion,
            port=self.puerto)
    def extraer(self):
        Procesadordedatos.conectar()
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM {self.tabla_fuente}")
        rows = cursor.fetchall()
        column_names = [desc[0] for desc in cursor.description]
        df = pd.DataFrame(rows, columns=column_names)
        cursor.close()
        connection.close()
        print(f'Estos son los datos de {self.tabla_fuente} \ {df}')
    def transformar(self):
        Procesadordedatos.extraer()
        df['Promedio'] = df.mean(axis=1)
        print(f'Incorporo una nueva columna con los promedios. \ {df}')
    def load(self):
        Procesadordedatos.transformar()
        Procesadordedatos.conectar()
        engine = create_engine('postgresql+psycopg2://', creator=lambda: connection)
        df.to_sql(self.tabla_destino, engine, if_exists='replace', index=False)
        connection.close()
        print(f'La base de datos {self.tabla_destino} se ha cargado con éxito')

mi_basededatos = Procesadordedatos("54.67.75.40", "myuser", "test", "paco", "tabla_paco", "tabla_paco1", "5432")

mi_basededatos.extraer()
mi_basededatos.transformar()
mi_basededatos.load()
