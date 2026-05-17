# 🛠️ Lab 4 — Serverless Image Resizer

> **Type**: Build-on-your-own
> **Time**: ~75 minutes
> **Difficulty**: Intermediate
> **Cost**: Free (Lambda + S3 free tier)

---

## 🎯 What you'll build

Drop an image into an S3 bucket and watch a Lambda function automatically resize it into a thumbnail. No servers, no SSH, no Nginx. This is what serverless really feels like.

## 📋 Prerequisites

- [ ] Comfortable with the AWS Console
- [ ] Basic Python (you'll edit a Lambda function — provided starter code)
- [ ] An IAM user (not just root) for cleaner permission management

## 🛠️ AWS Services used

- **S3** — image storage + event trigger
- **Lambda** — Python runtime that handles the resize logic
- **CloudWatch Logs** — for debugging
- **IAM Roles** — Lambda's execution permissions
- **Pillow Lambda Layer** — Python image library, attached as a layer

---

## 📖 The full walkthrough

Open **[`Week2_Lab4_Lambda_Resizer.html`](./Week2_Lab4_Lambda_Resizer.html)** in your browser. It's a complete step-by-step guide with screenshots, code snippets, and inline hints.

> 💡 The HTML file is self-contained — no install, no internet needed once you've cloned the repo. Just double-click to open in your browser.

---

## 🆘 If you get stuck

1. Re-read the relevant step in the HTML walkthrough
2. Check the **Common Mistakes** callouts (red boxes in the walkthrough)
3. Expand the **💡 Hint** sections for guidance
4. WhatsApp the group with a screenshot of the error
5. Tag your post with `#week2done`

---

## 🎓 Submission

1. Screenshot of an original image + the resized thumbnail in S3 (side by side)
2. Screenshot of your CloudWatch Logs showing the Lambda invocation

---

⬅️ [Back to Week 2](../README.md)
