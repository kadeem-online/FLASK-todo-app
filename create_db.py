from app import ( create_app )
from app.db import ( initialize_database )

app = create_app()
with app.app_context():
  initialize_database()