FROM python:3-alpine AS builder

WORKDIR /app
RUN apk --no-cache add curl
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
ENV PATH="/root/.poetry/bin:${PATH}"

COPY . .

RUN poetry install
RUN poetry build


FROM python:3-alpine
COPY --from=builder /app/dist/clitool-*.whl .
RUN pip install ./*.whl
CMD ['python -m clitool --help']