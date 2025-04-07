from services.language_model_integration import gemini_generate

class DesignAgent:
    """
    Agent responsible for generating software design artifacts from user stories.
    """
    def __init__(self):
        # Initialize any design-specific parameters if necessary
        pass

    def generate_design(self, user_stories: str) -> str:
        """
        Generate a comprehensive software design based on the provided user stories.
        """
        prompt = (
            "Based on the following user stories:\n"
            f"{user_stories}\n\n"
            "Generate a detailed software design. Include system architecture, component interactions, "
            "and if necessary, textual descriptions of diagrams. Ensure the design is both feasible and "
            "scalable."
        )
        design_artifact = gemini_generate(prompt)
        return design_artifact
