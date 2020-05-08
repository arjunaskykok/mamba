FROM python:3

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        apt-utils \
        gcc \
        git \
        libc6-dev \
        libc-dev \
        libssl-dev \
        libgmp-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip install vyper==0.1.0b17 pytest==5.4.1 web3==5.9.0 eth-tester==0.4.0b1 py-evm==0.3.0a14 black-mamba==0.3.4

RUN mkdir code

WORKDIR /code

RUN apt-get purge -y --auto-remove apt-utils gcc libc6-dev libc-dev libssl-dev

ENTRYPOINT ["mamba"]
