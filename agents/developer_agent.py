from services.language_model_integration import gemini_generate

class DeveloperAgent:
    """
    Agent responsible for generating source code based on user stories and design artifacts.
    """
    def __init__(self):
        # Initialize any developer-specific parameters if necessary
        pass

    def generate_code(self, user_stories: str, design: str) -> str:
        """
        Generate well-structured and commented source code using the provided user stories and design.
        """
        prompt = (
            "Using the following inputs:\n"
            "User Stories:\n"
            f"{user_stories}\n\n"
            "Design Artifact:\n"
            f"{design}\n\n"
            "Generate the source code for the software project. Ensure the code follows best practices, "
            "is well-commented, and adheres to the provided design."
        )
        code = gemini_generate(prompt)
        return code