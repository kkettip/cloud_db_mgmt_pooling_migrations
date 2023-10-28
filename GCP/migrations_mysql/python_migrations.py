"""

pip install sqlalchemy alembic mysql-connector-python pymysql

"""

## Part 1 - Define SQLAlchemy models for patients and their medical records:
### this file below could always be called db_schema.py or something similar

from sqlalchemy import create_engine, inspect, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

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

DB_URL = os.getenv("DB_URL")

# Connection string
conn_string = (
    f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}"
    f"?charset={DB_CHARSET}"
)

# Create a database engine
db_engine = create_engine(conn_string, echo=False)


engine = create_engine(DB_URL)


Base = declarative_base()

class Patient(Base):
    __tablename__ = 'patients'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    date_of_birth = Column(Date, nullable=False)
    gender = Column(String(10), nullable=False)
    contact_number = Column(String(100))
    #is_alive = column(Boolean, nullable=False)

    records = relationship('MedicalRecord', back_populates='patient')



class Doctor(Base):
    __tablename__ = 'doctors'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    contact_number = Column(String(100))

    medical_records = relationship('MedicalRecord', back_populates='doctor')



#Base = declarative_base()

class MedicalRecord(Base):
    __tablename__ = 'medical_records'

    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, ForeignKey('patients.id'), nullable=False)
    doctor_id = Column(Integer, ForeignKey('doctors.id'), nullable=False)
    diagnosis = Column(String(100), nullable=False)
    treatment = Column(String(200))
    admission_date = Column(Date, nullable=False)
    discharge_date = Column(Date, nullable=False)

    patient = relationship('Patient', back_populates='records')
    #doctor = relationship('Doctor', back_populates='records')


Base.metadata.create_all(engine)



### Part 2 - initial sqlalchemy-engine to connect to db:

#DB_URL = "mysql+mysqlconnector://username:password@host/database_name"
#engine = create_engine("mysql+mysqlconnector://username:password@host/database_name")
#engine = create_engine("mysql+mysqlconnector://username:password@host/database_name")

#engine = create_engine(DB_URL)

#engine = create_engine("mysql+pymysql://username:password@host/database_name",
                         #connect_args={'ssl': {'ssl-mode': 'preferred'}},
                         #)
#engine = create_engine(DB_URL, connect_args={'ssl': {'ssl-mode': 'preferred'}},)



## Test connection

inspector = inspect(engine)
inspector.get_table_names()

### Part 3 - create the tables using sqlalchemy models, with no raw SQL required:

Base.metadata.create_all(engine)

### Running migrations 
#""" these steps are then performed in the termainl, outside of your python code

#1. alembic init migrations
#` alembic init migrations `

#2. edit alembic.ini to point to your database
#` sqlalchemy.url = mysql+mysqlconnector://username:password@host/database_name `

#3. edit env.py to point to your models
#`from db_schema import Base`
#`target_metadata = Base.metadata `

#4. create a migration
#` alembic revision --autogenerate -m "create tables" `

#5. run the migration
#` alembic upgrade head `

#in addition, you can run ` alembic history ` to see the history of migrations
#or you can run with the --sql flag to see the raw SQL that will be executed

#so it could be like:
#` alembic upgrade head --sql `

#or if you then want to save it:
#` alembic upgrade head --sql > migration.sql `

#6. check the database

#7. roll back: To roll back a migration in Alembic, you can use the downgrade command. 
#The downgrade command allows you to revert the database schema to a previous 
#migration version. Here's how you can use it:

#`alembic downgrade <target_revision>` 

#or if you want to roll back to the previous version, you can use the -1 flag:
#`alembic downgrade -1`
 

#"""