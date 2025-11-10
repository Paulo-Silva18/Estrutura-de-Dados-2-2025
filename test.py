# pip install selenium webdriver-manager

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
# Importa a 'espera explícita'
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 1. Configuração: 
print("Iniciando o navegador Chrome...")
service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()

try:
    # 2. Navegação:
    print("Acessando a Wikipedia...")
    driver.get("https://pt.wikipedia.org")
    
    # 3. Ação: Encontrar o campo de busca
    # Usando XPath para o campo de busca (só para manter o padrão)
    print("Encontrando o campo de busca e digitando 'Python'...")
    campo_busca = driver.find_element(By.XPATH, "//*[@id='searchInput']")
    
    # 4. Ação: Digitar no campo de busca
    campo_busca.send_keys("Python")
    
    time.sleep(1) # Pausa didática

    # 5. Ação: Encontrar o botão de busca e clicar
    print("Clicando no botão de busca...")
    
    botao_busca = driver.find_element(By.XPATH, "//*[@id='searchform']//button")
    botao_busca.click()

    # 6. Verificação (Assert):
    print("Aguardando a página de resultados...")
    
    # Vamos esperar até 10s para que o título CONTENHA "Python"
    WebDriverWait(driver, 10).until(
        EC.title_contains("Python")
    )

    # Se a linha acima passou, o título já foi carregado.
    titulo_pagina = driver.title
    print(f"O título da nova página é: {titulo_pagina}")

    if "Python – Wikipédia, a enciclopédia livre" in titulo_pagina:
        print("\nSUCESSO: O teste foi concluído e a página correta foi carregada.")
    else:
        print(f"\nFALHA: O título esperado não foi encontrado. Título atual: {titulo_pagina}")

except Exception as e:
    print(f"\nOcorreu um erro inesperado: {e}")

finally:
    # 7. Finalização:
    print("Fechando o navegador em 5 segundos...")
    time.sleep(5)
    driver.quit()