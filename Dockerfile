FROM python:3.11

WORKDIR /HABBOT

COPY . /HABBOT

RUN pip install -r requirements.txt

CMD ["python", "bot.py"]
