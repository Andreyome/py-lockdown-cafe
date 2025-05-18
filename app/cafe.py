from datetime import date
from app.errors import (NotVaccinatedError,
                        NotWearingMaskError,
                        OutdatedVaccineError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if not visitor.get("vaccine"):
            raise NotVaccinatedError(f"{visitor["name"]}"
                                     f" has not vaccinated!")
        if visitor["vaccine"]["expiration_date"] < date.today():
            raise OutdatedVaccineError(f"{visitor["name"]}"
                                       f" vaccine expired!")
        if visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError(f"{visitor["name"]}"
                                      f" is not a wearing mask")
        return f"Welcome to {self.name}"
