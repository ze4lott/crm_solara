"""Funciones puras de dimensionamiento fotovoltaico preliminar."""
from __future__ import annotations
import math
from typing import Any

def num(value: Any, default: float = 0.0) -> float:
    try:
        return float(value)
    except (TypeError, ValueError):
        return default

def solar_calculation(consumo_mensual: float, tarifa: float, panel_w: float,
                      hsp: float, rendimiento: float, cobertura: float,
                      precio_kwp: float = 18500.0, autoconsumo: float = 0.85) -> dict[str, float]:
    """Cálculo preliminar, con guardas para entradas inválidas."""
    consumo_mensual = max(0.0, consumo_mensual)
    tarifa = max(0.0, tarifa)
    panel_w = max(1.0, panel_w)
    hsp = max(0.1, hsp)
    rendimiento = min(1.0, max(0.1, rendimiento))
    cobertura = min(200.0, max(0.0, cobertura))
    consumo_anual = consumo_mensual * 12
    energia_objetivo = consumo_anual * cobertura / 100
    generacion_kwp = hsp * 365 * rendimiento
    potencia_requerida = energia_objetivo / generacion_kwp if generacion_kwp else 0
    paneles = math.ceil(potencia_requerida * 1000 / panel_w) if potencia_requerida > 0 else 0
    potencia_instalada = paneles * panel_w / 1000
    generacion_anual = potencia_instalada * generacion_kwp
    cobertura_real = generacion_anual / consumo_anual * 100 if consumo_anual else 0
    inversion = potencia_instalada * max(0, precio_kwp)
    energia_autoconsumida = min(consumo_anual, generacion_anual * min(1.0, max(0.0, autoconsumo)))
    ahorro_anual = energia_autoconsumida * tarifa
    payback = inversion / ahorro_anual if ahorro_anual > 0 else 0
    return {"consumo_anual": consumo_anual, "energia_objetivo": energia_objetivo,
            "potencia_requerida": potencia_requerida, "paneles": float(paneles),
            "potencia_instalada": potencia_instalada, "generacion_anual": generacion_anual,
            "cobertura_real": cobertura_real, "inversion": inversion,
            "ahorro_anual": ahorro_anual, "ahorro_mensual": ahorro_anual / 12,
            "payback": payback}

