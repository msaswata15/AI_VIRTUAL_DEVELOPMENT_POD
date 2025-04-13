# AI-powered Virtual Development Pod

## Overview

The **AI-powered Virtual Development Pod** simulates a complete software project lifecycle by orchestrating a team of AI agents. These agents assume specific roles—such as Business Analyst, Design, Developer, Testing, Security Analyst, and Performance Agent—to generate project artifacts from high-level business requirements. The system uses the Gemini API for text generation and CrewAI for managing agent interactions, all integrated with a user-friendly Streamlit interface.

This project is designed to:
- Generate detailed user stories from high-level business requirements.
- Produce comprehensive software design artifacts and diagrams.
- Create production-quality source code.
- Generate and execute test cases with definitive test results.
- Analyze security vulnerabilities and provide robust recommendations.
- Optimize performance by identifying bottlenecks and suggesting improvements.

## Features

- **Multi-Agent Workflow:**  
  Orchestrates a team of AI agents, each handling a distinct aspect of the project lifecycle.
- **Conversational UI:**  
  A Streamlit interface that allows the Project Manager to view master outputs and chat with individual agents.
- **Definitive, Sure-Shot Responses:**  
  All agents generate responses that are clear, complete, and free of placeholders or uncertainty.
- **Integrated Environment:**  
  All configurations are managed via environment variables, ensuring seamless integration and deployment.

## Folder Structure

ai_virtual_dev_pod/
├── agents/
│   ├── __init__.py                   # Imports all agent classes.
│   ├── business_analyst_agent.py     # Creates user stories from high-level requirements.
│   ├── design_agent.py                # Generates software design artifacts and diagrams.
│   ├── developer_agent.py             # Generates production-quality source code.
│   ├── testing_agent.py               # Generates and executes test cases.
│   ├── security_analyst_agent.py      # Provides security analysis and recommendations.
│   └── performance_agent.py           # Provides performance optimization recommendations.
├── config/
│   ├── __init__.py                   # Imports all configuration settings.
│   └── settings.py                   # Global configuration (API keys, Pinecone, Langchain, CrewAI, etc.)
├── data/
│   ├── artifacts_templates/          # Templates for project artifacts.
│   │   ├── user_stories_template.md
│   │   ├── design_template.md
│   │   ├── code_template.py
│   │   └── test_cases_template.md
│   └── requirements/                 # Business requirements and related documentation.
│       └── business_requirements.txt
├── interfaces/
│   ├── __init__.py                   # Initializes the interfaces module.
│   └── streamlit_app.py              # Main Streamlit UI for the Project Manager.
├── services/
│   ├── __init__.py                   # Imports all service modules.
│   ├── agent_orchestration.py        # Orchestrates the multi-agent workflow using CrewAI.
│   ├── crewai_integration.py         # Integrates with CrewAI for agent communication.
│   └── language_model_integration.py # Wraps Gemini API calls for text generation.
├── tests/
│   ├── __init__.py                   # Initializes the tests module.
│   ├── test_agents.py                # Unit tests for agent logic.
│   ├── test_services.py              # Unit tests for service integrations.
│   └── test_ui.py                    # Tests for Streamlit UI functionality.
├── utils/
│   ├── __init__.py                   # Initializes the utilities module.
│   ├── helper_functions.py           # Common utility functions.
│   └── logger.py                     # Logging utilities.
├── .env                            # Environment variables (API keys, etc.)
├── requirements.txt                # Python dependencies.
├── README.md                       # Project documentation and setup instructions.
└── main.py                         # Entry point to launch the orchestration and Streamlit UI.
```

## Installation

1. **Clone the Repository:**

   ```bash
   git clone <repository-url>
   cd ai_virtual_dev_pod
   ```

2. **Create and Activate a Virtual Environment:**

   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install Dependencies:**

   Ensure you have the required dependencies by running:
   
   ```bash
   pip install -r requirements.txt
   ```

## Environment Setup

Create a **.env** file in the root of your project with the following content (replace placeholder values as needed):

```dotenv
# .env file for AI-powered virtual development pod project

# Gemini API Configuration
GEMINI_API_KEY=
GEMINI_API_MODEL=

# Pinecone API Configuration for RAG (if applicable)
PINECONE_API_KEY=
PINECONE_INDEX_NAME=
PINECONE_ENVIRONMENT=

# (Optional) CrewAI and Langchain Configuration
# CREWAI_API_KEY=
# LANGCHAIN_API_KEY=
```

## Running the Application

To launch the application using Streamlit, run the following command from your project root:

```bash
streamlit run main.py
```

This will start the Streamlit server and open your browser to view the Project Manager dashboard, where you can run the project workflow and interact with the agents.

## Testing

Run the unit tests to ensure all components are functioning correctly:

```bash
python -m unittest discover tests
```

## Project Workflow

1. **Input Business Requirements:**  
   Enter high-level business requirements in the Streamlit UI.

2. **Master Workflow Execution:**  
   The system orchestrates the agents to generate:
   - Detailed user stories (Business Analyst Agent)
   - Software design artifacts (Design Agent)
   - Production-quality source code (Developer Agent)
   - Comprehensive test cases and execution results (Testing Agent)
   - Security analysis report (Security Analyst Agent)
   - Performance optimization report (Performance Agent)

3. **Agent Conversation:**  
   The Project Manager can interact with individual agents via the chat interface to get more detailed, definitive updates on their specific artifacts.

## Contribution

Feel free to fork the repository and submit pull requests with improvements or bug fixes. Please ensure all tests pass before submitting changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
