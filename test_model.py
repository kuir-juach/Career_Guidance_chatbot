from transformers import T5ForConditionalGeneration, T5Tokenizer
import torch
import os

class ModelTester:
    def __init__(self):
        model_path = './career_model' if os.path.exists('./career_model') else './fine_tuned_model'
        
        if os.path.exists(model_path):
            self.tokenizer = T5Tokenizer.from_pretrained(model_path)
            self.model = T5ForConditionalGeneration.from_pretrained(model_path)
            print(f"Loaded model from {model_path}")
        else:
            self.tokenizer = T5Tokenizer.from_pretrained("t5-small")
            self.model = TFT5ForConditionalGeneration.from_pretrained("t5-small")
            print("Using base T5 model (no fine-tuning found)")
    
    def generate_response(self, question):
        input_text = f"career guidance: {question}"
        input_ids = self.tokenizer.encode(input_text, return_tensors='tf', max_length=128, truncation=True)
        
        outputs = self.model.generate(
            input_ids, 
            max_length=256, 
            num_beams=4, 
            early_stopping=True,
            temperature=0.7
        )
        
        response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return response
    
    def test_model(self):
        test_questions = [
            "I love chemistry and math. What career should I consider?",
            "I enjoy biology and helping people. What career is good for me?",
            "Can I do law if I'm not good at math?",
            "I want to work in tech but don't know programming. What options do I have?",
            "What's the weather like today?"  # Out-of-domain test
        ]
        
        print("Testing Career Guidance Chatbot:")
        print("=" * 50)
        
        for i, question in enumerate(test_questions, 1):
            response = self.generate_response(question)
            print(f"\nTest {i}:")
            print(f"Q: {question}")
            print(f"A: {response}")
            print("-" * 50)

if __name__ == "__main__":
    tester = ModelTester()
    tester.test_model()