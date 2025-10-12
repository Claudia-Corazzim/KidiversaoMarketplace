#!/usr/bin/env python3
"""
Script para testar conexão com o banco PostgreSQL
"""

import os
import sys
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

def test_connection():
    """Testa conexão com o banco de dados"""
    
    # Pegar a URL do banco de dados
    database_url = os.environ.get('DATABASE_URL')
    
    if not database_url:
        print("❌ ERRO: DATABASE_URL não encontrada nas variáveis de ambiente")
        print("Certifique-se de que o arquivo .env existe e contém a DATABASE_URL")
        return False
    
    print(f"🔗 Tentando conectar ao banco: {database_url.split('@')[-1].split('/')[0]}")
    
    try:
        # Criar engine de conexão
        engine = create_engine(database_url)
        
        # Testar conexão
        with engine.connect() as conn:
            result = conn.execute(text("SELECT version();"))
            version = result.fetchone()[0]
            print(f"✅ Conexão bem-sucedida!")
            print(f"📊 Versão do PostgreSQL: {version}")
            
            # Testar se o banco existe e está acessível
            result = conn.execute(text("SELECT current_database();"))
            current_db = result.fetchone()[0]
            print(f"💾 Banco de dados atual: {current_db}")
            
            return True
            
    except SQLAlchemyError as e:
        print(f"❌ ERRO ao conectar ao banco de dados: {e}")
        return False
    except Exception as e:
        print(f"❌ ERRO inesperado: {e}")
        return False

if __name__ == "__main__":
    # Carregar variáveis do .env
    from dotenv import load_dotenv
    load_dotenv()
    
    print("🧪 Testando conexão com PostgreSQL...")
    print("=" * 50)
    
    success = test_connection()
    
    print("=" * 50)
    if success:
        print("✅ Teste concluído com sucesso!")
        sys.exit(0)
    else:
        print("❌ Teste falhou!")
        sys.exit(1)