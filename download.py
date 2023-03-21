# In this file, we define download_model
# It runs during container build time to get model weights built into the container

import pathlib
from modelscope.pipelines import pipeline
from huggingface_hub import snapshot_download

def download_model():
    # do a dry run of loading the huggingface model, which will download weights
    model_dir = pathlib.Path('weights')
    snapshot_download('damo-vilab/modelscope-damo-text-to-video-synthesis', repo_type='model', local_dir=model_dir)

if __name__ == "__main__":
    download_model()