#pip install faker pyodbc

#import libraries
from faker import Faker
import pyodbc
import random

# Initializing generation - fake data
faker = Faker('pt_BR')  # Brazilian location

# SQL Server Connection
conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=SEU_SERVIDOR;'
    'DATABASE=SEU_BANCO_DE_DADOS;'
    'UID=SEU_USUARIO;'
    'PWD=SUA_SENHA'
)
cursor = conn.cursor()

# Number of clients
num_clientes = 50

# Randon gender function
def gerar_genero():
    return random.choice(['M', 'F', 'O'])

# Insert data loop
for _ in range(num_clientes):
    name = faker.name()
    email = faker.email()
    birhtday = faker.date_of_birth(minimum_age=18, maximum_age=80)
    gender = gerar_genero()
    cpf = faker.cpf()
    telephone = faker.phone_number()
    HouseAddress = faker.address().replace('\n', ', ')
    city = faker.city()
    ClientState = faker.estado_sigla()
    status = random.choice(['Active', 'Inactive', 'Blocked']) #randon function

    cursor.execute("""
        INSERT INTO BB_Clientes (
            ClientName, Email, Birthday, Gender, CPF,
            Telephone, HouseAddress, City, ClientState, StatusClient
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (name, email, birhtday, gender, cpf, telephone, HouseAddress, city, ClientState, status))

# Save
conn.commit()
cursor.close()
conn.close()

print(f"{num_clientes} clientes inseridos com sucesso!")
