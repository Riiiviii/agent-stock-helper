from utils.confidence_calculator import (
    calculate_confidence_score,
    calculate_financial_deduction,
    calculate_information_deductions,
    calculate_news_deductions,
    calculate_price_history_deduction,
    NEWS_COUNT_DEDUCTION,
    NEWS_RECENCY_DEDUCTION,
    MISSING_COMPANY_FIELDS_DEDUCTION,
    PRICE_HISTORY_DEDUCTION,
    MISSING_FINANCIALS_DEDUCTION,
)


#######################################################################################
#                          COMPANY CONFIDENCE SCORE TESTING                           #
#######################################################################################
def test_calculate_confidence_score_valid_data(valid_mcp_data):
    result = calculate_confidence_score(valid_mcp_data)

    assert result["confidence_score"]["score"] == 100
    assert result["issues"] == []
    assert result["confidence_score"]["deductions"]["missing_financials"] == 0
    assert result["confidence_score"]["deductions"]["news_count_below_3"] == 0
    assert result["confidence_score"]["deductions"]["news_older_than_14_days"] == 0
    assert result["confidence_score"]["deductions"]["price_history_under_90_days"] == 0
    assert result["confidence_score"]["deductions"]["missing_company_fields"] == 0


#######################################################################################
#                              COMPANY FINANCIAL TESTING                              #
#######################################################################################


def test_calculate_financial_deduction_valid(valid_company_financials):
    assert calculate_financial_deduction(valid_company_financials) == 0


def test_calculate_financial_deduction_invalid(empty_financials):
    assert (
        calculate_financial_deduction(empty_financials) == MISSING_FINANCIALS_DEDUCTION
    )


#######################################################################################
#                                 COMPANY NEWS TESTING                                #
#######################################################################################


def test_calculate_news_deductions_valid(valid_company_news):
    count_deduction, time_deduction = calculate_news_deductions(valid_company_news)
    assert count_deduction == 0
    assert time_deduction == 0


def test_calculate_news_deductions_empty(empty_news):
    assert calculate_news_deductions(empty_news) == (
        NEWS_COUNT_DEDUCTION,
        NEWS_RECENCY_DEDUCTION,
    )


def test_calculate_news_deductions_insufficient(insufficient_company_news):
    assert calculate_news_deductions(insufficient_company_news) == (
        NEWS_COUNT_DEDUCTION,
        0,
    )


def test_calculate_news_deductions_stale(stale_company_news):
    assert calculate_news_deductions(stale_company_news) == (0, NEWS_RECENCY_DEDUCTION)


#######################################################################################
#                             COMPANY INFORMATION TESTING                             #
#######################################################################################


def test_calculate_information_deductions(valid_company_info):
    assert calculate_information_deductions(valid_company_info) == (
        0,
        [],
    )


#######################################################################################
#                              COMPANY PRICE HISTORY TESTING                          #
#######################################################################################


def test_calculate_price_history_deduction(valid_company_price_history):
    assert calculate_price_history_deduction(valid_company_price_history) == 0
