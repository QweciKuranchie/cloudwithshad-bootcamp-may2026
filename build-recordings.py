#!/usr/bin/env python3
"""
═══════════════════════════════════════════════════════════════
  cloudwithshad — Recordings Builder (TWO sessions per week)
═══════════════════════════════════════════════════════════════

WHAT THIS DOES
  Reads each week's own config at videos/week-XX/config.json and
  regenerates each week's recording page (videos/week-XX/index.html)
  with TWO video embeds — Session A and Session B.

HOW TO USE
  1. Upload your two videos to YouTube for the week.
  2. Open that week's folder, e.g. videos/week-02/, and edit its
     config.json — paste each video's ID into the 'youtube' field
     for session A and B.
     (The ID is the part after watch?v= in the URL.)
  3. Run:   python3 build-recordings.py
  4. Commit + push.

  Leave a session's 'youtube' blank ('') if it's not uploaded yet —
  it shows a tasteful "coming soon" placeholder instead of an embed.

SAFE TO RE-RUN — each week's config.json is its own source of truth.
═══════════════════════════════════════════════════════════════
"""

import json
import sys
from pathlib import Path

ROOT = Path(__file__).parent
VIDEOS = ROOT / "videos"
CONFIG = VIDEOS / "recordings.json"


def esc(s):
    return (str(s if s is not None else "")
            .replace("&", "&amp;").replace("<", "&lt;")
            .replace(">", "&gt;").replace('"', "&quot;"))


def session_block(week, sess, accent_var, num):
    """Render one session: either a video embed or a coming-soon placeholder.
    `num` is the auto-assigned session number (1-based, from array order)."""
    title = esc(sess.get("title", ""))
    topics = esc(sess.get("topics", ""))
    duration = esc(sess.get("duration", ""))
    yt = sess.get("youtube", "").strip()

    dur_pill = f'<span class="sess-pill">⏱️ {duration}</span>' if duration else ""

    if yt:
        media = f'''
      <div class="video-aspect">
        <iframe
          src="https://www.youtube-nocookie.com/embed/{esc(yt)}?rel=0&modestbranding=1"
          title="Week {week} Session {num} — cloudwithshad Bootcamp"
          frameborder="0"
          allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
          referrerpolicy="strict-origin-when-cross-origin"
          allowfullscreen>
        </iframe>
      </div>
      <a href="https://www.youtube.com/watch?v={esc(yt)}" target="_blank" rel="noopener" class="sess-yt-btn">▶ Open in YouTube</a>'''
    else:
        media = '''
      <div class="video-aspect coming-soon-aspect">
        <div class="cs-inner">
          <div class="cs-icon">🎬</div>
          <div class="cs-text">This session hasn't been uploaded yet.<br>Check back after the live class.</div>
        </div>
      </div>'''

    return f'''
    <div class="session-card">
      <div class="session-head">
        <span class="session-tag" style="background: {accent_var}; ">Session {num}</span>
        <div class="session-titles">
          <h3>{title}</h3>
          <div class="session-topics">{topics}</div>
        </div>
        {dur_pill}
      </div>{media}
    </div>'''


def build_week_page(week_data):
    week = week_data["week"]
    nn = f"{week:02d}"
    folder = VIDEOS / f"week-{nn}"
    folder.mkdir(exist_ok=True)

    accent = week_data.get("accent", "cyan")
    accent_var = "var(--gold)" if accent == "gold" else "var(--cyan)"
    title = esc(week_data.get("title", f"Week {week}"))
    subtitle = esc(week_data.get("subtitle", ""))
    date_label = esc(week_data.get("dateLabel", ""))
    materials = esc(week_data.get("materialsPath", "../../"))
    sessions = week_data.get("sessions", [])

    sessions_html = "\n".join(
        session_block(week, s, accent_var, i + 1) for i, s in enumerate(sessions)
    )

    # Grid sizing: 1 video = single wide, 2 = side by side, 3+ = wrap into rows.
    count = len(sessions)
    if count <= 1:
        grid_class = "sessions sessions-1"
    elif count == 2:
        grid_class = "sessions sessions-2"
    else:
        grid_class = "sessions sessions-many"

    # Human label for the subtitle
    if count == 1:
        session_count_label = "One live session"
    elif count == 2:
        session_count_label = "Two live sessions"
    else:
        session_count_label = f"{count} live sessions"
    session_count_label_lower = session_count_label[0].lower() + session_count_label[1:]

    uploaded = sum(1 for s in sessions if s.get("youtube", "").strip())
    if uploaded:
        sess_word = "session" if count == 1 else "sessions"
        status_pill = f'<span class="pill live">🟢 {uploaded} of {count} {sess_word} up</span>'
    else:
        status_pill = '<span class="pill">🔒 Recordings coming soon</span>'

    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Week {week} — Live Recordings | cloudwithshad Bootcamp</title>
<meta name="description" content="Watch the Week {week} live sessions: {title} — {subtitle}.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Playfair+Display:wght@700;800&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>
  :root {{
    --navy:#0A1628; --navy-2:#13243A; --navy-3:#1A2F4A;
    --cyan:#00B4D8; --gold:#F4B942; --green:#2EA043;
    --white:#fff; --gray:#94A3B8; --gray-2:#64748B;
  }}
  *{{box-sizing:border-box;margin:0;padding:0}}
  html{{scroll-behavior:smooth}}
  body{{font-family:'Inter',system-ui,sans-serif;background:var(--navy);color:var(--white);line-height:1.65;overflow-x:hidden}}
  html,body{{max-width:100vw}}
  nav.topbar{{background:rgba(10,22,40,.92);backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px);position:sticky;top:0;z-index:100;border-bottom:1px solid rgba(255,255,255,.06)}}
  .nav-inner{{max-width:1100px;margin:0 auto;padding:14px 24px;display:flex;justify-content:space-between;align-items:center}}
  .brand{{font-size:17px;color:var(--white);text-decoration:none}}
  .brand span{{font-weight:800;color:var(--cyan)}}
  .nav-back{{color:var(--gray);text-decoration:none;font-size:13px}}
  .nav-back:hover{{color:var(--cyan)}}
  main{{max-width:1000px;margin:0 auto;padding:36px 24px 80px}}
  .breadcrumbs{{font-size:12px;color:var(--gray-2);margin-bottom:18px;font-family:'JetBrains Mono',monospace}}
  .breadcrumbs a{{color:var(--gray);text-decoration:none}}
  .breadcrumbs a:hover{{color:var(--cyan)}}
  .breadcrumbs .sep{{margin:0 8px;opacity:.5}}
  h1.video-title{{font-family:'Playfair Display',serif;font-size:clamp(28px,5vw,44px);font-weight:800;margin-bottom:8px;line-height:1.1}}
  .video-subtitle{{font-size:16px;color:var(--gray);margin-bottom:16px}}
  .video-pills{{display:flex;gap:8px;flex-wrap:wrap;margin-bottom:34px}}
  .pill{{font-family:'JetBrains Mono',monospace;font-size:12px;color:var(--gray);background:rgba(255,255,255,.04);border:1px solid rgba(255,255,255,.08);padding:6px 12px;border-radius:100px}}
  .pill.live{{color:var(--green);border-color:rgba(46,160,67,.3);background:rgba(46,160,67,.1)}}

  .sessions{{display:grid;gap:22px;margin-bottom:40px}}
  .sessions-1{{grid-template-columns:1fr;max-width:680px}}
  .sessions-2{{grid-template-columns:1fr 1fr}}
  .sessions-many{{grid-template-columns:repeat(auto-fill,minmax(300px,1fr))}}
  @media (max-width:760px){{.sessions{{grid-template-columns:1fr !important;max-width:100%}}}}
  .session-card{{background:rgba(255,255,255,.03);border:1px solid rgba(255,255,255,.08);border-radius:16px;padding:18px;min-width:0}}
  .session-head{{display:flex;align-items:flex-start;gap:12px;margin-bottom:16px}}
  .session-tag{{flex-shrink:0;color:var(--navy);font-weight:700;font-size:12px;font-family:'JetBrains Mono',monospace;padding:5px 10px;border-radius:8px;letter-spacing:.5px}}
  .session-titles{{flex:1;min-width:0}}
  .session-titles h3{{font-family:'Playfair Display',serif;font-size:19px;font-weight:700;line-height:1.2;margin-bottom:4px}}
  .session-topics{{font-size:12.5px;color:var(--gray);line-height:1.5}}
  .sess-pill{{flex-shrink:0;font-family:'JetBrains Mono',monospace;font-size:11px;color:var(--gray);background:rgba(255,255,255,.05);padding:4px 9px;border-radius:8px;white-space:nowrap}}
  .video-aspect{{position:relative;width:100%;aspect-ratio:16/9;background:#000;border-radius:10px;overflow:hidden}}
  .video-aspect iframe{{position:absolute;inset:0;width:100%;height:100%;border:0}}
  .coming-soon-aspect{{background:linear-gradient(135deg,var(--navy-2),var(--navy-3));display:flex;align-items:center;justify-content:center;border:1px dashed rgba(255,255,255,.12)}}
  .cs-inner{{text-align:center;padding:20px}}
  .cs-icon{{font-size:40px;margin-bottom:10px;opacity:.7}}
  .cs-text{{font-size:13px;color:var(--gray);line-height:1.5}}
  .sess-yt-btn{{display:inline-flex;align-items:center;gap:6px;margin-top:12px;font-size:13px;font-weight:600;color:#FF4444;text-decoration:none}}
  .sess-yt-btn:hover{{text-decoration:underline}}

  .actions{{display:flex;gap:10px;flex-wrap:wrap;margin-bottom:40px}}
  .btn{{display:inline-flex;align-items:center;gap:7px;padding:11px 18px;border-radius:10px;font-size:13px;font-weight:600;text-decoration:none;border:1px solid transparent;cursor:pointer;font-family:inherit;transition:all .2s}}
  .btn-secondary{{background:rgba(255,255,255,.05);color:var(--white);border-color:rgba(255,255,255,.12)}}
  .btn-secondary:hover{{border-color:var(--cyan);color:var(--cyan)}}

  .about{{background:rgba(255,255,255,.02);border:1px solid rgba(255,255,255,.06);border-radius:14px;padding:24px;margin-bottom:24px}}
  .about h2{{font-family:'Playfair Display',serif;font-size:22px;margin-bottom:12px}}
  .about p{{color:#CBD5E1;font-size:14.5px;margin-bottom:10px}}
  .about p:last-child{{margin-bottom:0}}

  footer{{border-top:1px solid rgba(255,255,255,.06);padding:30px 24px;text-align:center;color:var(--gray-2);font-size:13px}}
  footer a{{color:var(--cyan);text-decoration:none}}
</style>
</head>
<body>
<nav class="topbar">
  <div class="nav-inner">
    <a href="../../index.html" class="brand">cloud<span>withshad</span></a>
    <a href="../index.html" class="nav-back">← All recordings</a>
  </div>
</nav>
<main>
  <div class="breadcrumbs">
    <a href="../../index.html">Home</a><span class="sep">/</span>
    <a href="../index.html">Live Recordings</a><span class="sep">/</span>
    <span>Week {week}</span>
  </div>

  <h1 class="video-title">Week {week} — {title}</h1>
  <div class="video-subtitle">{session_count_label} · {subtitle}</div>
  <div class="video-pills">
    {status_pill}
    <span class="pill">📅 {date_label}</span>
    <span class="pill">🎯 Week {week} of 4</span>
  </div>

  <div class="{grid_class}">
{sessions_html}
  </div>

  <div class="actions">
    <a href="{materials}" class="btn btn-secondary">📂 Week {week} materials</a>
    <button onclick="navigator.clipboard.writeText(window.location.href);this.textContent='✓ Link copied!';setTimeout(()=>this.textContent='🔗 Share this page',2500)" class="btn btn-secondary">🔗 Share this page</button>
  </div>

  <div class="about">
    <h2>About Week {week}</h2>
    <p>This week was delivered as <strong>{session_count_label_lower}</strong>, recorded live with the cohort — questions and all. Watch them in order; each one builds on the last.</p>
    <p>Watch these <strong>before</strong> attempting the week's labs — they'll make a lot more sense afterwards.</p>
  </div>
</main>
<footer>
  Built for the <a href="../../index.html">cloudwithshad</a> AWS Bootcamp · 🇬🇭
</footer>
</body>
</html>'''

    out = folder / "index.html"
    out.write_text(html, encoding="utf-8")
    return uploaded, len(sessions)


def load_weeks():
    """Read each week's own config.json from videos/week-XX/config.json.

    Falls back to the legacy central recordings.json if no per-folder
    configs exist, so nothing breaks during migration.
    """
    week_configs = sorted(VIDEOS.glob("week-*/config.json"))
    if week_configs:
        weeks = []
        for cfg_path in week_configs:
            data = json.loads(cfg_path.read_text(encoding="utf-8"))
            wk = {k: v for k, v in data.items() if not k.startswith("_")}
            if "week" not in wk:
                wk["week"] = int(cfg_path.parent.name.split("-")[1])
            weeks.append(wk)
        weeks.sort(key=lambda w: w["week"])
        return weeks

    if CONFIG.exists():
        return json.loads(CONFIG.read_text(encoding="utf-8"))["weeks"]

    sys.exit("❌ No week configs found (looked for videos/week-*/config.json)")


def main():
    weeks = load_weeks()
    print(f"🎬 Building {len(weeks)} weekly recording pages (2 sessions each)\n")
    total_up = 0
    for wk in weeks:
        up, total = build_week_page(wk)
        total_up += up
        state = f"{up}/{total} uploaded" if up else "none uploaded yet"
        icon = "✅" if up == total else ("🟡" if up else "🔒")
        print(f"  {icon} Week {wk['week']} — {wk.get('title','')} ({state})")
    print(f"\n🎉 Done. {total_up} session videos live across all weeks.")
    print("   Edit each videos/week-XX/config.json to add YouTube IDs, then re-run.")


if __name__ == "__main__":
    main()
