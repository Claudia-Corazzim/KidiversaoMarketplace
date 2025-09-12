from app import create_app, db
from app.models import CartItem

app = create_app()

with app.app_context():
    db.create_all()
    print("Todas as tabelas foram criadas com sucesso!")
