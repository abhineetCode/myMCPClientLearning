from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain_groq import ChatGroq
from langgraph.prebuilt import create_react_agent
import os
import asyncio
from dotenv import load_dotenv
load_dotenv()
os.environ["GROQ_API_KEY"]=""

async def main():
    client=MultiServerMCPClient(
        {
            "Math":{
                "command":"python",
                "args":["mathServer.py"],
                "transport":"stdio"
            },
            "Weather":{
                "url":"http://127.0.0.1:8000/mcp",
                
                "transport":"streamable_http"
            }
        }
    )
    try:
    
        model = ChatGroq( model = "Gemma2-9b-It")
    
        tools = await client.get_tools()
        print("tools loaded: ")
        print(tools)

        agent=create_react_agent(model,tools)

        math_response = await agent.ainvoke(
            { "messages": [{"role": "user", "content": "What is (2 + 3)*12"}]}
        )
        #and what is the weather in New York?
        print("math_response: " + math_response["messages"][-1].content)
    except Exception as e:
        print(f"An error occurred: {e}")    



if __name__ == "__main__":
    asyncio.run(main())

