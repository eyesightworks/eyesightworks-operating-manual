from fastapi import FastAPI

app = FastAPI(title="EyesightWorks Property Service")


properties = [
    {
        "id": 1,
        "title": "Modern 3-Bedroom House",
        "location": "Ibadan",
        "price": 45000000,
    },
    {
        "id": 2,
        "title": "Luxury 4-Bedroom Duplex",
        "location": "Lagos",
        "price": 85000000,
    },
]


@app.get("/")
def root():
    return {
        "message": "EyesightWorks Property Service is running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.get("/properties")
def get_properties():
    return properties