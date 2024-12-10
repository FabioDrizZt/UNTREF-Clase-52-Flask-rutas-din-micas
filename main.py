from app.config import create_app
from app.routes.fruta_routes import frutas_bp
app =  create_app()
app.register_blueprint(frutas_bp)
if __name__ == "__main__":
  app.run(debug=True)