# dev container setup

1. Install Remote-SSH and Dev Containers VSCode Extension
2. Clone the repository in local machine
3. Open the same directory
4. From the bottom right green button, reopen the same using devcontainers

## Set airflow user id

1. run `echo $UID` in your terminal to get your user's userid.
2. make sure that you update user id in [.env](../.env) if it is different.

## Set docker GID

1. run `getent group docker` in your terminal to get your docker group's GID.
2. make sure that you update docker GID in [.env](../.env) if it is different.

## Notes

1. Once you successfully able to setup dev container, you should able to access airflow UI at `<localhost|your_machine_ip>:8080`.
2. use `airflow:airflow` as credentials to login to dev container airflow UI.
