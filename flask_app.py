from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Simple career guidance responses
COMMON_RESPONSES = {
    "chemistry math": "Based on your interest in chemistry and math, consider careers in chemical engineering, pharmacology, materials science, or data science.",
    "biology help people": "Your combination of biology interest and desire to help people makes you ideal for healthcare careers like medicine, nursing, physical therapy, or biomedical research.",
    "law math": "Absolutely! Law requires strong analytical thinking, reading comprehension, and communication skills rather than advanced math.",
    "tech programming": "Tech careers without programming include product management, technical writing, UX research, digital marketing, data analysis, or tech sales.",
    "art creative": "Creative talents can lead to graphic design, web design, animation, marketing, architecture, interior design, or multimedia production."
}

def is_out_of_domain(question):
    out_keywords = ['weather', 'cook', 'recipe', 'joke', 'game', 'sport', 'movie']
    return any(keyword in question.lower() for keyword in out_keywords)

def generate_response(question):
    if is_out_of_domain(question):
        return "I'm designed to help with career and education guidance. Could you ask me about career paths or educational choices?"
    
    question_lower = question.lower()
    
    for key, response in COMMON_RESPONSES.items():
        if all(word in question_lower for word in key.split()):
            return response
    
    return "I'd be happy to help with career guidance! Could you tell me about your interests, favorite subjects, or what type of work environment you prefer?"

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>🎓 Career Guidance Chatbot</title>
        <style>
            body { font-family: Arial, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; }
            .chat-container { border: 1px solid #ddd; height: 400px; overflow-y: scroll; padding: 10px; margin: 20px 0; }
            .message { margin: 10px 0; padding: 10px; border-radius: 5px; }
            .user { background-color: #e3f2fd; text-align: right; }
            .bot { background-color: #f5f5f5; }
            input[type="text"] { width: 70%; padding: 10px; }
            button { padding: 10px 20px; background-color: #4CAF50; color: white; border: none; cursor: pointer; }
            .examples { margin: 20px 0; }
            .example-btn { margin: 5px; padding: 5px 10px; background-color: #2196F3; color: white; border: none; cursor: pointer; }
        </style>
    </head>
    <body>
        <h1>🎓 Career Guidance Chatbot</h1>
        <p>Ask me about career paths based on your interests!</p>
        <div class="status">✅ Career Guidance System Ready</div>
        
        <div class="chat-container" id="chat"></div>
        
        <div>
            <input type="text" id="userInput" placeholder="Ask about your career interests..." onkeypress="if(event.key==='Enter') sendMessage()">
            <button onclick="sendMessage()">Send</button>
        </div>
        
        <div class="examples">
            <h3>Example Questions:</h3>
            <button class="example-btn" onclick="askExample('I love chemistry and math. What career should I consider?')">Chemistry & Math</button>
            <button class="example-btn" onclick="askExample('I enjoy biology and helping people. What career is good for me?')">Biology & Helping</button>
            <button class="example-btn" onclick="askExample('Can I do law if I am not good at math?')">Law Career</button>
            <button class="example-btn" onclick="askExample('I want to work in tech but don not know programming. What options do I have?')">Tech Career</button>
        </div>

        <script>
            function sendMessage() {
                const input = document.getElementById('userInput');
                const message = input.value.trim();
                if (!message) return;
                
                addMessage(message, 'user');
                input.value = '';
                
                fetch('/chat', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({message: message})
                })
                .then(response => response.json())
                .then(data => addMessage(data.response, 'bot'));
            }
            
            function askExample(question) {
                document.getElementById('userInput').value = question;
                sendMessage();
            }
            
            function addMessage(text, sender) {
                const chat = document.getElementById('chat');
                const div = document.createElement('div');
                div.className = 'message ' + sender;
                div.textContent = text;
                chat.appendChild(div);
                chat.scrollTop = chat.scrollHeight;
            }
        </script>
    </body>
    </html>
    '''

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    message = data.get('message', '')
    response = generate_response(message)
    return jsonify({'response': response})

if __name__ == '__main__':
    print("Career Guidance Chatbot")
    print("Access at: http://localhost:5000")
    app.run(debug=True, host='0.0.0.0', port=5000)