from app import create_app

@given('I access the home endpoint')
def step_impl(context):
    app = create_app()
    context.client = app.test_client()
    context.response = context.client.get('/')