import gc
import torch
import base64
import pathlib
from modelscope.pipelines import pipeline
from modelscope.outputs import OutputKeys
from huggingface_hub import snapshot_download

# Init is ran on server startup
# Load your model to GPU as a global variable here using the variable name "model"
def init():
    global model
    model_dir = pathlib.Path('weights')
    snapshot_download('damo-vilab/modelscope-damo-text-to-video-synthesis', repo_type='model', local_dir=model_dir)
    model = pipeline('text-to-video-synthesis', model_dir.as_posix())

# Inference is ran for every server call
# Reference your preloaded global model variable here.
def inference(model_inputs:dict) -> dict:
    global model

    # Parse out your arguments
    prompt = model_inputs.get('prompt', None)
    if prompt == None:
        return {'message': "No prompt provided"}
    
    # Run the model
    input_text = {
        'text': prompt,
    }
    result_path = model(input_text,)[OutputKeys.OUTPUT_VIDEO]

    # read the mp4 file as bytes
    with open(result_path, 'rb') as file:
        mp4_bytes = file.read()

    # encode the mp4 file as base64
    base64_bytes = base64.b64encode(mp4_bytes)
    base64_string = base64_bytes.decode('utf-8')
    
    # create a response object with the base64-encoded mp4 file as the content
    response = {'mp4_bytes': base64_string}

    return response
