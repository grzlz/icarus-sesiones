class Procesador_datos:
    def __init__(self,conexion,basededatos, tabla_fuente, tabla_destino):
        self.conexion = conexion
        self.basededatos = basededatos
        self.tabla_fuente = tabla_fuente
    def extraer(self):
        print(f"Extrayendo la tabla {self.tabla_fuente} de la base de datos {self.basededatos} con la conexión {self.conexion}.")
    def transformar(self):
        print(f"Estoy transformando los datos de la tabla {self.tabla_fuente}.")
    def load(self):
        print(f"Estoy cargando {self.basededatos} desde {self.tabla_fuente} hacia {tabla_destino}.")
    
mi_basededatos = Procesador_datos(1,"portos","tabla1","tabla2")

mi_basededatos.extraer()
