FROM python:3.10

WORKDIR /backend

RUN apt update && apt install -y default-jre

COPY requirements.txt .
RUN pip install --upgrade pip \
    && pip install -r requirements.txt
# Force download of Tika
RUN python -e 'from tika import parser; parser.from_buffer('abc', xmlContent=True, requestOptions={'timeout': 300})'

COPY . .

EXPOSE 80

ARG COMMIT_ID="No commit ID specified"
ENV COMMIT_ID=$COMMIT_ID

CMD ["bash", "startup.sh"]
