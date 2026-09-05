import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

import pytest
from fastapi.testclient import TestClient
from app import app, validate_expense_ratio
client = TestClient(app)


def test_user_can_ask_question_successfully():
    response = client.post(
        "/ask",
        headers={"Authorization": "Bearer token-user-a"},
        json={
            "upload_id": 125,
            "question": "What is the expense ratio?"
        }
    )

    assert response.status_code == 200
    body = response.json()
    assert body["answer"] == "The expense ratio is 0.75%."
    assert body["citation"] == "Page 3"


def test_ask_rejects_empty_question():
    response = client.post(
        "/ask",
        headers={"Authorization": "Bearer token-user-a"},
        json={
            "upload_id": 125,
            "question": ""
        }
    )

    assert response.status_code == 422


def test_user_cannot_access_another_users_upload():
    response = client.post(
        "/ask",
        headers={"Authorization": "Bearer token-user-a"},
        json={
            "upload_id": 200,
            "question": "What is the NAV?"
        }
    )

    assert response.status_code == 404


def test_llm_failure_returns_503():
    response = client.post(
        "/ask",
        headers={"Authorization": "Bearer token-user-a"},
        json={
            "upload_id": 125,
            "question": "llm-fail test"
        }
    )

    assert response.status_code == 503
    assert response.json()["detail"] == "AI service temporarily unavailable"


def test_validate_expense_ratio_business_rule():
    assert validate_expense_ratio(0.75) == 0.75

    with pytest.raises(ValueError):
        validate_expense_ratio(-1)

    with pytest.raises(ValueError):
        validate_expense_ratio("abc")
