# 📊 MarketPulse — Customer Feedback Dashboard for SMEs

> **A real-time AI feedback dashboard for Ghanaian small businesses. The project most likely to turn into a startup after the bootcamp.**
>
> Group size: 3-4 · Duration: 1 week · Awards: 5 categories

---

## 🎯 What you're building

Customers scan a QR code → submit feedback through a Streamlit form. The app:
- Runs **Comprehend** for sentiment + entities
- Stores results in **DynamoDB**
- Sends **SNS alerts** to the owner if feedback is strongly negative
- Shows the owner a beautiful dashboard with charts, top entities, and recent reviews

## 🛠️ AWS services

- **EC2** — multi-page Streamlit app (customer form + owner dashboard)
- **Comprehend** — sentiment analysis + entity extraction
- **DynamoDB** — feedback storage
- **SNS** — real-time alerts on negative feedback
- **CloudWatch** — app + service monitoring

## 👥 Team roles

1. **Frontend Lead** — the customer form + owner dashboard
2. **Backend Lead** — Comprehend wiring + DynamoDB schema + SNS triggers
3. **AWS Engineer** — EC2, IAM, security groups
4. **Product & Demo Lead** — talk to real Accra businesses + presentation

---

## 📖 The full walkthrough

Open **[`GroupProject2_MarketPulse_Feedback.html`](./GroupProject2_MarketPulse_Feedback.html)** in your browser. It's an 8-phase guided build with code, AWS setup, EC2 deployment, polish checklist, demo prep, and award criteria.

The walkthrough is self-contained — no internet needed once you have the file.

---

## 💡 Strategic tip for this project

**Get 1-2 REAL businesses to use it before demo day.** Auntie Akos, a salon, a barber, anyone. Their actual name + their actual feedback in your demo = automatic credibility. Judges remember authenticity.

---

## 🏅 Awards (5 categories)

| 🎨 Most Polished | 💡 Most Innovative | 🎤 Best Demo | 📚 Best Documentation | ❤️ People's Choice |
|---|---|---|---|---|

Read the **🏆 Awards** section of the walkthrough for what specifically wins each one for THIS project.

---

⬅️ [Back to Group Projects](../README.md)
