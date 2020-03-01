FROM python:3.6.8-alpine

LABEL maintainer="Robert <1648855816@qq.com>"

ADD . /fastapi
WORKDIR ./fastapi
RUN pip install -U pip & \
pip install fastapi && \
pip install uvicorn

EXPOSE 8000/tcp
CMD ["/bin/sh","-c","uvicorn main:app --reload"]
