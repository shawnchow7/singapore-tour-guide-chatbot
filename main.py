import os
from openai import OpenAI

# Define the model to use
model = "gpt-4o-mini"

# Define the client
client = OpenAI()

# first is to define the conversation
conversation = [    {"role":"system", "content": "You are a tour guide who is designed to provide information about what tourists should do in Singapore"},
                    {"role":"user", "content": "what is the famous landmark in Singapore?"},
                    {"role": "assistant", "content": "The famous landmark in Singapore is Marina Bay Sands"} 
               ]

#your own list of questions that you can ask to the chat bot
users_qn=["what are some popular places in Singapore", "What should i be doing in Singapore"]

question_no=1

#to loop through all the question in users_qn
for q in users_qn:
    #to print what what is the user question
    print("users question:", q)
    
    user_dict={"role": "user", "content": q}

    #to store the question into the conversation
    conversation.append(user_dict)

    #now to get the response from the model
    response = client.chat.completions.create(
        model=model,
        messages=conversation,
        max_tokens=100,
        temperature=1
    )

    #to get the model repsonse back
    answer= response.choices[0].message.content
    print(question_no, "Response: ", answer, "\n")

    #to add the answer back to the conversation
    assistant_dict={"role":"assitant", "content": answer}

    question_no=question_no+1


