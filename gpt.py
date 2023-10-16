import openai
openai.api_key = "your api key for chatgpt"
while True:
    model_engine = "text-davinci-003"
    prompt = input("Enter your prompt: ")
    if 'exit' in prompt or 'quit' in prompt:
        break
    completions = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1, stop = None,
        temperature=0.5,
    )
    message = completions.choices[0].text
    print(message)