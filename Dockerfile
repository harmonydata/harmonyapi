FROM python:3.10

WORKDIR /backend

COPY requirements.txt .
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

RUN apt update && apt install -y default-jre tesseract-ocr

RUN python -c 'from tika import parser; parser.from_buffer("abc", xmlContent=True)'

COPY . .

EXPOSE 80

ARG COMMIT_ID="No commit ID specified"
ENV COMMIT_ID=$COMMIT_ID
ENV STAGE=prod

# Download the models
RUN python harmony/src/harmony/util/model_downloader.py 

CMD ["uvicorn", "main:app_fastapi", "--host", "0.0.0.0", "--port", "80"]
