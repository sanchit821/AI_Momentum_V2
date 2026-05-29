# import streamlit as st

# st.set_page_config(page_title="AI Momentum Dashboard", layout="wide")

# st.title("⚡ AI Momentum Dashboard")

# # Get data safely
# habits = st.session_state.get("habits", [])
# moods = st.session_state.get("mood_log", [])

# # Basic calculations
# habit_count = len(habits)

# mood_score = 0
# for m in moods:
#     if "Great" in m:
#         mood_score += 5
#     elif "Good" in m:
#         mood_score += 4
#     elif "Neutral" in m:
#         mood_score += 3
#     elif "Bad" in m:
#         mood_score += 2
#     else:
#         mood_score += 1

# avg_mood = mood_score / len(moods) if moods else 0

# momentum_score = (habit_count * 10) + (avg_mood * 10)

# # UI
# col1, col2, col3 = st.columns(3)

# with col1:
#     st.metric("Habits", habit_count)

# with col2:
#     st.metric("Mood Entries", len(moods))

# with col3:
#     st.metric("Momentum Score", round(momentum_score, 1))

# st.divider()

# st.write("### Insights")

# if habit_count == 0:
#     st.warning("Start adding habits to build momentum.")
# elif habit_count < 3:
#     st.info("You are building consistency. Keep going.")
# else:
#     st.success("Strong habit base forming. Good momentum.")

# if len(moods) == 0:
#     st.info("Track your mood daily to improve accuracy.")







import streamlit as st

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

# Momentum score
momentum_score = (
    completion_percent +
    (completed_habits * 5)
)

# Dashboard cards
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("📌 Total Habits", total_habits)

with col2:
    st.metric("✅ Completed Today", completed_habits)

with col3:
    st.metric("⚡ Momentum Score", momentum_score)

st.divider()

# Progress section
st.write("## Today's Progress")

st.progress(completion_percent / 100)

st.write(f"### {completion_percent}% Completed")

# Insight section
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