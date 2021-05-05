import os
import random

# Use the package we installed
from slack_bolt import App
from dotenv import load_dotenv
from owoify import owoify as owo

load_dotenv()


# Necessary for Mac OS:
# CERT_PATH=$(python -m certifi)
# export SSL_CERT_FILE=${CERT_PATH}
# export REQUESTS_CA_BUNDLE=${CERT_PATH}



# Initializes your app with your bot token and signing secret
app = App(
    token=os.environ["SLACK_BOT_TOKEN"],
    signing_secret=os.environ["SLACK_SIGNING_SECRET"]
)


@app.event("app_home_opened")
def update_home_tab(client, event, logger):
  try:
    # views.publish is the method that your app uses to push a view to the Home tab
    client.views_publish(
      # the user that opened your app's app home
      user_id=event["user"],
      # the view object that appears in the app home
      view={
        "type": "home",
        "callback_id": "home_view",

        # body of the view
        "blocks": [
          {
            "type": "section",
            "text": {
              "type": "mrkdwn",
              "text": "*Wewcwomwe two owobwot* ＼(＾▽＾)／"
            }
          },
        ]
      }
    )
  
  except Exception as e:
    logger.error(f"Error publishing home tab: {e}")



@app.event("app_mention")
def on_mention(body, say, logger):
    print('DEBUG INFO: ' + str(body))
    say("Hewwow! ＼(＾▽＾)／")

@app.event("message")
def on_message(body, say, logger):
    print('DEBUG INFO: ' + str(body))
    say(owo(body['event']['text'], random.choice(('owo', 'uwu', 'uvu'))))

@app.command("/owoify")
def on_command(ack, body, say, logger):
    print('DEBUG INFO: ' + str(body))
    ack()
    say(owo(body['text'], random.choice(('owo', 'uwu', 'uvu'))))



# Start your app
if __name__ == "__main__":
    app.start(port=3000)
