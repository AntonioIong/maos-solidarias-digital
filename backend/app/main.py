from fastapi import FastAPI

app = FastAPI(
    title="Mãos Solidárias Digital API",
    version="0.1.0",
    description="API inicial do MVP Mãos Solidárias Digital.",
)


@app.get("/health", tags=["system"])
def health_check() -> dict[str, str]:
    """Return a basic status response for availability checks."""
    return {"status": "ok"}
