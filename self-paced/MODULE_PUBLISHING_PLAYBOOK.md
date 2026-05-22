# 📚 Module Publishing Playbook (v2 — config.json)

> No more find-and-replace! Just edit one JSON file per module.

---

## How it works

Every module folder has the **same** `index.html` (never touch it). 
The page reads from `config.json` in the same folder to fill in all the details.

```
self-paced/
├── index.html                    ← Library hub (reads ALL config.json files)
├── module-template/index.html    ← Master copy (don't edit)
└── module-01/
    ├── index.html                ← Identical copy of template (don't edit)
    ├── config.json               ← ✏️ EDIT THIS FILE
    ├── your-notes.pdf            ← Drop PDF here
    └── audio/
        └── your-podcast.mp3      ← Drop MP3 here
```

---

## Publishing a module (5 minutes)

### Step 1: Prepare your content
- Upload video to YouTube as **Unlisted** → copy the video ID (the part after `?v=`)
- Export your PDF study notes → drop into `self-paced/module-XX/`
- Generate NotebookLM podcast → drop MP3 into `self-paced/module-XX/audio/`

### Step 2: Edit config.json

Open `self-paced/module-XX/config.json` and fill it in:

```json
{
  "number": "01",
  "title": "Introduction to Cloud Computing",
  "subtitle": "What is the cloud and why does it matter?",
  "duration": "14 min",
  "date": "2026-05-24",
  "youtube_id": "dQw4w9WgXcQ",
  "pdf_file": "week1-cloud-intro.pdf",
  "audio_file": "week1-podcast.mp3",
  "description": "Understand the fundamentals of cloud computing, service models, and deployment models.",
  "published": true
}
```

**That's it.** Change `published` to `true` and fill in the fields.

### Step 3: Push

```bash
git add .
git commit -m "Publish Module 01 — Introduction to Cloud Computing"
git push
```

Wait ~90 seconds for GitHub Pages to deploy. Done.

---

## Field reference

| Field | What it does | Example |
|---|---|---|
| `number` | Module number (2 digits) | `"01"` |
| `title` | Main heading | `"Introduction to Cloud Computing"` |
| `subtitle` | Short tagline | `"What is the cloud?"` |
| `duration` | Video/audio length | `"14 min"` |
| `date` | Publish date | `"2026-05-24"` |
| `youtube_id` | YouTube video ID only | `"dQw4w9WgXcQ"` |
| `pdf_file` | PDF filename in same folder | `"week1-notes.pdf"` |
| `audio_file` | MP3 filename in `audio/` subfolder | `"week1-podcast.mp3"` |
| `description` | Longer description shown on page | Any text |
| `published` | Controls visibility | `true` or `false` |

---

## Partial publishing

You don't need all 3 formats ready at once. Leave any field empty and the page shows "Coming soon" for that tab:

```json
{
  "youtube_id": "abc123",
  "pdf_file": "",
  "audio_file": "",
  "published": true
}
```
☝️ This publishes the module with only the video. Audio and PDF tabs show "Coming soon".

---

## Quick checklist

- [ ] Video uploaded to YouTube (Unlisted) → copy ID
- [ ] PDF dropped in `self-paced/module-XX/`
- [ ] MP3 dropped in `self-paced/module-XX/audio/`
- [ ] `config.json` updated (all fields + `"published": true`)
- [ ] `git add . && git commit -m "Publish Module XX" && git push`
- [ ] WhatsApp announcement sent

---

[Back to Instructor Notes](../instructor-notes/README.md)
