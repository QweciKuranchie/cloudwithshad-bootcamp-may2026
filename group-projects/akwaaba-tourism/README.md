# 🌍 Akwaaba — AI Tourism Guide for Ghana

> **A web app that identifies Ghanaian landmarks, food, and signs — and narrates them in the tourist's own language.**
>
> Group size: 3-4 · Duration: 1 week · Awards: 5 categories

---

## 🎯 What you're building

Tourists in Accra (or anywhere in Ghana) upload a photo of any landmark, dish, or sign. Within 10 seconds:
- **Rekognition** identifies what's in the photo
- Your curated `facts.csv` provides cultural context
- **Translate** converts the context to the tourist's language (French, Spanish, Twi, Mandarin)
- **Polly** narrates it aloud in a natural voice

## 🛠️ AWS services

- **EC2** — Streamlit web app
- **Rekognition** — image labeling
- **Polly** — text-to-speech (multi-language voices)
- **Translate** — text translation
- **S3** — photo uploads

## 👥 Team roles

1. **UI Lead** — the Streamlit app interface
2. **AWS Engineer** — EC2, IAM, security groups, deployment
3. **AI Engineer** — Rekognition + Polly + Translate boto3 calls
4. **Data & Story Lead** — curate landmarks/dishes content + demo script

---

## 📖 The full walkthrough

Open **[`GroupProject1_Akwaaba_Tourism_Guide.html`](./GroupProject1_Akwaaba_Tourism_Guide.html)** in your browser. It's an 8-phase guided build with code, AWS setup, EC2 deployment, polish checklist, demo prep, and award criteria.

The walkthrough is self-contained — no internet needed once you have the file.

---

## 💡 Strategic tip for this project

**Curate aggressively.** A working app with only 5 landmarks looks like a school project. The same app with 30 landmarks (with depth: history, year, cultural significance) looks like a real product. **The Data Lead's work matters more than the code.**

---

## 🏅 Awards (5 categories)

| 🎨 Most Polished | 💡 Most Innovative | 🎤 Best Demo | 📚 Best Documentation | ❤️ People's Choice |
|---|---|---|---|---|

Read the **🏆 Awards** section of the walkthrough for what specifically wins each one for THIS project.

---

⬅️ [Back to Group Projects](../README.md)
