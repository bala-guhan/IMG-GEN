## Image Generation Bot Readme

### Overview
This image generation bot is designed to transform text into corresponding images and provide explanations for given images. It utilizes the power of pre-trained Language Models (LLMs) such as DALL-E3 and OpenAI's SceneX API to achieve these tasks seamlessly.

### Features
1. **Text-to-Image Generation**: The bot can transform text inputs into images using the DALL-E3 model through OpenAI's API access. Various Langchain tools are employed to enhance the output quality.
2. **Image Understanding and Explanation**: Given an image, the bot can provide detailed explanations of the scene depicted in the image. This is facilitated by pre-trained LLMs from OpenAI and the SceneX API.

### Installation and Dependencies
- Python 3.x: Ensure you have the latest version of Python installed on your system.
- Key Dependencies: Install the required modules by running:
  ```
  pip install -r requirements.txt
  ```
- Python IDE: Use a Python integrated development environment (IDE) such as Visual Studio Code, PyCharm, etc., to run the bot files.

### Setup Instructions
1. **Obtain API Keys**:
   - Sign up for accounts with OpenAI [OpenAI-api-key](https://platform.openai.com/api-keys) and SceneX [Scenex-api-key](https://scenex.jina.ai/api) to obtain API access.
   - After signing up, obtain API keys for both platforms.
   - Place these API keys in the specified location in the `secret_key.py` file.

2. **Verify Credits**:
   - Ensure that you have eligible credits available for OpenAI API usage.
   - Check your available credits [HERE](https://platform.openai.com/usage).

3. **Run the Bot**:
   - Open your terminal and navigate to the directory where the bot files are located.
   - Run the bot file using Streamlit:
     ```
     streamlit run ImgX.py
     ```

4. **Usage**:
   - Once the bot is running locally, you can interact with it through the provided interface.
   - For text-to-image generation, input your desired text and let the bot generate the corresponding image.
   - For image understanding and explanation, provide the URL or upload the image file, and the bot will analyze and explain the scene depicted.

### Note:
- OpenAI provides a limited free trial period, after which premium charges may apply. Ensure you have necessary credits for extended usage.
- Existing OpenAI accounts may not be eligible for the free trial. Check your eligibility before proceeding.
