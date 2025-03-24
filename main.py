import smtplib
import os
from bs4 import BeautifulSoup
import requests
from dotenv import load_dotenv
load_dotenv()
header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-GB,de;q=0.8,fr;q=0.6,en;q=0.4,ja;q=0.2",
    "Dnt": "1",
    "Priority": "u=1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Sec-Gpc": "1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:126.0) Gecko/20100101 Firefox/126.0",
}
flipper = requests.get("https://www.amazon.pl/Flipper-FLP-Z-W-R04-Zero/dp/B0BFXKSFNT/ref=sr_1_1?__mk_pl_PL=ÅMÅŽÕÑ&crid=HJ1AIQRAVS01&dib=eyJ2IjoiMSJ9.S-Q5-nn-pIz8yV6PuJ5dsK-UOjpdWYe9wWZ5UYfkrLSq1MyV2rahdHm6lvuQsEr8yTqYOjJ81BOcNlaqKKmm7deQ4O7YzKaI4EXf6XstpznAt4HAD9foBzAW61UnJDov43473jZMjktuAY03f07-MhZeQbk2X6XlTjODk5_DHTLp8iSbP2Qe7pEc3j3r7uzrgWfY0KwgBveiwmjyePOf8oQiWbNdGNDkYAHWKZaA4vT6vzF_b2UlpTFTyEHWU3tzDRXGAPZIZTgH0rb4a2Gvk-CaCaIA1o8bNOSd0P2pNjUwfuwzxtENmRfGBYpqkC8l9ZvrCv_mkUQdmD4N9CA7MqM18TJy8Gn9cOvtYVN05YW6O-bRrYJ-t1vxU-yfueARuLVkLBZpZCyb6pLnWnz527ogE01pLUBwAUxYN8gHJxalp0NFIftKPbT9YwPv2B4v.6Zm0A1OzwoEYU9MQXMbgfxPfeKRjBxtFmlabnDG4pro&dib_tag=se&keywords=flipper&qid=1739966246&sprefix=flipper%2Caps%2C164&sr=8-1", headers=header)
soup = BeautifulSoup(flipper.text, "html.parser")
price = soup.find("span", class_="a-offscreen").text
price = float((price.split("zł")[0]).replace(",", "."))
title = soup.find("span", id="productTitle").text
title = " ".join(title.split())
if price < 700:
    connection = smtplib.SMTP('smtp.gmail.com', 587)
    connection.starttls()
    connection.login(user=os.environ["EMAIL_ADDRESS"], password=os.environ["EMAIL_PASSWORD"])
    connection.sendmail(from_addr=os.environ["EMAIL_ADDRESS"], to_addrs="test@gmail.com", msg=f"{title} is now {price} zł!")
    connection.quit()