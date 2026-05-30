import streamlit as st
from datetime import datetime

st.set_page_config(page_title="AI Momentum Dashboard", layout="wide")

st.title("⚡ AI Momentum Dashboard")

# Load habits safely
habits = st.session_state.get("habits", [])

# Today's date
today = datetime.now().strftime("%Y-%m-%d")

# Basic stats
total_habits = len(habits)

completed_habits = 0

# Count today's completed habits
for habit in habits:
    history = habit.get("history", [])

    for entry in history:
        if isinstance(entry, dict):
            if (
                entry.get("date") == today
                and entry.get("completed")
            ):
                completed_habits += 1

# Completion percentage
if total_habits > 0:
    completion_percent = int(
        (completed_habits / total_habits) * 100
    )
else:
    completion_percent = 0

# =========================
# 🔥 Streak v2
# =========================

# =========================
# 🔥 REAL STREAK CALCULATION
# =========================

completed_dates = set()

for habit in habits:
    history = habit.get("history", [])

    for entry in history:

        if (
            isinstance(entry, dict)
            and entry.get("completed")
        ):
            completed_dates.add(entry.get("date"))

# Convert strings to date objects
date_objects = sorted(
    datetime.strptime(d, "%Y-%m-%d").date()
    for d in completed_dates
)

streak = 0

if date_objects:

    streak = 1

    for i in range(
        len(date_objects) - 1,
        0,
        -1
    ):

        current_day = date_objects[i]
        previous_day = date_objects[i - 1]

        if (current_day - previous_day).days == 1:
            streak += 1
        else:
            break

# =========================
# 📊 Consistency Analytics
# =========================

total_history_entries = 0
completed_history_entries = 0

for habit in habits:
    history = habit.get("history", [])

    for entry in history:
        if isinstance(entry, dict):

            total_history_entries += 1

            if entry.get("completed"):
                completed_history_entries += 1

if total_history_entries > 0:
    consistency_rate = int(
        (completed_history_entries / total_history_entries) * 100
    )
else:
    consistency_rate = 0

# =========================
# ⚡ Momentum Score
# =========================

momentum_score = (
    completion_percent +
    (streak * 10)
)

# =========================
# Dashboard Cards
# =========================

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric("📌 Total Habits", total_habits)

with col2:
    st.metric("✅ Completed Today", completed_habits)

with col3:
    st.metric("🔥 Streak", streak)

with col4:
    st.metric("⚡ Momentum Score", momentum_score)

with col5:
    st.metric("📊 Consistency", f"{consistency_rate}%")

st.divider()

# =========================
# Progress Section
# =========================

st.write("## Today's Progress")

st.progress(completion_percent / 100)

st.write(f"### {completion_percent}% Completed")

st.divider()

# =========================
# Insights
# =========================

st.write("## Insights")

if total_habits == 0:
    st.warning("Add habits to start tracking momentum.")

elif completion_percent == 100:
    st.success("Excellent consistency today 🔥")

elif completion_percent >= 60:
    st.info("Good progress. Keep pushing.")

else:
    st.warning("Momentum is low today. Complete small tasks first.")