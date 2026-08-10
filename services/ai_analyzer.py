import json

from google import genai

from config import Config


client = genai.Client(
    api_key=Config.GEMINI_API_KEY
)


def analyze_resume(resume_text, career_goal):

    prompt = f"""
You are an expert AI career and resume coach.

Analyze the user's resume according to their specific career goal.

CAREER GOAL:
{career_goal}

RESUME:
{resume_text}

Return ONLY valid JSON.

Do not use markdown.
Do not use ```json.
Do not add explanations outside JSON.

Use exactly this structure:

{{
    "career_goal": "",
    "resume_score": 0,
    "career_readiness": 0,

    "summary": "",

    "strong_skills": [],

    "missing_skills": [],

    "strengths": [],

    "weaknesses": [],

    "recommendations": [],

    "roadmap": [
        {{
            "step": 1,
            "title": "",
            "description": ""
        }}
    ],

    "project_suggestions": [],

    "resume_improvements": []
}}

Rules:

1. resume_score must be between 0 and 100.
2. career_readiness must be between 0 and 100.
3. Only identify skills that are relevant to the career goal.
4. Do not invent experience that is not present in the resume.
5. Give practical recommendations.
6. Roadmap should contain 4 to 6 steps.
7. Project suggestions should match the career goal.
8. Resume improvements should be specific.
"""

    response = client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents=prompt
)

    text = response.text.strip()

    # Remove accidental markdown fences
    if text.startswith("```json"):

        text = text[7:]

    if text.startswith("```"):

        text = text[3:]

    if text.endswith("```"):

        text = text[:-3]

    text = text.strip()

    result = json.loads(text)

    return result