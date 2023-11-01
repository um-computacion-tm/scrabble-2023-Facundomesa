FROM python:3-alpine
LABEL authors="Facundo"

RUN apk update
RUN apk add git
RUN git clone 
WORKDIR /scrabble-2023- https://github.com/um-computacion-tm/scrabble-2023-Facundomesa.git
RUN git checkout dev
RUN pip install -r requirements.txt

CMD [ "sh", "-c", "python3 -m coverage report && python3 -m coverage run -m unittest discover -s test" ]