import os
import google.generativeai as genai


os.environ['GOOGLE_API_KEY'] = "AIzaSyCEaocHi1fcC0mLT2UM0Y6j7F773xZpwg8" 
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])

model = genai.GenerativeModel('gemini-pro')

def llm_function(query):
    response = model.generate_content(query)
    return response.text

print("Bot: Hello! How can I assist you today?")

while True:
    user_input = input("You: ")

    if user_input.lower() in ['exit', 'quit', 'stop']:
        print("Bot: Goodbye!")
        break
    
    bot_response = llm_function(user_input)

    print(f"Bot: {bot_response}")
