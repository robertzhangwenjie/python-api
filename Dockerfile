FROM tiangolo/uvicorn-gunicorn:python3.7-alpine3.8  
LABEL maintainer="Robert Zhang <robertzhangwenjie@gmail.com>"

RUN pip install -U pip \
  && pip install fastapi 

WORKDIR ./fastapi

EXPOSE 8000/tcp
CMD ["/bin/sh","-c","uvicorn main:app --host 0.0.0.0 --reload"]
