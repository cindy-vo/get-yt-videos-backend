FROM python:3.10 as python-base
RUN mkdir code
WORKDIR  /code
COPY /pyproject.toml /code
RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-root
RUN mkdir -p /etc/cont-init.d \
    && echo 'echo "vm.overcommit_memory=1" > /etc/sysctl.d/overcommit_memory.conf' > /etc/cont-init.d/overcommit_memory \
    && chmod +x /etc/cont-init.d/overcommit_memory
COPY . .
CMD ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "main:app", "--bind", "0.0.0.0:8000", "--reload"]
