from fastapi import FastAPI, HTTPException

from model.Footprint import Footprint
from controller.InputCheck import InputCheck
from service.CarbonService import CarbonService

app = FastAPI()

@app.get("/")
def read_root():
    return "Welcome to Highcast's baby API."

@app.post("/calculate/")
async def home_footprint(footprint: Footprint):

    footprint_dict = footprint.model_dump()

    input_checker = InputCheck(footprint_dict)

    electricity_check = input_checker.is_electricity("type")
    if electricity_check is not True:
        raise HTTPException(status_code=400, detail=electricity_check)

    kwh_check = input_checker.is_kwh("electricity_unit")
    if kwh_check is not True:
        raise HTTPException(status_code=400, detail=kwh_check)

    positive_number_check = input_checker.is_positive_number("electricity_value")
    if positive_number_check is not True:
        raise HTTPException(status_code=400, detail=positive_number_check)

    carbon_service = CarbonService(footprint_dict)

    try:
        emission = carbon_service.get_emission()

        return {
            "message": "Voici votre empreinte carbone.",
            "emission_carbone": emission.get("data").get("attributes").get("carbon_kg"),
            "unité": "kgCO2e"
        }
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=f"Erreur lors du calcul de l'empreinte carbone: {e.detail}")
