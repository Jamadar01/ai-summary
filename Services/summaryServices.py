from openai import OpenAI
from dotenv import load_dotenv
import os
import json
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

    def extract(story):
        response = client.responses.create(
            model="gpt-4o-mini",
            instructions = """
            You are a story data extraction assistant.

            Analyze the uploaded story and extract ONLY information explicitly present in the story.

            Rules:
            1. Do not hallucinate or infer unsupported details.
            2. If information is not available, return null.
            3. Return valid JSON only.
            4. Do not include explanations, markdown, or extra text.
            5. Character names must be unique.
            6. Keep summaries concise (max 100 words).

            Output Schema:
            {
                "title": "",
                "characters": [],
                "protagonist": "",
                "antagonist": "",
                "setting": {
                    "location": "",
                    "time_period": ""
                },
                "theme": [],
                "tone": [],
                "genre": [],
                "conflict": "",
                "plot_summary": "",
                "keywords": []
            }

            Example 1

            Story:
            "A detective investigates a series of mysterious disappearances in a small coastal town."

            Output:
            {
                "title": null,
                "characters": ["detective"],
                "protagonist": "detective",
                "antagonist": null,
                "setting": {
                    "location": "small coastal town",
                    "time_period": null
                },
                "theme": ["mystery"],
                "tone": ["suspenseful"],
                "genre": ["mystery"],
                "conflict": "Detective investigates disappearances.",
                "plot_summary": "A detective investigates mysterious disappearances in a coastal town.",
                "keywords": ["detective", "disappearances", "town"]
            }

            Example 2

            Story:
            "Sarah finds a magical key that opens doors to different worlds."

            Output:
            {
                "title": null,
                "characters": ["Sarah"],
                "protagonist": "Sarah",
                "antagonist": null,
                "setting": {
                    "location": null,
                    "time_period": null
                },
                "theme": ["adventure", "discovery"],
                "tone": ["wonderful"],
                "genre": ["fantasy"],
                "conflict": "Sarah explores worlds using a magical key.",
                "plot_summary": "Sarah discovers a magical key that opens portals to different worlds.",
                "keywords": ["Sarah", "key", "magic", "worlds"]
            }

            Now analyze the uploaded story and return only the JSON object.
            """,
            max_output_tokens=1000,
            temperature=0.3,
            input=story
        )
        result=json.loads(response.output[0].content[0].text)
        print("response.output[0].content[0].text",result,type(result))
        return result

    def ask(question):
        with open("suspense.txt", "r", encoding="utf-8") as f:
            story=f.read()
            response = client.responses.create(
                model="gpt-4o-mini",
                instructions = f"""
                    You are a Story Question Answering Assistant.

                    Story:
                    {story}

                    Rules:
                    1. Answer questions using ONLY the story above.
                    2. Do not use external knowledge.
                    3. Do not invent facts.
                    4. If the answer is not found in the story, respond:
                    "The story does not provide enough information to answer this question."
                    5. Return valid JSON only.

                    Output Schema:
                    {{
                        "question": "",
                        "answer": "",
                        "reasoning_summary": "",
                        "evidence": [],
                        "confidence": "high|medium|low"
                    }}
                    """,
                max_output_tokens=1000,
                temperature=0.3,
                input=question
            )
        result=json.loads(response.output[0].content[0].text)
        print("response.output[0].content[0].text",result,type(result))
        return result