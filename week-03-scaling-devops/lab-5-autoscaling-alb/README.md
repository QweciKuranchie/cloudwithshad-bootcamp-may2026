# 🛠️ Lab 5 — Auto-Scaling + Application Load Balancer

> **Type**: Guided lab
> **Time**: ~90 minutes
> **Difficulty**: Intermediate
> **Cost**: ~$1 if cleaned up promptly. ⚠️ ALB costs $0.50/day — DELETE IT after the lab

---

## 🎯 What you'll build

Build a load-balanced app that auto-scales from 2 → 6 EC2 servers when CPU spikes, then scales back down when traffic dies. The exact same pattern Netflix, Spotify, and your bank use.

## 📋 Prerequisites

- [ ] Comfortable launching EC2 instances
- [ ] Understanding of security groups
- [ ] **A clear schedule for cleanup** — don't start this lab if you can't clean up the same day

## 🛠️ AWS Services used

- **EC2 Launch Templates** — blueprint for new instances
- **Auto Scaling Group (ASG)** — min 2 / desired 2 / max 6
- **Target Group** — list of instances the ALB sends to
- **Application Load Balancer (ALB)** — Layer 7 traffic distribution
- **CloudWatch** — CPU metrics that trigger scaling

---

## 📖 The full walkthrough

Open **[`Week3_Lab5_AutoScaling_ALB.html`](./Week3_Lab5_AutoScaling_ALB.html)** in your browser. It's a complete step-by-step guide with screenshots, code snippets, and inline hints.

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

1. Screenshot of your ALB DNS name in the browser (refresh to see different instance IDs)
2. Screenshot of the ASG Activity history showing BOTH a scale-out AND scale-in event
3. Screenshot proving cleanup is complete (EC2 → Instances showing 0 running)

---

⬅️ [Back to Week 3](../README.md)
