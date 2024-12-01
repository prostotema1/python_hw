FROM python:3.9-slim

# Устанавливаем LaTeX
RUN apt-get update && apt-get install -y texlive texlive-latex-extra texlive-fonts-recommended texlive-fonts-extra \
    && apt-get install -y --no-install-recommends \
    libcurl4-openssl-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /tmp/
RUN pip install --upgrade pip && pip install -r /tmp/requirements.txt

COPY ./latex_generator /app
COPY ./latex_generator/example_image.png /app/example_image.png

WORKDIR /app

CMD pdflatex generated_document.tex
