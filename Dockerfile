FROM python:3.10

WORKDIR /backend

RUN apt update && apt install -y default-jre

RUN wget http://search.maven.org/remotecontent?filepath=org/apache/tika/tika-server-standard/2.6.0/tika-server-standard-2.6.0.jar -o /tmp/tika-server.jar

COPY requirements.txt .
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

COPY . .
COPY harmony/src/harmony .

EXPOSE 80

ARG COMMIT_ID="No commit ID specified"
ENV COMMIT_ID=$COMMIT_ID

CMD ["bash", "startup.sh"]
