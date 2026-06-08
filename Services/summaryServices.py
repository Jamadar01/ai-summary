from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client=OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)


class DocServices:
    def summary(story):
        response = client.responses.create(
            model="gpt-4o-mini",
            instructions="""You are a story summarization assistant. Analyze the uploaded story and provide:
            1. Story Summary
            2. Main Characters
            3. Key Events
            4. Theme or Moral (if applicable)

            Keep the summary concise, accurate, and factual. Do not add details that are not present in the story.""",
            max_output_tokens=100,
            temperature=0.2,
            input=story
        )
        return response.output[0].content[0].text