import psycopg2

try:
    connection = psycopg2.connect(
        user="myuser",
        password="test",
        host="54.67.75.40",
        port="5432",
        database="paco"
    )

    cursor = connection.cursor()



    # Print PostgreSQL version
    query = """
    CREATE TABLE IF NOT EXISTS testing(first_number INT, second_number INT);
    INSERT INTO testing(first_number, second_number) VALUES (2, 7);
    SELECT * FROM testing;
    """
    cursor.execute(query)
    record = cursor.fetchall()
    print(record)

except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL", error)
