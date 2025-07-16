from fastapi import FastAPI, Request
from pydantic import BaseModel
import subprocess

app = FastAPI()

class Message(BaseModel):
    text: str

@app.post("/generate/")
async def generate_text(msg: Message):
    prompt = msg.text
    # استبدل هذا بالخطوات اللازمة لتشغيل النموذج
    result = subprocess.run(['python3', 'run_model.py', '--prompt', prompt], capture_output=True, text=True)
    output = result.stdout
    return {"response": output}

