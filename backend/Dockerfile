FROM python:3.10-slim
WORKDIR /app
ENV PYTHONUNBUFFERED=1
COPY ./requirements.txt /app/
RUN python -m pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt
COPY ./src /app/src
COPY ./scripts /app/scripts
COPY ../data /app/data
ENV PYTHONPATH=/app
CMD ["uvicorn", "src.app.main:app", "--host", "0.0.0.0", "--port", "8000"]
