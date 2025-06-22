# 🎓 Career Guidance Chatbot

A domain-specific chatbot for career guidance using fine-tuned T5 transformer model with TensorFlow.

## 🎯 Overview

**Domain**: Education (Career Guidance)  
**Target Users**: High school Students.
**Model**: Fine-tuned T5 with TensorFlow

## 📁 Project Structure

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

## 🚀 Quick Start

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

Visit: `http://localhost:5000`

## 📊 Dataset

The dataset contains 12 career guidance Q&A pairs covering:

- STEM fields (chemistry, math, biology)
- Technology careers
- Creative fields
- Business and economics
- Out-of-domain handling

## 🧠 Model Training

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

## 📈 Evaluation

```bash
python evaluate_model.py
```

Metrics:

- **BLEU Score**: N-gram overlap measurement
- **ROUGE-1/2/L**: Recall and precision evaluation
- **F1 Score**: Harmonic mean of precision and recall

## 🧪 Testing

```bash
python test_model.py
```

Tests model with sample questions including out-of-domain handling.

## 💬 Example Interactions

```
Q: I love chemistry and math. What career should I consider?
A: Based on your interest in chemistry and math, consider careers in chemical engineering, pharmacology, materials science, or data science.
<<<<<<< HEAD
Q: Can I do law if I'm not good at math?
A: Absolutely! Law requires strong analytical thinking, reading comprehension, and communication skills rather than advanced math.
=======

Q: Can I do law if I'm not good at math?
A: Absolutely! Law requires strong analytical thinking, reading comprehension, and communication skills rather than advanced math.

>>>>>>> e45b47b (updated)
Q: What's the weather like today?
A: I'm designed to help with career and education guidance. Could you ask me about career paths or educational choices?
```

## 🔧 Configuration

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

## 📋 Requirements

```
transformers>=4.21.0
tensorflow>=2.10.0
gradio>=3.35.0
rouge-score>=0.1.2
sacrebleu>=2.3.1
numpy>=1.21.0
```

## 🎬 Demo Video Guide

1. **Dataset Creation** (1 min): Show `dataset.py` output
2. **Model Training** (2 min): Demonstrate `train_model.py` process
3. **Evaluation** (1 min): Run `evaluate_model.py` and show metrics
4. **Live Demo** (3 min): Use `app.py` interface with various questions
5. **Out-of-Domain** (1 min): Test non-career questions

<<<<<<< HEAD
## Performance
=======
## 🔍 Performance
>>>>>>> e45b47b (updated)

Expected results after training:

- BLEU Score: ~0.15-0.25
- ROUGE-1: ~0.25-0.35
- ROUGE-L: ~0.20-0.30
- Domain accuracy: ~80-90%

<<<<<<< HEAD
## Troubleshooting
=======
## 🚨 Troubleshooting
>>>>>>> e45b47b (updated)

**TensorFlow Issues:**

```bash
pip install --upgrade tensorflow
```

**Memory Errors:**

- Reduce batch size in training scripts
- Use T5-small instead of larger models

**Model Not Found:**

- Ensure training completed successfully
- Check `./career_model` or `./fine_tuned_model` directories exist

<<<<<<< HEAD
## Usage
=======
## 📞 Usage
>>>>>>> e45b47b (updated)

1. **Generate dataset**: Creates training data
2. **Train model**: Fine-tune T5 for career guidance
3. **Evaluate**: Measure performance with metrics
4. **Test**: Verify functionality
5. **Deploy**: Launch web interface

Built for helping students make informed career choices! 🎓
