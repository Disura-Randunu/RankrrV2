from flask import request, jsonify
import services.text_analyzer as text_analyzer
import services.sentiment_analyzer as sentiment_analyzer

from __main__ import app

@app.route('/text/analyze', methods=['POST'])
def anayze_text():
    
    text = request.json['text']
    text = text.lower()
    
    basic_text = text_analyzer.get_basic_preprocessed_text(text)
    advanced_text = text_analyzer.get_advanced_preprocessed_text(text)
    ml_text = text_analyzer.get_ml_preprocessed_text(text)

    return jsonify({
        "status": True,
        "basic": {
            "cleaned_text": basic_text,
            "sentiment_scores": sentiment_analyzer.get_sentiment_scores(basic_text)
        },
        "advanced": {
            "cleaned_text": advanced_text,
            "sentiment_scores": sentiment_analyzer.get_sentiment_scores(advanced_text)
        },
        "ml": {
            "cleaned_text": ml_text,
            "sentiment_scores": sentiment_analyzer.get_sentiment_scores(ml_text)
        },
    })