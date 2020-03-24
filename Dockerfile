FROM python:3.8.0-alpine3.10

ENV PORT 8081

COPY ./requirements.txt /app/requirements.txt

COPY ./app/app.py /app/app.py

WORKDIR /app

RUN pip install -r requirements.txt

ENTRYPOINT [ "python" ]
CMD [ "app.py" ]