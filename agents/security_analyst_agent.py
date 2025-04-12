from services.language_model_integration import gemini_generate

class SecurityAnalystAgent:
    """
    Analyzes code to detect security vulnerabilities and recommend best practices.
    """
    def __init__(self):
        pass

    def analyze_security(self, code: str) -> str:
        prompt = f"""
You are a security analyst reviewing the following source code:

{code}

Generate a markdown-formatted Security Analysis Report using this structure:

# Security Analysis Report

## Code Scope
[Describe the code or module analyzed here.]

##  Identified Vulnerabilities
- Vulnerability 1  
  -  Description:  
  -  Impact:  
  -  Recommendation:  

##  Code Security Best Practices Checklist
- [ ] Input validation present
- [ ] SQL injection prevention in place
... (rest of the checklist)

##  Suggestions for Improvement
[Add suggestions]

##  Additional Notes
[Other tools, dependencies, etc.]
"""
        return gemini_generate(prompt)
