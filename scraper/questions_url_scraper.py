from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver
from tqdm import tqdm
import pandas as pd
import time


def extract_questions_url():
    base_url = "https://stackoverflow.com/questions?tab=newest"
    questions_urls = []

    try:
        for idx in tqdm(range(1510)):
            page_no = idx + 1
            page_url = f"{base_url}&page={page_no}"
            driver.get(page_url)

            questions = driver.find_elements(
                By.XPATH,
                "//h3[contains(@class,'s-post-summary--content-title')]//a[contains(@class,'s-link')]",
            )

            try:
                for question in questions:
                    question_title = question.text
                    question_url = question.get_attribute("href")

                    questions_urls.append(
                        {"Title": question_title, "URL": question_url}
                    )

                time.sleep(1)
            except:
                continue
    except:
        print("error occured!")

    return questions_urls


if __name__ == "__main__":
    options = Options()
    options.add_argument("--incognito")
    options.add_experimental_option("excludeSwitches", ["enable-logging"])

    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()), options=options
    )
    questions_urls = extract_questions_url()

    df = pd.DataFrame(data=questions_urls, columns=questions_urls[0].keys())
    df.to_csv("data/questions_urls.csv", index=False)

    driver.quit()
