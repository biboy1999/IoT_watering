FROM python:3.8

ENV TZ=Asia/Taipei
RUN pip install "poetry==1.0.0"

WORKDIR /backend

COPY poetry.lock pyproject.toml /backend/

RUN poetry install --no-interaction --no-ansi --no-dev

COPY server.py /backend/

EXPOSE 8000

CMD poetry run python3 server.py