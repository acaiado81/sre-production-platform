import json
import logging
import random
import time
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse

app = FastAPI(title="SRE Production Platform")

# ---------- Logging ----------
logging.basicConfig(
    level=logging.INFO,
    format='%(message)s'
)

logger = logging.getLogger("sre-app")


def log(event: str, **kwargs):
    logger.info(json.dumps({
        "event": event,
        **kwargs
    }))


# ---------- Endpoints ----------
@app.get("/health")
def health():
    log("health_check")
    return {"status": "ok"}


@app.get("/work")
def do_work(latency_ms: int = 0, error_rate: float = 0.0):
    """
    Simulates work with optional latency and error injection.

    latency_ms: artificial delay in milliseconds
    error_rate: probability between 0.0 and 1.0
    """

    log("work_request_received",
        latency_ms=latency_ms,
        error_rate=error_rate
    )

    if latency_ms > 0:
        time.sleep(latency_ms / 1000)

    if random.random() < error_rate:
        log("work_request_failed")
        raise HTTPException(status_code=500, detail="Injected failure")

    log("work_request_success")
    return JSONResponse({
        "result": "success",
        "latency_ms": latency_ms
    })
