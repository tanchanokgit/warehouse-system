from flask import Flask
from routes.user_route import register_routes

app = Flask(__name__)
app.secret_key = "warehouse_secret_key_123"
register_routes(app)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
import pymysql
