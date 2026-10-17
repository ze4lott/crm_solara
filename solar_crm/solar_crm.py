from __future__ import annotations

"""

Solar CRM proyecto para Manuel S. Aguilar

"""
"""
Hosted  by Utopian Nexus
"""


import reflex as rx
from solar_crm.pages.index import index_page
from solar_crm.pages.dashboard import dashboard_page
from solar_crm.pages.login import login_page
from solar_crm.pages.calculadora import calc_page


app = rx.App(
    theme=rx.theme(
        appearance="light",
        accent_color="green",
        radius="large"
    )
)
