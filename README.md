# n8n-local

A local development environment for [n8n](https://n8n.io/) using Docker and Pipenv.

---

## Prerequisites

- [Docker](https://docs.docker.com/get-docker/) installed and running
- [Pipenv](https://pipenv.pypa.io/en/latest/) installed (`pip install --user pipenv`)

---

## Installation

1. Navigate to the `scripts` directory:
    ```sh
    cd scripts/
    ```
2. Install dependencies:
    ```sh
    pipenv install --dev
    ```

---

## Usage

### Start the Service

```sh
pipenv run start
```

### Stop the Service

```sh
pipenv run stop
```

---

## Access the n8n Setup Page

Once the service is running, open your browser and navigate to:

[http://localhost:5678/setup](http://localhost:5678/setup)

---