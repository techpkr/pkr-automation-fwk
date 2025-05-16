FROM python@sha256:e8381c802593deb0c4d25bd3f4e05e94382f6bf33090de22679fc7488cd68bbb

RUN apt-get update \
    && apt-get install curl jq --no-install-recommends -y \
    && apt-get clean && rm -rf /var/lib/apt/lists/*
RUN mkdir /pkrdir
WORKDIR /pkrdir
COPY requirements.txt requirements.txt
RUN python -m pip install -r requirements.txt
COPY . .
ENTRYPOINT ["pytest"]
CMD ["-v", "--maxfail=1"]