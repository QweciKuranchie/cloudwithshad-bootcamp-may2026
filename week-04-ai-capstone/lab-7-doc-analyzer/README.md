# 🛠️ Lab 7 — Smart Document Analyzer

> **Type**: Guided lab
> **Time**: ~90 minutes
> **Difficulty**: Intermediate
> **Cost**: Free (Textract: 1000 free pages/month for 3 months)

---

## 🎯 What you'll build

Upload any PDF or document image to S3 and watch AWS automatically extract the text (Textract), analyze the sentiment + entities (Comprehend), and save the results to DynamoDB. Real production AI in 90 minutes.

## 📋 Prerequisites

- [ ] Comfortable creating Lambda functions
- [ ] Basic Python (provided starter handles 90% of it)
- [ ] An understanding of IAM roles for Lambda

## 🛠️ AWS Services used

- **S3** — document uploads
- **Lambda** — orchestrator that chains the AI calls
- **Textract** — pulls text from PDFs and images
- **Comprehend** — sentiment + entity extraction
- **DynamoDB** — stores analysis results

---

## 📖 The full walkthrough

Open **[`Week4_Lab7_Smart_Doc_Analyzer.html`](./Week4_Lab7_Smart_Doc_Analyzer.html)** in your browser. It's a complete step-by-step guide with screenshots, code snippets, and inline hints.

> 💡 The HTML file is self-contained — no install, no internet needed once you've cloned the repo. Just double-click to open in your browser.

---

## 🆘 If you get stuck

1. Re-read the relevant step in the HTML walkthrough
2. Check the **Common Mistakes** callouts (red boxes in the walkthrough)
3. Expand the **💡 Hint** sections for guidance
4. WhatsApp the group with a screenshot of the error
5. Tag your post with `#week4done`

---

## 🎓 Submission

1. Screenshot of a DynamoDB item showing extracted text + sentiment + entities from a real document
2. Bonus: try it with your own CV and screenshot the entities Comprehend pulled out

---

⬅️ [Back to Week 4](../README.md)
