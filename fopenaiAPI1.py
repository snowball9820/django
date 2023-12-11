from openai import OpenAI

def qna(question) :
   
    client = OpenAI(api_key = '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')

    messages = [ {"role": "system", "content": "You are a intelligent assistant."} ]
    messages.append(
                {"role": "user", "content": question},
            )
    
    chat = client.chat.completions.create(
    model="gpt-4-1106-preview", messages=messages )
    
    return chat.choices[0].message.content
        