from flask import Flask, request, jsonify
from dotenv import load_dotenv
from googletrans import Translator
import google.generativeai as palm
import os

load_dotenv()
API_KEY = os.environ.get('API_KEY')
palm.configure(api_key=str(API_KEY))
app = Flask(__name__)

models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
model = models[0].name
translator = Translator()


def translation(text, destination = 'en'):
    result = translator.translate(text, dest=destination).text
    
    return str(result)


@app.route('/')
def hello():
    return 'success'


@app.route('/chat', methods=['POST'])
def chat():
    params = request.get_json()
    question = params['question']
    response = ''

    try:
        question = translation(question) 
        response = palm.generate_text(
            model=model,
            prompt=question,
            temperature=0,
            max_output_tokens=500
        )
        return jsonify({"code": '200', "message": 'success', "data": translation(response.result, 'ko')})
     
    except:
        return jsonify({"message": '시스템 점검중입니다'})
    


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)