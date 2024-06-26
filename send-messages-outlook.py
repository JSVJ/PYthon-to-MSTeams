# Description: Send email using O365 and redmail library

from O365 import Message, Account, MSGraphProtocol

html_template = """
                <!DOCTYPE html>
                <html>
                <head>
                    <title>Notification</title>
                </head>
                <body>
                    <h1>Notification</h1>
                    <p>This is a notification email.</p>
                </body>
                </html>
                """

O365_AUTH = ('Sabari.Vishnu.Jayanthan.Jaikrishnan@wdc.com', 'MilkyWay@2428')

protocol = MSGraphProtocol()
account = Account(credentials=O365_AUTH, protocol=protocol)

mbox = account.mailbox()
m = mbox.new_message()

# Set the recipients, subject, and body of the message
m.to.add('')
m.subject = ''
m.body = html_template  # Assuming html_template is a string containing the HTML body
m.send()


# # using 3rd party library
# from redmail import outlook
# outlook.username = ""
# outlook.password = ""
# outlook.send(receivers = [""],
#              subject = "Dummy Notification",
#              text = "This is a notification email.")


