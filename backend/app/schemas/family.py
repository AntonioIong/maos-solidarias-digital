from pydantic import BaseModel, ConfigDict, Field, field_validator


class FamilyCreate(BaseModel):
    """Input contract for registering a household without direct identifiers."""

    model_config = ConfigDict(extra="forbid")

    residents: int = Field(gt=0)
    children: int = Field(default=0, ge=0)
    pregnant_people: int = Field(default=0, ge=0)
    older_adults: int = Field(default=0, ge=0)
    consent_given: bool

    @field_validator("consent_given")
    @classmethod
    def require_consent(cls, value: bool) -> bool:
        if not value:
            raise ValueError("O consentimento deve ser registrado antes do cadastro.")
        return value
