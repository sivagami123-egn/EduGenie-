import google.generativeai as genai

def summarize_text(text):
    model = genai.GenerativeModel("gemini-1.5-flash")
    prompt = f"Summarize in 5 bullet points: {text}"
    return model.generate_content(prompt).text
