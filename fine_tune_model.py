import tensorflow as tf
from transformers import TFT5ForConditionalGeneration, T5Tokenizer, AdamWeightDecay
import json

def fine_tune_model():
    tokenizer = T5Tokenizer.from_pretrained("t5-small")
    model = TFT5ForConditionalGeneration.from_pretrained("t5-small")
    
    with open('career_dataset.json', 'r') as f:
        data = json.load(f)
    
    inputs = [f"career guidance: {item['input']}" for item in data]
    targets = [item['output'] for item in data]
    
    input_encodings = tokenizer(inputs, truncation=True, padding=True, max_length=128, return_tensors='tf')
    target_encodings = tokenizer(targets, truncation=True, padding=True, max_length=256, return_tensors='tf')
    
    dataset = tf.data.Dataset.from_tensor_slices({
        'input_ids': input_encodings['input_ids'],
        'attention_mask': input_encodings['attention_mask'],
        'labels': target_encodings['input_ids']
    }).batch(2)
    
    optimizer = AdamWeightDecay(learning_rate=3e-5, weight_decay_rate=0.01)
    model.compile(optimizer=optimizer)
    
    callbacks = [
        tf.keras.callbacks.EarlyStopping(patience=2, restore_best_weights=True),
        tf.keras.callbacks.ReduceLROnPlateau(factor=0.5, patience=1)
    ]
    
    model.fit(dataset, epochs=5, callbacks=callbacks, verbose=1)
    
    model.save_pretrained('./fine_tuned_model')
    tokenizer.save_pretrained('./fine_tuned_model')
    print("Fine-tuned model saved!")

if __name__ == "__main__":
    fine_tune_model()