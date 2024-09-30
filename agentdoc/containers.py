from dependency_injector import containers, providers
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables.base import RunnableSequence
from langchain_ollama.llms import OllamaLLM

from .config import Settings


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()
    config.from_dict(Settings().model_dump(mode="json"))

    local_llm = providers.Singleton(
        OllamaLLM,
        model=config.llm_model,
    )

    llm = providers.Selector(
        config.environment,
        local=local_llm,
    )

    summarization_prompt = providers.Singleton(
        ChatPromptTemplate.from_template,
        (
            "Summarize the following text in a clear and concise manner, "
            "focusing only on the key points and main ideas. "
            "Avoid including any personal opinions, interpretations, "
            "or unnecessary details. "
            "The output should be a well-structured summary "
            "that captures the essence of the original content. "
            "The response should consist only of the summarized text, "
            "without any additional comments, explanations, or context. "
            "Ensure that the summary is precise, accurate, "
            "and easy to understand while retaining the core message "
            "of the original text. "
            "Please keep the summary within a 100 words length "
            "and omit any extraneous information. "
            "TEXT: {input_text}"
        ),
    )
    summarization_chain = providers.Factory(
        RunnableSequence,
        summarization_prompt,
        llm,
    )
