from __future__ import print_function
from telesign.messaging import MessagingClient

customer_id = "A2552C7B-4C01-48FE-B239-A5F7FC981232"
api_key = "H0Y9u9MTkjMCa5OPK5NxOVce50nIe/GeUfErHBwxADxgJ5Kb4UXFOW3pZVNc8qW+FODzN84t+5AbtpOInGOVjA=="

phone_number = "998919037389"
message = "You're scheduled for a dentist appointment at 2:30PM."
message_type = "ARN"

messaging = MessagingClient(customer_id, api_key)
response = messaging.message(phone_number, message, message_type)