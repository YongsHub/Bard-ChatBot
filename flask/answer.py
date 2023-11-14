from dotenv import load_dotenv
from translation import translate
import google.generativeai as palm
import os

load_dotenv()
API_KEY = os.environ.get('API_KEY')
palm.configure(api_key=str(API_KEY))

models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
model = models[0].name

def get_answer(category, question):
    try:
        question = translate(category + '분야에서' + question + '예시는 없어도 돼') 
        response = palm.generate_text(
            model=model,
            prompt=question,
            temperature=0,
            max_output_tokens=500
            )
        return translate(response.result, 'ko')
     
    except:
        return '시스템 점검중입니다'