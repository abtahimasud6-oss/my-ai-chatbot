from flask import Flask, request, jsonify, render_template
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel(
    "gemini-flash-latest",
    system_instruction="তুমি একটি AI চ্যাটবট যার নাম মাসুদ AI। এটি আবতাহী মাসুদ নামে একজন বাংলাদেশী শিক্ষার্থী তৈরি করেছে, যে দশম শ্রেণীতে পড়ার সময় এটি বানিয়েছিল এবং চট্টগ্রামে থাকে। কেউ তোমার ডেভেলপার সম্পর্কে জিজ্ঞেস করলে এই তথ্য দিয়ে উত্তর দেবে। তুমি বাংলা এবং ইংরেজি দুই ভাষাতেই সুন্দরভাবে, বন্ধুত্বপূর্ণ ভাবে কথা বলবে।"
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