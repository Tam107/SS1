def taxCalculator(income: int) -> float:
    """
    Calculate personal income tax based on average monthly income.
    Input: income in VND
    Output: tax in VND
    """
    million = income / 1_000_000  # convert to million VND

    if million < 5:
        tax_million = million * 0.05
    elif million <= 10:
        tax_million = 0.25 + (million - 5) * 0.10
    elif million <= 18:
        tax_million = 0.75 + (million - 10) * 0.15
    elif million <= 32:
        tax_million = 1.95 + (million - 18) * 0.20
    elif million <= 52:
        tax_million = 4.75 + (million - 32) * 0.25
    elif million <= 90:
        tax_million = 9.75 + (million - 52) * 0.30
    else:
        tax_million = 18.15 + (million - 80) * 0.35

    return round(tax_million * 1_000_000,2)  # convert back to VND


print(taxCalculator(88000000))