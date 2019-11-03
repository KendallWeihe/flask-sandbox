FROM python

COPY ./requirements.txt /app/requirements.txt
COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT [ "python3" ]

CMD [ "main.py" ]