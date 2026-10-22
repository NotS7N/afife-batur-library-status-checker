import time
import os
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright
from winotify import Notification

load_dotenv()

USERNAME = os.getenv("LIBRARY_USERNAME").strip()
PASSWORD = os.getenv("LIBRARY_PASSWORD")
URL = "https://kutuphanerezervasyon.ibb.gov.tr/?p=1&dil=0"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_context().new_page()

    while True:
        print(time.strftime("%H:%M:%S"), "checking...")
        try:
            page.goto(URL)

            # sign in only if the login form is showing
            if page.locator('input[name="kullanici"]').count() > 0:
                page.locator('input[name="kullanici"]').fill(USERNAME)
                page.locator('input[name="sifre"]').fill(PASSWORD)
                page.get_by_role("button", name="Giriş Yap").click()
                page.wait_for_load_state()

                # press the reservation link
                page.locator("div").filter(
                    has_text="İBB Kütüphaneleri Rezervasyon Sistemine Hoş Geldiniz... İPA İSTANBUL KİTAPLIĞI"
                ).get_by_role("link").click()
                page.wait_for_load_state()

            if page.get_by_text("İBB AFİFE BATUR KÜTÜPHANESİ").first.is_visible():
                print("FOUND")
                Notification(app_id="Library", title="Found", msg="AFİFE BATUR is on the page").show()
            else:
                print("not found")
        except Exception as e:
            print("error:", e)

        time.sleep(60)