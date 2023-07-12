FROM python:3.10

WORKDIR /backend

COPY requirements.txt .
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

COPY . .

EXPOSE 80

ARG COMMIT_ID="No commit ID specified"
ENV COMMIT_ID=$COMMIT_ID
ENV STAGE=prod

CMD ["python", "main.py"]
