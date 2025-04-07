from services.language_model_integration import gemini_generate

class TestingAgent:
    """
    Agent responsible for generating and executing test cases for the generated code.
    """
    def __init__(self):
        # Initialize any testing-specific parameters if necessary
        pass

    def generate_test_cases(self, code: str) -> str:
        """
        Generate comprehensive test cases for the given source code.
        """
        prompt = (
            "Given the following source code:\n"
            f"{code}\n\n"
            "Generate a set of comprehensive test cases. The test cases should cover functional, edge, "
            "and performance aspects of the code in a clear and structured format."
        )
        test_cases = gemini_generate(prompt)
        return test_cases

    def execute_tests(self, code: str, test_cases: str) -> str:
        """
        Execute the generated test cases on the given code and return a summary of the test results.
        """
        prompt = (
            "Execute the following test cases on the provided source code and summarize the outcomes:\n\n"
            "Source Code:\n"
            f"{code}\n\n"
            "Test Cases:\n"
            f"{test_cases}\n\n"
            "Provide a summary of any failures, issues, or successes observed during testing."
        )
        test_results = gemini_generate(prompt)
        return test_results
