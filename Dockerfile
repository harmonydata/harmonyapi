FROM python:3.10

WORKDIR /backend

RUN apt update && apt install -y default-jre

COPY requirements.txt .
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

RUN python -c 'from tika import parser; parser.from_buffer("abc", xmlContent=True)'

COPY . .

EXPOSE 80

ARG COMMIT_ID="No commit ID specified"
ENV COMMIT_ID=$COMMIT_ID
ENV STAGE=prod

CMD ["python", "main.py"]
