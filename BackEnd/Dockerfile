FROM python:3.12.3-alpine

LABEL maintainer="Daniel Mombeyni"

ENV PYTHONUNBUFFERED 1

ENV PATH="/py/bin/:$PATH"

COPY ./requirements.txt /tmp/requirements.txt
COPY ./requirements.dev.txt /tmp/requirements.dev.txt

COPY . /app

WORKDIR /app

EXPOSE 8000

ARG DEV=false



# RUN python -m venv /py && \
#         /py/bin/pip install --upgrade pip && \
#         apk add --update --no-cache postgresql-client jpeg-dev && \
#         apk add --update --no-cache --virtual .tmp-build-deps \
#         build-base postgresql-dev musl-dev zlib zlib-dev && \
#         /py/bin/pip install -r /tmp/requirements.txt && \
#         if [ $DEV = "true" ]; \
#         then /py/bin/pip install -r /tmp/requirements.dev.txt; \
#         fi && \
#         rm -rf /tmp && \
#         apk del .tmp-build-deps

# RUN apk add --update --no-cache \
#         postgresql-client \
#         build-base \
#         postgresql-dev \
#         musl-dev \
#         zlib \
#         zlib-dev \
#         jpeg-dev

RUN apk add --no-cache \
        postgresql-client \
        jpeg-dev && \
        apk add --no-cache --virtual .build-deps \
        build-base \
        postgresql-dev \
        musl-dev \
        zlib \
        zlib-dev

RUN python -m venv /py && \
        /py/bin/pip install --upgrade pip

RUN /py/bin/pip config set global.timeout 300

RUN /py/bin/pip install -r /tmp/requirements.txt

RUN if [ "$DEV" = "true" ]; then /py/bin/pip install -r /tmp/requirements.dev.txt; fi


RUN apk del .build-deps && \
        rm -rf /var/cache/apk/* /tmp/*

# Add non-root user
RUN  adduser \
        --disabled-password \
        --no-create-home \
        django-user

RUN  mkdir -p /vol/web/media && \
        mkdir -p /vol/web/static && \
        chown -R django-user:django-user /vol && \
        chmod -R 755 /vol



USER django-user