# The below code is specifically for sending email using win32com library
import win32com.client as win32

FROM = ""
TO = ""

# win32 allows us to communicate python with our windows application
olApp = win32.Dispatch('Outlook.Application')
olNS = olApp.GetNameSpace('MAPI')

mail_item = olApp.CreateItem(0)
mail_item.Subject = "FROM PYTHON - TEST"
mail_item.BodyFormat = 1 
mail_item.Body = "Dummy Notification from Python - PIVA Project"
mail_item.Sender = FROM
mail_item.To = TO

# mail_item.Display() # to display the mail box
mail_item.save()
mail_item.Send()