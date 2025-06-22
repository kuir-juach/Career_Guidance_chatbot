# Career Guidance Chatbot

## Overview
This project presents a comprehensive Career Guidance Chatbot built using TensorFlow and Flask, designed to provide personalized career advice to students and professionals. The system leverages advanced Natural Language Processing (NLP) techniques, utilizing the T5 transformer model, to deliver domain-specific career guidance across multiple fields, including STEM, healthcare, business, creative arts, and technology.

**Domain**: Education (Career Guidance)  
**Target Users**: High school Students.
**Model**: Fine-tuned T5 with TensorFlow

##  Project Structure

```
Chat_bot/
├── dataset.py             # Create training dataset
├── train_model.py         # Basic model training
├── fine_tune_model.py     # Advanced fine-tuning
├── evaluate_model.py      # Model evaluation (BLEU, ROUGE)
├── test_model.py          # Test model functionality
├── app.py                 # Gradio web interface
└── README.md              # Documentation
```

##  Quick Start

### 1. Install Dependencies

```bash
pip install streamlit transformers rouge-score sacrebleu
```

### 2. Run Flask App

```bash
python app.py
```

### 2. Generate Dataset

```bash
python dataset.py
```

### 3. Train Model

```bash
python train_model.py
```

### 4. Launch Flask Interface

```bash
python app.py
```



## Dataset

The dataset contains 12 career guidance Q&A pairs covering:

- STEM fields (chemistry, math, biology)
- Technology careers
- Creative fields
- Business and economics
- Out-of-domain handling

## Model Training

### Basic Training

```bash
python train_model.py
```

- Uses T5-small base model
- 3 epochs, batch size 2
- Saves to `./career_model`

### Advanced Fine-tuning

```bash
python fine_tune_model.py
```

- Includes callbacks and optimization
- 5 epochs with early stopping
- Saves to `./fine_tuned_model`

## Evaluation

```bash
python evaluate_model.py
```

Metrics:

- **BLEU Score**: N-gram overlap measurement
- **ROUGE-1/2/L**: Recall and precision evaluation
- **F1 Score**: Harmonic mean of precision and recall

## Testing

```bash
python test_model.py
```

Tests model with sample questions including out-of-domain handling.

```

## Configuration

### Hyperparameters

- Learning rate: 3e-5
- Batch size: 2
- Max input length: 128
- Max output length: 256
- Epochs: 3-5

### Model Architecture

- Base: T5-small (60M parameters)
- Framework: TensorFlow
- Tokenizer: T5Tokenizer
- Generation: Beam search (num_beams=4)

## Requirements

```
transformers>=4.21.0
tensorflow>=2.10.0
gradio>=3.35.0
rouge-score>=0.1.2
sacrebleu>=2.3.1
numpy>=1.21.0
```
