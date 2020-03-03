FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
LABEL maintainer="Robert Zhang <robertzhangwenjie@gmail.com>"


ADD ./src ./fastapi
WORKDIR ./fastapi

EXPOSE 8000/tcp
CMD ["/bin/sh","-c","uvicorn main:app --host 0.0.0.0 --reload"]
