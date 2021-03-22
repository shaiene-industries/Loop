from django.core import mail
from users.models import ContactInfo

def send_contact_info_mails(form) -> bool:
    CLEAN_DATA = form.cleaned_data
    PRODUCT_1 = CLEAN_DATA["product_chosen"]
    PRODUCT_2 = CLEAN_DATA["product_to_exchange"]
    USER_1 = PRODUCT_1.user
    USER_2 = PRODUCT_2.user
    
    SUBJECTS = {
        USER_1 : "Troca do item: " + str(PRODUCT_2),
        USER_2 : "Troca do item: " + str(PRODUCT_1),
    }

    BODY_BASE_TEXT = \
        """\
        Olá, {user}! Tudo bem?
        <br><br>
        Eis as informações de contato de {other_user}.
        <br><br>
        Estamos torcendo para que vocês consigam trocar <strong>{prod_1}</strong> e <strong>{prod_2}</strong>!
        <br><br>
        """
    
    # Creating emails
    users_contact_info = ContactInfo.objects.filter(user__in=[USER_1, USER_2])
    email_messages = []
    for i in range(2):
        user, other_user = (USER_1, USER_2) if(i==0) else (USER_2, USER_1)
 
        # Organising users contact info
        contact_list = [info for info in users_contact_info if(info.user != user)]
        contact_dict = {
            contact.get_type_display(): contact.info
            for contact in contact_list
        }

        # Writing current user info
        body_text = BODY_BASE_TEXT.format(
            user=user,
            prod_1=PRODUCT_1,
            prod_2=PRODUCT_2,
            other_user=other_user
        )

        # Adding other user contact info
        for contact in contact_dict:
            body_text += \
                """\
                <strong>{type}</strong> : <strong>{info}</strong>
                <br><br>\
                """.format(
                    type=contact,
                    info=contact_dict[contact]
                )

        # Loop Message

        body_text += "Atenciosamente, Loop. <br>"

        # Joining user's email data
        email_messages.append({
            "subject" : SUBJECTS[user],
            "body" : body_text,
            "to" : (user.email, )
        })
        

    with mail.get_connection() as connection:
        for message in email_messages:
            mail_message = mail.EmailMessage(
                subject=message["subject"],
                body=message["body"],
                to=message["to"],
                connection=connection,
            )
            mail_message.content_subtype = "html"
            mail_message.send()

    return True