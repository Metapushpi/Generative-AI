Gemini Diet Planner 🍎🥦🥛

Overview
The Gemini Diet Planner is a Streamlit application that allows users to input a text prompt and upload an image. The application uses Google Gemini’s Generative AI model to analyze the uploaded image and provide a diet plan explanation in response to the provided prompt. The AI model evaluates the uploaded image and offers diet recommendations in a structured format.

Features
Text Prompt: Allows users to input a custom prompt.
Image Upload: Supports image uploads in JPG, JPEG, and PNG formats.
Generative AI Model (Google Gemini): Uses Google's Gemini-1.5 model to generate responses based on the image content.
Diet Plan Analysis: The AI analyzes the image and responds with a diet plan, indicating the quantity and types of food items to take.
Requirements
To run this app, ensure you have the following installed:

Python 3.7+
Streamlit
Google Generative AI SDK
Pillow (PIL)
dotenv

You can install the necessary dependencies using the following command:


pip install streamlit google-generativeai pillow python-dotenv

Setup
Clone the repository:

bash
Copy code
git clone <repository-url>
cd <repository-folder>
Set up environment variables:

Create a .env file in the project root.
Add your Google API key:
makefile
Copy code
GOOGLE_API_KEY=your_google_api_key_here
Run the Streamlit app:

bash
Copy code
streamlit run app.py
This will start the application, and you can access it via your web browser at http://localhost:8501.

How to Use
Enter a prompt: Type a prompt in the provided input box to guide the AI response.
Upload an image: Select an image (JPG, JPEG, PNG) that contains a diet chart or food-related information.
Click the 'Explain the image to me 👇' button: Once the image is uploaded and the prompt is set, click the button to receive the AI-generated response.
Explanation of the AI Response
The AI will provide a response in the following format:

How many items the person should take.
How much of each item the person should take.
The AI utilizes the uploaded image and the input prompt to generate a detailed explanation based on its analysis.

Example Workflow
Enter Prompt: "Analyze the diet plan."
Upload Image: Upload an image that contains a diet chart.
Click 'Explain the image to me 👇': Get a response in the format of a diet plan explanation.
Error Handling
If no image is uploaded, the app will prompt the user to upload an image before submitting.
If there’s an issue with the image processing or API interaction, an error message will be displayed.
License
This project is open source and available under the MIT License.
