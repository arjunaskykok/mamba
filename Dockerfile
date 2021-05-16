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

RUN pip install py-evm==0.4.0a4 vyper==0.2.12 pytest==6.2.1 web3==5.19.0 black-mamba==0.6.3 pytest-mock==3.5.1 eth-tester==0.5.0b4

RUN mkdir code

WORKDIR /code

RUN apt-get purge -y --auto-remove apt-utils gcc libc6-dev libc-dev libssl-dev

ENTRYPOINT ["mamba"]
