import pandas as pd
import psycopg2

class ETL:
    def __init__(self, host, port, database, user, password):
        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.password = password

    def extract(self, table_name):
        connection = psycopg2.connect(
            host=self.host,
            port=self.port,
            database=self.database,
            user=self.user,
            password=self.password
        )
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM {table_name}")
        rows = cursor.fetchall()
        column_names = [desc[0] for desc in cursor.description]
        cursor.close()
        connection.close()
        return pd.DataFrame(rows, columns=column_names)

    def transform(self, df):
        df['mean'] = df.mean(axis=1)
        return df

    def load(self, df, table_name):
        connection = psycopg2.connect(
            host=self.host,
            port=self.port,
            database=self.database,
            user=self.user,
            password=self.password
            )
        cursor = connection.cursor()
        #columns = ', '.join([f"{column_name} {data_type}" for column_name, data_type in zip(df.columns, df.dtypes)])
        #cursor.execute(f"CREATE TABLE {table_name} ({columns})")
        cursor.execute(f"CREATE TABLE {table_name} (zero float, one float, mean float)")
        for _, row in df.iterrows():
            cursor.execute(f"INSERT INTO {table_name} VALUES {tuple(row)}")
        connection.commit()
        cursor.close()
        connection.close()


etl = ETL("54.67.75.40", "5432", "paco", "myuser", "test")

paso1 = etl.extract("tablapaco")
paso2 = etl.transform(paso1)
paso3 = etl.load(paso2, "tablapaco1")

