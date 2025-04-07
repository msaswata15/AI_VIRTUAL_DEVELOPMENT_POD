import unittest
from unittest.mock import patch
from agents.business_analyst_agent import BusinessAnalystAgent
from agents.design_agent import DesignAgent
from agents.developer_agent import DeveloperAgent
from agents.testing_agent import TestingAgent

class TestAgents(unittest.TestCase):
    
    @patch("services.language_model_integration.gemini_generate", return_value="generated text")
    def test_business_analyst_generate_user_stories(self, mock_gemini):
        agent = BusinessAnalystAgent()
        result = agent.generate_user_stories("High-level requirements sample")
        self.assertEqual(result, "generated text")

    @patch("services.language_model_integration.gemini_generate", return_value="generated design")
    def test_design_agent_generate_design(self, mock_gemini):
        agent = DesignAgent()
        result = agent.generate_design("User stories sample")
        self.assertEqual(result, "generated design")

    @patch("services.language_model_integration.gemini_generate", return_value="generated code")
    def test_developer_agent_generate_code(self, mock_gemini):
        agent = DeveloperAgent()
        result = agent.generate_code("User stories sample", "Design artifact sample")
        self.assertEqual(result, "generated code")

    @patch("services.language_model_integration.gemini_generate", return_value="generated test cases")
    def test_testing_agent_generate_test_cases(self, mock_gemini):
        agent = TestingAgent()
        result = agent.generate_test_cases("Source code sample")
        self.assertEqual(result, "generated test cases")

    @patch("services.language_model_integration.gemini_generate", return_value="executed tests summary")
    def test_testing_agent_execute_tests(self, mock_gemini):
        agent = TestingAgent()
        result = agent.execute_tests("Source code sample", "Test cases sample")
        self.assertEqual(result, "executed tests summary")

if __name__ == '__main__':
    unittest.main()
