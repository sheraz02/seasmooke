# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# from jinja2 import Template


# # sender_email = "sheraz.ahmad8814@gmail.com"
# # receiver_email = "fintechgroup0@gmail.com"
# # password = "ynlr alyo ofdx hbgv"
# # subject = "Hello Sheraz"
# # body = "Hello, how are you?"

# class EmailBot:
#     def __init__(self):
#         self.sender_email = "sheraz.ahmad8814@gmail.com"
#         self.receiver_email = "fintechgroup0@gmail.com"
#         self.password = "ynlr alyo ofdx hbgv"
#         self.subject = "Hello Sheraz"
#         self.body =  "Hello, how are you?"
    

#     def send_email(self, template_str, data={}):
#         template = Template(template_str)
#         body = template.render(data)

#         msg = MIMEMultipart()
#         msg['From'] = self.sender_email
#         msg['To'] = self.receiver_email
#         msg['Subject'] = self.subject
#         msg.attach(MIMEText(body, 'plain'))

#         try:
#             server = smtplib.SMTP('smtp.gmail.com', 587)
#             server.starttls()  # Start TLS encryption for security

#             server.login(self.sender_email, self.password)
#             server.sendmail(self.sender_email, self.receiver_email, msg.as_string())

#             print("Templated email sent successfully!")

#         except Exception as e:
#             print(f"Failed to send email. Error: {e}")

#         finally:
#             server.quit()


# if __name__ == '__main__':


#     template_str = """
# Hello {{ name }},

# This is a templated email. Your order number is {{ order_number }}.
# Here are the items you purchased:
# {% for item in items %}
# - {{ item }}
# {% endfor %}

# Thank you for your purchase!

# Best regards,
# Your Company
# """

# # Data to insert into the template
#     data = {
#     'name': 'John Doe',
#     'order_number': '12345',
#     'items': ['Item 1', 'Item 2', 'Item 3']
# }
#     em = EmailBot()
    
#     em.send_email(template_str=template_str, data=data)


# # # Create a Jinja2 Template object
# # template = Template(template_str)

# # # Render the email body with the provided data
# # body = template.render(data)

# # # Set up the MIME
# # msg = MIMEMultipart()
# # msg['From'] = sender_email
# # msg['To'] = receiver_email
# # msg['Subject'] = subject

# # # Attach the body with the MIMEText object
# # msg.attach(MIMEText(body, 'plain'))

# # try:
# #     # Establish connection with the Gmail SMTP server
# #     server = smtplib.SMTP('smtp.gmail.com', 587)
# #     server.starttls()  # Start TLS encryption for security

# #     # Log in to the server
# #     server.login(sender_email, password)

# #     # Send the email
# #     server.sendmail(sender_email, receiver_email, msg.as_string())

# #     print("Templated email sent successfully!")

# # except Exception as e:
# #     print(f"Failed to send email. Error: {e}")

# # finally:
# #     # Close the connection
# #     server.quit()




import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import os

# SMTP server configuration
smtp_server = "smtp.gmail.com"
smtp_port = 587
smtp_user = "sheraz.ahmad8814@gmail.com"
smtp_password = "ynlr alyo ofdx hbgv"

# Email configuration
from_address = "sheraz.ahmad8814@gmail.com"
to_address = "fintechgroup0@gmail.com"
subject = "Subject of the Email"
html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Beta Accountancy Email</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f4f4f4;
        }
        table {
            width: 100%;
            max-width: 600px;
            margin: 0 auto;
            background-color: #ffffff;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        img {
            max-width: 100%;
            height: auto;
            border-radius: 8px;
        }
        .header {
            background-color: #003366;
            color: #ffffff;
            padding: 20px;
            text-align: center;
            border-top-left-radius: 8px;
            border-top-right-radius: 8px;
        }
        .header h1 {
            font-size: 36px;
            margin: 0;
        }
        .content {
            padding: 30px;
            font-size: 16px;
            line-height: 1.5;
            color: #333333;
        }
        .content h2 {
            font-size: 24px;
            color: #003366;
        }
        .cta-button {
            display: inline-block;
            background-color: #92bbe7;
            color: #ffffff;
            padding: 12px 30px;
            text-decoration: none;
            border-radius: 5px;
            font-size: 18px;
            margin-top: 20px;
            text-align: center;
        }
        .cta-button:hover {
            background-color: #a6b3c1;
        }
        .cta-button-container {
            text-align: center;
            margin-top: 20px;
        }
        .footer {
            background-color: #003366;
            color: #ffffff;
            padding: 20px;
            text-align: center;
            border-bottom-left-radius: 8px;
            border-bottom-right-radius: 8px;
        }
        .footer .social-icons a {
            color: #ffffff;
            text-decoration: none;
            margin: 0 10px;
            font-size: 18px;
        }
        .footer .social-icons img {
            width: 30px;
            height: auto;
            margin: 0 10px;
        }
        .footer .address {
            font-size: 14px;
            margin-top: 10px;
            color: #dddddd;
        }
        .footer .address p {
            margin: 5px 0;
        }
        .footer .social-icons {
            margin-bottom: 10px;
        }
        .footer .contact-info {
            margin-top: 20px;
        }
        .footer .contact-info a {
            color: #ffffff;
            text-decoration: none;
        }
    </style>
</head>
<body>
    <table>
        <!-- Header -->
        <tr>
            <td class="header">
                <h1>Beta Accountancy</h1>
                <p>Expert Bookkeeping, Payroll & Financial Services</p>
            </td>
        </tr>

        <!-- Content -->
        <tr>
            <td class="content">
                <p>Dear Sir/Madam,</p>
                <p>Managing your business finances shouldn’t be a hassle! Beta Accountancy provides expert bookkeeping, payroll, and financial reporting services using advanced accounting software, ensuring accuracy, efficiency, and peace of mind.</p>

                <h2>🚀 Save time, reduce stress, and focus on growing your business!</h2>
                <p>Let’s discuss how we can support your success. Schedule a free consultation today!</p>

                <div class="cta-button-container">
                    <a href="https://betaaccountancy.com" class="cta-button">Schedule a Consultation</a>
                </div>

                <p>📞 <strong>WhatsApp us:</strong> +44 7880 583425</p>
                <p>🌐 <strong>Visit our website:</strong> <a href="https://betaaccountancy.com" target="_blank">betaaccountancy.com</a></p>

                <p>Looking forward to helping you achieve financial clarity!</p>

                <p>Best regards,</p>
                <p><strong>Shahzad Ahmad</strong><br>Business Development Manager<br>Beta Accountancy</p>
            </td>
        </tr>

        <!-- Footer -->
        <tr>
            <td class="footer">
                
                <div class="address">
                    <p>Kumharan Wala Chowk Multan, Punjab, Pakistan</p>
                </div>
                <div class="contact-info">
                    <p>Email: <a href="mailto:contact@betaaccountancy.com">contact@betaaccountancy.com</a></p>
                    <p>Phone: +44 7880 583425</p>
                </div>
            </td>
        </tr>
    </table>
</body>
</html>
"""

# Prepare the email message
msg = MIMEMultipart()
msg['From'] = from_address
msg['To'] = to_address
msg['Subject'] = subject

# Attach the HTML body to the email
msg.attach(MIMEText(html_content, 'html'))


# Connect to the SMTP server and send the email
try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  # Secure the connection
    server.login(smtp_user, smtp_password)  # Log in to the server
    server.sendmail(from_address, to_address, msg.as_string())  # Send the email
    print("Email sent successfully!")
except Exception as e:
    print(f"Error: {e}")
finally:
    server.quit()  # Close the server connection
