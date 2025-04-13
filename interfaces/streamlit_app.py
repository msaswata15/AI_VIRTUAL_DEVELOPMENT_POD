import streamlit as st
from services.agent_orchestration import AgentOrchestrator
from services.language_model_integration import gemini_generate
import re
import datetime

# Set page configuration
st.set_page_config(page_title="AI-powered Virtual Development Pod", layout="wide")

# Define agent roles and responsibilities
AGENT_ROLES = {
    "Business Analyst Agent": "Creates detailed user stories from high-level requirements.",
    "Design Agent": "Generates software design artifacts and flowcharts.",
    "Developer Agent": "Produces production-quality code and folder structure.",
    "Testing Agent": "Generates test cases and test execution results.",
    "Security Analyst Agent": "Performs vulnerability and security analysis.",
    "Optimizer Agent": "Suggests performance optimizations and bottlenecks."
}
# Ensure session state is initialized early
def init_session_state():
    if "conversation_history" not in st.session_state:
        st.session_state.conversation_history = {role: [] for role in AGENT_ROLES}
    if "project_context" not in st.session_state:
        st.session_state.project_context = ""
    if "master_output" not in st.session_state:
        st.session_state.master_output = {}

# Run init immediately
init_session_state()


# Inject professional UI CSS
st.markdown("""
    <style>
    body {
        background-color: #f0f4f7;
    }
    .main-container {
        background-color: #ffffff;
        border-radius: 8px;
        padding: 20px;
        margin: 20px auto;
        max-width: 1200px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    .artifact-box, .conversation-box {
        background-color: #ffffff;
        border-radius: 8px;
        padding: 20px;
        margin: 20px 0;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        font-size: 16px;
        line-height: 1.6;
        overflow-y: auto;
        max-height: 400px;
    }
    .artifact-box h4, .conversation-box h4 {
        margin-top: 0;
        color: #1565c0;
        font-weight: bold;
        text-decoration: underline;
    }
    .stCodeBlock pre {
        background-color: #fce4ec !important;
        border: 2px solid #f48fb1 !important;
        border-radius: 6px !important;
        font-size: 15px !important;
        padding: 15px !important;
        white-space: pre-wrap;
    }
    </style>
""", unsafe_allow_html=True)

# ---------- Session State Initialization ----------
def init_session_state():
    if "conversation_history" not in st.session_state:
        st.session_state.conversation_history = {role: [] for role in AGENT_ROLES}
    if "project_context" not in st.session_state:
        st.session_state.project_context = ""
    if "master_output" not in st.session_state:
        st.session_state.master_output = {}

init_session_state()

# ---------- Helper Functions ----------
def clean_text(text: str) -> str:
    text = re.sub(r"[#\*\-]+", "", text)
    return re.sub(r"[ ]{2,}", " ", text).strip()

def display_artifact(title: str, content: str, language: str = None):
    st.markdown(f"<div class='artifact-box'><h4><strong>{title}</strong></h4></div>", unsafe_allow_html=True)
    if title == "Generated Design Artifact":
        st.markdown(f"<pre>{content}</pre>", unsafe_allow_html=True)
    elif language:
        st.code(content, language=language)
    else:
        for p in content.splitlines():
            if p.strip():
                st.markdown(f"<p>{p.strip()}</p>", unsafe_allow_html=True)

def chat_with_agent(agent_role: str, message: str) -> str:
    greeting = "Good morning" if datetime.datetime.now().hour < 12 else "Good afternoon" if datetime.datetime.now().hour < 18 else "Good evening"
    prompt = (f"Respected Sir, {greeting}. I am the Project Manager. "
              f"The project is defined as: {st.session_state.project_context}. "
              f"My question for you, as the {agent_role}, is: '{message}'. "
              "Provide a detailed and definitive update on the quality, progress, and results of your artifact. "
              "Respond with absolute clarity and certainty. End your response with 'Thank you, with regards.'")
    return gemini_generate(prompt)

def display_conversation(agent_role: str):
    history = st.session_state.conversation_history.get(agent_role, [])
    html = f"<div class='conversation-box'><h4><strong>Conversation with {agent_role}</strong></h4>"
    if not history:
        html += "<p>No conversation yet.</p></div>"
    else:
        for speaker, msg in reversed(history):
            html += f"<p><strong>{speaker}:</strong> {msg}</p>"
        html += "</div>"
    st.markdown(html, unsafe_allow_html=True)

def summarize_artifacts():
    output = st.session_state.master_output
    st.sidebar.header("📌 Artifact Summary")
    st.sidebar.markdown("#### ✅ Generated Artifacts")
    for k, v in {
        "User Stories": output.get("user_stories"),
        "Design": output.get("design_artifact"),
        "Code": output.get("code"),
        "Tests": output.get("test_cases"),
        "Test Results": output.get("test_results"),
        "Security": output.get("security_report"),
        "Performance": output.get("performance_report")
    }.items():
        if v and v.strip():
            st.sidebar.markdown(f"- ✅ **{k}**")
        else:
            st.sidebar.markdown(f"- ⏳ {k}")

# ---------- Main Application ----------
def main():
    st.markdown('<div class="main-container">', unsafe_allow_html=True)
    st.title("🤖 AI-powered Virtual Development Pod")
    st.subheader("Project Manager Dashboard")

    st.markdown("### Enter High-Level Business Requirements")
    business_requirements = st.text_area(
        "Business Requirements",
        height=250,
        placeholder="Provide your high-level business requirements here..."
    )

    if st.button("Run Project Workflow"):
        if not business_requirements.strip():
            st.error("Please enter valid business requirements.")
        else:
            with st.spinner("🧠 Coordinating agents..."):
                orchestrator = AgentOrchestrator()
                results = orchestrator.orchestrate_pipeline(business_requirements.strip())
                st.session_state.project_context = business_requirements.strip()
                st.session_state.master_output = results
                st.success("✅ Workflow Execution Completed!")

    # Display artifacts if available
    if st.session_state.master_output:
        output = st.session_state.master_output
        summarize_artifacts()
        display_artifact("Generated User Stories", clean_text(output.get("user_stories", "")))
        display_artifact("Generated Design Artifact", clean_text(output.get("design_artifact", "")))
        display_artifact("Generated Source Code", clean_text(output.get("code", "")), language="python")
        display_artifact("Generated Test Cases", clean_text(output.get("test_cases", "")))
        display_artifact("Test Execution Results", clean_text(output.get("test_results", "")))
        display_artifact("Security Analysis Report", clean_text(output.get("security_report", "")))
        display_artifact("Performance Optimization Suggestions", clean_text(output.get("performance_report", "")))

    # Conversation Interface
    st.markdown("### 💬 Chat with an Agent")
    agent_choice = st.selectbox("Choose an Agent", list(AGENT_ROLES.keys()))
    user_message = st.text_input("Your Message to the Agent", placeholder="Type your message here...")

    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("📨 Send Message"):
            if not user_message.strip():
                st.error("Please enter a message.")
            else:
                st.session_state.conversation_history[agent_choice].append(("Project Manager", user_message))
                with st.spinner(f"💬 {agent_choice} is replying..."):
                    response = chat_with_agent(agent_choice, user_message)
                st.session_state.conversation_history[agent_choice].append((agent_choice, response))
    with col2:
        if st.button("🧹 Clear Conversation"):
            st.session_state.conversation_history[agent_choice] = []

    display_conversation(agent_choice)
    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
