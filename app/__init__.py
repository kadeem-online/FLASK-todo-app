from flask import Flask

def create_app():
  # create flask app instance
  app = Flask("Todo App", instance_relative_config=None)
  
  @app.route("/")
  def index():
    return f"<h1>Todo App</h1>"
  
  # return flask app instance
  return app
  
if __name__ == "__main__":
  app = create_app()
  app.run()