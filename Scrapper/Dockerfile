# Используйте базовый образ Python
FROM continuumio/miniconda3

# Установка рабочей директории внутри контейнера
WORKDIR /data

# Копирование зависимостей проекта
ADD environment.yml /tmp/environment.yml

# Install Conda environment from environment.yml
RUN conda env create -f /tmp/environment.yml
RUN conda install -c anaconda unixodbc
RUN pip install telebot
RUN pip install beautifulsoup4
RUN pip install pyodbc
RUN pip install aiosmtplib
RUN pip install python-telegram-bot
RUN pip install aiogram
RUN pip install asyncio
RUN pip install pyTelegramBotAPI

# Pull the environment name out of the environment.yml
RUN echo "source activate $(head -1 /tmp/environment.yml | cut -d' ' -f2)" > ~/.bashrc
ENV PATH /opt/conda/envs/$(head -1 /tmp/environment.yml | cut -d' ' -f2)/bin:$PATH

# Copy your project files into the container
COPY . /data

# Activate the virtual environment
# SHELL ["python3", "run", "-n", "amazon-bot-env"]
# SHELL ["conda", "run", "-n", "env", "/bin/bash", "-c"]

# Command to be executed when the container is run
CMD [ "python3", "amazon_bot.py" ]
     
