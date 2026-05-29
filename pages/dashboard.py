import streamlit as st
from datetime import datetime, timedelta

st.set_page_config(page_title="AI Momentum Dashboard", layout="wide")

st.title("⚡ AI Momentum Dashboard")

# Load habits safely
habits = st.session_state.get("habits", [])

# Basic stats
total_habits = len(habits)

completed_habits = sum(
    1 for habit in habits if habit["completed"]
)

# Completion percentage
if total_habits > 0:
    completion_percent = int(
        (completed_habits / total_habits) * 100
    )
else:
    completion_percent = 0

# =========================
# 🔥 STREAK LOGIC
# =========================

today = datetime.now().strftime("%Y-%m-%d")

completed_today = any(
    habit["completed"] and habit["date"] == today
    for habit in habits
)

if completed_today:
    streak = 1
else:
    streak = 0

# =========================
# Momentum score
# =========================

momentum_score = (
    completion_percent +
    (streak * 10)
)

# Dashboard cards
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("📌 Total Habits", total_habits)

with col2:
    st.metric("✅ Completed Today", completed_habits)

with col3:
    st.metric("🔥 Streak", streak)

with col4:
    st.metric("⚡ Momentum Score", momentum_score)

st.divider()

# Progress section
st.write("## Today's Progress")

st.progress(completion_percent / 100)

st.write(f"### {completion_percent}% Completed")

# Insights
st.divider()

st.write("## Insights")

if total_habits == 0:
    st.warning("Add habits to start tracking momentum.")

elif completion_percent == 100:
    st.success("Excellent consistency today 🔥")

elif completion_percent >= 60:
    st.info("Good progress. Keep pushing.")

else:
    st.warning("Momentum is low today. Complete small tasks first.")