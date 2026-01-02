from flask import Flask, render_template
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

def conectar_bd():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='csv_db 11', # Nombre de tu base de datos
        port=3306 
    )

@app.route('/')
def index():
    try:
        conexion = conectar_bd()
        cursor = conexion.cursor(dictionary=True)
        
        # Usamos comillas invertidas (`) porque los nombres tienen espacios
        query = """
            SELECT `COL 2`, `COL 7`, `COL 13`, `COL 19` 
            FROM `programas_de_universidades_8`
        """
        
        cursor.execute(query)
        mis_programas = cursor.fetchall()
        
        cursor.close()
        conexion.close()
        
        return render_template('index.html', programas=mis_programas)
        
    except Error as e:
        return f"Hubo un error al conectar a la base de datos: {e}"

if __name__ == '__main__':
    app.run(debug=True)