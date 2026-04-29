from utils.types import CompanySnapshot

from utils.research_pack import (
    build_research_pack,
    get_company_snapshot,
    get_company_summary,
    get_financial_snapshot,
    get_price_movement,
    get_recent_news,
)


# ── Research Pack Generation Testing ────────────────────────────────────────


def test_build_research_pack_valid(valid_deduced_mcp):
    result = build_research_pack(valid_deduced_mcp)

    assert result["company_summary"] != ""
    assert result["company_snapshot"]["symbol"] == "AAPL"
    assert result["financial_snapshot"] != {}
    assert result["price_movement"]["current_price"] is not None
    assert len(result["recent_news"]) <= 15
    assert result["data_confidence"] == 100
    assert result["flags"] == []


# ── Research Pack Company Summary Testing ────────────────────────────────────


def test_get_company_summary_valid(valid_company_info):
    assert get_company_summary(valid_company_info) != ""


def test_get_company_summary_missing_field(empty_company_info):
    assert get_company_summary(empty_company_info) == ""


# ── Research Pack Company Snapshot Testing ────────────────────────────────────


def test_get_company_snapshot_valid(valid_company_info):
    assert get_company_snapshot(valid_company_info) != {}


def test_get_company_snapshot_missing_fields(invalid_company_info):
    result: CompanySnapshot = get_company_snapshot(invalid_company_info)
    for v in result.values():
        assert v is None
