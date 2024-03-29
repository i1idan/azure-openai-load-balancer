from openai_load_balancer import initialize_load_balancer
from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional
from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv
import os
import json



# Load environment variables from .env file
load_dotenv()

# Fetch the environment variable as a string
endpoints_str = os.getenv("ENDPOINTS")

# Convert the string representation of list into an actual list of dictionaries
ENDPOINTS = json.loads(endpoints_str)

# Now you can use the 'endpoints' list in your code
print(ENDPOINTS)


MODEL_ENGINE_MAPPING = {
    "gpt-3.5-turbo": "gpt-3.5-turbo", 
    "text-embedding-ada-002": "text-embedding-ada-002"
    # Add more mappings as needed
}


openai_load_balancer = initialize_load_balancer(
    endpoints=ENDPOINTS, model_engine_mapping=MODEL_ENGINE_MAPPING)


class ChatCompletionRequest(BaseModel):
    messages: List[Dict[str, Any]] =  [ {"role": "system", "content": "You are a helpful assistant."},
                                       {"role": "user", "content": "Hello! This is a request."} ]
    temperature: Optional[float] = 0.7
    max_tokens: Optional[int] = 300
    stop: Optional[List[str]] = None


app = FastAPI()



@app.post("/chat_completion")
async def chat_completion(request_body: ChatCompletionRequest):
    try:
        completion_params = {
            "temperature": request_body.temperature,
            "max_tokens": request_body.max_tokens,
            "stop": request_body.stop
        }
        response = openai_load_balancer.ChatCompletion.create(
            messages=request_body.messages, **completion_params)
        return response
    except Exception as e:
        raise HTTPException(status_code=503, detail=str(e))


class EmbeddingRequest(BaseModel):
    input: str =  "your chunk of text"


@app.post("/embedding")
async def embedding(request_body: EmbeddingRequest):
    try:
        embedding_params = {
            "input": request_body.input,
        }
        response = openai_load_balancer.Embedding.create(
            **embedding_params)
        return response
    except Exception as e:
        raise HTTPException(status_code=503, detail=str(e))