import google.generativeai as genai

def generate_quiz(topic):
    model = genai.GenerativeModel("gemini-1.5-flash")
    prompt = f"Create 3 MCQ quiz questions on {topic} with 4 options and correct answer"
    return model.generate_content(prompt).text
