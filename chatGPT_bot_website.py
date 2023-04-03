import openai
import gradio

openai.api_key = "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"

messages = [{"role": "system", "content": "You are an AI like JARVIS"}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "JARVIS")

demo.launch(share=True)