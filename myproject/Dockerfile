# Use the official Python runtime image
FROM python:3.12  

# Create the app directory
RUN mkdir /app

# WORKDIR: コンテナ内のアプリケーションの作業ディレクトリを設定します。
WORKDIR /app

# ENV: アプリケーションのビルドに必要な環境変数を設定します
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1 

# Upgrade pip
RUN pip install --upgrade pip 

# Copy the Django project  and install dependencies
COPY requirements.txt  /app/

# run this command to install all dependencies 
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Django project to the container
COPY . /app/

# Expose the Django port
EXPOSE 8000

# Run Django’s development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]