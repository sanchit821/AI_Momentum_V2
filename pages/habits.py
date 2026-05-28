import streamlit as st
import json
import os

st.set_page_config(page_title="Habits", layout="wide")

DATA_FILE = "data/habits.json"

# Load habits from file
def load_habits():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []

# Save habits to file
def save_habits(habits):
    with open(DATA_FILE, "w") as f:
        json.dump(habits, f)

# Initialize
if "habits" not in st.session_state:
    st.session_state.habits = load_habits()

st.title("📌 Habit Tracker (Saved)")

new_habit = st.text_input("Add a new habit")

if st.button("Add Habit"):
    if new_habit.strip() != "":
        st.session_state.habits.append(new_habit)
        save_habits(st.session_state.habits)
        st.success(f"Added: {new_habit}")
    else:
        st.warning("Please enter a habit")

st.divider()

st.write("### Your Habits")

if len(st.session_state.habits) == 0:
    st.info("No habits added yet")
else:
    for i, habit in enumerate(st.session_state.habits):
        col1, col2 = st.columns([4, 1])

        with col1:
            st.write(f"{i+1}. {habit}")

        with col2:
            if st.button("❌", key=f"del_{i}"):
                st.session_state.habits.pop(i)
                save_habits(st.session_state.habits)
                st.rerun()