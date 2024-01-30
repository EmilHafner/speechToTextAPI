FROM ubuntu:latest
LABEL authors="hafne"

ENTRYPOINT ["top", "-b"]