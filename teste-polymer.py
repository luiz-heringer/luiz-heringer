import mysql.connector

config = {
    'user': 'luiz.heringer',
    'password': 123456,
    'host': 'localhost',
    'database': 'meu_banco_de_dados',
}

try:
    connection = mysql.connector.connect(**config)

    if connection.is_connected():
        print("Conexão bem-sucedida.")

except mysql.connector.Error as err:
    print(f"Erro ao conectar: {err}")
finally:
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print("Conexão fechada.")
