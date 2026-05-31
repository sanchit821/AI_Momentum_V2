import streamlit as st
import pandas as pd
from datetime import datetime
import json
import os

st.set_page_config(page_title="AI Momentum Dashboard", layout="wide")

st.markdown("""
# ⚡ AI Momentum Dashboard

Track habits. Build momentum. Improve daily.
""")

st.info(
    "🚀 Focus on consistency, not perfection."
)

# Load habits safely
habits = st.session_state.get("habits", [])
# Load moods
moods = []

if os.path.exists("data/mood.json"):
    with open("data/mood.json", "r") as f:
        moods = json.load(f)
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
# 😊 Average Mood
# =========================

mood_values = {
    "Great 😊": 5,
    "Good 🙂": 4,
    "Neutral 😐": 3,
    "Bad 😕": 2,
    "Terrible 😣": 1
}

average_mood = 0

if moods:

    scores = []

    for entry in moods:

        mood_name = entry.get("mood")

        if mood_name in mood_values:
            scores.append(
                mood_values[mood_name]
            )

    if scores:
        average_mood = round(
            sum(scores) / len(scores),
            1
        )

# =========================
# ⚡ Productivity Score
# =========================

productivity_score = round(
    (completion_percent * 0.7) +
    ((average_mood / 5) * 100 * 0.3)
)

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

# Current Streak
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
# 🏆 Most Consistent Habit
# =========================

most_consistent_habit = "No habits yet"
most_completions = 0

for habit in habits:

    history = habit.get("history", [])

    completed_count = 0

    for entry in history:

        if (
            isinstance(entry, dict)
            and entry.get("completed")
        ):
            completed_count += 1

    if completed_count > most_completions:

        most_completions = completed_count
        most_consistent_habit = habit.get(
            "name",
            "Unknown"
        )


# =========================
# 🏆 Habit Leaderboard
# =========================

habit_rankings = []

for habit in habits:

    history = habit.get("history", [])

    completed_count = 0

    for entry in history:

        if (
            isinstance(entry, dict)
            and entry.get("completed")
        ):
            completed_count += 1

    habit_rankings.append(
        (
            habit.get("name", "Unknown"),
            completed_count
        )
    )

habit_rankings.sort(
    key=lambda x: x[1],
    reverse=True
)


# =========================
# 📊 Last 7 Days Analytics
# =========================

st.divider()

st.subheader("📊 Last 7 Days Analytics")

from datetime import timedelta

last_7_days = {}

for i in range(7):

    day = (
        datetime.now().date()
        - timedelta(days=i)
    ).strftime("%Y-%m-%d")

    last_7_days[day] = 0

for habit in habits:

    history = habit.get("history", [])

    for entry in history:

        if (
            isinstance(entry, dict)
            and entry.get("completed")
        ):

            date = entry.get("date")

            if date in last_7_days:
                last_7_days[date] += 1

                total_last_7_days = sum(
    last_7_days.values()
)

average_per_day = round(
    total_last_7_days / 7,
    1
)

best_day = max(
    last_7_days,
    key=last_7_days.get
)

lowest_day = min(
    last_7_days,
    key=last_7_days.get
)


col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "✅ Total",
        total_last_7_days
    )

with col2:
    st.metric(
        "📈 Avg / Day",
        average_per_day
    )

with col3:
    st.metric(
        "🏆 Best Day",
        best_day
    )

with col4:
    st.metric(
        "📉 Lowest Day",
        lowest_day
    )


    analytics_df = pd.DataFrame(
    list(last_7_days.items()),
    columns=[
        "Date",
        "Completions"
    ]
)

analytics_df = analytics_df.sort_values(
    "Date"
)

st.bar_chart(
    analytics_df.set_index("Date")
)



# =========================

# 🏆 Habit Analytics Display

# =========================
st.divider()
st.subheader("🏆 Habit Analytics")

st.info(
    f"Most Consistent Habit: "
    f"{most_consistent_habit} "
    f"({most_completions} completions)"
)

st.write("### 🏆 Top Habits")

medals = ["🥇", "🥈", "🥉"]

for i, habit_data in enumerate(habit_rankings[:3]):

    habit_name = habit_data[0]
    completions = habit_data[1]

    st.write(
        f"{medals[i]} {habit_name} — {completions} completions"
    ) 

# Longest Streak
longest_streak = 0

if date_objects:

    current_streak = 1
    longest_streak = 1

    for i in range(1, len(date_objects)):

        if (
            date_objects[i] -
            date_objects[i - 1]
        ).days == 1:

            current_streak += 1

            if current_streak > longest_streak:
                longest_streak = current_streak

        else:
            current_streak = 1

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

col1, col2, col3, col4, col5, col6 = st.columns(6)

with col1:
    st.metric("📌 Total Habits", total_habits)

with col2:
    st.metric("✅ Completed Today", completed_habits)

with col3:
    st.metric("🔥 Streak", streak)

with col4:
    st.metric("⚡ Momentum Score", momentum_score)

with col5:
    st.metric("🏆 Longest Streak", longest_streak)

with col6:
    st.metric(
        "⚡ Productivity",
        f"{productivity_score}%"
    )

st.divider()

# =========================
# Progress Section
# =========================

st.subheader("📈 Today's Progress")

st.progress(completion_percent / 100)

st.write(f"### {completion_percent}% Completed")

# =========================
# 🤖 Smart Insights
# =========================

st.divider()

st.subheader("🤖 Smart Insights")

if total_habits == 0:

    st.warning(
        "Add habits to start building momentum."
    )

else:

    # Completion Insight
    if completion_percent == 100:
        st.success(
            "🔥 Perfect day. Every habit is completed."
        )

    elif completion_percent >= 75:
        st.info(
            "💪 Strong progress today. Keep the momentum going."
        )

    elif completion_percent >= 50:
        st.info(
            "📈 You're halfway there. One more habit can change the day."
        )

    else:
        st.warning(
            "⚠️ Momentum is low today. Start with your easiest habit."
        )

    # Consistency Insight
    if consistency_rate >= 80:
        st.success(
            "🏆 Your consistency is excellent."
        )

    elif consistency_rate >= 60:
        st.info(
            "📊 Your consistency is improving steadily."
        )

    else:
        st.warning(
            "📉 Consistency needs attention. Focus on showing up daily."
        )

    # Streak Insight
    if streak >= 7:
        st.success(
            f"🔥 You are on a {streak}-day streak. Protect it."
        )

    elif streak >= 3:
        st.info(
            f"🔥 Nice work. Current streak: {streak} days."
        )

    else:
        st.info(
            "🌱 Build a streak by completing habits every day."
        )

    # Longest Streak Insight
    if longest_streak >= 10:
        st.success(
            f"🏅 Longest streak: {longest_streak} days. Great discipline."
        )

    elif longest_streak >= 5:
        st.info(
            f"🏅 Longest streak: {longest_streak} days."
        )

    # -------------------------------------------------------------------------------------------------------------

    # =========================
# 📊 Weekly Analytics
# =========================

st.divider()

st.subheader("📊 Habit Completion History")

completion_data = {}

for habit in habits:

    history = habit.get("history", [])

    for entry in history:

        if (
            isinstance(entry, dict)
            and entry.get("completed")
        ):

            date = entry.get("date")

            if date in completion_data:
                completion_data[date] += 1
            else:
                completion_data[date] = 1

if completion_data:

    df = pd.DataFrame(
        list(completion_data.items()),
        columns=["Date", "Completed Habits"]
    )

    df = df.sort_values("Date")

    st.bar_chart(
        df.set_index("Date")
    )

else:
    st.info("No completion history available yet.")
