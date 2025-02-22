from io import BytesIO
import os
import pandas as pd
import streamlit as st
import random
import datetime

st.set_page_config(
    page_title="Growth Mindset Challenge",  # Title shown in the browser tab
    page_icon="💡",  # Favicon icon (you can use emoji or a URL to an image)
    layout="wide"  # "centered" or "wide" for better layout control
)

# Initialize session state
if 'journal_entries' not in st.session_state:
    st.session_state.journal_entries = []
if 'progress' not in st.session_state:
    st.session_state.progress = 0
if 'goal' not in st.session_state:
    st.session_state.goal = ""
if 'quiz_score' not in st.session_state:
    st.session_state.quiz_score = 0
if 'quiz_attempted' not in st.session_state:
    st.session_state.quiz_attempted = 0

# Sidebar Navigation
st.sidebar.title("🌱 Growth Mindset Challenge")
page = st.sidebar.radio("Navigate", ["Home", "Daily Challenge", "Quiz", "Motivational Stories", "Reflection Journal", "Progress Tracking", "Goal Setting"])

# Home Page
if page == "Home":
    st.title("🌟 Welcome to the Growth Mindset Challenge! 🌟")
    st.markdown(
        """
        ### This app helps you develop a growth mindset with:
        - ✅ **Daily challenges** to push your limits.
        - ✅ **Interactive quizzes** to reinforce learning.
        - ✅ **Motivational stories** to keep you inspired.
        - ✅ **Reflection journaling** to track your progress.
        - ✅ **Goal setting and tracking** for personal development.
        """
    )
    st.markdown("### 🚀 Start your journey to a better mindset today!")

# Daily Challenge
elif page == "Daily Challenge":
    challenges = [
        "Write down three things you learned today.",
        "Take on a difficult task and embrace the struggle.",
        "Turn a mistake into a learning opportunity.",
        "Teach someone else a skill you’ve recently learned.",
        "Try a new way of solving a problem you faced before.",
        "Reflect on a recent failure and write down how it helped you grow.",
        "Step outside your comfort zone and try something new."
    ]
    st.title("🚀 Your Daily Challenge")
    st.subheader(random.choice(challenges))
    st.write("💡 Tip: Growth happens when you embrace challenges!")

# Quiz
# Quiz
elif page == "Quiz":
    st.title("🧠 Growth Mindset Quiz")

    questions = {
        "What does a growth mindset encourage?": ["Belief in fixed intelligence", "Effort and learning", "Avoiding challenges"],
        "How do you react to failure with a growth mindset?": ["Give up", "Use it as a learning experience", "Blame others"],
        "Which is an example of a growth mindset?": ["I’m just not good at math", "If I work hard, I can improve", "Some people are born talented"],
        "What should you do when facing a difficult problem?": ["Give up", "Try a different approach", "Ignore it"]
    }

    user_answers = {}
    
    for question, options in questions.items():
        user_answers[question] = st.radio(question, options, index=None)  # No pre-selected option

    if st.button("Submit Quiz"):
        score = sum(1 for q, a in user_answers.items() if a == questions[q][1])  # Check correct answers
        st.session_state.quiz_score = score
        st.session_state.quiz_attempted += 1

        st.write(f"### 🎯 Your Score: {score}/{len(questions)}")

        if score == 4:
            st.success("🎉 Outstanding! You got all answers correct! Keep up the great work! 🚀")
            st.balloons()
        elif score == 3:
            st.info("🌟 Great job! You scored 3/4. You're doing amazing!")
        elif score == 2:
            st.warning("👍 Good effort! You scored 2/4. Keep practicing and improving!")
        elif score == 1:
            st.warning("🌱 You scored 1/4. Growth takes time—don't give up!")
        else:
            st.error("😅 You scored 0/4. No worries, keep learning and try again!")

        # Show correct answers
        st.write("### ✅ Correct Answers:")
        for question, options in questions.items():
            st.write(f"**{question}**")
            st.write(f"✔ Correct Answer: **{options[1]}**")


# Motivational Stories
elif page == "Motivational Stories":
    st.title("📖 Motivational Stories")
    stories = [
        "Thomas Edison failed 1,000 times before inventing the light bulb!",
        "Michael Jordan was cut from his high school basketball team but became a legend.",
        "J.K. Rowling faced multiple rejections before publishing Harry Potter.",
        "Oprah Winfrey was fired from her first TV job but became a media mogul.",
        "Albert Einstein was considered a slow learner in school but changed the world of physics."
    ]
    st.write(random.choice(stories))
    st.write("🌟 Remember: Success comes from perseverance and learning from failure!")

# Reflection Journal
elif page == "Reflection Journal":
    st.title("📝 Reflection Journal")
    entry = st.text_area("Write about your learning experience today:")
    if st.button("Save Entry"):
        st.session_state.journal_entries.append(f"{datetime.date.today()}: {entry}")
        st.success("Your reflection has been saved!")
    st.write("### Previous Entries")
    for entry in st.session_state.journal_entries:
        st.write(entry)

# Progress Tracking
elif page == "Progress Tracking":
    st.title("📊 Progress Tracking")
    st.session_state.progress = st.slider("How much have you improved this week?", 0, 100, st.session_state.progress)
    st.write(f"### Your current progress: {st.session_state.progress}%")
    st.write("🌟 Keep going! Every step forward is growth.")

# Goal Setting
elif page == "Goal Setting":
    st.title("🎯 Goal Setting")
    st.session_state.goal = st.text_input("Set your growth goal:", st.session_state.goal)
    if st.button("Save Goal"):
        st.success("Goal saved successfully!")
    st.write(f"### Your Goal: {st.session_state.goal}")
    st.write("💪 Stay committed and take small steps every day!")

   