from dotenv import find_dotenv, load_dotenv
from transformers import pipeline
from langchain import PromptTemplate, LLMChain
from langchain.chat_models import ChatOpenAI
import os

load_dotenv(find_dotenv())

# img2text


def img2text(url):
    image_to_text = pipeline(
        "image-to-text", model="Salesforce/blip-image-captioning-base")

    text = image_to_text(url)[0]["generated_text"]

    print(text)
    return (text)


def generate_story(scenario):
    template = """
                You are a story teller: 
                You can generate a short story based on a simple narrative,
                the story should be not more than 20 words.

                CONTEXT: {scenario}
                """
    prompt = PromptTemplate(template=template, input_variables=["scenario"])

    story_llm = LLMChain(llm=ChatOpenAI(
        model_name="gpt-3.5-turbo", temperature=1, penai_api_key=os.environ['OPENAI_API_KEY']), prompt=prompt, verbose=True)

    story = story_llm.predict(scenario=scenario)
    print(story)
    return (story)


# img2text("./005-photo.jpg")
generate_story(img2text("./005-photo-2.jpg"))
