from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def web_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--verbose")
    options.add_argument('--no-sandbox')
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument("--window-size=1920, 1200")
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=options)
    return driver

data = [
    {'user': 'gakosantos@gasss.net', 'password': '@@Masuk123#oZ', 'wallet': '0x2d4d6792eef05e263d50fa2a0cd709ecbce640ff'},
    {'user': 'edwardsbud@gasss.net', 'password': '@@Masuk123#oZ', 'wallet': '0x05bd5bf4d370c5428d63eb882be3e98b12759501'},
    {'user': 'sovkas5@gasss.net', 'password': '@@Masuk123#oZ', 'wallet': '0x851eb7be4ccbce55696de3c6d5411f71cdb83a36'},
    {'user': 'natalkad@gasss.net', 'password': '@@Masuk123#oZ', 'wallet': '0x48b3dd626328d53352d7b51f379371423747baac'},
    {'user': 'beav21@gasss.net', 'password': '@@Masuk123#oZ', 'wallet': '0xe5363c45eec7a5cb4ec0c6a381068dab08b51da5'},


]

for idx, line in enumerate(data, start=1):  # Menambahkan fungsi enumerate untuk melacak nomor akun
    try:
        driver = web_driver()
        user = line['user']
        password = line['password']
        wallet_address = line['wallet']

        # LOGIN
        driver.get('https://auth.alchemy.com/')
    
        time.sleep(3)

        driver.find_element(By.XPATH,'//*[@id="gatsby-focus-wrapper"]/div/div[1]/div[2]/div/div[2]/form/label[1]/input').send_keys(user)
        time.sleep(2)

        driver.find_element(By.XPATH,'//*[@id="gatsby-focus-wrapper"]/div/div[1]/div[2]/div/div[2]/form/label[2]/input').send_keys(password)
        time.sleep(2)

        driver.find_element(By.XPATH,'//*[@id="gatsby-focus-wrapper"]/div/div[1]/div[2]/div/div[2]/form/button').click()
        time.sleep(3)


        driver.get('https://www.alchemy.com/faucets/ethereum-sepolia')
        time.sleep(3)

        driver.find_element(By.XPATH,'//*[@id="root"]/div[1]/div[1]/div/div[3]/span/div/button').click()
        print("Current URL is: %s" % driver.current_url)
        time.sleep(15)

       
        # END LOGIN

       

        def claim_arbit_sepolia(driver, wallet, max_attempts=4):
            attempt = 0
            
            while attempt < max_attempts:
                try:
                    # ARBIT SEPOLIA
                    driver.get('https://www.alchemy.com/faucets/arbitrum-sepolia')
                    time.sleep(2)

                    driver.find_element(By.XPATH,'//*[@id="root"]/div[1]/div[2]/div[2]/div[2]/div/span/form/div/div[1]/input').send_keys(wallet)
                    time.sleep(3)

                    driver.find_element(By.XPATH,'//*[@id="root"]/div[1]/div[2]/div[2]/div[2]/div/span/form/div/div[2]/button/div/span').click()
                    time.sleep(4)

                    element = WebDriverWait(web, 2).until(
                        EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div[1]/div[2]/div[3]/div[2]/div/div[2]/div/div[2]'))
                    )
                    print(f"Akun ke-{idx}: BERHASIL CLAIM ARBIT !! .")
                    break  # Keluar dari loop jika klaim berhasil dilakukan

                except:
                    
                    attempt += 1  # Tambah jumlah percobaan

                    if attempt == max_attempts:
                        try:
                            si_eror = driver.find_element(By.XPATH,'//*[@id="root"]/div[1]/div[2]/div[1]/div[3]/div/span')
                            pesan = si_eror.text
                            print(f"Akun ke-{idx}: GAGAL CLAIM ARBIT  - {pesan} ")
                                
                        except:
                            print(f"Akun ke-{idx}: GAGAL CLAIM ARBIT .")

     

       
        claim_arbit_sepolia(driver, wallet_address)
        driver.close()
        
    except:
        print(f"Akun ke-{idx}: TERJADI ERROR")
        driver.close()
