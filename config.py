import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')
    
    # Configuração do banco de dados
    # Use SQLite para desenvolvimento local e PostgreSQL para produção
    DATABASE_URL = os.environ.get('DATABASE_URL')
    
    # Se não houver DATABASE_URL definido, use SQLite para desenvolvimento local
    if not DATABASE_URL:
        # Caminho para o banco de dados SQLite
        db_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'app.db')
        SQLALCHEMY_DATABASE_URI = f"sqlite:///{db_path}"
    else:
        # Corrigir URL PostgreSQL se necessário
        if DATABASE_URL.startswith("postgres://"):
            DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)
        SQLALCHEMY_DATABASE_URI = DATABASE_URL
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Configurações de email (para produção)
    MAIL_SERVER = os.environ.get('MAIL_SERVER', 'smtp.gmail.com')
    MAIL_PORT = int(os.environ.get('MAIL_PORT', '587'))
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'true').lower() in ['true', 'on', '1']
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = os.environ.get('MAIL_DEFAULT_SENDER', 'noreply@kidiversao.com')
    
    # URL base para callbacks
    HOST_URL = os.environ.get('HOST_URL', 'http://localhost:5000')

