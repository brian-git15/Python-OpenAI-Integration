import openai
openai.api_key = "hidden key"

model = "tts-1"
question = input("Question: ")

def gptconvo(model,question):
    response = openai.Completion.create(
        engine=model,
        prompt=(f"Question: {question}\n""Answer:"),
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5
    )
    return(response)

response = gptconvo(model,question)
answer = response.choices[0].text.split('\n')[0]
print(answer)
