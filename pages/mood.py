import streamlit as st
import pandas as pd

st.set_page_config(page_title="Mood Tracker", layout="wide")

st.title("😊 Mood Tracker")

if "mood_log" not in st.session_state:
    st.session_state.mood_log = []

mood = st.selectbox("How are you feeling today?", ["Great 😊", "Good 🙂", "Neutral 😐", "Bad 😕", "Terrible 😣"])

if st.button("Save Mood"):
    from datetime import datetime

    st.session_state.mood_log.append({
    "mood": mood,
    "date": datetime.now().strftime("%Y-%m-%d")
})
 
    st.success("Mood saved!")

st.divider()

st.write("### Mood Trend")

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