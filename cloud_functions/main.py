#main.py
import functions_framework
import vertexai
from vertexai.preview.language_models import TextGenerationModel
import json

# Replace with your project ID !!!
PROJECT_ID = ""

def interview(text:str):
    parameters = {
        "temperature": 0.2,
        "max_output_tokens": 256,   
        "top_p": .8,                
        "top_k": 40,                 
    }
    vertexai.init(project=PROJECT_ID)
    model = TextGenerationModel.from_pretrained("text-bison@001")
    response = model.predict(
        f"Make a short summary : {text}",
        **parameters,
    )
    print(f"Response from Model: {response.text}")
    return response.text

@functions_framework.http
def hello_vertex(request):
    parsed_data = (str(request.data)).replace('"',"").replace("'","").replace(",","").replace("\n","")
    model_response =  interview(parsed_data)
    headers = {"Access-Control-Allow-Origin": "*"}
    return (model_response, 200, headers)