

"""
Main entry point for the AI-powered Virtual Development Pod project.
This file launches the Streamlit UI which in turn uses the agent orchestrator to simulate the software development lifecycle.
"""

from interfaces.streamlit_app import main as streamlit_main

if __name__ == '__main__':
    streamlit_main()