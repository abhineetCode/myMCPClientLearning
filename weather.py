from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Weather")

@mcp.tool()
async def get_weather(city: str) -> str:
    """Fetches the current weather for a given city."""
    # Simulated weather data retrieval
    weather_data = {
        "New York": "Sunny, 25°C",
        "Los Angeles": "Cloudy, 22°C",
        "Chicago": "Rainy, 18°C"
    }
    return weather_data.get(city, "Weather data not available for this city.")

if __name__ == "__main__":    
    mcp.run(transport="streamable-http")


