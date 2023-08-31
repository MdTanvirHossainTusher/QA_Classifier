from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver
from tqdm import tqdm
import pandas as pd
import time


def extract_questions_details():
    df = pd.read_csv("data/questions_urls.csv")
    questions_urls = df.URL.to_list()

    questions_data = []

    for question_url_idx in tqdm(range(22257)):
        try:
            driver.get(questions_urls[question_url_idx])
            time.sleep(1)

            title = df[df["URL"] == questions_urls[question_url_idx]]["Title"].values[0]

            question = driver.find_element(
                By.XPATH, "//div[contains(@class,'js-post-body')]"
            ).text.replace("\n", "")

            categories = driver.find_elements(
                By.XPATH,
                "//div[contains(@class,'d-flex')]//ul//li[contains(@class,'d-inline')]//a",
            )

            all_categories = []

            for category in categories:
                category_name = category.text
                all_categories.append(category_name)

            questions_data.append(
                {
                    "Title": title,
                    "URL": questions_urls[question_url_idx],
                    "Question": question,
                    "Categories": all_categories,
                }
            )
            time.sleep(1)

            df_new = pd.DataFrame(data=questions_data, columns=questions_data[0].keys())
            df_new.to_csv("data/questions_details.csv", index=False)

        except:
            time.sleep(1)
            continue


if __name__ == "__main__":
    options = Options()
    options.add_argument("--incognito")
    options.add_experimental_option("excludeSwitches", ["enable-logging"])

    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()), options=options
    )

    extract_questions_details()

    driver.quit()
