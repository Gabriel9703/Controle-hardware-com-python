import mysql.connector
from faker import Faker
"""
Esse script conecta com meu banco SQL, gera dados aleatórios com biblioteca Faker
e inclui todos esses dados na minha tabela, para eu fazer os tratamentos necessários
"""

#conectando com meu banco de dados
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password = '@Jesus_974426',
    database="netflix"
)
cursor = conn.cursor()

#Gerando dados aleatórios, salvando em dicionario e incluindo numa lista
fake = Faker('pt-BR')
registros = []
for _ in range(200):
    nome = fake.first_name()
    sobrenome = fake.last_name()
    email = fake.email()
    estado = fake.estado_sigla()
    pais = 'Brasil'

    registro = {
        "nome": nome,
        "sobrenome": sobrenome,
        "email": email,
        "estado": estado,
        "pais": pais
    }
    registros.append(registro)

#comando SQL para inserir, e iterar adcionando os dados na minha tabela
sql = "INSERT INTO usuario_netflix (nome, sobrenome, email, estado, pais) VALUES (%s,%s,%s,%s,%s)"   
for regist in registros:
    cursor.execute(sql, (regist['nome'], regist['sobrenome'], regist['email'], regist['estado'], regist['pais'] ))

#comando para enviar os dados
conn.commit()

#Fechando todas as conexões que abri
cursor.close()
conn.close()
