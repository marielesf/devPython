from twilio import rest

account_sid = "ACafdcf670b4a5a57524168e2f51a53b22" # Your Account SID from www.twilio.com/console
auth_token  = "153071647f49af5cb2d083a85591ed7b"  # Your Auth Token from www.twilio.com/console

client = rest.TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="Parei :)",
    to="+5551985756942",    # Replace with your phone number
    from_="+16572014259") # Replace with your Twilio number

print(message.sid)
