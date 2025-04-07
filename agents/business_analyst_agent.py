from services.language_model_integration import gemini_generate

class BusinessAnalystAgent:
    """
    Agent responsible for creating detailed user stories from high-level business requirements.
    """
    def __init__(self):
        # Any initialization parameters can be added here
        pass

    def generate_user_stories(self, business_requirements: str) -> str:
        """
        Generate user stories from the provided high-level business requirements using the Gemini API.
        """
        prompt = (
            "Based on the following high-level business requirements:\n"
            f"{business_requirements}\n\n"
            "Generate detailed, structured user stories for a software development project. "
            "Ensure that the user stories are clear and actionable."
        )
        user_stories = gemini_generate(prompt)
        return user_stories
