import streamlit as st

from utils.extract_text import extract_text
from utils.preprocess import preprocess
from utils.skill_extractor import (
    load_skills,
    extract_skills
)
from utils.similarity import (
    calculate_similarity
)
from utils.resume_summary import (
    generate_summary
)

st.set_page_config(
    page_title="AI Resume Screening System",
    layout="wide"
)

st.title("📄 AI Resume Screening System")

st.write(
    "Upload a resume and compare it with a Job Description."
)

resume_file = st.file_uploader(
    "Upload Resume PDF",
    type=["pdf"]
)

job_description = st.text_area(
    "Paste Job Description",
    height=250
)

if st.button("Analyze Resume"):

    if resume_file and job_description:

        with st.spinner("Extracting Resume..."):

            resume_text = extract_text(
                resume_file
            )

            resume_clean = preprocess(
                resume_text
            )

            jd_clean = preprocess(
                job_description
            )

        with st.spinner("Calculating Match Score..."):

            score = calculate_similarity(
                resume_clean,
                jd_clean
            )

        skills = load_skills(
            "data/skills.txt"
        )

        resume_skills = extract_skills(
            resume_clean,
            skills
        )

        jd_skills = extract_skills(
            jd_clean,
            skills
        )

        missing_skills = sorted(
            list(
                set(jd_skills)
                - set(resume_skills)
            )
        )

        st.success(
            "Analysis Complete"
        )

        st.metric(
            "Match Score",
            f"{score}%"
        )

        col1, col2 = st.columns(2)

        with col1:

            st.subheader(
                "✅ Resume Skills"
            )

            if resume_skills:

                for skill in resume_skills:
                    st.write(
                        f"• {skill}"
                    )

            else:

                st.write(
                    "No skills found"
                )

        with col2:

            st.subheader(
                "❌ Missing Skills"
            )

            if missing_skills:

                for skill in missing_skills:
                    st.write(
                        f"• {skill}"
                    )

            else:

                st.write(
                    "No missing skills"
                )

        st.divider()

        with st.spinner(
            "Generating AI Candidate Assessment..."
        ):

            ai_analysis = generate_summary(
                resume_text,
                job_description,
                score,
                resume_skills,
                missing_skills
            )

        st.subheader(
            "🤖 AI Candidate Assessment"
        )

        st.markdown(
            ai_analysis
        )

        st.divider()

        st.subheader(
            "📋 Resume Preview"
        )

        with st.expander(
            "View Extracted Resume Text"
        ):

            st.text_area(
                "",
                value=resume_text,
                height=300
            )

    else:

        st.warning(
            "Please upload a resume and enter a job description."
        )