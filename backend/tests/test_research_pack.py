from utils.research_pack import (
    build_research_pack,
    get_company_snapshot,
    get_company_summary,
    get_financial_snapshot,
    get_price_movement,
    get_recent_news,
)

#######################################################################################
#                          RESEARCH PACK GENERATION TESTING                           #
#######################################################################################


def test_build_research_pack(valid_mcp_data):
    result = build_research_pack(valid_mcp_data)

    assert result["company_summary"] != ""
    assert result["company_snapshot"]["symbol"] == "AAPL"
    assert result["financial_snapshot"] != {}
    assert result["price_movement"]["current_price"] is not None
    assert len(result["recent_news"]) <= 15
    assert result["data_confidence"] == 100
    assert result["flags"] == []
