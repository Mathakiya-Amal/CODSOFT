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
    elif "How are you" in user_input:
        response = "I'm just bot, but i am doing good. What about you?"
    elif "help" in user_input:
        response = "Sure, I am here to help you! What do you want."
    elif "What is codsoft" in user_input or user_input=="codsoft":
        response = "CodSoft are IT services and IT consultancy that" \
        " specializes in creating innovative solutions for businesses." \
        " Codsoft are passionate about technology and believe in the power " \
        "of software to transform the world."
    else:
        response = "I'm sorry, I didn't understand that."

    return jsonify({"reply": response})

if __name__ == '__main__':
    print("Flask is about to run...")
    app.run(debug=True)
