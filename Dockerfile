FROM python:3.10
RUN mkdir -p /bot
WORKDIR /bot
COPY . /bot
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "bot.py"]