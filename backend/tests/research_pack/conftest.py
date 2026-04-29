import pytest


# ── Research Pack Data Fixture ────────────────────────────────────────


@pytest.fixture
def valid_deduced_mcp(valid_mcp_data):
    from utils.confidence_calculator import calculate_confidence_score

    return calculate_confidence_score(valid_mcp_data)


# ── Research Pack Data Fixture ────────────────────────────────────────


@pytest.fixture
def empty_company_info():
    return {}
