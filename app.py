from flask import Flask, render_template, request, jsonify, send_from_directory
import os
from dotenv import load_dotenv
import sqlite3
# PrometheusMetrics can be included if you want to show basic metrics setup, but requires more config
# from prometheus_flask_exporter import PrometheusMetrics

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Import the blueprint (will create ai_routes.py next)
from ai_routes import ai_routes as ai_bp

# Register blueprint
app.register_blueprint(ai_bp, url_prefix='/api')

# --- Basic Routes (demonstrating templates and static files) ---

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ai')
def ai_chat():
    return render_template('ai.html')

@app.route('/cache')
def cache_view():
    # Simplified cache view for demo - just shows the template
    return render_template('cache.html', cache_rows=[]) # Pass empty list for now

# Basic Error Handlers (for demo)
@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html', error_code=404, error_message='Page Not Found', error_description='The page you are looking for does not exist.'), 404

# --- Serve static files (handled by Flask by default in debug mode) ---

# --- Main run block ---

if __name__ == '__main__':
    app.run(debug=True) 