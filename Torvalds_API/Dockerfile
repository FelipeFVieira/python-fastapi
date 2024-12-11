FROM python:3.10-slim AS build

# Instale dependências do sistema operacional
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential && rm -rf /var/lib/apt/lists/*

# Defina o diretório de trabalho
WORKDIR /app

# Copie apenas os arquivos necessários para instalar as dependências
COPY requirements.txt ./

# Instale as dependências do Python
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copie o restante do código da aplicação
COPY . .

# Etapa final para criar uma imagem leve
FROM python:3.10-slim

# Defina o diretório de trabalho
WORKDIR /app

# Copie os arquivos e dependências da etapa de build
COPY --from=build /app /app

# Exponha a porta usada pela aplicação
EXPOSE 8080

# Comando de inicialização para o Uvicorn
ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
