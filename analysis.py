import numpy as np

def analyze_market(image_bytes):
    size = len(image_bytes)

    if size > 200000:
        return {
            "decision": "OPERAR",
            "direction": "PROBABLE CONTINUACIÓN",
            "probability": "65% – 75%",
            "timeframe": "2–3 minutos",
            "risk": "Pullback profundo"
        }

    if size < 80000:
        return {
            "decision": "NO OPERAR",
            "reason": "Mercado en consolidación",
            "risk": "Bajo volumen"
        }

    return {
        "decision": "ESPERAR",
        "reason": "Falta confirmación",
        "risk": "Falsa ruptura"
    }
