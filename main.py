import streamlit as st

st.title("🛌 Insomnia Severity Index Calculator")

st.markdown("""
This tool helps you assess the severity of insomnia symptoms based on the **Insomnia Severity Index (ISI)**.
Each question is scored from 0 (no problem) to 4 (very severe problem).
""")

questions = [
    "1. Difficulty falling asleep",
    "2. Difficulty staying asleep",
    "3. Problems waking up too early",
    "4. Satisfaction with current sleep pattern",
    "5. Interference of sleep problems with daily functioning",
    "6. Noticeability of sleep problems to others",
    "7. Worry/distress caused by sleep problems"
]

scores = []
for q in questions:
    score = st.slider(q, 0, 4, 0)
    scores.append(score)

total_score = sum(scores)

st.subheader(f"🧮 Total ISI Score: {total_score}")

# Severity interpretation
if total_score <= 7:
    severity = "No clinically significant insomnia"
elif 8 <= total_score <= 14:
    severity = "Subthreshold insomnia"
elif 15 <= total_score <= 21:
    severity = "Moderate severity insomnia"
else:
    severity = "Severe insomnia"

st.markdown(f"**🩺 Severity Level:** {severity}")

st.markdown("---")
st.caption("This tool is for educational purposes and not a substitute for professional medical advice.")
