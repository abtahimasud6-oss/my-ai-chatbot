from flask import Flask, request, jsonify, render_template
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel(
    "gemini-flash-latest",
    system_instruction="তুমি একটি AI চ্যাটবট, যেটা [আবতাহী মাসুদ ইয়াফি] তৈরি করেছে। কেউ তোমার ডেভেলপার কে জিজ্ঞেস করলে বলবে তোমাকে [আবতাহী মাসুদ ইয়াফি] বানিয়েছে। তুমি বাংলা এবং ইংরেজি দুই ভাষাতেই সুন্দরভাবে কথা বলতে পারো।"
)

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    response = model.generate_content(user_message)
    return jsonify({"reply": response.text})

if __name__ == "__main__":
    app.run(debug=True)