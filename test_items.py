import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
def test_find_button(browser):
    browser.get(link)
    assert browser.find_element_by_class_name('btn.btn-lg.btn-primary.btn-add-to-basket').is_displayed(), \
        'Кнопка добавления товара в корзину отсутсвует'
    time.sleep(30) 