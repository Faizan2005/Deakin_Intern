from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
async def home():
    return {"message": "MCP Server Running"}

@app.post("/invoke")
async def invoke_tool(request: Request):
    data = await request.json()
    tool = data.get("tool")
    user_input = data.get("input")
    if tool == "echo":
        return {"output": f"You said: {user_input}"}
    return JSONResponse(status_code=404, content={"error": "Tool not found"})
