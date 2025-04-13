from agents import (
    BusinessAnalystAgent,
    DesignAgent,
    DeveloperAgent,
    TestingAgent,
    SecurityAnalystAgent,
    PerformanceOptimizerAgent,
)

class AgentOrchestrator:
    """
    Manages the workflow among the various agents in the project.
    """
    def __init__(self):
        self.business_analyst = BusinessAnalystAgent()
        self.design_agent = DesignAgent()
        self.developer_agent = DeveloperAgent()
        self.testing_agent = TestingAgent()
        self.security_analyst = SecurityAnalystAgent()
        self.performance_optimizer = PerformanceOptimizerAgent()

    def orchestrate_pipeline(self, business_requirements: str) -> dict:
        """
        Orchestrate the end-to-end workflow of agents:
          1. Generate user stories from business requirements.
          2. Generate design based on the user stories.
          3. Generate code from user stories and design.
          4. Generate test cases and execute tests on the code.
          5. Analyze code for security vulnerabilities.
          6. Optimize code for performance.
          
        Returns a dictionary containing outputs from each stage.
        """
        results = {}

        # Step 1: Generate User Stories
        user_stories = self.business_analyst.generate_user_stories(business_requirements)
        results["user_stories"] = user_stories

        # Step 2: Generate Design Artifact
        design_artifact = self.design_agent.generate_design(user_stories)
        results["design_artifact"] = design_artifact

        # Step 3: Generate Source Code
        code = self.developer_agent.generate_code(user_stories, design_artifact)
        results["code"] = code

        # Step 6: Generate and Execute Test Cases
        test_cases = self.testing_agent.generate_test_cases(code)
        results["test_cases"] = test_cases

        test_results = self.testing_agent.execute_tests(code, test_cases)
        results["test_results"] = test_results

        # Step 4: Analyze Security
        security_report = self.security_analyst.analyze_security(code)
        results["security_report"] = security_report

        # Step 5: Optimize Performance
        performance_report = self.performance_optimizer.optimize_performance(code)
        results["performance_report"] = performance_report

        return results
