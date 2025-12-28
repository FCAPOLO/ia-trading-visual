import cv2
import numpy as np

def analyze_market(image_bytes):
    image = cv2.imdecode(np.frombuffer(image_bytes, np.uint8), cv2.IMREAD_GRAYSCALE)

    volatility = np.std(image)
    strength = np.mean(np.abs(np.diff(image.astype(float))))

    if volatility > 35 and strength > 12:
        return {
            "decision": "OPERAR",
            "direction": "PROBABLE CONTINUACIÓN",
            "probability": "65% – 75%",
            "timeframe": "2–3 minutos",
            "risk": "Pullback profundo"
        }

    if volatility < 20:
        return {
            "decision": "NO OPERAR",
            "reason": "Mercado en consolidación",
            "risk": "Alto ruido"
        }

    return {
        "decision": "ESPERAR",
        "reason": "Falta confirmación estructural",
        "risk": "Falsa ruptura"
    }
