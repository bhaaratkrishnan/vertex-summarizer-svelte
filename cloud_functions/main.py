# Copyright 2022 Google LLC

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#     https://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import functions_framework  # Import the functions_framework library for HTTP functions
import vertexai  # Import the vertexai library for AI model handling
from vertexai.preview.language_models import TextGenerationModel  # Import the TextGenerationModel from vertexai
import json  # Import the JSON library for working with JSON data

# Replace with your project ID !!!
PROJECT_ID = ""  

# Define a function named "summarize" that takes a text input and generates a response
def summarize(text: str):
    parameters = {
        "temperature": 0.2,          # Control the randomness of the generated text
        "max_output_tokens": 256,    # Limit the maximum number of output tokens
        "top_p": 0.8,               # Set a nucleus sampling threshold
        "top_k": 40,                # Set a top-k sampling threshold
    }

    # Initialize the Vertex AI project with the provided project ID
    vertexai.init(project=PROJECT_ID)

    # Load the pre-trained TextGenerationModel named "text-bison@001"
    model = TextGenerationModel.from_pretrained("text-bison@001")

    # Generate a response by providing the input text and model parameters
    response = model.predict(
        f"Make a short summary : {text}",  # Format the input text
        **parameters,  # Pass the defined parameters
    )

    # Print the response from the model
    print(f"Response from Model: {response.text}")

    # Return the generated response as text
    return response.text

# Define an HTTP function using the functions_framework library
@functions_framework.http
def hello_vertex(request):
    # Process and clean the input data received from the HTTP request
    parsed_data = (str(request.data)).replace('"', "").replace("'", "").replace(",", "").replace("\n", "")

    # Call the "summarize" function with the cleaned input data to generate a model response
    model_response = summarize(parsed_data)

    # Define headers for the HTTP response to allow cross-origin requests
    headers = {"Access-Control-Allow-Origin": "*"}

    # Return the model response, HTTP status code 200 (OK), and the headers
    return (model_response, 200, headers)
