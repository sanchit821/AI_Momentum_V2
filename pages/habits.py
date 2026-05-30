import streamlit as st
import json
import os
from datetime import datetime

st.set_page_config(page_title="Habits", layout="wide")

DATA_FILE = "data/habits.json"


# Load habits
def load_habits():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []


# Save habits
def save_habits(habits):
    with open(DATA_FILE, "w") as f:
        json.dump(habits, f, indent=4)


# Initialize session state
if "habits" not in st.session_state:
    st.session_state.habits = load_habits()


st.title("📌 Daily Habit Tracker")


# Add new habit
new_habit = st.text_input("Add a new habit")

if st.button("Add Habit"):
    if new_habit.strip():

        habit_data = {
            "name": new_habit,
            "history": []
        }

        st.session_state.habits.append(habit_data)
        save_habits(st.session_state.habits)

        st.success(f"Added: {new_habit}")

    else:
        st.warning("Please enter a habit")


st.divider()

st.write("### Today's Habits")

if len(st.session_state.habits) == 0:
    st.info("No habits added yet")

else:

    today = datetime.now().strftime("%Y-%m-%d")

    for i, habit in enumerate(st.session_state.habits):

        col1, col2, col3 = st.columns([5, 2, 1])

        with col1:
            st.write(f"**{habit['name']}**")

        with col2:

            history = habit.get("history", [])

            today_entry = None

            for entry in history:
                if isinstance(entry, dict):
                    if entry.get("date") == today:
                        today_entry = entry
                        break

            initial_value = False

            if today_entry:
                initial_value = today_entry.get("completed", False)

            completed = st.checkbox(
                "Completed Today",
                value=initial_value,
                key=f"habit_{i}"
            )

            if today_entry:
                today_entry["completed"] = completed

            else:
                history.append({
                    "date": today,
                    "completed": completed
                })

            habit["history"] = history

            save_habits(st.session_state.habits)

        with col3:
            if st.button("❌", key=f"delete_{i}"):

                st.session_state.habits.pop(i)

                save_habits(st.session_state.habits)

                st.rerun()