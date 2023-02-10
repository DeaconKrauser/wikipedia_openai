import openai
import wikipediaapi

# Initialize the OpenAI API
openai.api_key = "your_api_key"

# Initialize the Wikipedia API
wiki_wiki = wikipediaapi.Wikipedia(language='en', extract_format=wikipediaapi.ExtractFormat.WIKI)

# Continuously prompt the user for input
while True:
    user_input = input("Ask what you want to know: ")
    person_or_object = input("Enter someone's name, brand, object, country: ")
    # Use OpenAI's GPT-3 to generate a response
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=person_or_object + user_input,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    ).get("choices")[0].text

    # If the response contains information from Wikipedia, retrieve it using the Wikipedia API
    if "wikipedia" in response.lower():
        query = response.split("Wikipedia: ")[1]
        page = wiki_wiki.page(query)
        response = page.text
    print(response)
