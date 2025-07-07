from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json['message'].lower()

    # Rule-based responses
    if user_input in ["hello", "hi"]:
        response = "Hello! How can I help you?"
    elif "name" in user_input:
        response = "I am a rule-based chatbot."
    elif "bye" in user_input or user_input == "exit":
        response = "Goodbye! Have a nice day!"
    else:
        response = "I'm sorry, I didn't understand that."

    return jsonify({"reply": response})

if __name__ == '__main__':
    print("Flask is about to run...")
    app.run(debug=True)