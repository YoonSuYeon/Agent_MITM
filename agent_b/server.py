from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import time

app = FastAPI()

@app.post("/tool")
async def tool(req: Request):
    payload = await req.json()
    # 로그로 "수신 JSON" 증거 남기기
    print("[Agent B] Received JSON:", payload, flush=True)

    resp = {
        "id": payload.get("id"),
        "type": "tool_result",
        "tool_name": payload.get("tool_name"),
        "received_at": time.time(),
        "result": {
            "ok": True,
            "echo": payload.get("arguments", {}),
        }
    }
    return JSONResponse(resp)
