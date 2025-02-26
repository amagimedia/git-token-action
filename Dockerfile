FROM python:3.11 AS builder

ARG WORKDIR=/app
WORKDIR $WORKDIR

# Copy Project Files
COPY poetry.lock ./
COPY pyproject.toml ./

# Install poetry
RUN pip install poetry && poetry self add poetry-plugin-export && poetry export --format=requirements.txt --without-hashes -n --no-cache -o requirements.txt && pip install -r requirements.txt --target ./packages/

# Performing cleanup
RUN find . -regex '^.*\(__pycache__\|\.py[co]\)$' -delete


FROM public.ecr.aws/amagi-media-labs-sec/secure-container-base/python:3.11

ARG WORKDIR=/app
WORKDIR $WORKDIR

# Ensure GITHUB_ENV is accessible
ENV GITHUB_ENV=/github_env

COPY Dockerfile ./
COPY ./utilities ./utilities
COPY main.py ./
COPY --from=builder $WORKDIR/packages/ $WORKDIR/

ENTRYPOINT ["python", "main.py"]