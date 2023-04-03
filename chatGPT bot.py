import openai

openai.api_key = "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"

messages = []
system_msg = input("What type of chatbot would you like to create? : ")
messages.append({"role": "system", "content": system_msg})

print("Your new assistant is ready!")
while input != "quit()":
    message = input("LYN> ")
    messages.append({"role": "user", "content": message})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages)
    reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": reply})
    print("\n" + reply + "\n")
