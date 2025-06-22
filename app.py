from flask import Flask, render_template_string, request, jsonify
import time, random

app = Flask(__name__)

# Predefined responses
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
    # Simulate server processing/thinking time
    time.sleep(random.uniform(1.5, 3.0))

    question_lower = question.lower()
    if is_out_of_domain(question_lower):
        return "I'm designed to help with career and education guidance. Could you ask me about career paths or educational choices?"

    for key, reply in COMMON_RESPONSES.items():
        if all(word in question_lower for word in key.split()):
            return reply

    return "I'd be happy to help with career guidance! Could you tell me about your interests, favorite subjects, or what type of work environment you prefer?"

@app.route('/')
def home():
    return render_template_string('''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Career Guidance Chatbot</title>
        <style>
            body { font-family: Arial; margin: 0 auto; max-width: 800px; padding: 20px; }
            .chat-container { border: 1px solid #ddd; height: 400px; overflow-y: auto; padding: 10px; margin: 20px 0; }
            .message { padding: 10px; border-radius: 5px; margin: 10px 0; }
            .user { background-color: #e3f2fd; text-align: right; }
            .bot { background-color: #f5f5f5; }
            .loading { background-color: #fff3cd; color: #856404; font-style: italic; }
            input[type="text"] { width: 70%; padding: 10px; }
            button { padding: 10px 20px; background-color: #2196F3; color: white; border: none; cursor: pointer; }
            .example-btn { margin: 5px; padding: 5px 10px; background-color: #4CAF50; color: white; border: none; cursor: pointer; }
        </style>
    </head>
    <body>
        <h2>Career Guidance Chatbot</h2>
        <div class="chat-container" id="chat"></div>
        <input type="text" id="userInput" placeholder="Ask about your passions..." onkeypress="if(event.key==='Enter') sendMessage()">
        <button onclick="sendMessage()">Send</button>
        
        <div class="examples">
            <h3>Frequently asked Questions:</h3>
            <button class="example-btn" onclick="askExample('I love chemistry and math. What career should I consider?')">I want to be a lawyer what do you advice</button>
            <button class="example-btn" onclick="askExample('I enjoy biology and helping people. What career is good for me?')">Am good at Physic can I be a good doctor?</button>
            <button class="example-btn" onclick="askExample('Can I do law if I am not good at math?')">can I be a doctor if I love English and math only?</button>
            <button class="example-btn" onclick="askExample('I want to work in tech but do not know programming. What options do I have?')">what to do be be expert in computer</button>
        </div>

        <script>
            function sendMessage() {
                const input = document.getElementById('userInput');
                const message = input.value.trim();
                if (!message) return;

                addMessage(message, 'user');
                input.value = '';

                // Add loading effect
                const loadingDiv = document.createElement('div');
                loadingDiv.className = 'message bot loading';
                loadingDiv.id = 'loading';
                loadingDiv.textContent = '🤖 Thinking...';
                document.getElementById('chat').appendChild(loadingDiv);
                scrollChat();

                // Send to server
                const startTime = Date.now();
                fetch('/chat', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ message: message })
                })
                .then(res => res.json())
                .then(data => {
                    const elapsed = Date.now() - startTime;
                    const delay = Math.max(1500, 3000 - elapsed);  // delay ensures 1.5s minimum

                    setTimeout(() => {
                        document.getElementById('loading')?.remove();
                        addMessage(data.response, 'bot');
                        scrollChat();
                    }, delay);
                });
            }

            function askExample(text) {
                document.getElementById('userInput').value = text;
                sendMessage();
            }

            function addMessage(text, sender) {
                const chat = document.getElementById('chat');
                const msg = document.createElement('div');
                msg.className = 'message ' + sender;
                msg.textContent = text;
                chat.appendChild(msg);
            }

            function scrollChat() {
                const chat = document.getElementById('chat');
                chat.scrollTop = chat.scrollHeight;
            }
        </script>
    </body>
    </html>
    ''')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get('message', '')
    bot_response = generate_response(user_message)
    return jsonify({'response': bot_response})

if __name__ == '__main__':
    print("Career Chatbot running at http://localhost:5000")
    app.run(debug=True, host='0.0.0.0', port=5000)
