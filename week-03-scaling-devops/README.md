# 3️⃣ Week 3 — Scaling, Automation & DevOps

> **Theme**: Make your apps survive traffic spikes and deploy themselves.
> **Live session**: Sat 6 Jun 2026 · 3 PM GMT
> **Time commitment**: 2 hr live + 5-7 hr labs

---

## 🎯 By the end of this week, you'll have

- ✅ An auto-scaling application that adds servers automatically when traffic spikes
- ✅ A working Application Load Balancer distributing traffic across servers
- ✅ A CI/CD pipeline that auto-deploys every `git push` to AWS
- ✅ A clear understanding of DevOps fundamentals

---

## 📚 This week's content

| Item | Type | Time | Link |
|------|------|------|------|
| 🎬 Week 3 Slides | Live session | 2 hr | [`slides/`](./slides/) |
| 🛠️ Lab 5 — Auto-Scaling + ALB | Guided lab | 90 min | [`lab-5-autoscaling-alb/`](./lab-5-autoscaling-alb/) |
| 🛠️ Lab 6 — CI/CD Pipeline | Build-on-your-own | 75 min | [`lab-6-cicd-pipeline/`](./lab-6-cicd-pipeline/) |
| 🎯 Week 3 Quiz | Interactive | 15 min | [`quiz/`](./quiz/) |

---

## 📅 Suggested schedule

| Day | What to do |
|-----|------------|
| **Sat 6 Jun** | Live session 3 PM GMT |
| **Sun 7 Jun** | Lab 5 (Auto-scaling + ALB) |
| **Mon-Wed** | Lab 6 (CI/CD pipeline) |
| **Thu 11 Jun** | Quiz + push |
| **Fri 12 Jun** | Week 4 (the AI capstone week!) drops |

---

## 🧠 Concepts we'll cover

- **Why one server isn't enough** — and the cost of forgetting that
- **Vertical vs horizontal scaling** — when each one wins
- **Application Load Balancer (ALB)** — how it spreads traffic and detects unhealthy servers
- **Auto Scaling Groups (ASG)** — launch templates, min/desired/max, scaling policies
- **CloudWatch** — the sensor that triggers scaling
- **CI/CD pipelines** — what CI really means, what CD really means
- **GitHub Actions** — the easiest CI/CD platform for AWS deploys

---

## 🚨 Big cost warning

**Lab 5 uses an Application Load Balancer**. ALBs cost ~$0.50/day even with zero traffic.

> **DELETE THE ALB the same day you finish Lab 5.** Don't leave it running overnight.
> 
> Cleanup order: **ASG → ALB → Target Group → Launch Template**. Get this wrong and Auto Scaling will keep trying to register new instances with a deleted ALB.

---

## 💡 Tips for this week

- **Lab 5 is the most expensive lab in the bootcamp** (~$1 total if you clean up promptly). Plan to do it in one sitting.
- **Lab 6 turns into your CI/CD demo for life** — make it look nice, the GitHub repo is your portfolio piece
- **Never commit AWS keys to git** — Lab 6 covers this, but seriously, never do it

---

## 📦 Folder contents

```
week-03-scaling-devops/
├── slides/
│   └── Week3_CloudWithShad.pptx
├── lab-5-autoscaling-alb/
│   ├── README.md
│   └── Week3_Lab5_AutoScaling_ALB.html
├── lab-6-cicd-pipeline/
│   ├── README.md
│   ├── Week3_Lab6_CICD_Pipeline.html
│   └── starter-code/
│       └── deploy.yml
└── quiz/
    └── Week3_Quiz_Pipeline.html
```

---

## 🎓 Submission

After Lab 5 + Lab 6:
1. Screenshot of your ASG Activity history showing scale-out AND scale-in events
2. Screenshot of a successful GitHub Actions workflow run + your live S3 URL
3. Push your `deploy.yml` to your fork
4. Tag posts with `#week3done`

---

➡️ [Next: Week 4 — AI Services & Capstone](../week-04-ai-capstone/)
⬅️ [Previous: Week 2 — Networking](../week-02-networking/)
⬅️ [Back to repo](../README.md)
