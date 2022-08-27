FROM python:3.9

RUN mkdir /app
COPY . /app
WORKDIR /app

RUN pip install --upgrade pip && pip install -r requirements.txt

CMD streamlit run HOME.py --server.port $PORT