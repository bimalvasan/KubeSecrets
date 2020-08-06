FROM python:3.6.10-alpine3.11

COPY . /

#ENTRYPOINT [ "python3" ]

CMD [ "python3", "src/reader.py" ]