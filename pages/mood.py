import streamlit as st
import pandas as pd
import json
import os
from datetime import datetime

st.set_page_config(page_title="Mood Tracker", layout="wide")
DATA_FILE = "data/mood.json"


def load_moods():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []


def save_moods(moods):
    with open(DATA_FILE, "w") as f:
        json.dump(moods, f, indent=4)

st.title("😊 Mood Tracker")

if "mood_log" not in st.session_state:
    st.session_state.mood_log = load_moods()

mood = st.selectbox("How are you feeling today?", ["Great 😊", "Good 🙂", "Neutral 😐", "Bad 😕", "Terrible 😣"])

if st.button("Save Mood"):
    from datetime import datetime

today = datetime.now().strftime("%Y-%m-%d")

existing_entry = None

for entry in st.session_state.mood_log:

    if entry["date"] == today:
        existing_entry = entry
        break

if existing_entry:

    existing_entry["mood"] = mood

else:

    st.session_state.mood_log.append({
        "mood": mood,
        "date": today
    })

save_moods(st.session_state.mood_log)

st.success("Mood saved!")
save_moods(st.session_state.mood_log)

st.divider()



# =========================
# 😊 Mood Analytics
# =========================

if len(st.session_state.mood_log) > 0:

    mood_values = {
        "Great 😊": 5,
        "Good 🙂": 4,
        "Neutral 😐": 3,
        "Bad 😕": 2,
        "Terrible 😣": 1
    }

    scores = [
        mood_values[entry["mood"]]
        for entry in st.session_state.mood_log
    ]

    average_mood = round(
        sum(scores) / len(scores),
        1
    )

    st.metric(
        "😊 Average Mood",
        f"{average_mood}/5"
    )
st.write("### Mood Trend")
# =========================
# 📈 Mood Trend Analysis
# =========================

if len(st.session_state.mood_log) >= 2:

    latest_mood = mood_values[
        st.session_state.mood_log[-1]["mood"]
    ]

    previous_mood = mood_values[
        st.session_state.mood_log[-2]["mood"]
    ]

    if latest_mood > previous_mood:

        st.success(
            "📈 Your mood is improving."
        )

    elif latest_mood < previous_mood:

        st.warning(
            "📉 Your mood is declining."
        )

    else:

        st.info(
            "➖ Your mood is stable."
        )



if len(st.session_state.mood_log) > 0:

    mood_values = {

        "Great 😊": 5,

        "Good 🙂": 4,

        "Neutral 😐": 3,

        "Bad 😕": 2,

        "Terrible 😣": 1

    }

    values = [mood_values[e["mood"]] for e in st.session_state.mood_log]

    dates = [e["date"] for e in st.session_state.mood_log]

    df = pd.DataFrame({

        "Date": dates,

        "Mood": values

    })

    st.line_chart(df.set_index("Date"))

else:

    st.info("No data yet")