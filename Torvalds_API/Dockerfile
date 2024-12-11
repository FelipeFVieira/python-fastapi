FROM bitnami/python:3.11.1
WORKDIR /Torvalds_API

COPY . /Torvalds_API

RUN pip install -r requirements.txt

EXPOSE 8000

CMD python -m uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload 