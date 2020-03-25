FROM python:3.8.0

ENV PORT 8081

COPY ./requirements.txt /app/requirements.txt

COPY ./app/app.py /app/app.py

COPY ./templates /app/

WORKDIR /app

RUN pip install -r requirements.txt

ENTRYPOINT [ "python" ]
CMD [ "app.py" ]
