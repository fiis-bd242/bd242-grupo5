import reflex as rx


class QueryEspacioComun(rx.State):
    fecha_inicio: str
    fecha_fin: str
    id_espacio_comun: str
    espacios_comunes: list[list]

    @rx.event
    @rx.var
    def get_espacio_comun_for_evento(self):
        with rx.session() as session:
            # Base de la consulta
            query = """
                SELECT ec.id_espacio_comun
                FROM Espacio_comun ec
                LEFT JOIN Evento e ON ec.id_espacio_comun = e.id_espacio_comun
                WHERE (
                    e.fecha_inicio IS NULL OR
                    e.fecha_fin < :fecha_inicio OR
                    e.fecha_inicio > :fecha_fin
                )
                AND ec.id_espacio_comun LIKE :cadena;
                """
            params = {
                "fecha_inicio": self.fecha_inicio,
                "fecha_fin": self.fecha_fin,
                "cadena": f"%{self.id_espacio_comun}%",
            }

            # Ejecutar la consulta
            result = session.exec(query, params).all()

            # Convertir los resultados en listas
            self.espacios_comunes = [list(row) for row in result]
