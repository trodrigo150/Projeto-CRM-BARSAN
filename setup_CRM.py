import mysql.connector
import os
from dotenv import load_dotenv

# Carrega as senhas do arquivo .env
load_dotenv()

#1. Conecta ao banco de dados MySQL
conexao = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database="barsan_crm"
)
cursor = conexao.cursor()

#2. O comando SQL que você estruturou para os Leads

comando_criar_tabela_leads = """
CREATE TABLE IF NOT EXISTS Leads (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    telefone VARCHAR(20),
    empresa VARCHAR(255),
    cargo VARCHAR(255),
    status VARCHAR(50) DEFAULT 'Novo',
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
"""

#3. Executa o comando SQL para criar a tabela Leads
cursor.execute(comando_criar_tabela_leads)
print("Tabela 'Leads' criada com sucesso.")

#4. Fechar a conexão para liberar a memória
cursor.close()
conexao.close()