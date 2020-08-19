from django.core.mail import send_mail


def email_message(message_dict):
   contents = f"""
   Hi, thank you for registering to our blog.
   """
   send_mail(
      'Welcoming email',
      contents,
      '<YOUR SENDING ACCOUNT (EMAIL ADDRESS) REGISTERED WITH SEND IN BLUE>',
      [message_dict['email']],
      fail_silently=False
   )
