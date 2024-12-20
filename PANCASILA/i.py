import openai
from flask import Flask, request, jsonify

# Set API key OpenAI
openai.api_key = 'YOUR_OPENAI_API_KEY'

app = Flask(__name__)

@app.route('/ask', methods=['POST'])
def ask_ai():
    user_input = request.json.get("input")
    
    if not user_input:
        return jsonify({"error": "No input provided"}), 400

    try:
        # Meminta respons dari OpenAI (GPT-4)
        response = openai.Completion.create(
            model="gpt-4",  # Atau gpt-3.5-turbo
            prompt=user_input,
            max_tokens=150
        )
        
        answer = response.choices[0].text.strip()
        return jsonify({"response": answer})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
