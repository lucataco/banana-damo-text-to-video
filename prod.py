# This file is used to verify your http server acts as expected
# Run it with `python3 test.py`
import base64
import banana_dev as banana

model_inputs = {'prompt': 'A panda eating bamboo on a rock.'}

api_key=""
model_key=""
res = banana.run(api_key, model_key, model_inputs)
out = res["modelOutputs"][0]

video_byte_string = out["mp4_bytes"]
video_encoded = video_byte_string.encode('utf-8')
video_bytes = base64.b64decode(video_encoded)

# save the video bytes to a file
with open('output.mp4', 'wb') as f:
    f.write(video_bytes)