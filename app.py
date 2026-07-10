from flask import Flask
from database import db

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///smart_task.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

@app.route("/")
def home():
    return {
        "application": "Smart Task Manager API",
        "version": "1.0"
    }

if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)
