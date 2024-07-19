import os
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

client = OpenAI(api_key=os.getenv('OPENAI_TOKEN'))

def comp(PROMPT, MaxToken=50):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are converting short, Discord-style messages to a medium-sized email-style message for a newsletter. This will be directly sent out, so please NO '[insert __]'. Also please keep very short for testing. You may sign the emails as 'New England Weather Balloon Society (N.E.W.B.S.). NO [something here] EVER!!! KEEP SHORTER THAN 1000 TOKENS!!!! NO CUTTOFF TEXT'"},
            {"role": "user", "content": PROMPT}
        ],
        max_tokens=MaxToken
    )
    return response.choices[0].message.content