FROM  python:3.9

RUN pip install pipenv

ENV PROJECT_DIR /pngMerge

WORKDIR ${PROJECT_DIR}

COPY Pipfile Pipfile.lock ${PROJECT_DIR}

COPY . .

RUN PIPENV_VENV_IN_PROJECT=1 pipenv install --system --deploy

CMD ["pipenv", "run", "python3", "main.py"]