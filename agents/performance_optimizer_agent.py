from services.language_model_integration import gemini_generate

class PerformanceOptimizerAgent:
    """
    Agent responsible for analyzing generated source code for performance bottlenecks 
    and providing definitive performance optimization recommendations.
    """
    def __init__(self):
        pass

    def optimize_performance(self, code: str) -> str:
        prompt = f"""
You are a performance optimization expert reviewing the following source code:

{code}

Generate a markdown-formatted Performance Optimization Report using the following structure:

# Performance Optimization Report

## Code Scope
Clearly describe the code or module analyzed.

## Performance Bottlenecks Identified
- Bottleneck 1  
  - Description: Provide a clear and definitive description of the performance issue.
  - Cause: Identify the root cause.
  - Optimization Recommendation: Provide a specific, measurable recommendation for improvement.

## Performance Best Practices Checklist
- Redundant loops are eliminated.
- Lazy loading is implemented where beneficial.
- Efficient data structures are used.
- Database queries are optimized.
- Resource utilization is minimized.

## Suggested Refactors
List specific changes to optimize performance.

## Additional Notes
Include details on any profiling tools used and final performance metrics.

Respond with absolute clarity and certainty, with no placeholders or uncertain language.
End your response with 'Thank you, with regards.'
"""
        return gemini_generate(prompt)
