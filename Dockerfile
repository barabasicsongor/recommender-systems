FROM python:3-onbuild

RUN pip install --upgrade pip

RUN pip install flask
RUN pip install tensorflow
RUN pip install surprise

WORKDIR src

RUN mkdir code
WORKDIR code
COPY . .

EXPOSE 5000

CMD ["python", "flask_app.py"]
