from flask import Flask
from db import db
from routes.clients import clients_bp
from routes.products import products_bp
from routes.orders import orders_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@db:5432/crm'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

app.register_blueprint(clients_bp)
app.register_blueprint(products_bp)
app.register_blueprint(orders_bp)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
