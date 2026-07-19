import os
import json
from dotenv import load_dotenv
from google import genai


# Load environment variables from .env file
load_dotenv()


# Create Gemini client
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def analyze_resume(resume_text, user_goal):

    prompt = f"""
You are an experienced ATS Resume Reviewer.

Analyze the following resume for the role: {user_goal}

Return ONLY valid JSON in the following format:

{{
    "ats_score": 0,
    "skills": [],
    "missing_skills": [],
    "strengths": [],
    "improvements": [],
    "roadmap": [],
    "interview_questions": []
}}

Rules:

1. ats_score must be an integer between 0 and 100.
2. skills should contain technical and soft skills found in the resume.
3. missing_skills should contain important skills missing for the target role.
4. strengths should list the resume's strengths.
5. improvements should list areas that need improvement.
6. roadmap should provide 5 learning steps.
7. interview_questions should provide 5 role-specific interview questions.
8. Return ONLY valid JSON.
9. Do NOT use markdown.
10. Do NOT wrap the response inside ```json blocks.

Resume:

{resume_text}
"""


    try:

        response = client.models.generate_content(
            model="gemini-flash-latest",
            contents=prompt
        )


        text = response.text.strip()


        print("\n========== GEMINI RESPONSE ==========")
        print(text)
        print("=====================================\n")


        # Remove markdown if Gemini still adds it
        if text.startswith("```json"):
            text = text.replace("```json", "")
            text = text.replace("```", "")
            text = text.strip()


        result = json.loads(text)


        return result



    except Exception as e:


        print("\n========== GEMINI ERROR ==========")
        print(e)
        print("==================================\n")


        return {

            "ats_score": 0,

            "skills": [],

            "missing_skills": [],

            "strengths": [],

            "improvements": [],

            "roadmap": [],

            "interview_questions": [],

            "error": str(e)

        }