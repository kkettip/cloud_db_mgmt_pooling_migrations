# cloud_db_mgmt_pooling_migrations



##GCP Setup and Configuration 

Log into GCP account

Select SQL

Select Create an instance

Select MySQL

Provide information for Instance

Adjust settings 

In Cloud SQL Edition Section: Select Enterprise and Select Sandbox

In Machine configuration Select Shared core

In Connections select Public IP and  add network 0.0.0.0/0

Select Create the instance



## Database schema structure
The initial tables prior to the migrations are the patients table and the medical_records table. The id of the patients table is the primary key of the patients table and the id of the medical_records table is the primary key of the medical_records table. The foreign key of the medical_records table is the patient_id. The foreign key allows the medical_records table to associate with the patients table.

The tables after the migrations include the patients table, the medical_records table and the doctors tables. The primary key of the patients table is the id, the primary key of the medical_records table is the id and the primary key of the doctors table is also the id. The foreign key of the medical_records table is the patient_id and the doctor_id. The foreign keys allow the medical_records table to associate with the patients and doctors tables.


## Challenges Encountered

Only the patients table was created when the code to create both the patients tables and medical_records tables were run. Issues creating the medical_records table were resolved by moving the Base.metadata.create_all(engine) code closer to the table codes.


Received:
OperationalError: (pymysql.err.OperationalError) (1054, "Unknown column 'cancer' in 'field list'"). This issue was resolved by adding quotes to {diagnosis} to get the string form of the various diagnoses.


OperationalError: (1054, "Unknown column 'doctor_id' in 'field list'").
This issue occurred numerous times when running populate.py. The code seems correct and the alembic log of alterations (migration.sql file) indicates that the doctor_id column was added to the medical_records table and that the doctors table was created. However, when selecting for all columns of the medical_records table the doctor_id column was not added. This issue was resolved by rerunning the alembic migration code. But, the doctors table did not connect with the medical_records table as shown in the ERD. The reason for this issue is unknown because the code seems correct and no error messages were provided. 




AttributeError: 'NoneType' object has no attribute '_instantiate_plugins'.
Unable to connect to database error when running app.py or populate.py.
This issue was resolved by creating an additional .env file.


To solve the issues a search on the web using the error messages were performed.
