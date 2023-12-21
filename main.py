import time
from plyer import notification

if __name__ == "__main__":
    # Show notification
    notification.notify(
        title="WARNING",   # Notification title
        message="Do not forget to turn off the do not disturb mode on your computer!",  # Notification content or message

        # Duration of the notification on screen (in seconds)
        timeout=10
    )

    # Wait for 7 seconds
    # The notification will be displayed on the screen during this time
    time.sleep(7)

