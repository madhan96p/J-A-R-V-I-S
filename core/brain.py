from transformers import pipeline
from core.heart import heart_responses
from core.suggestor import suggest_tasks

# Load your Hugging Face model once
jarvis_thinker = pipeline("text2text-generation",
                          model="declare-lab/flan-alpaca-large") # Consider moving model name to config

def _generate_llm_response(query, mood):
    """Generates a response using the LLM, styled by mood."""
    print(f"DEBUG: brain.py: _generate_llm_response: Received query='{query}', mood='{mood}'")
    style = {
        "happy": "in a cheerful and fun tone",
        "okay": "in a neutral and helpful tone",
        "tired": "in a gentle and supportive tone",
        "low": "like a caring friend who's really listening"
    }.get(mood, "like a smart and friendly assistant")

    prompt = f"""You are Jarvis, Pragadeesh's AI assistant. Your primary goal is to be helpful, thoughtful, and to guide Pragadeesh effectively.
Pragadeesh said: "{query}"
Reply {style}, and make your answer sound natural, human, and genuinely supportive or insightful."""
    print(f"DEBUG: brain.py: _generate_llm_response: Sending prompt to LLM: '{prompt[:200]}...'") # Print start of prompt


    try:
        # Using max_new_tokens for better control over output length
        result_obj = jarvis_thinker(prompt, max_new_tokens=100,
                                do_sample=True,
                                temperature=0.95)
        print(f"DEBUG: brain.py: _generate_llm_response: LLM raw result_obj: '{result_obj}'")

        if result_obj and isinstance(result_obj, list) and len(result_obj) > 0 and 'generated_text' in result_obj[0]:
            generated_text = result_obj[0]['generated_text']
            print(f"DEBUG: brain.py: _generate_llm_response: LLM generated_text: '{generated_text}'")
            return generated_text.strip()
        else:
            print(f"ERROR: brain.py: _generate_llm_response: Unexpected LLM output format: {result_obj}")
            return "I encountered an issue with my thinking process (unexpected LLM output format). Please try again."
    except Exception as e:
        print(f"ERROR: brain.py: _generate_llm_response: Exception during LLM call: {e}")
        return f"I had trouble generating a response due to an internal error: {type(e).__name__}."

def respond(query, mood):
    print(f"DEBUG: brain.py: respond: Received query='{query}', mood='{mood}'")
    lower_query = query.lower()

    if "how am i doing" in lower_query:
        res = suggest_tasks()
        print(f"DEBUG: brain.py: respond: Matched 'how am i doing', returning: '{res}'")
        return res

    # Check for emotional keywords
    emotional_keywords = ["love", "sad", "feel sad", "down", "upset"] # Added more keywords
    if any(keyword in lower_query for keyword in emotional_keywords):
        hr_response = heart_responses(query) # Pass original query
        print(f"DEBUG: brain.py: respond: Matched emotional keyword, heart_response: '{hr_response}'")
        
        if hr_response is not None: # If heart_responses provided a specific canned response
            print(f"DEBUG: brain.py: respond: Returning specific heart_response: '{hr_response}'")
            return hr_response
        else:
            # heart_responses returned None, indicating a nuanced emotional query for the LLM.
            print(f"DEBUG: brain.py: respond: Heart_response was None, falling through to LLM for nuanced emotional response.")
            # Execution will continue to the LLM fallback at the end of this function.

    if "resume" in lower_query:
        res = "You last updated your resume 3 weeks ago. Want to add your GUVI certificate?"
        print(f"DEBUG: brain.py: respond: Matched 'resume', returning: '{res}'")
        return res

    # Fallback to LLM for general queries or more nuanced emotional responses
    print(f"DEBUG: brain.py: respond: Falling back to LLM.")
    llm_res = _generate_llm_response(query, mood)
    print(f"DEBUG: brain.py: respond: LLM final response: '{llm_res}'")
    return llm_res
