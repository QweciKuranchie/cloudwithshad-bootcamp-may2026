# 2️⃣ Week 2 — Networking, Storage & Real Architectures

> **Theme**: Build production-grade architectures. VPC, RDS, Lambda — the building blocks of every real app.
> **Live session**: Sat 30 May 2026 · 3 PM GMT
> **Time commitment**: 2 hr live + 5-7 hr labs

---

## 🎯 By the end of this week, you'll have

- ✅ A custom VPC with public and private subnets
- ✅ A two-tier app with an EC2 web server talking to an RDS database
- ✅ A serverless image resizer using S3 + Lambda
- ✅ Confidence with Security Groups, NACLs, and IAM roles

---

## 📚 This week's content

| Item | Type | Time | Link |
|------|------|------|------|
| 🎬 Week 2 Slides | Live session | 2 hr | [`slides/`](./slides/) |
| 🛠️ Lab 3 — VPC + RDS Two-Tier | Guided lab | 90 min | [`lab-3-vpc-rds/`](./lab-3-vpc-rds/) |
| 🛠️ Lab 4 — Lambda Image Resizer | Build-on-your-own | 75 min | [`lab-4-lambda-resizer/`](./lab-4-lambda-resizer/) |
| 🎯 Week 2 Quiz | Interactive | 15 min | [`quiz/`](./quiz/) |

---

## 📅 Suggested schedule

| Day | What to do |
|-----|------------|
| **Sat 30 May** | Live session 3 PM GMT |
| **Sun 31 May** | Lab 3 (VPC + RDS) — give this proper time, it's a chunky one |
| **Mon-Wed** | Lab 4 (Lambda Resizer) |
| **Thu 4 Jun** | Quiz + push to your fork |
| **Fri 5 Jun** | Week 3 drops — sync your fork |

---

## 🧠 Concepts we'll cover

- **VPC fundamentals**: CIDR blocks, subnets, public vs private
- **Routing**: route tables, Internet Gateways, NAT Gateways
- **Security**: Security Groups vs NACLs (a favourite exam topic)
- **RDS**: managed databases, Multi-AZ, automatic backups
- **Two-tier architecture**: the most important pattern in cloud
- **Lambda**: serverless functions, event triggers, free tier
- **Pillow Lambda Layer**: how to package Python dependencies

---

## 🚨 Cost warnings this week

| Resource | Cost if forgotten |
|----------|-------------------|
| **RDS db.t3.micro** | Free for 750 hrs/month (12 months). After that ~$15/month |
| **NAT Gateway** | ~$32/month — we'll avoid this in Lab 3 |
| **Lambda + S3** | Practically free at bootcamp scale |

⚠️ **Always clean up after Lab 3**: ASG → ALB → EC2 → RDS → VPC. Delete RDS first, it's the most expensive.

---

## 💡 Tips for this week

- **Read the SG vs NACL slide twice** — these come up in every cloud interview
- **Lab 3's biggest gotcha**: RDS Multi-AZ requires subnets in 2 different AZs. Plan your VPC accordingly.
- **Lab 4 uses Pillow** which isn't in Lambda by default — we'll use Klayers' public ARN

---

## 📦 Folder contents

```
week-02-networking/
├── slides/
│   └── Week2_CloudWithShad.pptx
├── lab-3-vpc-rds/
│   ├── README.md
│   └── Week2_Lab3_VPC_RDS.html
├── lab-4-lambda-resizer/
│   ├── README.md
│   ├── Week2_Lab4_Lambda_Resizer.html
│   └── starter-code/
│       └── lambda_function.py
└── quiz/
    └── Week2_Quiz_Architecture.html
```

---

## 🎓 Submission

After Lab 3 + Lab 4:
1. Screenshot of your EC2 SSHing into RDS and running a SELECT query
2. Screenshot of an image you uploaded + the resized thumbnail
3. Push your IaC/scripts to your fork
4. Tag posts with `#week2done`

---

➡️ [Next: Week 3 — Scaling, Automation & DevOps](../week-03-scaling-devops/)
⬅️ [Previous: Week 1 — Foundations](../week-01-foundations/)
⬅️ [Back to repo](../README.md)
