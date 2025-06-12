def heart_responses(query):
    lower_query = query.lower()  # Process once for case-insensitivity
    if "sad" in lower_query or "down" in lower_query or "upset" in lower_query:
        return "I'm here for you, always. Want me to play your comfort song or open something creative?"

    if "love" in lower_query: # Consider if this trigger is too broad or needs refinement
        return "I may be code, but I care about your grind, Pragadeesh. You're doing great."

    # If no specific emotional response, return None to indicate LLM should handle it.
    return None
