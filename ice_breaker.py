from langchain.prompts.prompt import PromptTemplate
from langchain_openai import ChatOpenAI

information = """
"""
if __name__ == "__main__":
    print("Hello")

    summary_template = """
        given the information {information} about a person from what I want you to create:
        1. a short summary
        2. two interesting facts about them
        """
    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    chain = summary_prompt_template | llm
    res = chain.invoke(input={"information": information})

    print(res)
