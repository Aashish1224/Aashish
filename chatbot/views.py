from django.http import JsonResponse
from django.shortcuts import render

def chatbot_view(request):
    return render(request, 'chatbot/index.html')

def get_response(request):
    user_message = request.GET.get('message', '')
    
    # Simple chatbot response logic
    responses = {
        "what is your name": ["I'm TechVista!",  "You can call me ChatBot.",   "My name is AI Assistant. 😊"],
        "what can you do": "I can chat with you, answer questions, and provide information!", 
        "hi": "Hey Hi",
        "hello": "Hi there! How can I help you?",
        "how are you": "I'm just a TechVista bot, but I'm doing great!",
        "bye": "Goodbye! Have a great day!",
        
       
    }
    
    bot_response = responses.get(user_message.lower(), "I'm not sure how to respond to that.")
    
    return JsonResponse({'response': bot_response})
