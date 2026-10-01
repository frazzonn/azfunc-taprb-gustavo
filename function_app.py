import logging
import azure.functions as func
import os
import pyodbc

app = func.FunctionApp()

@app.timer_trigger(schedule="0 * * * * *", arg_name="myTimer", run_on_startup=False,
            use_monitor=False) 

def extract_chamado(myTimer: func.TimerRequest) -> None:

    host = os.getenv("host")
    database = os.getenv("database")
    user = os.getenv("user")
    password = os.getenv("password")

    conn_str = (
        "DRIVER={ODBC Driver 18 for SQL Server};"
        f"SERVER={host};"
        f"DATABASE={database};"
        f"UID={user};"
        f"PWD={password};"
        "Encrypt=yes;"
        "TrustServerCertificate=no;"
        "Connection Timeout=30;"
    )
    
    connection = pyodbc.connect(conn_str)
    logging.info("Conectado!")
    cursor = connection.cursor()
    
    cursor.execute("SELECT * FROM itsm.chamado")
    for i in cursor.fetchall():
        logging.info(i)