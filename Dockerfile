FROM revolutionsystems/python:3.6.3-wee-optimized-lto
RUN mkdir -p /code
WORKDIR /code
RUN pip install --upgrade pip
ADD . /code
RUN python setup.py develop
CMD ["pytest", "-v"]