import tensorflow as tf
from transformers import TFT5ForConditionalGeneration, T5Tokenizer
from rouge_score import rouge_scorer
from sacrebleu import BLEU
import json
import numpy as np

class ModelEvaluator:
    def __init__(self, model_path='./career_model'):
        self.tokenizer = T5Tokenizer.from_pretrained(model_path)
        self.model = TFT5ForConditionalGeneration.from_pretrained(model_path)
        
    def generate_response(self, question):
        input_text = f"career guidance: {question}"
        input_ids = self.tokenizer.encode(input_text, return_tensors='tf', max_length=128, truncation=True)
        
        outputs = self.model.generate(input_ids, max_length=256, num_beams=4, early_stopping=True)
        response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return response
    
    def calculate_bleu(self, predictions, references):
        bleu = BLEU()
        formatted_refs = [[ref] for ref in references]
        score = bleu.corpus_score(predictions, formatted_refs)
        return score.score
    
    def calculate_rouge(self, predictions, references):
        scorer = rouge_scorer.RougeScorer(['rouge1', 'rouge2', 'rougeL'], use_stemmer=True)
        scores = {'rouge1': [], 'rouge2': [], 'rougeL': []}
        
        for pred, ref in zip(predictions, references):
            score = scorer.score(ref, pred)
            scores['rouge1'].append(score['rouge1'].fmeasure)
            scores['rouge2'].append(score['rouge2'].fmeasure)
            scores['rougeL'].append(score['rougeL'].fmeasure)
        
        return {k: np.mean(v) for k, v in scores.items()}
    
    def evaluate(self):
        with open('career_dataset.json', 'r') as f:
            data = json.load(f)
        
        test_data = data[:5]  # Use first 5 for evaluation
        predictions = []
        references = []
        
        for item in test_data:
            pred = self.generate_response(item['input'])
            predictions.append(pred)
            references.append(item['output'])
        
        bleu_score = self.calculate_bleu(predictions, references)
        rouge_scores = self.calculate_rouge(predictions, references)
        
        results = {
            'BLEU': bleu_score,
            'ROUGE-1': rouge_scores['rouge1'],
            'ROUGE-2': rouge_scores['rouge2'],
            'ROUGE-L': rouge_scores['rougeL']
        }
        
        print("Evaluation Results:")
        for metric, score in results.items():
            print(f"{metric}: {score:.4f}")
        
        return results

if __name__ == "__main__":
    evaluator = ModelEvaluator()
    evaluator.evaluate()