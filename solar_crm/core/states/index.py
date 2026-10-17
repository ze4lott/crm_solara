import reflex as rx

class IndexState(rx.State):
    active_page: str = "home"

    @rx.event
    def set_active(self, page_name: str):
        self.active_page = page_name



