from services.language_model_integration import gemini_generate

class SecurityAnalystAgent:
    """
    Agent responsible for analyzing source code for security vulnerabilities and providing definitive security recommendations.
    """
    def __init__(self):
        pass

    def analyze_security(self, code: str) -> str:
        prompt = f"""
You are a security expert reviewing the following source code:

{code}

Generate a markdown-formatted Security Analysis Report using the following structure:

# Security Analysis Report

## Code Scope
Clearly define the code or module that was analyzed.

## Identified Vulnerabilities
- Vulnerability 1  
  - Description: Provide a specific and definitive description of the vulnerability.
  - Impact: Specify the exact impact on the system.
  - Recommendation: Provide a concrete recommendation for remediation.

## Security Best Practices Checklist
- Input validation is fully implemented.
- SQL injection prevention measures are in place.
- Cross-site scripting (XSS) is effectively mitigated.
- Secure authentication and session management are enforced.
- Sensitive data is encrypted at rest and in transit.

## Suggested Improvements
List the specific changes required to enhance security.

## Additional Notes
Include details of any security tools used, quantitative assessment metrics, and final security ratings.

Respond with absolute clarity and certainty, without any placeholders or ambiguous language.
End your response with 'Thank you, with regards.'
"""
        return gemini_generate(prompt)
