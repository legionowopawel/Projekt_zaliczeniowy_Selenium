import unittest
from selenium import webdriver
import time
import autopy

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


class WizzairRegistration(unittest.TestCase):

    def setUp(self):

        print("- Przygotowanie testu")
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('https://wizzair.com/pl-pl/#/')
        self.driver.implicitly_wait(40)

    def tearDown(self):
        print("- Sprzątanie po teście")
        self.driver.quit()

    def testInvalidtelefon(self):
        print("- Zaczynam wykonywanie testu")
        driver = self.driver
        zaloguj_btn = driver.find_element_by_xpath('//button[@data-test="navigation-menu-signin"]')
        zaloguj_btn.click()
        time.sleep(2)
        driver.save_screenshot("_01_zaloguj.png")

        time.sleep(6)
        rejestracja_bn = driver.find_element_by_xpath('//button[@data-test="registration"]')
        rejestracja_bn.click()
        time.sleep(2)
        driver.save_screenshot("_02_rejestracja.png")

        #imie
        imie_input = driver.find_element_by_xpath('//input[@data-test="registrationmodal-first-name-input"]')
        imie_input.send_keys("Pawel")
        driver.save_screenshot("01_imie.png")

        #nazwisko
        nazwisko_input = driver.find_element_by_xpath('//input[@data-test="registrationmodal-last-name-input"]')
        nazwisko_input.send_keys("Testujacy")
        driver.save_screenshot("02_nazwisko.png")

        #wybranie plci
        plec_input = driver.find_element_by_xpath('//input[@value="male"]')
        plec_input.click()
        driver.save_screenshot("03_plci.png")

        #wybieranie numeru kierunkowego
        nr_kierunkowy = driver.find_element_by_xpath('//div[@data-test="booking-register-country-code"]')
        nr_kierunkowy.click()
        driver.save_screenshot("04_kierunkowy1.png")

        nr_kierunkowy1 = driver.find_element_by_xpath('//input[@name="phone-number-country-code"]')
        nr_kierunkowy1.send_keys("Polska",Keys.ENTER)
        driver.save_screenshot("05_kierunkowy2.png")

        #wpisanie nr telefonu
        telefon_input = driver.find_element_by_xpath('//input[@data-test="check-in-step-contact-phone-number"]')
        telefon_input.send_keys("")
        driver.save_screenshot("06_telefon.png")

        #wpisanie email
        mail_input = driver.find_element_by_xpath('//input[@data-test="booking-register-email"]')
        mail_input.send_keys("paweltesterski123456@gmail.com")
        driver.save_screenshot("07_email.png")

        #wpisanie hasla
        haslo_input = driver.find_element_by_xpath('//input[@data-test="booking-register-password"]')
        haslo_input.send_keys("trlala@22")
        driver.save_screenshot("08_haslo.png")

        #wpisanie narodowosci
        narodowosc_input = driver.find_element_by_xpath('//input[@data-test="booking-register-country"]')
        narodowosc_input.send_keys("Polska",Keys.ENTER)
        driver.save_screenshot("09_narodowosc.png")

        #newsler
        driver.find_element_by_xpath('//div[@data-test="checkbox-newsletter"]')
        two = driver.find_element_by_xpath('//input[@data-test="registration-newsletter-checkbox"]')
        actions = ActionChains(driver)
        actions.move_to_element(two).click(two).perform()
        driver.save_screenshot("10_news.png")

        #polityka prywatnosci
        driver.find_element_by_xpath('//div[@data-test="checkbox-privacyPolicy"]')
        one = driver.find_element_by_xpath('//input[@data-test="registration-privacy-policy-checkbox"]')
        actions = ActionChains(driver)
        actions.move_to_element(one).click(one).perform()
        driver.save_screenshot("11_prywatnosc.png")

        #wizz polityka
        driver.find_element_by_xpath('//div[@data-test="checkbox-wizzAccountPolicy"]')
        zero = driver.find_element_by_xpath('//input[@data-test="registration-wizz-account-policy-checkbox"]')
        actions = ActionChains(driver)
        actions.move_to_element(zero).click(zero).perform()
        driver.save_screenshot("12_polityka.png")

        #zarejestruj
        zarejestracja_bn = driver.find_element_by_xpath('//button[@data-test="booking-register-submit"]')
        zarejestracja_bn.click()
        driver.save_screenshot("13_zarejestruj.png")

        time.sleep(25)

        driver.save_screenshot("14_dol_strony_po_zakonczeniu.png")

        possible_errors = driver.find_elements_by_xpath('//span[@class="input-error__message"]/span')
        visible_errors = []

        for error in possible_errors:
            if error.is_displayed():
                visible_errors.append(error)

        print("Ilość błędów widocznych na stronie: ",len(visible_errors))


        assert len(visible_errors) == 1
        self.assertEqual(len(visible_errors), 1)

        print("Tekst błędu widoczny na stronie: ", visible_errors[0].text)
        assert visible_errors[0].text == "Wpisz prawidłowy numer telefonu komórkowego."
        self.assertEqual(visible_errors[0].text, "Wpisz prawidłowy numer telefonu komórkowego.")

if __name__=="__main__":
    # Włączamy testy
    unittest.main()
