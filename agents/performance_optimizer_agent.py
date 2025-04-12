from services.language_model_integration import gemini_generate

class PerformanceOptimizerAgent:
    """
    Analyzes code for performance bottlenecks and optimization opportunities.
    """
    def __init__(self):
        pass

    def optimize_performance(self, code: str) -> str:
        prompt = f"""
You are a performance optimizer reviewing the following source code:

{code}

Generate a markdown-formatted Performance Optimization Report using this structure:

#  Performance Optimization Report

##  Code Scope
[Mention the code/module analyzed]

##  Performance Bottlenecks Identified
- [ ] Bottleneck 1  
  -  Description:  
  -  Cause:  
  -  Optimization Tip:  

##  Performance Best Practices Checklist
- [ ] Avoided redundant loops
- [ ] Lazy loading implemented
... (rest of the checklist)

##  Suggested Refactors
[List specific changes]

##  Additional Notes
[Profiling tool used, complexity, etc.]
"""
        return gemini_generate(prompt)
