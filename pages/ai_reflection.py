import streamlit as st
from datetime import date

# ─────────────────────────────────────────────
# PAGE CONFIG
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="AI Reflection · AI Momentum",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ─────────────────────────────────────────────
# CUSTOM CSS
# ─────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Sans:wght@300;400;500&display=swap');

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
    background-color: #080c14;
    color: #e2e8f0;
}
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 2.5rem 3rem 4rem 3rem; max-width: 900px; }

/* ── Sidebar ── */
[data-testid="stSidebar"] { background: #0d1220; border-right: 1px solid #1e2a40; }
[data-testid="stSidebar"] * { font-family: 'DM Sans', sans-serif; color: #94a3b8; }
.sidebar-logo {
    font-family: 'Syne', sans-serif; font-weight: 800; font-size: 1.4rem;
    letter-spacing: -0.02em;
    background: linear-gradient(135deg, #38bdf8, #818cf8);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    padding: 0.5rem 0 1.5rem 0;
}
.sidebar-nav-item {
    display: flex; align-items: center; gap: 10px;
    padding: 10px 14px; border-radius: 8px; margin-bottom: 4px;
    color: #94a3b8; font-size: 0.95rem;
}
.sidebar-nav-item.active { background: #162036; color: #38bdf8; font-weight: 500; }
.sidebar-divider { border: none; border-top: 1px solid #1e2a40; margin: 1.2rem 0; }
.sidebar-section-label {
    font-size: 0.7rem; letter-spacing: 0.12em; text-transform: uppercase;
    color: #4a5568; padding: 0 14px; margin-bottom: 6px;
}

/* ── Page header ── */
.page-badge {
    display: inline-flex; align-items: center; gap: 6px;
    background: rgba(129,140,248,0.08); border: 1px solid rgba(129,140,248,0.25);
    color: #818cf8; font-size: 0.75rem; letter-spacing: 0.1em;
    text-transform: uppercase; padding: 5px 14px; border-radius: 999px;
    margin-bottom: 1.2rem; font-weight: 500;
}
.page-title {
    font-family: 'Syne', sans-serif; font-weight: 800; font-size: 2.4rem;
    letter-spacing: -0.03em; color: #f1f5f9; margin: 0 0 0.4rem 0;
}
.page-sub { font-size: 0.95rem; color: #4a5568; margin-bottom: 0.5rem; }
.section-divider { border: none; border-top: 1px solid #1e2a40; margin: 2rem 0; }
.section-label {
    font-family: 'Syne', sans-serif; font-weight: 700; font-size: 1rem;
    color: #e2e8f0; margin-bottom: 1rem; padding-bottom: 0.5rem;
    border-bottom: 1px solid #1e2a40;
}

/* ── Data snapshot pills ── */
.snapshot-row {
    display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 1.8rem;
}
.snapshot-pill {
    display: flex; align-items: center; gap: 7px;
    background: #0d1220; border: 1px solid #1e2a40;
    border-radius: 10px; padding: 8px 14px;
    font-size: 0.82rem; color: #64748b;
}
.snapshot-pill b { color: #e2e8f0; font-weight: 600; }
.pill-dot {
    width: 7px; height: 7px; border-radius: 50%; flex-shrink: 0;
}

/* ── Main AI reflection card ── */
.reflection-card {
    background: #0d1220;
    border: 1px solid #1e2a40;
    border-radius: 18px;
    padding: 2rem 2.2rem;
    position: relative;
    overflow: hidden;
    margin-bottom: 1.2rem;
}
.reflection-card::before {
    content: ''; position: absolute; top: 0; left: 0; right: 0; height: 3px;
}
.card-green::before  { background: linear-gradient(90deg, #2dd4bf, #38bdf8); }
.card-blue::before   { background: linear-gradient(90deg, #38bdf8, #818cf8); }
.card-purple::before { background: linear-gradient(90deg, #818cf8, #c084fc); }
.card-amber::before  { background: linear-gradient(90deg, #fbbf24, #f97316); }
.card-red::before    { background: linear-gradient(90deg, #f87171, #c084fc); }

.reflection-tag {
    display: inline-flex; align-items: center; gap: 6px;
    font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.1em;
    padding: 4px 11px; border-radius: 999px; font-weight: 600;
    margin-bottom: 1rem;
}
.tag-green  { background: rgba(45,212,191,0.1);  color: #2dd4bf; }
.tag-blue   { background: rgba(56,189,248,0.1);  color: #38bdf8; }
.tag-purple { background: rgba(129,140,248,0.1); color: #818cf8; }
.tag-amber  { background: rgba(251,191,36,0.1);  color: #fbbf24; }
.tag-red    { background: rgba(248,113,113,0.1); color: #f87171; }

.reflection-heading {
    font-family: 'Syne', sans-serif; font-weight: 800;
    font-size: 1.4rem; color: #f1f5f9; margin-bottom: 0.8rem;
    line-height: 1.25;
}
.reflection-body {
    font-size: 0.95rem; color: #64748b; line-height: 1.8;
}
.reflection-body b { color: #94a3b8; }

/* ── Action steps ── */
.steps-card {
    background: #080c14; border: 1px solid #1e2a40;
    border-radius: 14px; padding: 1.4rem 1.6rem; margin-bottom: 1.2rem;
}
.step-row {
    display: flex; align-items: flex-start; gap: 12px;
    padding: 0.65rem 0; border-bottom: 1px solid #0f1724;
    font-size: 0.9rem; color: #64748b; line-height: 1.5;
}
.step-row:last-child { border-bottom: none; }
.step-number {
    font-family: 'Syne', sans-serif; font-weight: 700; font-size: 0.75rem;
    min-width: 22px; height: 22px; border-radius: 6px;
    display: flex; align-items: center; justify-content: center;
    flex-shrink: 0; margin-top: 1px;
    background: rgba(129,140,248,0.12); color: #818cf8;
}

/* ── Quote block ── */
.quote-block {
    border-left: 3px solid #818cf8;
    padding: 1rem 1.4rem;
    margin: 0 0 1.2rem 0;
    background: rgba(129,140,248,0.04);
    border-radius: 0 10px 10px 0;
}
.quote-text {
    font-size: 1rem; color: #94a3b8;
    font-style: italic; line-height: 1.7; margin-bottom: 0.3rem;
}
.quote-author { font-size: 0.78rem; color: #4a5568; }

/* ── Score meter ── */
.meter-row {
    display: flex; gap: 10px; margin-bottom: 1.6rem; flex-wrap: wrap;
}
.meter-box {
    flex: 1; min-width: 120px;
    background: #0d1220; border: 1px solid #1e2a40;
    border-radius: 12px; padding: 1rem 1.1rem; text-align: center;
}
.meter-emoji { font-size: 1.4rem; margin-bottom: 4px; }
.meter-value {
    font-family: 'Syne', sans-serif; font-size: 1.6rem; font-weight: 800;
    background: linear-gradient(135deg, #818cf8, #c084fc);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    line-height: 1;
}
.meter-label { font-size: 0.72rem; color: #4a5568; text-transform: uppercase; letter-spacing: 0.08em; margin-top: 3px; }
.meter-grade {
    display: inline-block; margin-top: 6px; font-size: 0.68rem;
    padding: 2px 8px; border-radius: 999px; font-weight: 600; letter-spacing: 0.06em;
}
.grade-great  { background: rgba(45,212,191,0.1);  color: #2dd4bf; }
.grade-good   { background: rgba(56,189,248,0.1);  color: #38bdf8; }
.grade-ok     { background: rgba(251,191,36,0.1);  color: #fbbf24; }
.grade-low    { background: rgba(248,113,113,0.1); color: #f87171; }

/* ── No-data warning ── */
.warn-panel {
    background: rgba(251,191,36,0.06); border: 1px solid rgba(251,191,36,0.2);
    border-radius: 12px; padding: 1.4rem 1.6rem;
    font-size: 0.92rem; color: #94a3b8; line-height: 1.7;
}
.warn-panel b { color: #fbbf24; }

/* ── Footer ── */
.footer { margin-top: 4rem; text-align: center; font-size: 0.78rem; color: #2d3748; letter-spacing: 0.04em; }
</style>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────
# SIDEBAR
# ─────────────────────────────────────────────
with st.sidebar:
    st.markdown('<div class="sidebar-logo">⚡ AI Momentum</div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-section-label">Main</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="sidebar-nav-item">🏠&nbsp; Home</div>
    <div class="sidebar-nav-item">📊&nbsp; Dashboard</div>
    <div class="sidebar-nav-item">🎯&nbsp; Goals</div>
    <div class="sidebar-nav-item active">🤖&nbsp; AI Coach</div>
    """, unsafe_allow_html=True)
    st.markdown('<hr class="sidebar-divider">', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-section-label">Personal</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="sidebar-nav-item">✅&nbsp; Habits</div>
    <div class="sidebar-nav-item">🧠&nbsp; Mood & Focus</div>
    <div class="sidebar-nav-item">📈&nbsp; Progress</div>
    <div class="sidebar-nav-item">⚙️&nbsp; Settings</div>
    """, unsafe_allow_html=True)
    st.markdown('<hr class="sidebar-divider">', unsafe_allow_html=True)
    st.markdown("""
    <div style="padding:12px 14px;background:#0d1220;border-radius:10px;
                border:1px solid #1e2a40;display:flex;align-items:center;gap:10px;">
        <div style="width:34px;height:34px;border-radius:50%;
                    background:linear-gradient(135deg,#38bdf8,#818cf8);
                    display:flex;align-items:center;justify-content:center;
                    font-size:0.85rem;font-weight:700;color:#080c14;">U</div>
        <div>
            <div style="font-size:0.85rem;color:#e2e8f0;font-weight:500;">User</div>
            <div style="font-size:0.72rem;color:#4a5568;">Free Plan</div>
        </div>
    </div>
    """, unsafe_allow_html=True)


# ─────────────────────────────────────────────
# READ SESSION STATE DATA
#
# We pull in everything saved by habits.py and
# mood.py. The .get(key, default) pattern keeps
# the app from crashing when no data exists yet.
# ─────────────────────────────────────────────

# From habits.py
habits  = st.session_state.get("habits",  [])
checked = st.session_state.get("checked", [])

total_habits     = len(habits)
completed_habits = sum(checked)         # True = 1, False = 0
habit_pct        = int((completed_habits / total_habits * 100)
                       if total_habits > 0 else 0)

# From mood.py
checkin     = st.session_state.get("checkin", None)
mood_label  = checkin.get("mood",       "—")  if checkin else None
energy_val  = checkin.get("energy",     0)    if checkin else 0
focus_val   = checkin.get("focus",      0)    if checkin else 0
reflection  = checkin.get("reflection", "")   if checkin else ""

# Derived composite score out of 100
# Formula: average of (habit %, energy*10, focus*10) → gives one headline number
wellness = int((habit_pct + energy_val * 10 + focus_val * 10) / 3) if checkin else 0

MOOD_EMOJIS = {
    "Happy": "😊", "Neutral": "😐", "Tired": "😴",
    "Stressed": "😰", "Motivated": "🚀",
}
mood_emoji = MOOD_EMOJIS.get(mood_label, "—")

# Boolean flags — these make the if-else logic below easier to read
# instead of repeating raw comparisons everywhere
has_habits  = total_habits > 0
has_checkin = checkin is not None


# ─────────────────────────────────────────────
# PAGE HEADER
# ─────────────────────────────────────────────
st.markdown('<div class="page-badge">✦ Powered by AI Logic</div>', unsafe_allow_html=True)
st.markdown('<h1 class="page-title">AI Reflection</h1>', unsafe_allow_html=True)
st.markdown(
    f'<p class="page-sub">Your personalised daily debrief · {date.today().strftime("%A, %B %d %Y")}</p>',
    unsafe_allow_html=True
)


# ─────────────────────────────────────────────
# GUARD: No data at all → show friendly prompt
#
# If the user lands here without filling in any
# other page, we show a helpful message instead
# of empty or broken output.
# ─────────────────────────────────────────────
if not has_habits and not has_checkin:
    st.markdown("""
    <div class="warn-panel">
        🤖 <b>Nothing to reflect on yet.</b><br><br>
        The AI Reflection engine needs some data to work with. Here's what to do:<br><br>
        &nbsp;&nbsp;&nbsp;1. Go to <b>Habits</b> → add at least one habit and check some off.<br>
        &nbsp;&nbsp;&nbsp;2. Go to <b>Mood & Focus</b> → complete today's check-in.<br>
        &nbsp;&nbsp;&nbsp;3. Come back here — your personalised reflection will be waiting.
    </div>
    """, unsafe_allow_html=True)
    st.stop()   # st.stop() halts the script here — nothing below renders


st.markdown("<br>", unsafe_allow_html=True)


# ─────────────────────────────────────────────
# DATA SNAPSHOT ROW
#
# Small pills that show what data was found in
# session_state — so the user can see what the
# AI reflection is based on.
# ─────────────────────────────────────────────
st.markdown('<div class="section-label">Today\'s Data at a Glance</div>', unsafe_allow_html=True)

# Helper: turn a number into a letter grade label and CSS class
def get_grade(value, out_of_10=True):
    """
    Returns (label, css_class) based on how high the value is.
    Makes it easy to colour-code any score consistently.
    """
    score = value if out_of_10 else value / 10   # normalise to 0–10 scale
    if score >= 8:   return "Excellent", "grade-great"
    if score >= 6:   return "Good",      "grade-good"
    if score >= 4:   return "Fair",      "grade-ok"
    return "Needs Work", "grade-low"

# Meter boxes — energy / focus / habit %
st.markdown('<div class="meter-row">', unsafe_allow_html=True)

meters = [
    ("⚡", str(energy_val),        "/10", "Energy",      *get_grade(energy_val)),
    ("🎯", str(focus_val),         "/10", "Focus",       *get_grade(focus_val)),
    ("✅", str(completed_habits),  f"/{total_habits}", "Habits Done", *get_grade(habit_pct, out_of_10=False)),
    (mood_emoji, mood_label or "—", "",   "Mood",        "", ""),
]

meter_html = ""
for emoji, val, suffix, label, grade_label, grade_class in meters:
    grade_block = (
        f'<div class="meter-grade {grade_class}">{grade_label}</div>'
        if grade_label else ""
    )
    meter_html += f"""
    <div class="meter-box">
        <div class="meter-emoji">{emoji}</div>
        <div class="meter-value">{val}<span style="font-size:0.9rem;color:#4a5568;">{suffix}</span></div>
        <div class="meter-label">{label}</div>
        {grade_block}
    </div>
    """
st.markdown(f'<div class="meter-row">{meter_html}</div>', unsafe_allow_html=True)


st.markdown('<hr class="section-divider">', unsafe_allow_html=True)


# ─────────────────────────────────────────────
# AI REFLECTION ENGINE
#
# This is the core of the page. We use nested
# if-else statements to combine multiple data
# points and produce one of several different
# reflection "profiles".
#
# Think of it like a decision tree:
#
#   Focus high?
#   ├── YES → Habits high? → Peak Performance
#   │         Habits low?  → Focused but Idle
#   └── NO  → Energy high?
#             ├── YES → Mood stressed? → Burnout Risk
#             │         Otherwise     → Scattered Energy
#             └── NO  → Habits high?  → Gritty & Tired
#                       Otherwise     → Recovery Day
#
# Each profile has: a tag, heading, body text,
# 3 action steps, and a motivational quote.
# ─────────────────────────────────────────────

st.markdown('<div class="section-label">🤖 Your AI Reflection</div>', unsafe_allow_html=True)

# We'll build these variables inside each branch
profile_tag     = ""
profile_heading = ""
profile_body    = ""
action_steps    = []
quote_text      = ""
quote_author    = ""
card_color      = ""
tag_color       = ""

# ── BRANCH 1: High Focus ──────────────────────────────────────
if focus_val >= 7:

    if habit_pct >= 70:
        # Best case: focused AND productive
        profile_tag     = "🏆 Peak Performance"
        card_color      = "card-green"
        tag_color       = "tag-green"
        profile_heading = "You're operating at your best today."
        profile_body    = (
            f"With a focus score of <b>{focus_val}/10</b> and "
            f"<b>{completed_habits} out of {total_habits}</b> habits completed, "
            f"you're firing on all cylinders. "
            f"Days like this are rare — they're built, not stumbled upon. "
            f"Your consistency is the engine behind this result. "
            f"The momentum you generate today will carry forward into tomorrow, "
            f"so don't let up in the final stretch."
        )
        action_steps = [
            "Document one thing that made today feel so productive — so you can repeat it.",
            "Use any remaining energy to prep tomorrow's priorities before you switch off.",
            "Celebrate the win tonight — rest is part of the performance cycle.",
        ]
        quote_text   = "Success is neither magical nor mysterious. Success is the natural consequence of consistently applying basic fundamentals."
        quote_author = "— Jim Rohn"

    else:
        # Focused but not converting it into habit completion
        profile_tag     = "🔵 Focused but Idle"
        card_color      = "card-blue"
        tag_color       = "tag-blue"
        profile_heading = "Your focus is sharp — but habits need attention."
        profile_body    = (
            f"Your focus is strong at <b>{focus_val}/10</b>, which means your mind is ready. "
            f"But only <b>{completed_habits} of {total_habits}</b> habits are done so far. "
            f"You have the mental clarity to execute — "
            f"the gap is between intention and action. "
            f"Pick just one uncompleted habit right now and treat it as a 5-minute micro-task. "
            f"Starting is almost always the hardest part."
        )
        action_steps = [
            f"Pick your single most important incomplete habit and do it in the next 10 minutes.",
            "Set a 25-minute focused block — no distractions — to knock out 2 more habits.",
            "After each completed habit, pause for 10 seconds and acknowledge the win.",
        ]
        quote_text   = "You don't have to be great to start, but you have to start to be great."
        quote_author = "— Zig Ziglar"

# ── BRANCH 2: Low Focus, High Energy ─────────────────────────
elif energy_val >= 7:

    if mood_label == "Stressed":
        # Energy is there but stress is burning it
        profile_tag     = "🟡 Burnout Risk"
        card_color      = "card-amber"
        tag_color       = "tag-amber"
        profile_heading = "High energy, high stress — a fragile combination."
        profile_body    = (
            f"Your energy is at <b>{energy_val}/10</b>, but your focus sits at "
            f"<b>{focus_val}/10</b> and you're feeling <b>stressed</b>. "
            f"This pattern often means your energy is being consumed by anxiety "
            f"rather than directed toward output. "
            f"Unchecked, this leads to burnout — high input, low return. "
            f"The most productive thing you can do right now is slow down "
            f"intentionally before your body forces you to."
        )
        action_steps = [
            "Take a 5-minute breathing break now — 4 counts in, hold 4, out 6.",
            "Write down every open task in your head to clear mental RAM.",
            "Pick only ONE thing to focus on for the next hour. Ignore the rest.",
        ]
        quote_text   = "Almost everything will work again if you unplug it for a few minutes — including you."
        quote_author = "— Anne Lamott"

    else:
        # Energetic but scattered
        profile_tag     = "⚡ Scattered Energy"
        card_color      = "card-blue"
        tag_color       = "tag-blue"
        profile_heading = "You have fuel — but need a direction."
        profile_body    = (
            f"Energy at <b>{energy_val}/10</b> is a real asset today. "
            f"But a focus score of <b>{focus_val}/10</b> suggests that energy "
            f"is spreading in too many directions at once. "
            f"Think of it like sunlight through a magnifying glass — "
            f"unfocused, it just warms the surface. "
            f"Concentrated, it can start a fire. "
            f"You need a single clear priority right now, not a long to-do list."
        )
        action_steps = [
            "Write down your top 3 tasks — then cross out 2 and do only the first one.",
            "Remove all browser tabs and apps unrelated to your current task.",
            "Set a visible countdown timer for 30 minutes of uninterrupted work.",
        ]
        quote_text   = "The key is not to prioritize what's on your schedule, but to schedule your priorities."
        quote_author = "— Stephen Covey"

# ── BRANCH 3: Low Focus, Low Energy ──────────────────────────
else:

    if habit_pct >= 60:
        # Tired but still showing up — that's grit
        profile_tag     = "💪 Gritty & Tired"
        card_color      = "card-purple"
        tag_color       = "tag-purple"
        profile_heading = "Running on low — but still delivering. That's grit."
        profile_body    = (
            f"Energy at <b>{energy_val}/10</b>, focus at <b>{focus_val}/10</b> — "
            f"and yet you've completed <b>{completed_habits} of {total_habits}</b> habits. "
            f"That's not luck, that's discipline. "
            f"Motivation is unreliable — it's gone on hard days exactly like this one. "
            f"But systems and identity carry you through. "
            f"You showed up anyway. That is the most important data point of your day."
        )
        action_steps = [
            "Don't push for more output tonight — protect tomorrow's energy instead.",
            "Do a 10-minute wind-down routine: dim lights, no screens, slow breathing.",
            "Write one sentence about why you kept going today — read it on the next hard day.",
        ]
        quote_text   = "It's not about how hard you hit. It's about how hard you can get hit and keep moving forward."
        quote_author = "— Rocky Balboa"

    else:
        # Everything is low — this is a recovery day
        profile_tag     = "🌙 Recovery Day"
        card_color      = "card-red"
        tag_color       = "tag-red"
        profile_heading = "Today is a recovery day — and that's okay."
        profile_body    = (
            f"Low energy (<b>{energy_val}/10</b>), low focus (<b>{focus_val}/10</b>), "
            f"and <b>{completed_habits} of {total_habits}</b> habits completed. "
            f"Every high-performer has days like this — the body and mind cycle through "
            f"peaks and troughs naturally. "
            f"Treating a low day as a failure compounds the problem. "
            f"Treating it as a scheduled recovery makes you stronger for what comes next. "
            f"The goal today is not output — it's preservation."
        )
        action_steps = [
            "Drink a full glass of water and eat something nourishing in the next 30 minutes.",
            "Complete just ONE tiny habit — even 2 minutes counts — to protect your streak.",
            "Sleep 30 minutes earlier than usual tonight. Tomorrow starts now.",
        ]
        quote_text   = "Rest when you're weary. Refresh and renew yourself, your body, your mind, your spirit."
        quote_author = "— Ralph Waldo Emerson"


# ─────────────────────────────────────────────
# RENDER THE REFLECTION CARD
#
# Now we display whatever the if-else branches
# above filled into our variables.
# ─────────────────────────────────────────────
st.markdown(f"""
<div class="reflection-card {card_color}">
    <div class="reflection-tag {tag_color}">{profile_tag}</div>
    <div class="reflection-heading">{profile_heading}</div>
    <div class="reflection-body">{profile_body}</div>
</div>
""", unsafe_allow_html=True)

# ── Motivational quote ──
st.markdown(f"""
<div class="quote-block">
    <div class="quote-text">"{quote_text}"</div>
    <div class="quote-author">{quote_author}</div>
</div>
""", unsafe_allow_html=True)

# ── Action steps ──
st.markdown('<div class="section-label">Your 3 Action Steps for Today</div>', unsafe_allow_html=True)

steps_html = "".join([
    f"""
    <div class="step-row">
        <div class="step-number">{i + 1}</div>
        <span>{step}</span>
    </div>
    """
    for i, step in enumerate(action_steps)
])
st.markdown(f'<div class="steps-card">{steps_html}</div>', unsafe_allow_html=True)


st.markdown('<hr class="section-divider">', unsafe_allow_html=True)


# ─────────────────────────────────────────────
# MOOD-SPECIFIC BONUS INSIGHT
#
# On top of the main reflection, we layer one
# extra insight that reacts specifically to the
# user's reported mood. It's brief and targeted.
# ─────────────────────────────────────────────
if has_checkin and mood_label:
    st.markdown('<div class="section-label">Mood Deep-Dive</div>', unsafe_allow_html=True)

    # Each mood maps to a specific message and colour
    # We use a dictionary here instead of a long if-else chain —
    # it's cleaner when you have many fixed options.
    mood_insights = {
        "Happy": {
            "color": "#2dd4bf",
            "bg":    "rgba(45,212,191,0.06)",
            "border":"rgba(45,212,191,0.2)",
            "text":  (
                "Positive affect is a <b>performance multiplier</b>. "
                "When you feel good, your brain is more creative, more resilient, "
                "and more open to collaboration. "
                "Use this window to tackle any task that requires lateral thinking "
                "or interpersonal effort — happiness is a cognitive asset."
            ),
        },
        "Neutral": {
            "color": "#38bdf8",
            "bg":    "rgba(56,189,248,0.06)",
            "border":"rgba(56,189,248,0.2)",
            "text":  (
                "Neutral isn't bad — it's <b>stable and trainable</b>. "
                "Without emotional noise pulling your attention, "
                "you're actually well-positioned for deep analytical work. "
                "Try pairing this state with your most cognitively demanding task of the day."
            ),
        },
        "Tired": {
            "color": "#818cf8",
            "bg":    "rgba(129,140,248,0.06)",
            "border":"rgba(129,140,248,0.2)",
            "text":  (
                "Fatigue <b>impairs decision-making</b> before it impairs physical performance. "
                "Avoid making important choices when tired — delay them if possible. "
                "Instead, use this time for routine, well-practiced tasks that don't "
                "require high cognitive load. And prioritise sleep tonight above all else."
            ),
        },
        "Stressed": {
            "color": "#fbbf24",
            "bg":    "rgba(251,191,36,0.06)",
            "border":"rgba(251,191,36,0.2)",
            "text":  (
                "Stress is your nervous system signalling that <b>demands feel greater than resources</b>. "
                "The fastest physiological reset is a long exhale — breathe in for 4 counts, "
                "out for 8. Do this 3 times right now. "
                "Then identify one thing you can control in the next 10 minutes and do it. "
                "Control restores calm."
            ),
        },
        "Motivated": {
            "color": "#c084fc",
            "bg":    "rgba(192,132,252,0.06)",
            "border":"rgba(192,132,252,0.2)",
            "text":  (
                "Motivation is <b>powerful but temporary</b> — it's a wave, not a tide. "
                "The best use of a motivated state is not just doing more, "
                "but building the structures that will carry you when motivation fades: "
                "set a streak goal, schedule tomorrow's deep work block, or commit to a new habit."
            ),
        },
    }

    # Get the right insight dict for this mood (with a safe fallback)
    mi = mood_insights.get(mood_label, None)

    if mi:
        st.markdown(f"""
        <div style="background:{mi['bg']};border:1px solid {mi['border']};
                    border-radius:14px;padding:1.3rem 1.6rem;">
            <div style="display:flex;align-items:center;gap:8px;margin-bottom:0.7rem;">
                <span style="font-size:1.4rem;">{mood_emoji}</span>
                <span style="font-family:'Syne',sans-serif;font-weight:700;
                             color:{mi['color']};font-size:0.9rem;">
                    Feeling {mood_label}
                </span>
            </div>
            <div style="font-size:0.9rem;color:#64748b;line-height:1.75;">{mi['text']}</div>
        </div>
        """, unsafe_allow_html=True)


st.markdown('<hr class="section-divider">', unsafe_allow_html=True)


# ─────────────────────────────────────────────
# HABIT BREAKDOWN
#
# If habits exist, show a compact list of each
# one with a done/pending indicator — so the
# user sees exactly which ones are still open.
# ─────────────────────────────────────────────
if has_habits:
    st.markdown('<div class="section-label">Habit Breakdown</div>', unsafe_allow_html=True)

    # Split habits into two columns for a cleaner layout
    col_a, col_b = st.columns(2, gap="medium")
    half = len(habits) // 2 + len(habits) % 2   # ceiling division

    def habit_item_html(name, done):
        """Returns the HTML for one habit row."""
        dot_color   = "#2dd4bf" if done else "#1e2a40"
        name_style  = "text-decoration:line-through;color:#2d3748;" if done else "color:#94a3b8;"
        badge       = (
            '<span style="font-size:0.68rem;background:rgba(45,212,191,0.1);'
            'border:1px solid rgba(45,212,191,0.3);color:#2dd4bf;'
            'padding:2px 8px;border-radius:999px;">Done</span>'
            if done else
            '<span style="font-size:0.68rem;background:#0d1220;'
            'border:1px solid #1e2a40;color:#4a5568;'
            'padding:2px 8px;border-radius:999px;">Pending</span>'
        )
        return f"""
        <div style="display:flex;align-items:center;justify-content:space-between;
                    padding:0.7rem 1rem;background:#0d1220;border:1px solid #1e2a40;
                    border-radius:10px;margin-bottom:8px;">
            <div style="display:flex;align-items:center;gap:9px;">
                <div style="width:7px;height:7px;border-radius:50%;background:{dot_color};"></div>
                <span style="font-size:0.88rem;{name_style}">{name}</span>
            </div>
            {badge}
        </div>
        """

    # zip() pairs each habit name with its True/False completion status
    with col_a:
        for name, done in list(zip(habits, checked))[:half]:
            st.markdown(habit_item_html(name, done), unsafe_allow_html=True)

    with col_b:
        for name, done in list(zip(habits, checked))[half:]:
            st.markdown(habit_item_html(name, done), unsafe_allow_html=True)

    # Summary sentence below the list
    remaining = total_habits - completed_habits
    if remaining == 0:
        summary = "🎉 All habits complete — nothing left to do but protect that streak."
    elif remaining == 1:
        summary = f"One habit remaining. You're closer than you think — go get it."
    else:
        summary = f"{remaining} habits still open. Small progress now beats perfect progress never."

    st.markdown(
        f'<p style="font-size:0.85rem;color:#4a5568;margin-top:0.5rem;">{summary}</p>',
        unsafe_allow_html=True
    )


# ─────────────────────────────────────────────
# FOOTER
# ─────────────────────────────────────────────
st.markdown("""
<div class="footer">
    ⚡ AI Momentum &nbsp;·&nbsp; AI Reflection &nbsp;·&nbsp; 2025
</div>
""", unsafe_allow_html=True)