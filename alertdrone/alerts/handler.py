import os

def post_to_slack(event, context):
    slack_webhook_url = os.environ['SLACK_WEBHOOK_URL']
    print(event)

    return
