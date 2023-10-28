import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from faker import Faker
import random

# Load environment variables
load_dotenv()

# Database connection settings from environment variables
DB_HOST = os.getenv("DB_HOST")
DB_DATABASE = os.getenv("DB_DATABASE")
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_PORT = int(os.getenv("DB_PORT", 3306))
DB_CHARSET = os.getenv("DB_CHARSET", "utf8mb4")

# Connection string
conn_string = (
    f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}"
    f"?charset={DB_CHARSET}"
)

# Create a database engine
db_engine = create_engine(conn_string, echo=False)


fake = Faker()

diagnoses = [ 'cancer', 'diabetes', 'lung_disease', 'heart_disease']

treatments = ['treatment_1', 'treatment_2', 'treatment_3', 'treatment_4']

genders = ['male', 'female']



def insert_fake_data(engine, num_patients=100, num_medical_records=70): # Noqa: E501
    # Start a connection
    with engine.connect() as connection:
        # Insert fake data into patients
        for _ in range(num_patients):
            first_name = fake.first_name()
            last_name = fake.last_name()
            date_of_birth = fake.date_of_birth(minimum_age=10, maximum_age=90)
            gender = random.choice(genders)
            contact_number = fake.phone_number()

            connection.execute(f"INSERT INTO patients (first_name, last_name, date_of_birth, gender, contact_number) VALUES ('{first_name}', '{last_name}', '{date_of_birth}', '{gender}', '{contact_number}')") # Noqa: E501

      
        # Fetch all patient IDs 
        patient_ids = [row[0] for row in connection.execute("SELECT id FROM patients").fetchall()] # Noqa: E501
      


        # Insert fake data into medical_records
        for _ in range(num_medical_records):
            patient_id = random.choice(patient_ids)
            diagnosis = random.choice(diagnoses)
            treatment = random.choice(treatments)
            admission_date = fake.date_between(start_date="-5y", end_date="today")
            discharge_date = fake.date_between(start_date="-5y", end_date="today")
            connection.execute(f"""INSERT INTO medical_records (patient_id, diagnosis, treatment, admission_date, discharge_date) VALUES ({patient_id}, '{diagnosis}', '{treatment}', '{admission_date}', '{discharge_date}')""")
            
           
if __name__ == "__main__":
    insert_fake_data(db_engine)
    print("Fake data insertion complete!")
