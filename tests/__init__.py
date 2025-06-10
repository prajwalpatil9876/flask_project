from app import create_app

@given('I access the home endpoint')
def step_impl(context):
    app = create_app()
    context.client = app.test_client()
    context.response = context.client.get('/')

@then('I should receive a greeting message')
def step_impl(context):
    assert context.response.status_code == 200
    assert context.response.get_json() == {"message": "Hello, Flask!"}