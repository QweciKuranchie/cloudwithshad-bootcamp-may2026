# 📄 DocSmart — AI CV & Document Analyzer

> **Upload a CV. Paste a job description. Get a match score, missing skills, and improvement suggestions. The project everyone in the cohort will actually use.**
>
> Group size: 3-4 · Duration: 1 week · Awards: 5 categories

---

## 🎯 What you're building

A Streamlit app where users:
- Upload their CV (PDF or image) → **Textract** extracts the text
- Paste a job description
- **Comprehend** extracts entities + key phrases
- Your matching engine compares CV skills to job-description skills
- Returns: match score (0-100), green chips for matched skills, red chips for missing, blue for extras
- Plus 3-5 personalized improvement suggestions

## 🛠️ AWS services

- **EC2** — Streamlit app
- **Textract** — read CVs from PDFs and images
- **Comprehend** — entities + key phrases
- **S3** — temporary document storage

## 👥 Team roles

1. **UI Lead** — the upload form + score visualization + skill chips
2. **Textract Engineer** — PDF/image handling + text cleaning
3. **Matching Engineer** — the skills taxonomy + scoring algorithm + suggestions logic
4. **AWS & Polish Lead** — EC2/IAM + demo prep

---

## 📖 The full walkthrough

Open **[`GroupProject3_DocSmart_CV_Analyzer.html`](./GroupProject3_DocSmart_CV_Analyzer.html)** in your browser. It's an 8-phase guided build with code, AWS setup, EC2 deployment, polish checklist, demo prep, and award criteria.

The walkthrough is self-contained — no internet needed once you have the file.

---

## 💡 Strategic tip for this project

**Use your own team's CVs as test data.** Four CVs in hand on day 1, more than any other team. Anonymize them, run them through your own app — your suggestions will be smarter than teams using public sample CVs.

---

## 🏅 Awards (5 categories)

| 🎨 Most Polished | 💡 Most Innovative | 🎤 Best Demo | 📚 Best Documentation | ❤️ People's Choice |
|---|---|---|---|---|

Read the **🏆 Awards** section of the walkthrough for what specifically wins each one for THIS project.

---

⬅️ [Back to Group Projects](../README.md)
