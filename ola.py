from langchain_community.llms import Ollama
import time

llm = Ollama(model="gemma")

start_time = time.time()
response = llm.invoke("I am thinking about raining some chickens to get eggs, is this ethical or not?")
end_time = time.time()

print(response)
print("time taken:",end_time-start_time)