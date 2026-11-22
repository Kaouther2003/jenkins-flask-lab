
import os
from flask import Flask, jsonify

# Create the Flask application
app = Flask(__name__)

# Home page
@app.route("/")
def home():
    version = os.getenv("APP_VERSION", "local")
    return f"<h1>Jenkins CI/CD Lab</h1><p>Version: {version}</p>"

# Health check endpoint
@app.route("/health")
def health():
    return jsonify(status="ok"), 200

# Start the application
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
