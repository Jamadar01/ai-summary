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

