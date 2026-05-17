# 🛠️ Lab 6 — CI/CD Pipeline (GitHub → AWS)

> **Type**: Build-on-your-own
> **Time**: ~75 minutes
> **Difficulty**: Intermediate
> **Cost**: Free (S3 + GitHub Actions free tier)

---

## 🎯 What you'll build

Wire up GitHub Actions to your AWS S3 bucket so every `git push` automatically deploys your site. Push code, wait 90 seconds, see it live. The exact workflow used by professional dev teams.

## 📋 Prerequisites

- [ ] A GitHub account
- [ ] Comfortable with `git` commands
- [ ] An understanding of IAM users + access keys

## 🛠️ AWS Services used

- **GitHub Actions** — the CI/CD runner
- **S3** — static website hosting
- **IAM User** — dedicated service account with limited permissions
- **GitHub Secrets** — secure credential storage

---

## 📖 The full walkthrough

Open **[`Week3_Lab6_CICD_Pipeline.html`](./Week3_Lab6_CICD_Pipeline.html)** in your browser. It's a complete step-by-step guide with screenshots, code snippets, and inline hints.

> 💡 The HTML file is self-contained — no install, no internet needed once you've cloned the repo. Just double-click to open in your browser.

---

## 🆘 If you get stuck

1. Re-read the relevant step in the HTML walkthrough
2. Check the **Common Mistakes** callouts (red boxes in the walkthrough)
3. Expand the **💡 Hint** sections for guidance
4. WhatsApp the group with a screenshot of the error
5. Tag your post with `#week3done`

---

## 🎓 Submission

1. Link to your GitHub repo with `.github/workflows/deploy.yml`
2. Screenshot of a green ✓ Actions run
3. Live S3 URL showing your updated content

---

⬅️ [Back to Week 3](../README.md)
