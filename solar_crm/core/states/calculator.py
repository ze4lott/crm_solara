import reflex as rx
from solar_crm.calculations import solar_calculation, num



class PublicCalculatorState(rx.State):
    consumo: str = "18000"
    tarifa: str = "2.70"
    panel: str = "600"
    hsp: str = "5.2"
    rendimiento: str = "0.80"
    cobertura: str = "80"

    def update(self, field: str, value: str):
        if field in {"consumo", "tarifa", "panel", "hsp", "rendimiento", "cobertura"}:
            setattr(self, field, value)

    @rx.var
    def result(self) -> dict[str, float]:
        return solar_calculation(num(self.consumo), num(self.tarifa), num(self.panel, 600), num(self.hsp, 5.2), num(self.rendimiento, .8), num(self.cobertura, 80), 18500)

    @rx.var
    def investment(self) -> float:
        return self.result["inversion"] * 1.25 * 1.16

    @rx.var
    def payback(self) -> float:
        return self.investment / self.result["ahorro_anual"] if self.result["ahorro_anual"] > 0 else 0