import openai
import requests
from bs4 import BeautifulSoup
import random
import json
import warnings
import numpy as np
from collections import Counter
from scipy.stats import linregress
import math
import json

warnings.filterwarnings("ignore")

openai.api_key = "<API Key>"
model_id = "gpt-3.5-turbo"

def get_chat_response(messages):
    try:
        response = openai.ChatCompletion.create(
            model=model_id,
            messages=messages,
            max_tokens=150,
            temperature=0.7,
        )
        
        return response
    except Exception as e:
        return f"Error: {e}"

"""
print("Hi! Welcome to DUTA. How can I help you?")
print("Please enter your message so that I will process it and generate the output.")
print("Type 'exit' or 'quit' to quit the chatbot.")
print()
"""

chatbot = []
msg = []


while True:
    single_message = {}
    # print("Role    : User")
    #entered_text = input("Content: ").strip()
    #print()

    if entered_text.lower() in ["exit", "quit"]:
        break

    user_message = {"role": "user", "content": entered_text}
    msg.append(user_message)

    prompt = msg[-10:]  # last 5 messages
    response = get_chat_response(prompt)
    output_text = response.choices[0].message["content"].strip()

    assistant_message = {"role": "assistant", "content": output_text}
    msg.append(assistant_message)

    # print("Role    : Assistant")
    # print("Content : ", output_text)
    # print()

    single_message = [user_message, assistant_message]
    chatbot += single_message

ctr = 0
with open("chatbot.json", 'w') as fp:
    for i in chatbot:
        json.dump(i, fp)     
        ctr += 1
        if ctr % 2 == 0:
            fp.write("\n")
        fp.write("\n")