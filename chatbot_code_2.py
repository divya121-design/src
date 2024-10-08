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
model_id = "gpt-4o-mini"



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



chatbot = []
msg = []

zipfs = []
ttr = []
mltd = []
burstiness = []

while True:
    single_message = {}
    entered_text = input("Content: ").strip()
    print()

    
    #if entered_text.lower() in ["exit", "quit"]:
    #    print("Your response has ended.")
    #    avg_zipfs = np.mean(zipfs)
    #    avg_ttr = np.mean(ttr)
    #    avg_mltd = np.mean(mltd)
    #    avg_burstiness = np.mean(burstiness)

    #    str_zipfs = "Average Zipf's Law Coefficient                         :  "+str(avg_zipfs)
    #    str_ttr = "Average Type-Token Ratio (TTR)                         :  "+str(avg_ttr)
    #    str_mltd = "Average Measure of Textual Lexical Diversity (MTLD)    :  "+str(avg_mltd)
    #    str_burstiness = "Average Burstiness Calculation                         :  "+str(avg_burstiness)

    #    st = [str_zipfs, str_ttr, str_mltd, str_burstiness]

    #    with open(file="evaluation_metrics_for_chatbot.jsonl",mode="w") as fp:
    #        for i in st:
    #            json_line = json.dumps(i)
    #            fp.write(json_line + '\n')
    #    break

    user_message = {"role": "user", "content": entered_text}
    msg.append(user_message)

    prompt = msg[-5:]  # last 5 messages
    response = get_chat_response(prompt)
    output_text = response.choices[0].message['content'].strip()

    assistant_message = {"role": "assistant", "content": output_text}
    msg.append(assistant_message)


    single_message = [user_message, assistant_message]
    chatbot += single_message

ctr = 0
with open("chatbot.json","w") as fp:
    for i in chatbot:
        json.dump(i, fp)
        ctr += 1
        if ctr % 2 == 0:
            fp.write("\n")
        fp.write("\n")