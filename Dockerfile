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

RUN pip install py-evm==0.3.0a20 vyper==0.2.7 pytest==6.0.2 web3==5.12.2 black-mamba==0.5.5 pytest-mock git+git://github.com/ethereum/eth-tester.git

RUN mkdir code

WORKDIR /code

RUN apt-get purge -y --auto-remove apt-utils gcc libc6-dev libc-dev libssl-dev

ENTRYPOINT ["mamba"]
