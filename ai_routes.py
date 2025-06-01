from flask import Blueprint, request, jsonify
import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

ai_routes = Blueprint("ai_routes", __name__)

# Configure Google API key (using a placeholder for demo)
genai.configure(api_key=os.getenv("GOOGLE_API_KEY") or "YOUR_GOOGLE_API_KEY")

@ai_routes.route("/ask", methods=["POST"])
def ask():
    # This will be the focus of the AI integration demo part
    data = request.get_json()
    prompt = data.get('prompt')

    if not prompt:
        return jsonify({'error': 'Prompt is required'}), 400

    try:
        # Basic AI call for demo purposes
        model = genai.GenerativeModel('models/gemini-1.5-pro-latest') # Or another suitable model
        response = model.generate_content(prompt)
        answer = response.text if hasattr(response, 'text') else str(response)

        # In a real demo, you'd show adding context, caching, etc. here

        return jsonify({
            'answer': answer,
            'source': 'AI Demo'
        })
    except Exception as e:
        return jsonify({'error': f'AI service error: {str(e)}'}), 500 