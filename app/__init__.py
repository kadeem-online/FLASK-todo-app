import os, sys
from flask import ( Flask )
from dotenv import ( load_dotenv )

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
  app = Flask("Todo App", instance_relative_config=None)
  
  # app configurations
  app.config["SECRET_KEY"] = os.getenv("SECRET_KEY") or "projectsecretkey"
  app.config["DATABASE"] = os.getenv("DATABASE") or "sqlite://"
  
  @app.route("/")
  def index():
    return f"<h1>Todo App</h1>"
  
  # return flask app instance
  return app
  
if __name__ == "__main__":
  app = create_app()
  app.run()