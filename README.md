# LLM-Ai-Practice  
### OpenAi offer free trial credit, which expires three months after you first created your OpenAI account.

Building Ai Agenet using LlamaIndex (LlamaIndex is Free & OpenSource)  

## Activate virtual env (setup)
(first command will create a pyvenv.cfg under ai folder)

### Mac:  
python3 -m venv ai  
source ai/bin/activate  (not sure)  

### Win:  
python -m venv ai  
source ai/Scripts/activate  

## Deactivate  
just type "deactivate"  

## install (pip/pip3)  
pip3 install llama-index pypdf python-dotenv pandas 

pip install llama-index-experimental


| Command | Description |
| --- | --- |
| pandas |  read csv file |
| pypdf | read pdf file |
| llama-index |  |
| python-dotenv |  |


## Chat GPT Key (Use your own Chat GPT key)
put it in .env file

https://platform.openai.com/api-keys

(OpenAi offer free trial credit, which expires three months after you first created your OpenAI account.)




## Data used:

1."World Population Data Set" by Kaggle (.csv file, account require)

https://www.kaggle.com/datasets/iamsouravbanerjee/world-population-dataset


2.Taiwan Wiki Page: Tool > Download as PDF

![Download from Wiki](https://github.com/sparklydavid/LLM-Ai-Practice/blob/main/rm-imgs/guide_wiki.png)


Issue Fix:

Venv setup if "access denied" try:

python -m venv /path/to/new/virtual/environment ai
