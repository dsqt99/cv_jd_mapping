FROM python:3.9

EXPOSE 2312
COPY . .

RUN apt-get update && apt-get install -y poppler-utils
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["python", "app.py"]