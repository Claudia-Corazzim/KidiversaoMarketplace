from app import create_app
import os
import sys
import traceback

try:
    app = create_app()

    if __name__ == '__main__':
        port = int(os.environ.get('PORT', 5000))
        debug = os.environ.get('FLASK_ENV') != 'production'
        print(f"Iniciando aplicação na porta {port}, modo debug: {debug}, Python {sys.version}")
        app.run(host='0.0.0.0', port=port, debug=debug)
except ImportError as e:
    print(f"Erro de importação: {e}")
    print("Verifique se todas as dependências estão instaladas e se a estrutura do projeto está correta.")
    print(f"Estrutura atual: {os.listdir('.')}")
    traceback.print_exc()
except Exception as e:
    print(f"Erro ao iniciar a aplicação: {e}")
    traceback.print_exc()
