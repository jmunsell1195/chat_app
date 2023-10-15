from django.shortcuts import render, HttpResponse
from llama_cpp import Llama
from django.http import JsonResponse

LLAMA_PATH = '/home/jeremy/Desktop/llama-2-13b.Q4_K_S.gguf'

model = Llama(model_path=LLAMA_PATH)

def generate(model,prompt):
    output = model(f"Q: {prompt} A: ", max_tokens=32, stop=["Q:", "\n"], echo=True)["choices"][0]["text"]
    return output

# Create your views here.
def llm_response(request):
    if request.method == "POST":
        prompt = request.POST["message"]
        output = generate(model,prompt)
        return JsonResponse({"message":prompt,"response":output})
    else:
        return render(request,"llm/UI.html")