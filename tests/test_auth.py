import pytest
from httpx import ASGITransport, AsyncClient

from app.main import app


@pytest.mark.anyio
async def test_register_existing_user(setup_service: None) -> None:
    """
    Проверяет регистрацию существующего пользователя.
    При попытке зарегистрировать пользователя с уже существующим именем,
    ожидается ошибка с кодом 409 и сообщением "User already exists".
    """
    username = "existing_user"
    password = "test_PASSWORD123#"

    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        await ac.post("/register", json={"username": username, "password": password})

    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        response = await ac.post("/register", json={"username": username, "password": password})

    assert response.status_code == 409
    assert response.json() == {"detail": "User already exists"}


@pytest.mark.anyio
async def test_login_user(setup_service: None, authenticated_user: str) -> None:
    """
    Проверяет успешный вход пользователя.
    Ожидается, что переданный пользователь будет авторизован.
    """
    assert authenticated_user is not None


@pytest.mark.anyio
async def test_login_invalid_credentials(setup_service: None) -> None:
    """
    Проверяет вход с неправильными учетными данными.
    При попытке войти с неправильным логином или паролем,
    ожидается ошибка с кодом 401 и сообщением "Invalid credentials".
    """
    username = "invalid_user"
    password = "test_PASSWORD123#_wrong"

    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        response = await ac.post("/login", json={"username": username, "password": password})

    assert response.status_code == 401
    assert response.json() == {"detail": "Invalid credentials"}


@pytest.mark.anyio
async def test_register_user_with_invalid_data(setup_service: None) -> None:
    """
    Проверяет регистрацию пользователя с некорректными данными.
    При попытке зарегистрировать пользователя с именем, которое слишком короткое,
    или паролем, который не соответствует требованиям, ожидается ошибка с кодом 422
    и соответствующим сообщением об ошибке.
    """
    username = "us"
    password = "12345"

    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        response = await ac.post("/register", json={"username": username, "password": password})

    assert response.status_code == 422