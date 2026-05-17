# 🏆 Group Projects + Demo Day

> **Form teams of 3-4. Build a Streamlit app. Deploy it on EC2. Demo it live. Win mini-awards.**
>
> **Demo day**: Sat 20 Jun 2026 · 3 PM GMT

This is the cohort's final week. Forget homework — you're now shipping something polished enough to put on your portfolio, defend in a demo, and (potentially) sell to real customers.

---

## 📅 Timeline

| Date | What happens |
|------|--------------|
| **Sat 13 Jun** | Last Week 4 session — project options revealed |
| **Sun 14 Jun** | Team formation (use the WhatsApp group) |
| **Mon 15 Jun** | Teams declare their project + start building |
| **Tue-Fri** | Build, ship, polish |
| **Sat 20 Jun 3 PM GMT** | **Demo day** — 5 min pitch + 3 min Q&A per team |
| **Sat 20 Jun (after)** | Awards announced + LinkedIn shout-outs |

---

## 🎯 Pick a project

Each team picks ONE of these three. Read all three first — they're different beasts.

| Project | Best for teams who… | Services |
|---------|----------------------|----------|
| 🌍 [**Akwaaba**](./akwaaba-tourism/) — AI Tourism Guide | …love design, want to learn computer vision, care about cultural impact | EC2 · Rekognition · Polly · Translate · S3 |
| 📊 [**MarketPulse**](./marketpulse-feedback/) — SME Feedback Dashboard | …want to build something they could sell, love data + dashboards | EC2 · Comprehend · DynamoDB · SNS · CloudWatch |
| 📄 [**DocSmart**](./docsmart-cv/) — AI CV Analyzer | …are job-hunting, want to dogfood your own product | EC2 · Textract · Comprehend · S3 |

---

## 👥 How to form teams

In the WhatsApp group on **Sunday 14 Jun**:

1. Anyone can post: *"Looking for a team — I'm strong in [skill]"*
2. People reply, teams self-organize
3. **By Mon 15 Jun, every team must declare**: team name, members, which project, who plays which role
4. If you don't have a team by Mon evening, message Shadrack and he'll match you

> 💡 **Team size**: 3-4 students. Smaller = more work each. Larger = communication overhead. Three is the sweet spot.

---

## 🎭 Roles within a team

Each project has 4 distinct roles defined in its guide. The pattern is similar across all three:

| Role | What they do |
|------|--------------|
| **UI Lead** | Owns the Streamlit interface, picks design, handles polish |
| **AWS Engineer** | Provisions EC2/S3/IAM, owns deployment + uptime |
| **AI/Backend Engineer** | Wires the boto3 calls to AWS AI services |
| **Data/Product Lead** | Curates content, owns the demo script + presentation |

Roles are assigned **on day 1**. Stick to them.

---

## 🏅 The 5 mini-awards

Every team has a real shot at one of these:

| Award | What wins it |
|-------|--------------|
| 🎨 **Most Polished** | Looks and feels like a real product. Beautiful UI, mobile-ready, attention to detail. |
| 💡 **Most Innovative** | Took the brief and added something unexpected — a feature nobody else thought of. |
| 🎤 **Best Demo** | Most compelling 5-minute pitch. Clear story, smooth live demo, confident speakers. |
| 📚 **Best Documentation** | A README a hiring manager would clone and run. Architecture diagram, setup steps, the works. |
| ❤️ **People's Choice** | Voted by the cohort. The team everyone wishes they were on. |

**You can win more than one.** Aim for the award that fits your team's strengths.

### 🎁 What you get

- 🏆 cloudwithshad swag (Shadrack-signed digital certificate + a physical sticker if you're in Accra)
- 📣 LinkedIn shout-out from Shadrack
- 🌍 Featured spot in the next cohort's promotional material
- 💼 Most importantly: a finished project for your CV

---

## 📐 Submission requirements

By **Friday 19 Jun 6 PM GMT** (before demo day), each team must submit in the WhatsApp group:

1. ✅ **Team name** + names of all members + LinkedIn URLs
2. ✅ **Live URL** of your deployed app (EC2 public IP works fine)
3. ✅ **GitHub repo URL** — must contain code + a proper README
4. ✅ **Backup demo video** — 60-90 seconds, screen recording of your app working (in case EC2 hiccups on demo day)
5. ✅ Which **single award** your team is gunning for (or "any")

---

## 🎬 The 5-minute demo structure

On demo day, you get 5 minutes to present + 3 minutes for Q&A. The winning structure (works for all 3 projects):

| Time | What |
|------|------|
| **0:00 — 0:30** | The problem you're solving. One clear sentence. |
| **0:30 — 1:00** | Team introduction + roles. Quick. |
| **1:00 — 2:30** | **THE LIVE DEMO.** Practice this 10 times beforehand. |
| **2:30 — 3:30** | Architecture + the hard parts you solved |
| **3:30 — 4:30** | Lessons learned + what's next |
| **4:30 — 5:00** | Strong closing — why your project matters |

> ⚠️ **Always have a backup demo video.** If the live demo breaks, you smile, say "here's a recording from earlier", play the video, and keep going.

---

## 🚨 Common pitfalls

| Pitfall | Fix |
|---------|-----|
| Team picks roles but ignores them | Daily 10-min standup. Each person reports what they did + what's blocking them. |
| App breaks on demo day | Test the EC2 URL from a phone (different network) the night before. Have a backup video. |
| Bad pitch | Rehearse with a timer. Five minutes goes FAST. |
| Last-minute scramble | Lock features by Wednesday. Spend Thursday + Friday on polish, not new features. |

---

## 📦 What's in each project folder

```
group-projects/
├── README.md                            ← you are here
├── akwaaba-tourism/
│   ├── README.md                        ← project-specific overview
│   ├── GroupProject1_Akwaaba...html     ← the full guided walkthrough
│   └── starter-code/                    ← example app.py + facts.csv
├── marketpulse-feedback/
│   ├── README.md
│   ├── GroupProject2_MarketPulse...html
│   └── starter-code/
└── docsmart-cv/
    ├── README.md
    ├── GroupProject3_DocSmart...html
    └── starter-code/
```

Open the HTML walkthrough in each folder for the **complete 8-phase guide** with code, AWS configuration, deployment steps, polish checklists, and demo rehearsal scripts.

---

## 🙌 A note about competition

This week is competitive — but **not against each other**. You're competing against your own previous best.

The team that wins Most Polished doesn't "beat" the team that wins Most Innovative. Five teams, five awards, all winners.

The real prize: **a project on your CV that helped you land a cloud role**.

---

⬅️ [Back to repo](../README.md)
