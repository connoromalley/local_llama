# pip install llama-cpp-python
#model_path = # download one of the models, store it in this folder

from llama_cpp import Llama 

# Load model directly
from transformers import AutoModel
model = AutoModel.from_pretrained("TheBloke/dolphin-2.6-mixtral-8x7b-GGUF")

#llm = Llama(model_path=model_path)
llm = model 

# chat

llm("who is steph curry")


