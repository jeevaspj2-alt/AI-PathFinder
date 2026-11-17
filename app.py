import streamlit as st

st.set_page_config(
    page_title="AI Pathfinder"
)

universities = {
    "Germany": [
        {
            "name": "Saarland University",
            "program": "M.Sc. Data Science and Artificial Intelligence",
            "cost": "No study fees",
            "language": "English",
            "focus": "AI, Machine Learning, Data Science"
        },
        {
            "name": "Technical University of Darmstadt",
            "program": "M.Sc. Artificial Intelligence and Machine Learning",
            "cost": "No tuition fees",
            "language": "English",
            "focus": "Artificial Intelligence and Machine Learning"
        },
        {
            "name": "Technical University of Munich",
            "program": "M.Sc. Data Engineering and Analytics",
            "cost": "Tuition fees for non-EU students",
            "language": "English",
            "focus": "Data Science, AI and Data Engineering"
        }
    ]
}

roadmaps = {
    "Artificial Intelligence & Machine Learning": [
        "Python fundamentals",
        "Mathematics and Statistics",
        "NumPy and Pandas",
        "Machine Learning",
        "Deep Learning",
        "AI Projects",
        "Research and Internships"
    ],
    "Data Science": [
        "Python",
        "Statistics",
        "SQL",
        "NumPy and Pandas",
        "Data Visualization",
        "Machine Learning",
        "Data Science Projects"
    ],
    "Software Development": [
        "Programming Fundamentals",
        "Data Structures and Algorithms",
        "Git and GitHub",
        "Web or Application Development",
        "Projects",
        "Internships"
    ],
    "Cybersecurity": [
        "Programming Fundamentals",
        "Computer Networks",
        "Operating Systems",
        "Cybersecurity Fundamentals",
        "Security Tools",
        "Practical Projects",
        "Certifications and Internships"
    ],
    "Business & Management": [
        "Business Fundamentals",
        "Communication Skills",
        "Marketing",
        "Finance Basics",
        "Data Analysis",
        "Leadership",
        "Business Projects"
    ],
    "Design & Creativity": [
        "Design Fundamentals",
        "Creative Thinking",
        "UI/UX Basics",
        "Design Tools",
        "Portfolio Development",
        "Real-world Projects"
    ]
}

st.title("AI Pathfinder")
st.write("Find the path that fits you and build your future.")

st.divider()

st.subheader("Tell us about yourself")

name = st.text_input("Your name")

goal = st.selectbox(
    "What is your main goal?",
    ["Higher Studies", "Career", "Research", "Skill Development"]
)

field = st.selectbox(
    "Which field interests you?",
    [
        "Artificial Intelligence & Machine Learning",
        "Data Science",
        "Software Development",
        "Cybersecurity",
        "Business & Management",
        "Design & Creativity"
    ]
)

country = st.selectbox(
    "Preferred country",
    ["Any Country", "Germany"]
)

budget = st.selectbox(
    "Budget preference",
    ["Low Cost / Scholarship", "Moderate Budget", "Flexible Budget"]
)

if st.button("Find My Path"):

    if not name:
        st.warning("Please enter your name.")

    else:
        st.success(f"Welcome, {name}")

        st.divider()

        st.subheader("Recommended Direction")

        if goal == "Higher Studies":
            st.write(
                f"Based on your goal, {field} is a suitable "
                "direction to explore for higher studies."
            )

        elif goal == "Career":
            st.write(
                f"Your selected career direction is {field}. "
                "Focus on building practical skills and projects."
            )

        elif goal == "Research":
            st.write(
                f"You can explore research opportunities in {field} "
                "by strengthening your fundamentals and research skills."
            )

        else:
            st.write(
                f"Your recommended skill direction is {field}."
            )

        st.divider()

        st.subheader("Roadmap")

        for step in roadmaps[field]:
            st.write(f"→ {step}")

        if goal == "Higher Studies" and country == "Germany":

            st.divider()

            st.subheader("Universities to Explore")

            for university in universities["Germany"]:

                st.write(f"### {university['name']}")
                st.write(f"Program: {university['program']}")
                st.write(f"Focus: {university['focus']}")
                st.write(f"Language: {university['language']}")
                st.write(f"Cost: {university['cost']}")

            st.divider()

            st.subheader("Funding")

            if budget == "Low Cost / Scholarship":
                st.write(
                    "Prioritize universities with low or no tuition "
                    "fees and investigate scholarship opportunities."
                )
            else:
                st.write(
                    "Compare tuition fees, living costs and available "
                    "scholarships before applying."
                )

        st.divider()

        st.subheader("Next Steps")

        st.write("1. Strengthen your foundation in the selected field.")
        st.write("2. Build practical projects.")
        st.write("3. Research university eligibility requirements.")
        st.write("4. Identify suitable scholarships and funding.")
        st.write("5. Prepare your application documents.")