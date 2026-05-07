from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain.tools import tool

# from tavily import TavilyClient
from langchain_tavily import TavilySearch
from typing import List
from pydantic import BaseModel, Field

load_dotenv()


class Source(BaseModel):
    """Schema for source used by agent"""

    url: str = Field(description="The URL of the source")


class AgentResponse(BaseModel):
    """Schema for agent response with answer and sources"""

    answer: str = Field(description="The answer to the user query")
    sources: List[Source] = Field(
        default_factory=List, description="List of sources used to generate the answer"
    )


## initializing tavily
# tavily = TavilyClient()

# ##tool definition
# @tool
# def search(query:str)->str :
#     """
#     Tool that searches over the internet
#     Args :
#        query : The query to search for
#     Returns :
#        The search result
#     """
#     print(f"searching for {query}")

#     return tavily.search(query=query)


def main():
    print("Hello from react-search-agent!")

    llm = ChatOpenAI(model="gpt-4.1-mini")
    tools = [TavilySearch()]

    agent = create_agent(model=llm, tools=tools, response_format=AgentResponse)

    result = agent.invoke(
        {
            "messages": HumanMessage(
                content="Search for 3 job postings for an AI Engineer whose primary skill is Langchain in LinkedIn"
            )
        }
    )

    print(result['structured_response'].answer)
    print("-----------------")
    print(result['structured_response'].sources)


if __name__ == "__main__":
    main()
