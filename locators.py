from selenium.webdriver.common.by import By

# базовый адрес приложения
BASE_URL = "https://stellarburgers.nomoreparties.site/"

# Хедер / навигация
LOGIN_BTN_ON_MAIN   = (By.XPATH, "//button[text()='Войти в аккаунт']")      # кнопка на главной
PERSONAL_ACCOUNT = (By.XPATH, "//p[text()='Личный Кабинет']")           # ссылка «Личный Кабинет»
CONSTRUCTOR_LINK = (By.XPATH, "//p[text()='Конструктор']")              # ссылка «Конструктор»
HEADER_LOGO = (By.XPATH, "//a[@href='/']")                         # логотип (ссылка на / с вложенной svg)

# Переходы между формами
REGISTER_LINK       = (By.XPATH, "//a[text()='Зарегистрироваться']")        # ссылка на регистрацию
LOGIN_LINK          = (By.XPATH, "//a[text()='Войти']")                      # ссылка «Войти» на формах
FORGOT_PASSWORD_LINK= (By.XPATH, "//a[text()='Восстановить пароль']")       # ссылка «Восстановить пароль»

# Регистрация 
REGISTER_NAME       = (By.XPATH, "//label[text()='Имя']/following-sibling::input")
REGISTER_EMAIL      = (By.XPATH, "//label[text()='Email']/following-sibling::input")
REGISTER_PASSWORD   = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")
REGISTER_SUBMIT     = (By.XPATH, "//button[text()='Зарегистрироваться']")
REGISTER_ERROR      = (By.XPATH, "//p[contains(@class,'input__error')]")    # текст ошибки под полем

# Логин 
LOGIN_EMAIL         = (By.XPATH, "//label[text()='Email']/following-sibling::input")
LOGIN_PASSWORD      = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")
LOGIN_SUBMIT        = (By.XPATH, "//button[text()='Войти']")

# Личный кабинет
PROFILE_EXIT_BUTTON = (By.XPATH, "//button[text()='Выход']")          # кнопка «Выход» в ЛК

# Конструктор: вкладки
TAB_BUNS            = (By.XPATH, "//span[text()='Булки']")
TAB_SAUCES          = (By.XPATH, "//span[text()='Соусы']")
TAB_FILLINGS        = (By.XPATH, "//span[text()='Начинки']")
ACTIVE_TAB          = (By.XPATH, "//div[contains(@class,'tab_tab_type_current')]/span")  # активный таб (текст)