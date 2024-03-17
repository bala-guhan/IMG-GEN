from langchain.llms import OpenAI
from langchain.agents import load_tools, initialize_agent
from langchain.memory import ConversationBufferMemory
import os
from secret_key import *
import streamlit as st
from io import BytesIO
import openai

os.environ["SCENEX_API_KEY"] = scenex_api_key
os.environ["OPENAI_API_KEY"] = openai_api_key

st.header("--------------------------IMG-GEN-----------------------",)
st.subheader("---------------------Text-to-Image Generation Bot-------------------")
st.subheader("----------Create Stunning Images from Text with Ease----------")
st.image("DripAI-Background.png")

tb1, tb2 = st.tabs(["Image Generation", "Image explanation"])
with tb1:
    st.header("Image generation")
    st.write("Write down your prompts to give it visual independence:sparkles: :rainbow:")
    def generate_image(input_text):
        response = openai.Image.create(
            prompt = input_text,
            n = 1,
            size = "512x512"
        )
        image_url = response['data'][0]['url']
        return image_url
    prompt = st.text_input("Enter your prompt here")
    if prompt is not None:
        if st.button("Generate Image"):
            st.code("for i in range(n): print('Image generation')")
            image = generate_image(prompt)
            st.image(image ,caption= "image gen powered by Dall-E3")
with tb2:
    tab1, tab2 = st.tabs(["Image URL", "Image File upload"])

    with tab1:
        st.header("Scene explanation using Image URL")
        st.write("Paste any image URL into the tab in order find what going on in there!:sparkles:")
        image = st.text_input("Enter the image url")
        tools = load_tools(["sceneXplain"])
        llm = OpenAI(model="gpt-3.5-turbo-instruct", temperature=0)
        memory = ConversationBufferMemory(memory_key="chat_history")
        agent = initialize_agent(tools, llm, memory=memory, agent_type="conversational-react-description",verbose=True)
        def imagx(image):
            output = agent.run(
                input=(
                    f"What is in the image {image}, Describe who is present in the image ,what is happening in the image"
                )
            )
            return output
        res = imagx(image)
        st.write(res)

    with tab2:
        st.header("Scene explanation using Image File upload")
        st.write("Upload any of your Images to get a expert comment on it!:sparkles:")
        image = st.file_uploader("Upload file", type=["png", "jpg", "jpeg"])
        show_file = st.empty()

        if not image:
            show_file.info("Please upload a file of type : {} ".format(' '.join(["png", "jpg", "jpeg"])))

        if isinstance(image, BytesIO):
            show_file.image(image)

        tools = load_tools(["sceneXplain"])

        llm = OpenAI(model="gpt-3.5-turbo-instruct", temperature=0)
        memory = ConversationBufferMemory(memory_key="chat_history")
        agent = initialize_agent(tools, llm, memory=memory, agent_type="conversational-react-description", verbose=True)
        def imagx(image):
            output = agent.run(
                input=(
                    f"What is in the image {image}, Describe who is present in the image ,what is happening in the image"
                )
            )
            return output
        res = imagx(image)
        st.write(res)

