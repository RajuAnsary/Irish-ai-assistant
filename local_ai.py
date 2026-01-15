# from ctransformers import AutoModelForCausalLM

# llm = AutoModelForCausalLM.from_pretrained(
#     "models",
#     model_file="tinyllama.gguf",
#     model_type="llama",
#     gpu_layers=0
# )

# def ask_local_ai(prompt):
#     chat_prompt = f"""
# You are Iris, a helpful AI assistant.
# Answer the user's question clearly and concisely.
# Do NOT ask questions back.

# User: {prompt}
# Assistant:
# """
#     response = llm(
#         chat_prompt,
#         max_new_tokens=200,
#         temperature=0.5,
#         stop=["User:"]
#     )
#     return response.strip()

# if __name__ == "__main__":
#     while True:
#         q = input("You: ")
#         if q.lower() == "exit":
#             break
#         print("Iris:", ask_local_ai(q))



import os
import sys
from ctransformers import AutoModelForCausalLM


def get_model_path():
    
    if getattr(sys, "frozen", False):
        base_path = sys._MEIPASS   
    else:
        base_path = os.path.dirname(os.path.abspath(__file__))

    return os.path.join(base_path, "models", "tinyllama.gguf")


MODEL_PATH = get_model_path()

llm = AutoModelForCausalLM.from_pretrained(
    MODEL_PATH,          
    model_type="llama",
    gpu_layers=0
)


def ask_local_ai(prompt):
    chat_prompt = f"""
You are Iris, a helpful AI assistant.
Answer the user's question clearly and concisely.
Do NOT ask questions back.

User: {prompt}
Assistant:
"""
    response = llm(
        chat_prompt,
        max_new_tokens=200,
        temperature=0.5,
        stop=["User:"]
    )
    return response.strip()


if __name__ == "__main__":
    while True:
        q = input("You: ")
        if q.lower() == "exit":
            break
        print("Iris:", ask_local_ai(q))
