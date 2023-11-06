from flask import Flask
from bardapi import BardCookies

app = Flask('bard_bot')

cookie_dict = {
    "__Secure-1PSID": "",
    "__Secure-1PSIDCC": ",
    "__Secure-1PAPISID": ""
}

bard = BardCookies(cookie_dict=cookie_dict)

response = bard.get_answer("데드락이 뭐야?")

result = response['choices'][0]['content'][0]

print(result)
# @app.route('/')
# def hello():
#     return "success"

# @app.route('/chat')
# def hello():
#     response = bard.get_answer("데드락이 뭐야?")

#     result = response['choices'][0]['content'][0]
#     return result


# if __name__ == 'bard_bot':
#     app.run()