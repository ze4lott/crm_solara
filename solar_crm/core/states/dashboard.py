import reflex as rx
from solar_crm.core.mock_data import *
from typing import Any
from solar_crm.calculations import solar_calculation, num

class DashboardState(rx.State):

    active_module: str = "overview"
    is_loading: bool = False
    search_query: str = ""
    prospectos: list[dict[str, Any]] = []
    cotizaciones: list[dict[str, Any]] = []
    proyectos: list[dict[str, Any]] = []
    actividades: list[dict[str, Any]] = []
    initialized: bool = False
    toast: str = ""

    # Formularios de captura
    nuevo_nombre: str = ""
    nueva_empresa: str = ""
    nuevo_correo: str = ""
    nuevo_consumo: str = "10000"
    nuevo_sector: str = "Industrial"
    quote_cliente: str = "Frío Norte Industrial"
    quote_consumo: str = "25000"
    quote_tarifa: str = "2.65"
    quote_panel: str = "600"
    quote_hsp: str = "5.2"
    quote_rendimiento: str = "0.80"
    quote_cobertura: str = "80"
    quote_margen: str = "25"
    quote_descuento: str = "0"
    quote_iva: str = "16"
    config_precio_kwp: str = "18500"
    config_iva: str = "16"
    config_hsp: str = "5.2"
    config_rendimiento: str = "0.80"
    actividad_titulo: str = ""
    actividad_cliente: str = "Frío Norte Industrial"
    actividad_tipo: str = "Llamada"

    # -----------------------------------------------------------------------------
    # Computed Vars
    # -----------------------------------------------------------------------------

    @rx.var
    def filtered_prospectos(self) -> list[dict[str, Any]]:
        q = self.search_query.strip().lower()
        return [p for p in self.prospectos if
                not q or q in p["nombre"].lower() or q in p["empresa"].lower() or q in p["correo"].lower()]

    @rx.var
    def filtered_cotizaciones(self) -> list[dict[str, Any]]:
        q = self.search_query.strip().lower()
        return [p for p in self.cotizaciones if not q or q in p["folio"].lower() or q in p["cliente"].lower()]

    @rx.var
    def total_pipeline(self) -> float:
        return sum(float(p.get("valor", 0)) for p in self.prospectos if p.get("etapa") not in {"Ganado", "Perdido"})

    @rx.var
    def capacidad_total(self) -> float:
        return sum(float(q.get("kwp", 0)) for q in self.cotizaciones)

    @rx.var
    def pendientes_actividades(self) -> int:
        return sum(1 for a in self.actividades if a.get("estado") == "Pendiente")

    @rx.var
    def quote_results(self) -> dict[str, float]:
        return solar_calculation(num(self.quote_consumo), num(self.quote_tarifa), num(self.quote_panel, 600),
                                 num(self.quote_hsp, 5.2), num(self.quote_rendimiento, .8),
                                 num(self.quote_cobertura, 80), num(self.config_precio_kwp, 18500))

    @rx.var
    def quote_total(self) -> float:
        r = self.quote_results
        base = r["inversion"]
        margen = min(90.0, max(0.0, num(self.quote_margen, 25)))
        precio = base / (1 - margen / 100) if margen < 100 else 0
        descuento = min(100.0, max(0.0, num(self.quote_descuento)))
        subtotal = precio * (1 - descuento / 100)
        return subtotal * (1 + max(0, num(self.quote_iva, 16)) / 100)

    @rx.var
    def quote_margin_value(self) -> float:
        base = self.quote_results["inversion"]
        return max(0, self.quote_total / (1 + max(0, num(self.quote_iva, 16)) / 100) - base)

    @rx.var
    def prospectos_por_etapa(self) -> dict[str, int]:
        etapas = ["Nuevo", "Contactado", "Calificado", "Propuesta", "Cerrado"]
        resultado = {etapa: 0 for etapa in etapas}

        for prospecto in self.prospectos:
            etapa = prospecto.get("etapa", "Nuevo")
            if etapa in resultado:
                resultado[etapa] += 1

        return resultado

    def on_load(self):
        if not self.initialized:
            self.load_prospectos()
            self.load_cotizaciones()
            self.load_proyectos()
            self.load_actividades()
            self.initialized = True

    def load_dashboard(self):
        self.load_prospectos(); self.load_cotizaciones(); self.load_proyectos(); self.load_actividades()
        self.initialized = True

    def load_prospectos(self):
        if not self.prospectos: self.prospectos = [dict(x) for x in DEMO_PROSPECTS]

    def load_clientes(self): self.load_prospectos()

    def load_cotizaciones(self):
        if not self.cotizaciones: self.cotizaciones = [dict(x) for x in DEMO_QUOTES]

    def load_proyectos(self):
        if not self.proyectos: self.proyectos = [dict(x) for x in DEMO_PROJECTS]

    def load_actividades(self):
        if not self.actividades: self.actividades = [dict(x) for x in DEMO_ACTIVITIES]

    def set_active_module(self, module: str):
        self.active_module = module; self.toast = ""

    def set_search_query(self, value: str):
        self.search_query = value

    def set_form_value(self, field: str, value: str):
        if field in {"nuevo_nombre", "nueva_empresa", "nuevo_correo", "nuevo_consumo", "nuevo_sector", "quote_cliente", "quote_consumo", "quote_tarifa", "quote_panel", "quote_hsp", "quote_rendimiento", "quote_cobertura", "quote_margen", "quote_descuento", "quote_iva", "config_precio_kwp", "config_iva", "config_hsp", "config_rendimiento", "actividad_titulo", "actividad_cliente", "actividad_tipo"}:
            setattr(self, field, value)

    def create_prospect(self):
        if not self.nuevo_nombre.strip() or not self.nueva_empresa.strip():
            self.toast = "Completa el nombre y la empresa del prospecto."; return
        new_id = max([int(p["id"]) for p in self.prospectos] + [0]) + 1
        self.prospectos = self.prospectos + [{"id": new_id, "nombre": self.nuevo_nombre.strip(), "empresa": self.nueva_empresa.strip(), "correo": self.nuevo_correo.strip() or "Sin correo", "telefono": "Pendiente", "ciudad": "Por definir", "sector": self.nuevo_sector, "consumo": max(0, num(self.nuevo_consumo)), "tarifa": 2.65, "etapa": "Nuevo", "valor": 0}]
        self.nuevo_nombre = ""; self.nueva_empresa = ""; self.nuevo_correo = ""; self.toast = "Prospecto agregado correctamente."

    def advance_prospect(self, prospect_id: int):
        stages = [
            "Nuevo",
            "Contactado",
            "Calificado",
            "Visita técnica",
            "Cotización en preparación",
            "Cotización enviada",
            "Negociación",
            "Ganado"
        ]
        updated = []
        for p in self.prospectos:
            item = dict(p)
            if item["id"] == prospect_id:
                idx = stages.index(item["etapa"]) if item["etapa"] in stages else -1
                item["etapa"] = stages[min(idx + 1, len(stages) - 1)]
            updated.append(item)
        self.prospectos = updated; self.toast = "Etapa comercial actualizada."

    def delete_prospect(self, prospect_id: int):
        self.prospectos = [
            p for p in self.prospectos if p["id"] != prospect_id
        ]; self.toast = "Prospecto eliminado de la sesión."

    def save_quote(self):
        r = self.quote_results
        folio = f"SOL-2026-{len(self.cotizaciones) + 1:03d}"
        margen = min(90.0, max(0.0, num(self.quote_margen, 25)))
        precio_base = r["inversion"] / (1 - margen / 100) if margen < 100 else 0
        total = self.quote_total
        quote = {"folio": folio, "cliente": self.quote_cliente, "kwp": round(r["potencia_instalada"], 2), "total": round(total, 2), "estado": "Borrador", "consumo": num(self.quote_consumo), "tarifa": num(self.quote_tarifa), "panel_w": num(self.quote_panel, 600), "hsp": num(self.quote_hsp, 5.2), "rendimiento": num(self.quote_rendimiento, .8), "cobertura": num(self.quote_cobertura, 80), "margen": margen, "costo_estimado": round(r["inversion"], 2), "precio_base": round(precio_base, 2), "generacion": round(r["generacion_anual"], 2), "ahorro": round(r["ahorro_anual"], 2)}
        self.cotizaciones = [quote] + self.cotizaciones
        self.active_module = "cotizaciones"; self.toast = f"Cotización {folio} guardada como borrador."

    def duplicate_quote(self, folio: str):
        original = next((q for q in self.cotizaciones if q["folio"] == folio), None)
        if not original: return
        copy = dict(original); copy["folio"] = f"SOL-2026-{len(self.cotizaciones) + 1:03d}"; copy["estado"] = "Borrador"
        self.cotizaciones = [copy] + self.cotizaciones; self.toast = f"Se creó una copia de {folio}."

    def set_quote_status(self, folio: str, status: str):
        self.cotizaciones = [{**q, "estado": status} if q["folio"] == folio else q for q in self.cotizaciones]
        self.toast = f"Estado de {folio}: {status}."

    def delete_quote(self, folio: str):
        self.cotizaciones = [
            q for q in self.cotizaciones if q["folio"] != folio
        ]; self.toast = f"Cotización {folio} eliminada de la sesión."

    def complete_activity_title(self, title: str):
        self.actividades = [{**a, "estado": "Completada"} if a.get("titulo") == title else a for a in self.actividades]
        self.toast = "Actividad marcada como completada."

    def add_activity(self):
        if not self.actividad_titulo.strip(): self.toast = "Escribe el título de la actividad."; return
        self.actividades = [
                               {
                                   "titulo": self.actividad_titulo.strip(),
                                   "cliente": self.actividad_cliente,
                                   "tipo": self.actividad_tipo,
                                   "fecha": "Hoy · Por programar",
                                   "estado": "Pendiente"
                               }
                           ] + self.actividades
        self.actividad_titulo = ""; self.toast = "Actividad agregada."

    def save_config(self):
        self.config_precio_kwp = str(max(0, num(self.config_precio_kwp, 18500)))
        self.config_iva = str(max(0, min(100, num(self.config_iva, 16))))
        self.config_hsp = str(max(.1, num(self.config_hsp, 5.2)))
        self.config_rendimiento = str(min(1, max(.1, num(self.config_rendimiento, .8))))
        self.quote_hsp = self.config_hsp; self.quote_rendimiento = self.config_rendimiento; self.quote_iva = self.config_iva
        self.toast = "Configuración aplicada a los cálculos nuevos."
