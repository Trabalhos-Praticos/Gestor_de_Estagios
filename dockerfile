
#Estágio 1: Linux
FROM python:3.8 AS linux-stage

# Instale o Node.js no Linux
RUN apt-get update && \
    apt-get install -y nodejs npm && \
    rm -rf /var/lib/apt/lists/*

# Estágio 2: Windows
FROM python:3.8 AS windows-stage

# Instale o Node.js no Windows
RUN curl -sL https://nodejs.org/dist/v14.17.6/node-v14.17.6-x64.msi -o node.msi && \
    msiexec /i node.msi /quiet && \
    del node.msi


# Copie o código da aplicação
COPY . /app

# Copie o Node.js do estágio correspondente
COPY --from=linux-stage /usr/bin/node /usr/bin/
COPY --from=windows-stage /Program Files/nodejs/ /Program Files/nodejs/


RUN source venv/bin/activate

# Instale as dependências Python
RUN pip install --no-cache-dir -r requirements.txt

# Exponha a porta que sua aplicação Django estará rodando
EXPOSE 8000

# Comando para iniciar a aplicação Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]