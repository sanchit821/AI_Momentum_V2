import streamlit as st
 
# ── Page config ────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="AI Momentum",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.markdown("""
<style>

/* Main app padding */
.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

/* Metric cards */
[data-testid="stMetric"] {
    background-color: #1E1E1E;
    border: 1px solid #333333;
    padding: 15px;
    border-radius: 12px;
}

/* Headers */
h1 {
    font-weight: 700;
}

h2 {
    padding-top: 10px;
}

</style>
""", unsafe_allow_html=True)

# ── Custom CSS ─────────────────────────────────────────────────────────────────
st.markdown("""
<style>
/* Import fonts */
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Sans:wght@300;400;500&display=swap');

/* ── Global reset & base ── */
html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
    background-color: #080c14;
    color: #e2e8f0;
}

/* Hide default Streamlit chrome */
#MainMenu, footer, header { visibility: hidden; }
.block-container {
    padding: 2.5rem 3rem 4rem 3rem;
    max-width: 1100px;
}

/* ── Sidebar ── */
[data-testid="stSidebar"] {
    background: #0d1220;
    border-right: 1px solid #1e2a40;
}
[data-testid="stSidebar"] * {
    font-family: 'DM Sans', sans-serif;
    color: #94a3b8;
}
[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3 {
    font-family: 'Syne', sans-serif;
    color: #e2e8f0;
}
.sidebar-logo {
    font-family: 'Syne', sans-serif;
    font-weight: 800;
    font-size: 1.4rem;
    letter-spacing: -0.02em;
    background: linear-gradient(135deg, #38bdf8, #818cf8);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    padding: 0.5rem 0 1.5rem 0;
}
.sidebar-nav-item {
    display: flex;
    align-items: center;
    gap: 10px;
    padding: 10px 14px;
    border-radius: 8px;
    margin-bottom: 4px;
    cursor: pointer;
    transition: background 0.2s;
    color: #94a3b8;
    font-size: 0.95rem;
}
.sidebar-nav-item:hover   { background: #1a2540; color: #e2e8f0; }
.sidebar-nav-item.active  { background: #162036; color: #38bdf8; font-weight: 500; }
.sidebar-divider {
    border: none;
    border-top: 1px solid #1e2a40;
    margin: 1.2rem 0;
}
.sidebar-section-label {
    font-size: 0.7rem;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: #4a5568;
    padding: 0 14px;
    margin-bottom: 6px;
}

/* ── Hero / Welcome ── */
.hero-badge {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: rgba(56,189,248,0.08);
    border: 1px solid rgba(56,189,248,0.25);
    color: #38bdf8;
    font-size: 0.75rem;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    padding: 5px 14px;
    border-radius: 999px;
    margin-bottom: 1.4rem;
    font-weight: 500;
}
.hero-title {
    font-family: 'Syne', sans-serif;
    font-weight: 800;
    font-size: clamp(2.4rem, 5vw, 3.6rem);
    line-height: 1.1;
    letter-spacing: -0.03em;
    margin: 0 0 1.2rem 0;
    color: #f1f5f9;
}
.hero-title span {
    background: linear-gradient(135deg, #38bdf8 0%, #818cf8 60%, #c084fc 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
.hero-sub {
    font-size: 1.1rem;
    color: #64748b;
    max-width: 560px;
    line-height: 1.7;
    font-weight: 300;
}
.hero-divider {
    border: none;
    border-top: 1px solid #1e2a40;
    margin: 2.5rem 0;
}

/* ── Stats row ── */
.stat-box {
    background: #0d1220;
    border: 1px solid #1e2a40;
    border-radius: 12px;
    padding: 1.2rem 1.5rem;
    text-align: center;
}
.stat-number {
    font-family: 'Syne', sans-serif;
    font-size: 1.9rem;
    font-weight: 800;
    background: linear-gradient(135deg, #38bdf8, #818cf8);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    line-height: 1;
}
.stat-label {
    font-size: 0.78rem;
    color: #475569;
    margin-top: 4px;
    letter-spacing: 0.05em;
    text-transform: uppercase;
}

/* ── Section heading ── */
.section-heading {
    font-family: 'Syne', sans-serif;
    font-weight: 700;
    font-size: 1.35rem;
    color: #e2e8f0;
    margin-bottom: 0.4rem;
}
.section-sub {
    font-size: 0.9rem;
    color: #4a5568;
    margin-bottom: 1.8rem;
}

/* ── Feature cards ── */
.feature-card {
    background: #0d1220;
    border: 1px solid #1e2a40;
    border-radius: 16px;
    padding: 1.8rem 1.6rem;
    height: 100%;
    position: relative;
    overflow: hidden;
    transition: border-color 0.25s, transform 0.25s;
}
.feature-card:hover {
    border-color: #38bdf8;
    transform: translateY(-3px);
}
.feature-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 2px;
}
.card-blue::before   { background: linear-gradient(90deg, #38bdf8, #818cf8); }
.card-purple::before { background: linear-gradient(90deg, #818cf8, #c084fc); }
.card-teal::before   { background: linear-gradient(90deg, #2dd4bf, #38bdf8); }

.card-icon {
    font-size: 2rem;
    margin-bottom: 1rem;
}
.card-title {
    font-family: 'Syne', sans-serif;
    font-weight: 700;
    font-size: 1.1rem;
    color: #e2e8f0;
    margin-bottom: 0.6rem;
}
.card-desc {
    font-size: 0.88rem;
    color: #4a5568;
    line-height: 1.65;
}
.card-tag {
    display: inline-block;
    margin-top: 1.2rem;
    font-size: 0.72rem;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    padding: 4px 10px;
    border-radius: 6px;
    font-weight: 500;
}
.tag-blue   { background: rgba(56,189,248,0.1);  color: #38bdf8; }
.tag-purple { background: rgba(129,140,248,0.1); color: #818cf8; }
.tag-teal   { background: rgba(45,212,191,0.1);  color: #2dd4bf; }

/* ── CTA button ── */
.cta-btn {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: linear-gradient(135deg, #38bdf8, #818cf8);
    color: #080c14;
    font-family: 'Syne', sans-serif;
    font-weight: 700;
    font-size: 0.9rem;
    padding: 12px 26px;
    border-radius: 10px;
    text-decoration: none;
    margin-top: 2rem;
    letter-spacing: 0.02em;
    transition: opacity 0.2s;
}
.cta-btn:hover { opacity: 0.88; }

/* ── Footer ── */
.footer {
    margin-top: 4rem;
    text-align: center;
    font-size: 0.78rem;
    color: #2d3748;
    letter-spacing: 0.04em;
}
</style>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# SIDEBAR
# ══════════════════════════════════════════════════════════════════════════════
with st.sidebar:
    st.markdown('<div class="sidebar-logo">⚡ AI Momentum</div>', unsafe_allow_html=True)

    st.markdown('<div class="sidebar-section-label">Main</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="sidebar-nav-item active">🏠&nbsp; Home</div>
    <div class="sidebar-nav-item">📊&nbsp; Dashboard</div>
    <div class="sidebar-nav-item">🎯&nbsp; Goals</div>
    <div class="sidebar-nav-item">🤖&nbsp; AI Coach</div>
    """, unsafe_allow_html=True)

    st.markdown('<hr class="sidebar-divider">', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-section-label">Personal</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="sidebar-nav-item">📓&nbsp; Journal</div>
    <div class="sidebar-nav-item">📈&nbsp; Progress</div>
    <div class="sidebar-nav-item">⚙️&nbsp; Settings</div>
    """, unsafe_allow_html=True)

    st.markdown('<hr class="sidebar-divider">', unsafe_allow_html=True)

    # User profile block
    st.markdown("""
    <div style="padding:12px 14px; background:#0d1220; border-radius:10px;
                border:1px solid #1e2a40; display:flex; align-items:center; gap:10px;">
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


# ══════════════════════════════════════════════════════════════════════════════
# HERO / WELCOME
# ══════════════════════════════════════════════════════════════════════════════
st.markdown('<div class="hero-badge">✦ Your AI-Powered Productivity Suite</div>', unsafe_allow_html=True)

st.markdown("""
<h1 class="hero-title">
    Build habits that<br><span>compound over time.</span>
</h1>
<p class="hero-sub">
    AI Momentum blends intelligent coaching, goal tracking, and daily reflection
    to help you grow — one focused day at a time.
</p>
""", unsafe_allow_html=True)

st.markdown('<hr class="hero-divider">', unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# STATS ROW
# ══════════════════════════════════════════════════════════════════════════════
c1, c2, c3, c4 = st.columns(4)
stats = [
    ("12", "Day Streak 🔥"),
    ("3 / 5", "Goals Active"),
    ("84%", "Task Rate"),
    ("26 min", "Avg Focus"),
]
for col, (num, label) in zip([c1, c2, c3, c4], stats):
    with col:
        st.markdown(f"""
        <div class="stat-box">
            <div class="stat-number">{num}</div>
            <div class="stat-label">{label}</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# FEATURE CARDS
# ══════════════════════════════════════════════════════════════════════════════
st.markdown("""
<div class="section-heading">Core Features</div>
<div class="section-sub">Everything you need to build unstoppable momentum.</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3, gap="medium")

with col1:
    st.markdown("""
    <div class="feature-card card-blue">
        <div class="card-icon">🤖</div>
        <div class="card-title">AI Daily Coach</div>
        <div class="card-desc">
            Get a personalized briefing every morning — your coach reviews 
            yesterday's wins, adapts your plan, and keeps you on the optimal 
            path toward your goals.
        </div>
        <span class="card-tag tag-blue">Smart Coaching</span>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card card-purple">
        <div class="card-icon">🎯</div>
        <div class="card-title">Goal Architect</div>
        <div class="card-desc">
            Break down ambitious goals into weekly milestones and daily 
            micro-actions. The AI automatically reprioritizes your roadmap 
            as your life changes.
        </div>
        <span class="card-tag tag-purple">Deep Focus</span>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature-card card-teal">
        <div class="card-icon">📈</div>
        <div class="card-title">Progress Insights</div>
        <div class="card-desc">
            Visual dashboards surface patterns in your behavior — showing 
            exactly when you're most productive and where your energy is 
            being lost each week.
        </div>
        <span class="card-tag tag-teal">Analytics</span>
    </div>
    """, unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# CTA
# ══════════════════════════════════════════════════════════════════════════════
st.markdown("""
<a class="cta-btn" href="#">
    🚀 &nbsp;Start Today's Session
</a>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# FOOTER
# ══════════════════════════════════════════════════════════════════════════════
st.markdown("""
<div class="footer">
    ⚡ AI Momentum &nbsp;·&nbsp; Built with Streamlit &nbsp;·&nbsp; 2025
</div>
""", unsafe_allow_html=True)

