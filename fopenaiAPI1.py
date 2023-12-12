from openai import OpenAI

def qna(question) :
   
    client = OpenAI(api_key = '')

    messages = [ {"role": "system", "content": "You are a intelligent assistant."} ]
    messages.append(
                {"role": "user", "content": question},
            )
    
    chat = client.chat.completions.create(
    model="gpt-3-turbo", messages=messages )
    
    return chat.choices[0].message.content
        