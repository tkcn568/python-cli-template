from kennethreitz/pipenv

WORKDIR /app


COPY . .

RUN pipenv install
RUN pipenv run python setup.py build

