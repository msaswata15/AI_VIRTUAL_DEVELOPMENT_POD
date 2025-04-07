import unittest
from unittest.mock import patch, MagicMock
from services.crewai_integration import CrewAIIntegration
from services.language_model_integration import gemini_generate
from services.agent_orchestration import AgentOrchestrator

class TestServices(unittest.TestCase):

    def test_crewai_send_message(self):
        crewai = CrewAIIntegration()
        response = crewai.send_message("TestAgent", "Test message")
        self.assertIn("Response from TestAgent", response)

    @patch("services.requests.post")
    def test_language_model_integration_gemini_generate(self, mock_post):
        # Prepare a fake response to simulate Gemini API
        fake_response = MagicMock()
        fake_response.json.return_value = {"generated_text": "dummy generated text"}
        fake_response.raise_for_status = lambda: None
        mock_post.return_value = fake_response

        result = gemini_generate("Test prompt")
        self.assertEqual(result, "dummy generated text")

    @patch("services.language_model_integration.gemini_generate", return_value="dummy")
    def test_agent_orchestrator_pipeline(self, mock_gemini):
        orchestrator = AgentOrchestrator()
        results = orchestrator.orchestrate_pipeline("Test requirements")
        self.assertEqual(results.get("user_stories"), "dummy")
        self.assertEqual(results.get("design_artifact"), "dummy")
        self.assertEqual(results.get("code"), "dummy")
        self.assertEqual(results.get("test_cases"), "dummy")
        self.assertEqual(results.get("test_results"), "dummy")

if __name__ == '__main__':
    unittest.main()
