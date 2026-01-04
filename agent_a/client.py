import os
import time
import json
import requests

SERVER_URL = os.environ.get("SERVER_URL", "http://agent-b:8000/tool")

tool_call = {
    "id": "call-0001",
    "type": "tool_call",
    "tool_name": "analyze_dependency",
    "arguments": {
        "repo": "demo-repo",
        "target": "libssl",
        "depth": 2
    }
}

def main():
    # 서버가 뜰 때까지 짧게 기다리는 용도
    for i in range(30):
        try:
            r = requests.get(SERVER_URL.replace("/tool", "/docs"), timeout=1.0)
            break
        except Exception:
            time.sleep(0.5)

    print("[Agent A] Sending JSON:", json.dumps(tool_call, ensure_ascii=False), flush=True)

    resp = requests.post(SERVER_URL, json=tool_call, timeout=5)
    print("[Agent A] Status:", resp.status_code, flush=True)
    print("[Agent A] Response JSON:", resp.json(), flush=True)

if __name__ == "__main__":
    main()
