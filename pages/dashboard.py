import streamlit as st

st.set_page_config(page_title="AI Momentum Dashboard", layout="wide")

st.title("⚡ AI Momentum Dashboard")

# Get data safely
habits = st.session_state.get("habits", [])
moods = st.session_state.get("mood_log", [])

# Basic calculations
habit_count = len(habits)

mood_score = 0
for m in moods:
    if "Great" in m:
        mood_score += 5
    elif "Good" in m:
        mood_score += 4
    elif "Neutral" in m:
        mood_score += 3
    elif "Bad" in m:
        mood_score += 2
    else:
        mood_score += 1

avg_mood = mood_score / len(moods) if moods else 0

momentum_score = (habit_count * 10) + (avg_mood * 10)

# UI
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Habits", habit_count)

with col2:
    st.metric("Mood Entries", len(moods))

with col3:
    st.metric("Momentum Score", round(momentum_score, 1))

st.divider()

st.write("### Insights")

if habit_count == 0:
    st.warning("Start adding habits to build momentum.")
elif habit_count < 3:
    st.info("You are building consistency. Keep going.")
else:
    st.success("Strong habit base forming. Good momentum.")

if len(moods) == 0:
    st.info("Track your mood daily to improve accuracy.")