from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Weather") # Server name

@mcp.tool()
def get_weather(city: str) -> str:
    """Get the weather for a city."""
    # Placeholder implementation - replace with actual weather API call
    return f"The weather in {city} is sunny."



if __name__=="__main__":
    mcp.run(transport="streamable-http")

# TRANSPORT = streamable-http tells the server to
#

