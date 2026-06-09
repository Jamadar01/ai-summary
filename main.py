from fastapi import FastAPI
from Services.summaryServices import DocServices
app=FastAPI()

@app.get("/")
async def read_root():
    return "Hello World"


@app.get("/sumarize")
async def read_root():
    with open("story.txt", "r", encoding="utf-8") as f:
        story=f.read()
        summary=DocServices.summary(story)
        print("end")
    return summary

@app.get("/extract")
async def read_root():
    with open("suspense.txt", "r", encoding="utf-8") as f:
        story=f.read()
        summary=DocServices.extract(story)
        print("end")
    return summary

@app.get("/ask")
async def read_root():  
    summary=DocServices.ask("who is main character in story?")
    print("end")
    return summary
