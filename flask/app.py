from flask import Flask, request, jsonify
from bardapi import BardCookies
import pandas as pd

app = Flask(__name__)

cookie_dict = {
    "__Secure-1PSID": "",
    "__Secure-1PSIDCC": "",
    "__Secure-1PAPISID": ""
}

bard = BardCookies(cookie_dict=cookie_dict)


@app.route('/')
def hello():
    return 'success'


@app.route('/chat', methods=['POST'])
def chat():
    params = request.get_json()
    question = params['question']
    response = ''

    try:
        response = bard.get_answer(question)
        df = pd.DataFrame(response['choices'])
    except:
        print(response)
        return jsonify({"message": '시스템 점검중입니다'})
    
    return jsonify({"code": '200', "message": 'success', "data": df['content'][0]})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)