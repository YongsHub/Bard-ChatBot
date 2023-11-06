FROM python:3.10

WORKDIR /test
COPY . .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 5000

CMD python ./app.py