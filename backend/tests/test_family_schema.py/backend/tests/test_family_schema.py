import pytest
from fastapi.testclient import TestClient
from pydantic import ValidationError

from app.main import app
from app.schemas.family import FamilyCreate


def test_family_schema_accepts_minimal_valid_household():
    family = FamilyCreate(residents=3, consent_given=True)

    assert family.residents == 3
    assert family.children == 0
    assert family.pregnant_people == 0
    assert family.older_adults == 0
    assert family.consent_given is True


@pytest.mark.parametrize(
    "payload",
    [
        {"residents": 0, "consent_given": True},
        {"residents": 2, "children": -1, "consent_given": True},
        {"residents": 2, "pregnant_people": -1, "consent_given": True},
        {"residents": 2, "older_adults": -1, "consent_given": True},
        {"residents": 2, "consent_given": False},
        {"residents": 2, "consent_given": True, "cpf": "00000000000"},
    ],
)
def test_family_schema_rejects_invalid_or_unexpected_data(payload):
    with pytest.raises(ValidationError):
        FamilyCreate.model_validate(payload)


def test_health_endpoint_returns_ok():
    client = TestClient(app)

    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
