from transformers import BartForConditionalGeneration, BartTokenizer

def load_model(model_name='facebook/bart-large-cnn'):
    try:
        tokenizer = BartTokenizer.from_pretrained(model_name)
        model = BartForConditionalGeneration.from_pretrained(model_name)
        return model, tokenizer
    except Exception as e:
        print(f"Error loading model {model_name}: {e}")
        raise

model_name = 'facebook/bart-large-cnn'
model, tokenizer = load_model(model_name)

def summarize(text: str) -> str:
    """
    Placeholder for the actual summarization logic.

    Parameters:
    - text: str, the text to be summarized

    Returns:
    - str, the summary of the text
    """
    try:
        
        text = text.strip()
        
        preprocessed_text = preprocess_text(text)
        summary = summarize_text(model, tokenizer, preprocessed_text)
        return summary
    except Exception as e:
        print(e)
        return ""

def preprocess_text(text):
    return text.strip()

def summarize_text(model, tokenizer, text, max_length=100):
    try:
        tokenizer.pad_token = tokenizer.eos_token

        inputs = tokenizer("summarize: " + text, return_tensors='pt', max_length=512, truncation=True, padding=True)

        summary_ids = model.generate(
            inputs['input_ids'], 
            attention_mask=inputs['attention_mask'], 
            max_length=max_length, 
            min_length=40, 
            length_penalty=2.0, 
            num_beams=4, 
            early_stopping=True,
            pad_token_id=tokenizer.eos_token_id,
            no_repeat_ngram_size=3
        )

        summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
        return summary
    except Exception as e:
        print(f"Error during summarization: {e}")
        raise

def load_model(model_name='facebook/bart-large-cnn'):
    try:
        tokenizer = BartTokenizer.from_pretrained(model_name)
        model = BartForConditionalGeneration.from_pretrained(model_name)
        return model, tokenizer
    except Exception as e:
        print(f"Error loading model {model_name}: {e}")
        raise
