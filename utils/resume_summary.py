import requests


def generate_summary(
    resume_text,
    job_description,
    score,
    resume_skills,
    missing_skills
):

    prompt = f"""
You are a senior HR recruiter.

Analyze the candidate resume against the provided job description.

Job Description:
{job_description}

Resume:
{resume_text}

Match Score:
{score}%

Resume Skills:
{', '.join(resume_skills)}

Missing Skills:
{', '.join(missing_skills)}

Provide the response in EXACTLY the following format:

## Candidate Summary
A brief professional overview of the candidate.

## Match Assessment
Explain how well the candidate fits the role.

## Key Strengths
- Strength 1
- Strength 2
- Strength 3

## Skill Gaps
- Gap 1
- Gap 2

## Hiring Recommendation
One paragraph recommendation.

## Interview Questions
1. Question
2. Question
3. Question
4. Question
5. Question

Keep the response concise, professional, and recruiter-focused.
"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "qwen2.5:3b",
            "prompt": prompt,
            "stream": False,
            "options": {
                "temperature": 0.3,
                "top_p": 0.9
            }
        }
    )

    return response.json()["response"]