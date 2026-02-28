import pytest
try:
    import barriga_api as api
except Exception:
    from copilot.api import barriga_api as api


@pytest.fixture
def client():
    api.app.config['TESTING'] = True
    with api.app.test_client() as client:
        yield client


@pytest.fixture
def token(client):
    resp = client.post('/signin', json={'email': 'user@mail.com', 'senha': '123456'})
    assert resp.status_code == 200
    return resp.get_json()['token']


def test_signin_success(client):
    r = client.post('/signin', json={'email': 'user@mail.com', 'senha': '123456'})
    assert r.status_code == 200
    assert 'token' in r.get_json()


def test_signin_fail(client):
    r = client.post('/signin', json={'email': 'wrong@mail.com', 'senha': '000'})
    assert r.status_code == 401


def test_unauthorized_access(client):
    r = client.get('/contas')
    assert r.status_code == 401


def test_create_and_list_accounts(client, token):
    headers = {'Authorization': f'Bearer {token}'}
    r = client.post('/contas', json={'nome': 'Conta A'}, headers=headers)
    assert r.status_code == 201
    assert r.get_json()['nome'] == 'Conta A'

    r2 = client.get('/contas', headers=headers)
    assert r2.status_code == 200
    assert any(c['nome'] == 'Conta A' for c in r2.get_json())


def test_create_duplicate(client, token):
    headers = {'Authorization': f'Bearer {token}'}
    client.post('/contas', json={'nome': 'Conta B'}, headers=headers)
    r = client.post('/contas', json={'nome': 'Conta B'}, headers=headers)
    assert r.status_code == 400


def test_update_account(client, token):
    headers = {'Authorization': f'Bearer {token}'}
    r = client.post('/contas', json={'nome': 'Conta C'}, headers=headers)
    acc = r.get_json()
    r2 = client.put(f"/contas/{acc['id']}", json={'nome': 'Conta C2'}, headers=headers)
    assert r2.status_code == 200
    assert r2.get_json()['nome'] == 'Conta C2'

    r3 = client.put('/contas/999', json={'nome': 'X'}, headers=headers)
    assert r3.status_code == 404


def test_delete_account(client, token):
    headers = {'Authorization': f'Bearer {token}'}
    r = client.post('/contas', json={'nome': 'Conta D'}, headers=headers)
    acc = r.get_json()
    r2 = client.delete(f"/contas/{acc['id']}", headers=headers)
    assert r2.status_code == 204

    r3 = client.delete('/contas/999', headers=headers)
    assert r3.status_code == 404


def test_reset(client, token):
    headers = {'Authorization': f'Bearer {token}'}
    client.post('/contas', json={'nome': 'Conta E'}, headers=headers)
    r = client.get('/reset', headers=headers)
    assert r.status_code == 200
    assert api.contas == []
