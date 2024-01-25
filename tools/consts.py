

""" Web Pages For Tests"""
HOME_PAGE = "https://www.jumbo.com/"
LOGIN_PAGE = "https://www.jumbo.com/account/inloggen?SourceURL=%2Fhome"
SEARCH_RESULTS_PAGE = "https://www.jumbo.com/zoeken/?searchType=keyword&searchTerms=Unicorn"
DETAILED_PRODUCT_PAGE = "https://www.jumbo.com/producten/jumbo-crunchy-unicorn-mix-200g-446446DS"

REJECT_COOKIES = "onetrust-reject-all-handler"

""" Welcome Page Navigation Panel And Shopping List"""
NAVI_PANEL = "//a[contains(@class, 'nav-menu-item')]"
SHOPPING_LIST = "//div[starts-with(@class, 'carousel jum-list-overview-carousel')]"
PRODUCT_BASKET = "//*[@id='jum-basket']"
NAVI_LIST = ("Producten", "Aanbiedingen & acties", "Recepten")

"""User Data"""
USERNAME_INPUT = "username"
PASSWORD_INPUT = "password"
LOGIN_BUTTON = "//*[@id='submit']"

"""Product Search"""
SEARCH_FOR = "Unicorn"
SEARCH_RESULTS = "//a[contains(@class, 'title-link')]"
CATEGORIES_COUNT = "//small[contains(@class, 'facet-count')]"

""" Detailed Info For Product """
PRICE_PER_PRODUCT = "//div[starts-with(@class, 'jum-price mb product-price prominent')]"
PRICE_FOR_ALL_PRODUCTS = "//div[starts-with(@class, 'current-price')]"
PRODUCT_BREADCRUMBS = "//ol[starts-with(@class, 'breadcrumb-trail')]"
ADD_TO_BASKET_BUTTON_ALL = "//button[contains(@class, 'jum-button button is-primary success')]"
ADD_TO_BASKET_MAIN = ".is-fullwidth > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > button:nth-child(1)"
REMOVE_FROM_BASKET = ".is-shown > button:nth-child(1) > svg:nth-child(1)"
BASKET_COUNT = "html body.using-mouse div#__nuxt div#__layout div.pb-m-5x div.header header.header-navigation.grocery-nav-is-active div.nav-bar div.jum-container.nav-bar-menu div.nav-bar-menu-main div.nav-bar-actions div div.nav-basket.nav-bar-basket div.basket-button.hide-on-mobile button.jum-button.compact span.nav-basket-badge.is-bottom span.nav-basket-badge-count-container span.nav-basket-badge-count"
