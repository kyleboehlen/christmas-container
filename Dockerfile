FROM ubuntu:latest

WORKDIR /app

# Get latest apt packages, and curl, verify we dont' get bad proxy hash mismatch issues
RUN echo "Acquire::http::Pipeline-Depth 0; \n Acquire::http::No-Cache true; \n Acquire::BrokenProxy    true;" > /etc/apt/apt.conf.d/99fixbadproxy
RUN apt update && apt upgrade -y && apt install -y && apt install -y curl

COPY . .

# Python tooling
RUN apt install -y python3
RUN apt install -y python3-pip
RUN apt install -y python3-numpy

CMD ["/bin/bash"]