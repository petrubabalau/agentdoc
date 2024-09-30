import os.path

from flask import Flask

from agentdoc.containers import Container

app = Flask(__name__)

FILE_PATH = os.path.join(os.getcwd(), "assets/example.pdf")


@app.route("/")
def hello_world():
    container = Container()

    text_extraction_agent = container.text_extraction_agent()
    extracted_text = text_extraction_agent.extract(file_path=FILE_PATH)

    summarization_agent = container.summarization_chain()
    result = summarization_agent.invoke(
        {
            "input_text": extracted_text,
        },
    )

    return f"{result}"
