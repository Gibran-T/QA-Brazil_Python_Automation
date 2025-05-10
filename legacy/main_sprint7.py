from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from urban_routes_project.urban_routes_main_page import UrbanRoutesPage
from urban_routes_project.helpers import retrieve_phone_code
from urban_routes_project import data
import time

def main():
    # Configuração do navegador com logging ativado para capturar o código do telefone
    options = Options()
    options.set_capability("goog:loggingPrefs", {"performance": "ALL"})
    driver = webdriver.Chrome(options=options)
    driver.get(data.URBAN_ROUTES_URL)

    page = UrbanRoutesPage(driver)

    print("📍 Definindo endereços...")
    page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
    time.sleep(1)

    print("🚕 Selecionando tarifa Comfort...")
    page.click_taxi_option()
    page.click_comfort_icon()
    time.sleep(1)

    print("📞 Preenchendo telefone e confirmando código...")
    page.click_number_text(data.PHONE_NUMBER)
    time.sleep(1)
    code = retrieve_phone_code(driver)
    code_input = driver.find_element(By.ID, "code")
    code_input.send_keys(code)
    driver.find_element(By.XPATH, '//button[contains(text(),"Confirmar")]').click()
    time.sleep(1)

    print("💳 Adicionando cartão de crédito...")
    page.click_add_cartao(data.CARD_NUMBER, data.CARD_CODE)
    time.sleep(1)

    print("🗒️ Adicionando comentário ao motorista...")
    page.add_comentario(data.MESSAGE_FOR_DRIVER)
    time.sleep(1)

    print("🛏️ Selecionando cobertor e lençóis...")
    page.switch_cobertor()
    time.sleep(1)

    print("🍦 Pedindo 2 sorvetes...")
    page.add_ice()
    page.add_ice()
    time.sleep(1)

    print("🚖 Solicitando o táxi...")
    page.call_taxi()
    time.sleep(2)

    print("✅ Fluxo completo da Sprint 7 executado com sucesso!")

    driver.quit()

if __name__ == "__main__":
    main()
