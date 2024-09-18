from dotenv import load_dotenv
from langchain.prompts.prompt import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent
from output_parsers import summary_parser
from third_parties.linkedin import scrape_linkedin_profile


def ice_breaker_with(name: str) -> str:
    linkedin_username = linkedin_lookup_agent(name=name)
    linkedin_data = scrape_linkedin_profile(linkedin_profile_url="https://linkedin.com/in/johnrmarty/")
    #linkedin_data = scrape_linkedin_profile(linkedin_profile_url=linkedin_username)

    summary_template = """
        given the Linkedin information {information} about a person from what I want you to create:
        1. a short summary
        2. two interesting facts about them
        \n{format_instructions}
        """
    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template,
        partial_variables={"format_instructions": summary_parser.get_format_instructions()}
    )

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    chain = summary_prompt_template | llm | summary_parser

   # linkedin_data = scrape_linkedin_profile(linkedin_profile_url="https://linkedin.com/in/johnrmarty/")
    res = chain.invoke(input={"information": linkedin_data})

    print(res)

if __name__ == "__main__":
    load_dotenv()
    print("Ice breaker Enter")
    ice_breaker_with(name="Masha Volska")

    absb