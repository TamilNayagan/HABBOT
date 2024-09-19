FROM python:3.11

WORKDIR /Test

COPY . /Test

RUN pip install -r requirements.txt

CMD ["python", "bot.py"]
