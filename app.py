from flask import Flask, request, jsonify, render_template
from transformers import AutoModelForSequenceClassification, AutoTokenizer, pipeline

app = Flask(__name__)

# Path to your local model directory
model_path = r"C:\Users\manjj\Desktop\AllInOne\swm\finiteautomata\models"

# Load the model and tokenizer
model = AutoModelForSequenceClassification.from_pretrained(model_path)
tokenizer = AutoTokenizer.from_pretrained(model_path)

# Initialize the sentiment analysis pipeline
sentiment_analysis = pipeline("text-classification", model=model, tokenizer=tokenizer)

@app.route('/')
def home():
    # Render the HTML template
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    if request.method == 'POST':
        data = request.get_json(force=True)  # Force JSON parsing
        text = data['text']
        try:
            # Perform sentiment analysis
            results = sentiment_analysis(text)
            sentiment = results[0]['label']
            # Prepare and send the JSON response
            result = {'tweet': text, 'sentiment': sentiment}
            return jsonify(result)
        except Exception as e:
            # Handle exceptions and errors
            return jsonify({'error': str(e)})

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
