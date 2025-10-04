from app import db, create_app
from app.models import *
import os

app = create_app()

with app.app_context():
    # Remove o banco de dados existente
    try:
        os.remove('app.db')
        print("Banco de dados antigo removido.")
    except:
        pass
    
    # Cria todas as tabelas do zero
    db.create_all()
    print("Banco de dados inicializado com sucesso!")