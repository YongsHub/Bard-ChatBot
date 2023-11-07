# Bard-ChatBot
Bard API를 활용한 챗봇서버 만들기

### 1. make .env
```shell
API_KEY=
```

### 2. make requirements.txt
```shell
pip freeze > requirements.txt
```

### 3. docker image build
```shell
docker build -t chat-bot .
```

### 4. docker run
```shell
docker run -d --name chat-bot -p 5000:5000 chat-bot
```