import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.bet365.com/#/AC/B3/C20691614/D1/E47203934/F2/")
htmlSoup = BeautifulSoup(response.content, 'html.parser')
odds = htmlSoup.select('body > div > div > div.wc-PageView > div.wc-PageView_Main > div.wcl-CommonElementStyle_NavContentContainer > div.wcl-CommonElementStyle_PrematchCenter > div.cm-CouponModule > div > div.gll-MarketGroup.cm-CouponMarketGroup.cm-CouponMarketGroup_DropdownIsAvailable.cm-CouponMarketGroup_Open > div.gll-MarketGroup_Wrapper > div > div:nth-child(2) > div.gll-ParticipantOddsOnlyDarker.gll-Participant_General.gll-ParticipantOddsOnly > span')
print(odds)