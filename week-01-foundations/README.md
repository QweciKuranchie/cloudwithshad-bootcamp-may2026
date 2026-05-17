# 1️⃣ Week 1 — Cloud Foundations

> **Theme**: Get hands-on with the AWS basics. Build a portfolio site on S3, deploy your first web server on EC2.
> **Live session**: Sat 23 May 2026 · 3 PM GMT
> **Time commitment**: 2 hr live + 4-6 hr labs

---

## 🎯 By the end of this week, you'll have

- ✅ A portfolio website live on the internet (hosted on S3 + CloudFront)
- ✅ A web server running on EC2 with Nginx
- ✅ A solid grasp of cloud fundamentals (regions, AZs, IAM, billing)
- ✅ Hands-on experience with the AWS Console

---

## 📚 This week's content

| Item | Type | Time | Link |
|------|------|------|------|
| 🎬 Week 1 Slides | Live session | 2 hr | [`slides/`](./slides/) |
| 🛠️ Lab 1 — S3 Portfolio | Guided lab | 60 min | [`lab-1-s3-portfolio/`](./lab-1-s3-portfolio/) |
| 🛠️ Lab 2 — EC2 Web App | Build-on-your-own | 75 min | [`lab-2-ec2-webapp/`](./lab-2-ec2-webapp/) |
| 🎯 Week 1 Quiz | Interactive | 15 min | [`quiz/`](./quiz/) |

---

## 📅 Suggested schedule

| Day | What to do |
|-----|------------|
| **Sat 23 May** | Attend the live session (3 PM GMT). Open `slides/` while watching. |
| **Sun 24 May** | Work through Lab 1 (S3 Portfolio). Should take ~60 minutes. |
| **Mon-Wed** | Work through Lab 2 (EC2 Web App). This one needs more thinking. |
| **Thu 28 May** | Take the Week 1 Quiz. Push your solutions to your fork. |
| **Fri 29 May** | Week 2 content drops — sync your fork: `git fetch upstream && git merge upstream/main` |

---

## 🧠 Concepts we'll cover

- **Cloud basics**: What is cloud computing? Why AWS? Regions vs Availability Zones
- **The AWS Console**: how to navigate, where the important menus live
- **S3**: Object storage explained. Buckets, objects, public access, static hosting
- **CloudFront**: CDN basics. Why your site loads fast in West Africa
- **EC2**: Virtual machines in the cloud. AMIs, instance types, key pairs, security groups
- **IAM basics**: Users, roles, policies. The principle of least privilege
- **Pricing & free tier**: How not to get billed accidentally

---

## 💡 Tips for this week

- **Take screenshots** of every step in the labs — they make the best blog posts later
- **Don't skip the cleanup step** at the end of each lab. EC2 left running = budget killer
- **The quiz is short but tricky** — it's designed to make you think, not memorize
- **Get unstuck quickly**: WhatsApp the group with a screenshot before you've spent 30 minutes stuck

---

## 🆘 Common Week 1 issues

| Problem | Fix |
|---------|-----|
| "Access Denied" when uploading to S3 | Bucket has Public Access blocked — see Lab 1 step 4 |
| EC2 site won't load | Security group missing port 80 — see Lab 2 step 5 |
| SSH key permission error | `chmod 400 your-key.pem` on Mac/Linux |
| Region confusion | Stick to ONE region — `eu-west-1` is recommended |

---

## 📦 What's in `slides/`

- `Week1_CloudWithShad.pptx` — the 11-slide deck used in the live session
- Slides include speaker notes if you want to review what was said

## 📦 What's in each lab folder

Each lab folder contains:
- `README.md` — overview, requirements, success criteria
- An HTML walkthrough (open it in your browser for the full step-by-step)
- Any starter code or assets you'll need

## 📦 What's in `quiz/`

- An interactive single-file HTML quiz — open in browser, no install needed
- Tracks your score + streaks as you go

---

## 🎓 Submission

After finishing Lab 1 + Lab 2:

1. Push to YOUR fork (not the original repo)
2. Drop a screenshot of your live S3 site + EC2 site in the WhatsApp group
3. Tag your post with `#week1done`
4. Take the quiz — your score is just for you, no need to share

---

➡️ [Next: Week 2 — Networking, Storage & Real Architectures](../week-02-networking/)
⬅️ [Back to repo](../README.md)
