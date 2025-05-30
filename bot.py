import google.generativeai as genai

# Set your API key
genai.configure(api_key="********************************************")

def AI(query):
    try:
        model = genai.GenerativeModel(
            model_name="gemini-2.0-flash",
            generation_config={
                "temperature": 0.8,
                "top_p": 1,
                "top_k": 1,
                "max_output_tokens": 200,
            }
        )

        # Use generate_content instead of start_chat()
        formatted_query = f'''
        chatgpt

        User: {query}
        Assistant:
        '''

        response = model.generate_content(formatted_query)
        resp = response.text.replace('*', ' ')
        print("\nAssistant:", resp.strip(), "\n")
        return resp

    except Exception as e:
        print("Error:", str(e))
        return "Try Again"
