from flask import Flask

def create_app():
    app = Flask(__name__)

    # Register blueprints

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=5000)