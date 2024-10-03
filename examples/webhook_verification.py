from paddle_billing.Entities.Notifications import NotificationEvent
from paddle_billing.Notifications import Secret, Verifier
from examples.Utils.Requests.Request import Request

# This example requires environment variable TEST_MODE=1 to disable time drift checks, e.g.
# TEST_MODE=1 python webhook_verification.py

secret = "pdl_ntfset_01hs0t3tw21j988db1pam5xg8m_GrOWLNef+vmtjJYq4mSnHNzvc8uWoJ1I"

request = Request.create_from_fixture(
    "webhook_payload.json",
    {
        "Paddle-Signature": "ts=1710498758;h1=558bf93944dbeb4790c7a8af6cb2ea435c8ca9c8396aafc1a4e37424ac132744",
    },
)

integrity_check = Verifier().verify(request, Secret(secret))

if integrity_check is True:
    print("Webhook is verified")

    notification = NotificationEvent.from_request(request)
    print(f"Notification ID: {notification.notification_id}")
    print(f"Event ID: {notification.event_id}")
    print(f"Event Type: {notification.event_type}")
    print(f"Occurred At: {notification.occurred_at}")

    customer = notification.data
    print(f"Customer ID: {customer.id}")
    print(f"Customer Name: {customer.name}")
    print(f"Customer Email: {customer.email}")
else:
    print("Webhook is not verified")
