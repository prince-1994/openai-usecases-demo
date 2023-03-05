from fastapi import FastAPI, UploadFile, Form
from transcript_summarization.usecases import summarize
app = FastAPI()


@app.post("/summarize/transcript/")
async def summarize_transcript(file: UploadFile, interviewee: str = Form()):
    contents = await file.read()
    result = summarize(text=contents.decode('ascii'), interviewee_name=interviewee)
    return {"Summary": result}