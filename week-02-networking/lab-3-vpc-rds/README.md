# 🛠️ Lab 3 — VPC + RDS Two-Tier App

> **Type**: Guided lab
> **Time**: ~90 minutes
> **Difficulty**: Intermediate
> **Cost**: Free (within free tier — delete RDS promptly after the lab)

---

## 🎯 What you'll build

Build the most important pattern in cloud: a two-tier application. Custom VPC with public + private subnets, EC2 web server in the public subnet, RDS MySQL database in the private subnet. The exact same architecture every fintech and SaaS app uses.

## 📋 Prerequisites

- [ ] Lab 1 + Lab 2 complete
- [ ] Comfortable with SSH and the EC2 launch wizard
- [ ] You've read the Week 2 slides on VPC + Security Groups

## 🛠️ AWS Services used

- **VPC** — custom network with subnets, route tables, IGW
- **EC2** — web tier (public subnet)
- **RDS** — MySQL database (private subnet, Multi-AZ)
- **Security Groups** — SG-to-SG references for tight security

---

## 📖 The full walkthrough

Open **[`Week2_Lab3_VPC_RDS.html`](./Week2_Lab3_VPC_RDS.html)** in your browser. It's a complete step-by-step guide with screenshots, code snippets, and inline hints.

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

1. Screenshot of your EC2 web server running
2. Screenshot of `mysql>` prompt showing you successfully connected to RDS from EC2
3. Result of a SELECT query you ran on a table you created

---

⬅️ [Back to Week 2](../README.md)
