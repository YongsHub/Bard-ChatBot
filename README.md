# Bard-ChatBot
Bard API를 활용한 챗봇서버 만들기


### 1. make requirements.txt
```shell
pip freeze > requirements.txt
```

### 2. docker image build
```shell
docker build -t chat-bot .
```

### 3. docker run
```shell
docker run -d --name chat-bot -p 3000:3000 chat-bot
```