from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>DevOps Pipeline App 🚀 v2</h1><p>Auto-deployed via CI/CD! Built with Flask + Docker + Terraform + K8s + GitHub Actions</p>"


@app.route("/health")
def health():
    return {"status": "healthy"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
