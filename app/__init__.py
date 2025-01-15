import os, sys
from flask import ( Flask )
from dotenv import ( load_dotenv )
from .blueprints import ( todo )

def load_environment_variables() -> None:
  # check if the .env file was loaded successfully
  if not load_dotenv(".env"):
    print("Error: .env file not found", file=sys.stderr)
    sys.exit(1)
  
  return

def create_app():
  # load env variables
  load_environment_variables()
  
  # create flask app instance
  app = Flask(__name__, instance_relative_config=None)
  
  # app configurations
  app.config["SECRET_KEY"] = os.getenv("SECRET_KEY") or "projectsecretkey"
  app.config["DATABASE"] = os.getenv("DATABASE") or os.path.join( app.instance_path, "database.sqlite" )
  
  # create the instance folder
  try:
    os.makedirs(app.instance_path)
  except OSError:
    pass
  
  # register todo blueprint
  app.register_blueprint( todo.todo_blueprint )
  
  # return flask app instance
  return app
  
if __name__ == "__main__":
  app = create_app()
  app.run()