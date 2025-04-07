# 🔍 AI-Powered Hiring Expert

> **“Better Feedback. Better Experience. Better Hiring.”**  
> Make every resume count with personalised AI-powered insights.

Welcome to the **AI Hiring Expert**, an intelligent and scalable solution that simplifies the hiring process using Generative AI. Whether you're evaluating a single resume or comparing multiple candidates for a role, this tool brings precision, consistency, and deep analysis to your recruitment pipeline.

---

## 💭 Why This Matters

Recruitment is more than just filling positions — it's a reflection of your company's **values**, **culture**, and **brand**.

> “Just like your sales cycle shapes your customer relationships, your recruitment cycle defines your employer brand.”

In today's world, most companies are inundated with job applications and often lack the bandwidth to provide personalised feedback. Candidates are left with generic responses like:

> *“We had many strong applicants, and unfortunately, you were not selected.”*

This adds no value to the candidate's journey and does not leave a lasting impression.

**Every applicant deserves meaningful feedback** — not only to help them grow, but to create a more humane, transparent, and trustworthy recruitment experience. With the power of **Generative AI**, it’s now possible to give **actionable, personalised, and constructive feedback** at scale—starting from the very first application touchpoint.

This project was born from that very thought:
> **To make hiring more empathetic, fair, and insightful—without adding more work for recruiters.**

By improving candidate experience, companies can:
- Build long-term brand equity
- Attract better talent in the future
- Leave every applicant with a positive impression, whether they’re hired or not

Let’s transform the way we recruit. One resume at a time. ✨

---

## Overview

This project provides **two powerful solutions** for hiring teams, recruiters, and talent acquisition professionals:

### ✅ 1. ATS Resume Scorer

Upload a **job description** and a **candidate’s resume**, and get a comprehensive AI-generated analysis covering:

- 🎯 **Resume-Job Match Score** (0%–100%)
- 🔍 **Section-wise Breakdown** (Experience, Skills, Education, Certifications, Soft Skills)
- 📄 **Formatting & Readability Review**
- ⚖️ **Bias & Inclusive Language Check**
- 📈 **Suggestions for Improvement**
- 🧠 **Missing Keywords**
- 💬 **Professional Feedback Summary**
- 🧪 **Questions that can be asked in interview?**
- 📧 **Personalised Email to Candidate**

> Designed for roles in **Data Science, Machine Learning, Deep Learning**, and **Generative AI**, but easily extendable to other domains.

---

### 🔄 2. Candidate Comparison Engine

Upload a **job description** and **resumes** of all candidates in the talent pool for job to get:

- 🥇 **Ranked Candidate List**
- 📊 **Evaluation Across 5 Dimensions**
  - Technical Skill Match (40%)
  - Relevant Experience (30%)
  - Keyword Match (10%)
  - Certifications & Education (10%)
  - Soft Skills (10%)
- 📋 **Structured Feedback Table**
- 🔍 **Justification for Each Ranking**
- 🌟 **Top 2-3 Recommendations**
- 📌 **Key Takeaways from the Talent Pool**

---

## 🧠 Powered By

- **LLM**: [Groq + LLaMA 3.3-70B Versatile](https://www.groq.com)
- **UI**: [Streamlit](https://streamlit.io/) (Multi-page app)
- **Tracing & Debugging**: [LangSmith](https://www.langchain.com/langsmith)
- **Resume Parsing**: PDF text extraction and processing

---

## 🖼️ How It Works

1. 📄 Upload a job description (text input).
2. 📎 Upload one or more resumes (PDFs).
3. 🧠 Our AI parses the documents and sends structured prompts to the LLM.
4. 📬 Get detailed analysis, rankings, and email-ready feedback in seconds!

---

## 🛠️ Installation

```bash
git clone https://github.com/your-username/ai-resume-scanner.git
cd ai-resume-scanner
pip install -r requirements.txt
streamlit run app.py
