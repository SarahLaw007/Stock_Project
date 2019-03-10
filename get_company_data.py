import asyncio
from bs4 import BeautifulSoup

def handle_request(raw_html):
    soup = BeautifulSoup(raw_html, "html.parser")
    
    # ex/eff rate and cash amount
    table_elements = soup.select(
            "#quotes_content_left_dividendhistoryGrid > tbody > tr:nth-child(1)").pop()
    cols = table_elements.find_all("td")

    ex_div_col = cols[0]
    cash_col = cols[2]

    ex_div = ex_div_col.text.strip("\n")

