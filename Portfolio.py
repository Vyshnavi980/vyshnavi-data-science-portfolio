import streamlit as st

# --- Page Config ---
st.set_page_config(page_title="Vyshnavi MR | Data Scientist", page_icon="📊", layout="wide")

# --- Sidebar Navigation ---
st.sidebar.title("📂 Navigation")
selected_section = st.sidebar.radio("Go to", [
    "👋 Home",
    "⚙️ Skills",
    "💼 Work Experience",
    "📂 Projects",
    "🎯 Accomplishments",
    "🏆 Awards",
    "✍️ Writing",
    "📬 Contact"
])
# --- Home ---
if selected_section == "👋 Home":
    st.markdown("### 👋 Hi, I'm Vyshnavi MR")
    st.markdown("#### Data Scientist | GenAI Explorer | Forecasting Enthusiast")

    # --- Profile Summary ---
    with st.container():

        # Add image to col1
        # with col1:
        #     st.image("https://imgur.com/a/VpUoq47", caption="Vyshnavi MR", use_container_width=True)  # Use the new parameter

        # Add text to col2
         with st.container():
            st.markdown("""
🎯 I’m a data scientist with **1.8 years of industry experience** in building scalable ML systems, enhancing forecasting accuracy, and exploring the frontiers of **Generative AI**.  
I’ve contributed to **supply chain optimization**, **video analytics** * projects at **Lululemon**, with a proven track record of boosting model reliability and performance.  
Passionate about translating data into impact, I thrive on solving business problems through innovation and thoughtful storytelling.
""")
            st.markdown("""
Welcome to my interactive resume!  
Use the **sidebar on the left** to explore my skills, projects, and accomplishments.
""")
            st.success("⬅️ Click on a section in the sidebar to get started!")

    st.markdown("---")




# --- Skills ---
elif selected_section == "⚙️ Skills":
    st.markdown("### ⚙️ Skills")

    st.markdown("#### 💻 Programming Languages")
    st.markdown("""
    - **Python**   
    - **SQL** 
    """)

    st.markdown("#### 🧠 Machine Learning & AI")
    st.markdown("""
    - **Regression**  
    - **Classification**  
    - **Model Evaluation**  
    - **Model Retraining**  
    - **Generative AI** (Prompt Engineering, LLMs)
    """)

    st.markdown("#### 📦 Data Science Tools")
    st.markdown("""
    - **Pandas**  
    - **NumPy**  
    - **Matplotlib**  
    - **Streamlit**  
    - **GenAI**
    """)

    st.markdown("#### 📊 Techniques")
    st.markdown("""
    - **Predictive Analytics**  
    - **Demand Forecasting**  
    - **Time Series Analysis**  
    - **Exploratory Data Analysis (EDA)**  
    - **Data Cleaning**  
    - **Hypothesis Testing**  
    - **A/B Testing**
    """)

    st.markdown("#### 🛠️ Tools & Platforms")
    st.markdown("""
    - **Databricks**  
    - **Snowflake**  
    - **JupyterHub**  
    - **AWS SageMaker**  
    - **AWS Bedrock**
    """)

    st.markdown("#### 🧩 Soft Skills")
    st.markdown("""
    - **Leadership**  
    - **Communication**  
    - **Problem-Solving**  
    - **Presentation**  
    - **Teamwork**  
    - **Collaboration**
    """)

    st.markdown("---")

# --- Work Experience ---
elif selected_section == "💼 Work Experience":
    st.markdown("### 💼 Work Experience")

    st.markdown("#### 🔹 Data Scientist | Lululemon, Bangalore")
    st.markdown("_Aug 2023 – Present_")
    st.markdown("""
- 📈 Improved forecasting accuracy by **10%**, enhancing inventory management efficiency  
- 🏭 Conducted impact analysis of new **distribution center (DC) launches**, improving supply chain optimization by 20%  
- 🛠️ Resolved model anomalies and stakeholder queries, enhancing model reliability and trust  
    """)

    st.markdown("#### 🔹 Junior Data Scientist | Lululemon, Bangalore")
    st.markdown("_May 2024 – Present_")
    st.markdown("""
- 🔁 Led model retraining efforts, boosting performance by **18%**  
- 📊 Analyzed production vs. retrained model outputs, improving precision by **12%**  
    """)
    st.markdown("---")

# --- Projects ---
elif selected_section == "📂 Projects":
    st.markdown("### 📂 Projects")

    with st.container():
        col1, col2 = st.columns([1, 2])
        with col1:
            st.image("https://d1.awsstatic.com/getting-started-guides/dev-center/gen-ai/Generative%20AI%20Banner%20circle%20-square.7c8271a36398a1c9a170c747588fba67f731aa21.png", width=100)
        with col2:
            st.markdown("#### 👗 Generative AI-Based Design Generation")
            st.markdown("""
- 🧵 Created a POC using GenAI to generate apparel designs for Lululemon  
- ✨ Combined prompt engineering with image generation workflows  
            """)

    with st.container():
        col1, col2 = st.columns([1, 2])
        with col1:
            st.image("https://spng.pngfind.com/pngs/s/114-1140409_cvlogoforportal-computer-vision-hd-png-download.png", width=100)
        with col2:
            st.markdown("#### 🎥 Video Analytics POC (Under Lululemon CTO)")
            st.markdown("""
- 🚀 Developed vision pipeline to analyze in-store footage  
- 🔍 Focused on store traffic and alert generation  
- 💡 Delivered actionable insights from video data streams  
            """)

    with st.container():
        col1, col2 = st.columns([1, 2])
        with col1:
            st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Time_Series_Analysis.png/800px-Time_Series_Analysis.png", width=100)
        with col2:
            st.markdown("#### 📦 Forecasting Optimization for Supply Chain")
            st.markdown("""
- 📉 Designed retraining pipelines to enhance forecasting accuracy  
- 🧠 Evaluated models by product class and region to ensure robustness  
- 📊 Enabled better planning on model promotions by aligning model outputs  
            """)
    st.markdown("---")

# --- Accomplishments ---
elif selected_section == "🎯 Accomplishments":
    st.markdown("### 🎯 Accomplishments")
    st.image("https://media.licdn.com/dms/image/v2/C5612AQGcjk6BelHZ2w/article-cover_image-shrink_720_1280/article-cover_image-shrink_720_1280/0/1613318203099?e=2147483647&v=beta&t=BKxkdNw0kUNB93x_ZXRrGY5JVAvjknMctTo6WG25-Ps", width=200)
    st.markdown("""
**Hackathon Highlight**  
- Led and presented a **GenAI-based POC** at the **Lululemon Global Hackathon 2024**  
- Developed **Vox Compendium** - a GenAI-powered review summarizer that transforms thousands of customer reviews into clear, concise product insights  
- Enables faster and more informed shopping decisions by surfacing common sentiments and feature highlights instantly  
    """)
    st.markdown("---")

# --- Awards ---
elif selected_section == "🏆 Awards":
    st.markdown("### 🏆 Awards & Recognition")
    st.markdown("""
- 🏅 **Thought Leadership** by CTO of Lululemon (2024)  
- 🌟 **Stood-Out From Crowd Award** – FacePrep (2019)  
- 🏆 **Student of the Year** (2017)
    """)
    st.markdown("---")

# --- Writing ---
elif selected_section == "✍️ Writing":
    st.markdown("### ✍️ Writing")
    st.markdown("🔗 [Building Responsible and Ethical AI with LLMs](https://medium.com/@vyshnavimr123/building-responsible-and-ethical-ai-with-large-language-models-llms-6c23f755d969)")
    st.markdown("---")

# --- Contact ---
elif selected_section == "📬 Contact":
    st.markdown("### 📬 Contact")
    st.markdown("- 📧 Email: vyshnavimr03@gmail.com")
    st.markdown("- 💼 LinkedIn Profile: [LinkedIn](https://www.linkedin.com/in/vyshnavi-m-r-0979921a3/)")
    st.markdown("✨ Let's build something exciting together – open to collaborations, innovative ideas, and meaningful connections!")
