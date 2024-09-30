# **AgentDoc - LangChain-Based Document Analysis Tool**

**AgentDoc** is an advanced document analysis tool powered by multi-agent systems (MAS) and language models. The project leverages **LangChain** to chain together agents for tasks like text extraction, summarization, keyword extraction, and entity recognition. The system is designed to automate complex document processing workflows, making it ideal for use cases such as patent research, legal document analysis, and large-scale text analysis.

**Features**:
- Multi-agent architecture for modular and scalable document analysis.
- Seamless integration with **OpenAI**, **Elasticsearch**, and other LLMs for robust NLP capabilities.
- Task chaining to handle document extraction, summarization, and entity extraction.
- Dynamic agent coordination and real-time adaptability for different document types.
- Extensible for additional functionality like trend analysis, clause detection, and cross-document processing.

**Technologies**:
- Python
- LangChain
- Flask (API)
- Dependency Injector (for agent and service management)
- OpenAI API
- Elasticsearch

AgentDoc is designed for flexibility, extensibility, and ease of deployment, with containerization support through **Docker**.


## Dependencies
* Python 3.11.1
* Pyenv
* [Poetry](https://python-poetry.org/)
* [Docker](https://www.docker.com/)


## Development

1. install dependencies
```shell
pyenv install 3.11.1
pyenv local 3.11.1

pip install poetry==1.8.2
poetry install
poetry shell
```

2. setup `.env`
```shell
cp .env.example .env
```

3. setup docker containers
```shell
docker compose up --no-start
docker compose start
```

4. run tests
```shell
pytest
```

## Code Coverage Tracking with Python Coverage

1. Run your tests with coverage tracking:
```shell
coverage run -m pytest tests/
```

2. Generate a command-line coverage report:
```shell
coverage report
```

3. Create an HTML coverage report for a detailed, interactive overview:
```shell
coverage html
```


## Code format

Use [`black`](https://black.readthedocs.io/en/stable/index.html),
[here](https://black.readthedocs.io/en/stable/integrations/editors.html) are
the setup instructions for each IDE.

Usage example:
```shell
black --check --diff --color agentdoc/
```

Use [`flake8`](https://flake8.pycqa.org/en/latest/index.html)

Usage example:
```shell
flake8 agentdoc/
```

## Import sorting

Use [`isort`](https://pycqa.github.io/isort/) to ensure imports are sorted
consistently.

Usage example:
```shell
isort agentdoc/ tests/
```
