FROM python:3-alpine

ENV PYTHONUNBUFFERED=1 \
    PYTHONIOENCODING=UTF-8 \
    FLASK_APP=/api.py \
    FLASK_RUN_HOST=0.0.0.0 \
    FLASK_RUN_PORT=8080 \
    MANIFEST_FILE_PATH=/app/manifest.json \
    BUCKET_TMP_DIR=/tmp/bucket_files

COPY . /app/

WORKDIR /app

RUN pip3 install --upgrade pip && \
    pip3 install -r requirements.txt && \
    mkdir -p "${BUCKET_TMP_DIR}"

CMD ["python3", "-m", "flask", "run"]
