import asyncio
from datetime import datetime, timezone

import reflex as rx


class tiempoTranscurridoDeLaBoda(rx.State):
    # Fecha en que “empieza” el contador (boda / unión)
    inicio: datetime = datetime(2024, 9, 14, 0, 0, 0, tzinfo=timezone.utc)

    # Solo para forzar recálculo de @rx.var en la UI
    _actualizacion: int = 0

    _tick_activo: bool = False

    @staticmethod
    def format_with_leading_zero(number: int) -> str:
        return f"{number:02}"

    def get_diferencia(self):
        """Tiempo transcurrido desde inicio hasta ahora."""
        ahora = datetime.now(timezone.utc)
        diferencia = ahora - self.inicio
        if diferencia.total_seconds() < 0:
            return None  # Aún no ha llegado esa fecha
        return diferencia

    @rx.var
    def años(self) -> str:
        diferencia = self.get_diferencia()
        if not diferencia:
            return "00"
        return self.format_with_leading_zero(diferencia.days // 365)

    @rx.var
    def meses(self) -> str:
        diferencia = self.get_diferencia()
        if not diferencia:
            return "00"
        return self.format_with_leading_zero((diferencia.days % 365) // 30)

    @rx.var
    def dias(self) -> str:
        diferencia = self.get_diferencia()
        if not diferencia:
            return "00"
        return self.format_with_leading_zero((diferencia.days % 365) % 30)

    @rx.event
    def tick(self, _=None):
        """Se llama desde el timer; basta con mutar estado para refrescar @rx.var."""
        self._actualizacion += 1

    @rx.event(background=True)
    async def tick_diario(self):
        """Bucle en segundo plano: un tick cada 24 h."""
        async with self:
            if self._tick_activo:
                return
            self._tick_activo = True

        while True:
            await asyncio.sleep(86_400)  # 24 horas
            async with self:
                self._actualizacion += 1

    def on_load(self):
        """Arranca el tick al cargar la página (una sola tarea en background)."""
        return tiempoTranscurridoDeLaBoda.tick_diario