from pathlib import Path

import joblib
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel, Field
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Energy Output Prediction API",
    description="Predict energy output using a trained ML model.",
    version="1.0.0",
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

MODEL_PATH = Path(__file__).resolve().parent / "energy_output_model.joblib"
model = joblib.load(MODEL_PATH)


class EnergyInput(BaseModel):
    AT: float = Field(description="Ambient temperature")
    V: float = Field(description="Exhaust vacuum")
    AP: float = Field(description="Ambient pressure")
    RH: float = Field(description="Relative humidity")


@app.get("/")
def home():
    return {
        "message": "Energy Output Prediction API is running"
    }


@app.get("/health")
def health():
    return {"status": "healthy", "model_loaded": model is not None}

@app.get("/app", include_in_schema=False)
def frontend():
    html_file = Path(__file__).resolve().parent / "index.html"
    return FileResponse(html_file)
@app.post("/predict")
def predict(data: EnergyInput):
    features = pd.DataFrame(
        [[data.AT, data.V, data.AP, data.RH]],
        columns=["AT", "V", "AP", "RH"],
    )

    prediction = model.predict(features)[0]

    return {
        "predicted_energy_output": round(float(prediction), 2)
    }
