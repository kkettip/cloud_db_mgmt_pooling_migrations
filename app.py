from flask import Flask, render_template
from pandas import read_sql
import pandas as pd
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, inspect
import sqlalchemy

app = Flask(__name__)


load_dotenv()  # Load environment variables from .env file

# Database connection settings from environment variables
DB_HOST = os.getenv("DB_HOST")
DB_DATABASE = os.getenv("DB_DATABASE")
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_PORT = int(os.getenv("DB_PORT", 3306))
DB_CHARSET = os.getenv("DB_CHARSET", "utf8mb4")

DB_URL = os.getenv("DB_URL")


engine = create_engine(DB_URL)


# Connection string
conn_string = (
    f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}"
    f"?charset={DB_CHARSET}"
)

# Create a database engine
db_engine = create_engine(conn_string, echo=False)



@app.route('/')
def index():
    query_patients = "SELECT * FROM patients limit 10"
    df_patients = read_sql(query_patients, db_engine)
    patients = df_patients.to_dict(orient='records')
   


    query_medical_records = "SELECT * FROM medical_records limit 10"
    df_medical_records= read_sql(query_medical_records, db_engine)
    medical_records = df_medical_records.to_dict(orient='records')
    

    return render_template('index.html', patients=patients, medical_records=medical_records)

if __name__ == '__main__':
    app.run(
        debug=True,
        port=3306
        )