import time
import os
import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from google import genai

app = FastAPI()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY") or "YOUR_API_KEY")

MODELS = [
    "gemini-3.8-flash",
    "gemini-1.5-flash",
    "gemini-1.5-pro"
]

def ask_ai(prompt: str):
    for model_name in MODELS:
        try:
            response = client.models.generate_content(model=model_name, contents=prompt)
            return response.text
        except Exception as e:
            error_msg = str(e)
            if "503" in error_msg or "429" in error_msg or "UNAVAILABLE" in error_msg:
                time.sleep(2)
                continue
            return f"Error: {error_msg}"
    return "All models are busy. Please wait 60 seconds and try again."

HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>EduGenie - AI Learning Assistant</title>
<style>
body { background: #f1f2f6; margin:0; font-family: Arial, sans-serif; padding: 12px; }
.card { background: white; border-radius: 20px; padding: 20px; margin-bottom: 16px; box-shadow: 0 2px 10px rgba(0,0,0,0.05); }
h1 { text-align: center; font-size: 32px; font-weight: 800; margin: 10px 0; line-height: 1.2; }
.sub { text-align: center; font-size: 16px; margin-bottom: 10px; }
h3 { font-size: 20px; margin: 5px 0 15px 0; }
input, textarea { width: 95%; padding: 12px; border-radius: 12px; border: 1.5px solid #b0b0b0; font-size: 16px; outline: none; }
button { background: #2f80ed; color: white; border: none; padding: 10px 18px; border-radius: 12px; font-size: 15px; font-weight: 600; margin-top: 10px; cursor: pointer; }
.result { margin-top: 12px; background: #f8f9fa; padding: 12px; border-radius: 10px; white-space: pre-wrap; display: none; }
</style>
</head>
<body>

<div class="card">
<h1>EduGenie - AI Learning Assistant</h1>
<div class="sub">Powered by Gemini 3.8 Flash</div>
</div>

<div class="card">
<h3>a. Ask Question:</h3>
<input id="q1" placeholder="Enter your question">
<br>
<button onclick="callApi('qna','question', 'q1', 'r1')">Get Answer</button>
<div id="r1" class="result"></div>
</div>

<div class="card">
<h3>b. Explanation:</h3>
<input id="q2" placeholder="Enter topic to explain">
<br>
<button onclick="callApi('explain','topic', 'q2', 'r2')">Explain</button>
<div id="r2" class="result"></div>
</div>

<div class="card">
<h3>c. Summarising:</h3>
<textarea id="q3" rows="3" placeholder="Paste text to summarize"></textarea>
<br>
<button onclick="callApi('sum','text', 'q3', 'r3')">Summarize</button>
<div id="r3" class="result"></div>
</div>

<div class="card">
<h3>d. Quiz Generator:</h3>
<input id="q4" placeholder="Enter topic for quiz">
<br>
<button onclick="callApi('quiz','topic', 'q4', 'r4')">Generate Quiz</button>
<div id="r4" class="result"></div>
</div>

<div class="card">
<h3>e. Study Plan:</h3>
<input id="q5" placeholder="Enter your learning goal">
<br>
<button onclick="callApi('plan','goal', 'q5', 'r5')">Create Plan</button>
<div id="r5" class="result"></div>
</div>

<script>
async function callApi(endpoint, paramName, inputId, resultId){
  let val = document.getElementById(inputId).value;
  if(!val) return alert("Please enter something");
  let resDiv = document.getElementById(resultId);
  resDiv.style.display = "block";
  resDiv.innerText = "Loading... Please wait...";
  let url = `/${endpoint}?${paramName}=` + encodeURIComponent(val);
  let res = await fetch(url);
  let data = await res.json();
  resDiv.innerText = data.result || data.quiz || "No response";
}
</script>
</body>
</html>
"""

@app.get("/", response_class=HTMLResponse)
def home():
    return HTML_PAGE

@app.get("/qna")
def qna(question: str):
    return {"result": ask_ai(question)}

@app.get("/explain")
def explain(topic: str):
    return {"result": ask_ai(f"Explain {topic} in simple 5 points")}

@app.get("/sum")
def summ(text: str):
    return {"result": ask_ai(f"Summarize this text in short: {text}")}

@app.get("/quiz")
def quiz(topic: str):
    return {"result": ask_ai(f"Create 5 MCQ quiz questions for {topic} with answers")}

@app.get("/plan")
def plan(goal: str):
    return {"result": ask_ai(f"Create a 7-day learning plan for {goal}")}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
