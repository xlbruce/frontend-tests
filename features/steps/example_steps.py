#*-* coding:utf-8 *-*
@given(u'a homepage é acessada')
def step_impl(context):
    url = 'https://clickbus.com.br'
    context.browser.get(url)


@when(u'usuário procura o logotipo da bus')
def step_impl(context):
    context.logo = context.browser.find_element_by_class_name('brand-logo')

@then(u'logotipo está na página')
def step_impl(context):
    assert context.logo.find_element_by_tag_name('img') is not None
