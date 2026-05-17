# 🔑 AWS Account Setup

> **Time needed**: 15-20 minutes (longer if AWS verification takes time)
> **Cost**: $0 — free tier covers everything in this bootcamp

This is the most important setup step. **Do not skip it.** AWS account verification sometimes takes hours, so start this NOW (not the night before Week 1).

---

## 📋 What you'll need

- A working email address (use your real one — AWS sends verification)
- A phone number that can receive SMS or voice calls
- **A credit or debit card** (Mastercard, Visa, or Verve — all work in West Africa)
- About 20 minutes of patience

> 💳 **About the card**: AWS will charge **$1.00** then refund it immediately as a verification check. You will NOT be billed during this bootcamp as long as you stay within the free tier. We'll teach you how.

---

## 🚀 Step-by-step

### 1. Go to aws.amazon.com

Click **"Create an AWS Account"** in the top right.

### 2. Account info

- **Root user email**: use your real email
- **AWS account name**: anything you want (e.g., `shadrack-bootcamp`)
- Click **Verify email address**, check your inbox for the 6-digit code, enter it

### 3. Set the root password

Pick a STRONG password. Save it in a password manager. **You'll rarely use this account again** — we'll create an IAM user for daily work.

### 4. Contact information

- Choose **Personal** (not Business)
- Fill in your real name, phone, address
- Tick the agreement box

### 5. Billing information

- Add your credit/debit card
- AWS will charge $1.00 as verification, then refund it

### 6. Identity verification

- **Pick SMS** (faster than voice for West Africa)
- Enter your phone number with country code (e.g., `+233 24 XXX XXXX` for Ghana)
- Wait for the SMS code

### 7. Support plan

- **PICK FREE / BASIC SUPPORT** ⚠️
- Don't accidentally tick "Developer" or "Business" — they cost $29/month+

### 8. Sign in

You're done! Sign in to the [AWS Console](https://console.aws.amazon.com/).

---

## 🚨 When verification gets stuck

This happens to about 30% of West African students. If your account is "pending verification" for more than 30 minutes, try these in order:

### Fix #1: Use Telecel (if you tried MTN, and vice versa)

AWS's SMS verification works better with Telecel in Ghana than MTN. If MTN didn't deliver the code after 5 minutes, switch to a different network's number.

### Fix #2: Try voice call instead of SMS

On the verification screen, pick "Call me with a code" instead of SMS. AWS will dial your number and a robot voice reads out the digits.

### Fix #3: Wait 6-12 hours

If neither network works, just wait. AWS sometimes batches verifications for new regions. Most accounts unlock within 12 hours automatically.

### Fix #4: Contact AWS Support

- Go to [Support Center](https://console.aws.amazon.com/support/home)
- Open a **case** → **Account and billing** → **Account verification issue**
- **Choose "Web (chat)"** — this is the fastest channel
- Note: the first reply is from an AI. Just reply asking for a human and they'll route you.

---

## ⚠️ Security must-dos (before you do ANYTHING else)

The root account has full power over everything in your AWS account. Protect it like your bank login.

### 1. Enable MFA (Multi-Factor Authentication)

- Sign in to the [AWS Console](https://console.aws.amazon.com)
- Top right: click your username → **Security credentials**
- Scroll to **Multi-factor authentication (MFA)** → **Assign MFA device**
- Pick **Authenticator app** (Google Authenticator, Authy, or 1Password)
- Scan the QR code, enter two consecutive codes
- ✅ Done

### 2. Set up a billing alarm

- Search **CloudWatch** in the top bar → open it
- Left sidebar → **Alarms** → **Billing**
- Create alarm at **$5 USD threshold**
- Have it email you if your bill ever crosses $5
- This is your safety net for the whole bootcamp

### 3. Pick a region — and stick to it

- Top right of the AWS Console, you'll see a dropdown (e.g., "N. Virginia")
- Pick **one** region for the bootcamp and use it for everything
- Good options for West Africa: **`eu-west-1`** (Ireland — lowest latency from Ghana)
- Or **`af-south-1`** (Cape Town — closest physically, but a few services aren't yet supported there)
- ⚠️ Most beginners' costs come from forgetting which region they created things in. **Pick one. Stick to it.**

---

## 🆓 What's in the free tier

The free tier covers everything you need for this bootcamp:

| Service | Free amount |
|---------|-------------|
| **EC2** | 750 hours/month of t2.micro / t3.micro (12 months) |
| **S3** | 5 GB storage + 20K GET requests + 2K PUT (12 months) |
| **RDS** | 750 hours/month db.t3.micro + 20 GB storage (12 months) |
| **Lambda** | 1M requests + 400K GB-seconds/month (forever) |
| **DynamoDB** | 25 GB storage + 25 read/write capacity units (forever) |
| **CloudFront** | 1 TB data transfer/month (12 months) |
| **Textract** | 1,000 pages/month (3 months only) |
| **Comprehend** | 50K text units/month (12 months) |
| **Rekognition** | 5,000 image API calls/month (12 months) |

You won't get close to these limits unless you forget to stop instances or delete RDS databases. **Always clean up after each lab!**

---

## 💰 What costs money (avoid these!)

| Service | Cost if you forget |
|---------|--------------------|
| **NAT Gateway** | ~$32/month |
| **Application Load Balancer** | ~$16/month |
| **RDS (after free tier)** | ~$15/month for db.t3.micro |
| **Elastic IP (unattached)** | $3.60/month |

**Rule of thumb**: at the end of every lab, delete the resources you created. If you're unsure whether something costs money — look it up before walking away.

---

## ✅ You're done when...

- [ ] You can sign in to the AWS Console
- [ ] MFA is enabled on your root account
- [ ] A $5 billing alarm is set up
- [ ] You've picked your region (e.g., `eu-west-1`) and noted it down somewhere

Welcome to AWS. The cloud is now yours. ☁️

---

⬅️ [Back to Start Here](./README.md)
