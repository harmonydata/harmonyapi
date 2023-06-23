FROM python:3.10

RUN apt-get update
#RUN apt-get install tesseract-ocr -y
# Needed for Camelot
RUN apt-get install ffmpeg libsm6 libxext6  -y
#RUN pip install sentence-transformers==2.2.2
#RUN python -c "from sentence_transformers import SentenceTransformer; model = SentenceTransformer('sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2')"

WORKDIR /backend

COPY requirements.txt .
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

COPY . .

EXPOSE 80

ARG COMMIT_ID="No commit ID specified"
ENV COMMIT_ID=$COMMIT_ID
ENV DATA_PATH=.

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
