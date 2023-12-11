from openai import OpenAI

def qna(question) :
   
    client = OpenAI(api_key = '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')

    messages = [ {"role": "system", "content": "You are a intelligent assistant."} ]
    messages.append(
                {"role": "user", "content": question},
            )
    
    chat = client.chat.completions.create(
    model="gpt-3-turbo", messages=messages )
    
    return chat.choices[0].message.content
        