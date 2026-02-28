import pytest
import requests
import uuid


BASE_URL = "https://barrigarest.wcaquino.me"
EMAIL = "a@a"
SENHA = "a"


# =========================
# FIXTURE DE AUTENTICAÇÃO
# =========================
@pytest.fixture(scope="session")
def token():
    payload = {
        "email": EMAIL,
        "senha": SENHA
    }

    response = requests.post(f"{BASE_URL}/signin", json=payload)
    assert response.status_code == 200

    return response.json()["token"]


@pytest.fixture
def headers(token):
    return {
        "Authorization": f"JWT {token}"
    }


# =========================
# TESTES
# =========================

def test_criar_conta(headers):
    nome_conta = f"Conta_{uuid.uuid4()}"

    response = requests.post(
        f"{BASE_URL}/contas",
        json={"nome": nome_conta},
        headers=headers
    )

    assert response.status_code == 201
    assert response.json()["nome"] == nome_conta


def test_listar_contas(headers):
    response = requests.get(
        f"{BASE_URL}/contas",
        headers=headers
    )

    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0


def test_atualizar_conta(headers):
    # Criar conta primeiro
    nome_conta = f"Conta_{uuid.uuid4()}"
    create_response = requests.post(
        f"{BASE_URL}/contas",
        json={"nome": nome_conta},
        headers=headers
    )

    assert create_response.status_code == 201
    conta_id = create_response.json()["id"]

    # Atualizar
    novo_nome = f"Conta_Atualizada_{uuid.uuid4()}"
    update_response = requests.put(
        f"{BASE_URL}/contas/{conta_id}",
        json={"nome": novo_nome},
        headers=headers
    )

    assert update_response.status_code == 200
    assert update_response.json()["nome"] == novo_nome

    # Cleanup
    requests.delete(
        f"{BASE_URL}/contas/{conta_id}",
        headers=headers
    )


def test_remover_conta(headers):
    # Criar conta
    nome_conta = f"Conta_{uuid.uuid4()}"
    create_response = requests.post(
        f"{BASE_URL}/contas",
        json={"nome": nome_conta},
        headers=headers
    )

    assert create_response.status_code == 201
    conta_id = create_response.json()["id"]

    # Remover
    delete_response = requests.delete(
        f"{BASE_URL}/contas/{conta_id}",
        headers=headers
    )

    assert delete_response.status_code == 204
    