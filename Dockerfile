# Imagen base
FROM python:3.12-slim

# Evita bufferin
ENV PYTHONUNBUFFERED 1

# Crear directorio del proyecto
WORKDIR /app
# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y \
    libpq-dev gcc && \
    apt-get clean

# Copiar requirements
COPY requirements.txt /app/

# Instalar dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el proyecto entero
COPY . /app/

# Comando por defecto (sobreescribe docker-compose)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]