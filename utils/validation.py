def validate_artifact(artifact_text: str, min_length: int = 50) -> bool:
    """
    Validates that the artifact text is not empty and meets a minimum length requirement.
    Returns True if valid; otherwise, returns False.
    """
    if not artifact_text or len(artifact_text.strip()) < min_length:
        return False
    return True

def validate_business_requirements(requirements: str) -> bool:
    """
    Validates that the business requirements text is not empty.
    Returns True if valid; otherwise, returns False.
    """
    return bool(requirements and requirements.strip())
