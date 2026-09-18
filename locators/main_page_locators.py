from selenium.webdriver.common.by import By


class MainPageLocators:
    """Локаторы для главной страницы Яндекс.Самокат"""

    # Кнопки "Заказать"
    ORDER_BUTTON_TOP = (By.XPATH, "//button[text()='Заказать']")
    ORDER_BUTTON_BOTTOM = (By.XPATH, "//button[contains(@class, 'Button_Middle')]")

    # Логотипы
    YANDEX_LOGO = (By.XPATH, "//a[contains(@class, 'Header_LogoYandex')]")
    SCOOTER_LOGO = (By.XPATH, "//a[contains(@class, 'Header_LogoScooter')]")