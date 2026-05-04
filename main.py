from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain.tools import tool
# from tavily import TavilyClient
from langchain_tavily import TavilySearch

load_dotenv()

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

    agent = create_agent(
        model=llm,
        tools= tools
    )

    result = agent.invoke({"messages" : HumanMessage(content="Search for 3 job postings for an AI Engineer whose primary skill is Langchain in LinkedIn")})

    print(result)


if __name__ == "__main__":
    main()
