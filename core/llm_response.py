from transformers import pipeline

# Load your Hugging Face model
jarvis_thinker = pipeline("text2text-generation",
                          model="declare-lab/flan-alpaca-large")


def respond_to_query(query):
    prompt = f"Jarvis is an intelligent, emotional AI assistant helping Pragadeesh. He said: \"{query}\". Respond like a caring, smart friend with a touch of humor or motivation."

    result = jarvis_thinker(prompt, max_new_tokens=100,
                            do_sample=True, 
                            temperature=0.95)[0]['generated_text']

    return result.strip()
