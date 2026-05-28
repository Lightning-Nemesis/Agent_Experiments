import langchain_mcp_adapters
from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_groq import ChatGroq
import os
import sys
from pathlib import Path
from dotenv import load_dotenv
load_dotenv()
import asyncio

async def main():
    base_dir = Path(__file__).resolve().parent
    client = MultiServerMCPClient(
        {
            "math":{
                "command": sys.executable,
                "args":[str(base_dir / "mathserver.py")],
                "transport":"stdio",
            },
            "weather":{
                    "url":"http://localhost:8000/mcp", # absolute path
                    "transport":"streamable-http",
            }
        
        }
    )
    import os
    os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

    tools = await client.get_tools()
    model = ChatGroq(model ="qwen/qwen3-32b")
    agent = create_react_agent(model, tools)

    math_response = await agent.ainvoke(
        {"messages":[{"role":"user","content":"What is (2+2) x 5  and hows the weather in California?"}]}
    )
    print("Math Response:", math_response['messages'][-1].content)


asyncio.run(main())

# keep the weather.py running in the background (python weather.py) to test the weather tool
# .\.venv\Scripts\python.exe mcp-demo-langchain\weather.py