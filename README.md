# Career Guidance Chatbot

## Project Overview

This project presents a comprehensive Career Guidance Chatbot built using TensorFlow and Flask, designed to provide personalized career advice to students and professionals. The system leverages advanced Natural Language Processing (NLP) techniques, utilizing the T5 transformer model, to deliver domain-specific career guidance across multiple fields, including STEM, healthcare, business, creative arts, and technology.

The system supports a wide array of career domains, including:

* STEM (Science, Technology, Engineering, Mathematics)
* Healthcare and Medicine
* Creative Arts and Design
* Business and Economics
* Information Technology

By utilizing modern NLP techniques, the chatbot interprets user queries and provides tailored guidance aligned with the user’s interests and goals.

## Dataset

The chatbot is trained on a curated dataset of 450+ question-answer pairs. These cover a spectrum of academic backgrounds and career concerns. The data structure emphasizes clarity, domain specificity, and out-of-domain detection.

Sample data points include:

* **Question:** *I love chemistry and math. What career should I consider?*
  **Answer:** *Consider chemical engineering, materials science, or pharmacology.*

* **Question:** *What can I do with an interest in technology and design?*
  **Answer:** *Careers such as UX design, software engineering, and product development are suitable.*


## Data Preprocessing

Before training, the dataset undergoes the following preprocessing steps:

* Lowercasing and text normalization
* Removal of special characters
* Tokenization using the T5 tokenizer
* Padding and truncation to standardized sequence lengths

These steps ensure compatibility with the T5 architecture and improve model generalization.



## Model Architecture

The core model used in this chatbot is **T5-small**, a transformer-based encoder-decoder architecture developed by Google Research. Key specifications include:

* **Base Model:** T5-small (approx. 60 million parameters)
* **Tokenizer:** T5Tokenizer from Hugging Face Transformers
* **Framework:** TensorFlow 2.x
* **Generation Strategy:** Beam Search (num\_beams=4)

The model has been fine-tuned on the custom dataset to optimize for relevance and accuracy of responses in the domain of career guidance.



## Hyperparameter Configuration

| Parameter         | Value      |
| ----------------- | ---------- |
| Learning Rate     | 3e-5       |
| Batch Size        | 2          |
| Max Input Length  | 128 tokens |
| Max Output Length | 256 tokens |
| Epochs            | 3–5        |

Advanced fine-tuning includes callbacks such as early stopping and dynamic learning rate adjustments.


## Evaluation Metrics

The performance of the chatbot is assessed using multiple evaluation metrics:

* **BLEU Score:** Evaluates the precision of predicted answers by comparing n-gram overlap.
* **ROUGE-1 / ROUGE-2 / ROUGE-L:** Measures the recall and precision of key words and phrases.
* **F1 Score:** Balances precision and recall in a single metric.
* **Manual Testing:** Includes qualitative review of answers and domain-relevance checks.

Evaluation scripts can be executed using:

```bash
python evaluate_model.py
```


## Project Structure

```
Chat_bot/
├── dataset.py             # Dataset generation script
├── train_model.py         # Base training script
├── fine_tune_model.py     # Enhanced training with callbacks
├── evaluate_model.py      # Evaluation using BLEU, ROUGE
├── test_model.py          # Run test queries through the model
├── app.py                 # Gradio/Flask web interface
└── README.md              # Project documentation
```
## Link to the Video:
https://youtu.be/OrswQLAdkYU

## How to Run

### 1. Install Dependencies

```bash
pip install streamlit transformers rouge-score sacrebleu
```

### 2. Generate Dataset

```bash
python dataset.py
```

### 3. Train the Model

```bash
python train_model.py
```

For advanced fine-tuning:

```bash
python fine_tune_model.py
```

### 4. Launch the Web Interface

```bash
python app.py
```

The chatbot will be accessible via a local browser interface.


## Testing

The system supports a test script for simulating real-world queries and verifying model output:

```bash
python test_model.py
```

This includes both in-domain and out-of-domain question testing.

---

## Requirements

The following Python packages are required:

```
transformers>=4.21.0
tensorflow>=2.10.0
gradio>=3.35.0
rouge-score>=0.1.2
sacrebleu>=2.3.1
numpy>=1.21.0
```

Install via:

```bash
pip install -r requirements.txt
```

---

## Future Improvements

To further enhance the chatbot’s capabilities and usability, the following features are planned:

* **Voice Integration:** Enable voice-based input using speech-to-text APIs for hands-free interaction.
* **User Personalization:** Store interaction history and preferences to deliver more tailored career suggestions.
* **Multilingual Support:** Expand the chatbot to support major languages, increasing accessibility.
* **Dataset Expansion:** Scale the dataset to over 1000 Q\&A pairs for better domain coverage and response diversity.
* **Mobile Support:** Optimize interface for mobile responsiveness and offline access.




