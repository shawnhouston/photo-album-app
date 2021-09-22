FROM registry.access.redhat.com/ubi8:latest

RUN dnf update -y && \
    dnf install -y python3-pip platform-python-devel curl vim

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip3 install -r requirements.txt
COPY . /app
RUN chmod 750 /app/uploads

ENV BUCKET_NAME "$BUCKET_NAME"
#ENV ENDPOINT_URL "$ENDPOINT_URL"
ENV  BUCKET_HOST "$BUCKET_HOST"
ENV AWS_ACCESS_KEY_ID "$AWS_ACCESS_KEY_ID"
ENV AWS_SECRET_ACCESS_KEY "$AWS_SECRET_ACCESS_KEY"

EXPOSE 8080
#EXPOSE 8081

ENTRYPOINT [ "python3" ]
CMD [ "app.py" ]

