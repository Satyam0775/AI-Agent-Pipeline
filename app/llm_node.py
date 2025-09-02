from transformers import pipeline
from app.config import LLM_MODEL, HUGGINGFACE_API_KEY

# HuggingFace LLM
generator = pipeline(
    "text2text-generation",
    model=LLM_MODEL,
    token=HUGGINGFACE_API_KEY  # ✅ fixed: use token instead of use_auth_token
)

def refine_answer(prompt: str) -> str:
    """Refine raw answer with HuggingFace LLM."""
    response = generator(prompt, max_length=200, do_sample=True)[0]['generated_text']
    return response
