import streamlit as st
from services.agent_orchestration import AgentOrchestrator

def main():
    st.title("AI-powered Virtual Development Pod")
    st.subheader("Project Manager Dashboard")
    
    st.markdown("### Enter High-Level Business Requirements")
    business_requirements = st.text_area("Business Requirements", height=200, 
                                         placeholder="Provide your high-level business requirements here...")
    
    if st.button("Run Project Workflow"):
        if not business_requirements.strip():
            st.error("Please enter valid business requirements.")
        else:
            st.info("Orchestrating the agents... Please wait.")
            orchestrator = AgentOrchestrator()
            results = orchestrator.orchestrate_pipeline(business_requirements)
            
            st.success("Workflow Execution Completed!")
            
            st.markdown("#### Generated User Stories")
            st.text_area("User Stories", value=results.get("user_stories", ""), height=150)
            
            st.markdown("#### Generated Design Artifact")
            st.text_area("Design Artifact", value=results.get("design_artifact", ""), height=150)
            
            st.markdown("#### Generated Source Code")
            st.text_area("Source Code", value=results.get("code", ""), height=150)
            
            st.markdown("#### Generated Test Cases")
            st.text_area("Test Cases", value=results.get("test_cases", ""), height=150)
            
            st.markdown("#### Test Execution Results")
            st.text_area("Test Results", value=results.get("test_results", ""), height=150)

if __name__ == '__main__':
    main()
