import pytest
from httpx import AsyncClient
from src.main import app
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))


@pytest.mark.asyncio
async def test_pin_ai_powered():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/pin_ai_powered/")
        assert response.status_code == 200
        assert "Welcome to the AI-Powered model" in response.json().get("message")


@pytest.mark.asyncio
async def test_pin_arcd():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/pin_arcd/")
        assert response.status_code == 200
        assert "Welcome to the ARCD model" in response.json().get("message")


@pytest.mark.asyncio
async def test_pin_customer_support():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/pin_customer_support/")
        assert response.status_code == 200
        assert "Welcome to the Customer Support model" in response.json().get("message")


@pytest.mark.asyncio
async def test_pin_forest():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/pin_forest/")
        assert response.status_code == 200
        assert "Welcome to the Forest model" in response.json().get("message")


@pytest.mark.asyncio
async def test_pin_inventory():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/pin_inventory/")
        assert response.status_code == 200
        assert "Welcome to the Inventory model" in response.json().get("message")


@pytest.mark.asyncio
async def test_pin_marketing():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/pin_marketing/")
        assert response.status_code == 200
        assert "Welcome to the Marketing model" in response.json().get("message")


@pytest.mark.asyncio
async def test_pin_PhiSNAIL():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/pin_PhiSNAIL/")
        assert response.status_code == 200
        assert "Welcome to the PhiSNAIL model" in response.json().get("message")


@pytest.mark.asyncio
async def test_pin_PhiUSIIL():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/pin_PhiUSIIL/")
        assert response.status_code == 200
        assert "Welcome to the PhiUSIIL model" in response.json().get("message")


@pytest.mark.asyncio
async def test_pin_sales():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/pin_sales/")
        assert response.status_code == 200
        assert "Welcome to the Sales model" in response.json().get("message")


@pytest.mark.asyncio
async def test_pin_security_hr():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/pin_security_hr/")
        assert response.status_code == 200
        assert "Welcome to the Security & HR model" in response.json().get("message")


@pytest.mark.asyncio
async def test_pin_supermarket():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/pin_supermarket/")
        assert response.status_code == 200
        assert "Welcome to the Supermarket model" in response.json().get("message")

@pytest.mark.asyncio
async def test_pin_technical_support():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/pin_technical_support/")
        assert response.status_code == 200
        assert "Welcome to the Technical Support model" in response.json().get("message")

@pytest.mark.asyncio
async def test_pin_wholesale():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/pin_wholesale/")
        assert response.status_code == 200
        assert "Welcome to the Wholesale model" in response.json().get("message")


