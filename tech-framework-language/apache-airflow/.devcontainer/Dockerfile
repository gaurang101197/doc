FROM apache/airflow:2.6.3
# group id of docker group in which airflow user is added so that it can have access to docker running on local machine.
ENV DOCKER_GID "135"

USER root

# Install git
# Install vim (to use vim with git commit command)
RUN apt-get update \
    && apt-get install -y vim git

# giving sudo access to airflow user
RUN echo "airflow ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

# creating docker group and adding airflow user to it so that it can access docker running on local machine.
RUN groupadd -g "${DOCKER_GID}" docker
RUN usermod -aG docker airflow
RUN newgrp docker

# Install Docker Compose
RUN LATEST_COMPOSE_VERSION=$(curl --insecure -sSL "https://api.github.com/repos/docker/compose/releases/latest" | grep -o -P '(?<="tag_name": ").+(?=")') \
    && curl --insecure -sSL "https://github.com/docker/compose/releases/download/${LATEST_COMPOSE_VERSION}/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose \
    && chmod +x /usr/local/bin/docker-compose

USER airflow

# installing packages to run linting and pre-commit hooks
RUN python -m pip install --upgrade pip && pip install flake8 pylint pre-commit pytest
