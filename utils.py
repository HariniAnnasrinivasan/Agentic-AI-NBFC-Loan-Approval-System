import re

def parse_money(text):
    """
    Converts money text like:
    '2 lakhs', '4,00,000', '90,000 per month'
    into integer rupees.
    """
    if not text:
        return 0

    text = text.lower()
    text = text.replace(",", "").replace("₹", "")

    lakh_match = re.search(r"(\d+)\s*lakh", text)
    if lakh_match:
        return int(lakh_match.group(1)) * 100000

    number_match = re.search(r"\d+", text)
    if number_match:
        return int(number_match.group())

    return 0
