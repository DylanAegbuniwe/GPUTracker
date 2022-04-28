FROM python:3.9
WORKDIR /app
RUN python -m pip install bs4
RUN python -m pip install mysql-connector-python
COPY scraper.py .
COPY demo_scraper.py .
CMD ["python", "demo_scraper.py"]
