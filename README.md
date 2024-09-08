# Introduction

This is a basic Flask API with the following:

- Supports fetching large amount of data
- In-memory cache storage (python dict)
- `/api/v1/fetch-data` Fetches a large data in small chunks
- `/api/v1/get-processed-data` Applies an operation on the large data concurrently

# Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Testing](#testing)

---

# Prerequisites

Make sure you have the following installed on your system:

- **Git**: For cloning the repository.
- [Pyenv](#install-pyenv): To manage the correct Python version.
- [Poetry](#install-poetry): For dependency management.

### Install `pyenv`

Run this for automatic install
```bash
curl https://pyenv.run | bash
```

For other installation options, [Pyenv Github](https://github.com/pyenv/pyenv?tab=readme-ov-file#installation)

### Install `poetry`

Poetry recommends installing it with `pipx`

```bash
pipx install poetry
```

# Installation

## 1. Clone the repository

   ```bash
   git clone <github_url>
   cd <folder>
   ```

## 2. Install project's python version

   The project has a `.python-version` file, which contains the correct python version. **Pyenv** will automatically install that version

   ```bash
   pyenv install
   ```

## 3. Install Python Dependencies

   You can use anything to install the dependencies, the project contains a `requirements.txt` and `pyproject.toml`

   This will setup a virtual environment and install the dependencies in it. It will also install the project.

   ```bash
   poetry install
   ```

# Usage

To run the flask server, use

```bash
poetry run app
```

Here `app` is a script defined in the **pyproject.toml** which runs the flask server

# Testing

You can run tests with pytest

```bash
poetry run pytest
```

# API Routes

This project provides the following API routes:
### <span class='request-type'>**GET**</span> <span class='route-name'>/api/v1/fetch-data</span>

  #### Description
  Fetches data from the CSV file in chunks.

  #### Parameters
  - **page** (int, required): The page number for pagination.
  - **chunk_size** (int, optional): Number of rows to fetch per request     (default: 100).
  - **shuffle** (bool, optional): If true, the data will be shuffled on every request (default: false).

  #### Returns
  - <span class='status-200'>**200 OK**</span>: A JSON object containing the chunked data.
  - <span class='status-error'>**500 Internal Server Error**</span>: If an error occurs during data retrieval.


### <span class='request-type'>**GET**</span> <span class='route-name'>/api/v1/get-processed-data</span>

  #### <span class="description">Description</span>
  Returns processed data after applying a data transformation function.

 #### Parameters
  - **page** (int, required): The page number for pagination.
  - **chunk_size** (int, optional): Number of rows to fetch per request     (default: 100).
  - **shuffle** (bool, optional): If true, the data will be shuffled on every request (default: false).

  #### Returns
  - <span class='status-200'>**200 OK**</span>: A JSON object with the processed data.<br />
  - <span class='status-error'>**404 Not Found**</span>: If the process_id does not exist.
  - <span class='status-error'>**500 Internal Server Error**</span>: If an error occurs during data processing.

These API routes provide functionality for data retrieval, processing, and cache management, supporting both efficient data handling and scalability.
