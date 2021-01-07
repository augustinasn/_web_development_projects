from flask_mail import Message
from robodokas import app, mail
from robodokas.config import ADMIN
import os


def send_mail(user, filename):
    msg = Message('Here\'s your report from Robodokas!',
                  sender=ADMIN,
                  recipients=[user])

    msg.html = f'Dear {user.split("@")[0].title()},<br/><br/>Robodokas has successfully created a report that you have requested, click <a href="https://robodokas-api.herokuapp.com/download/{filename}" target="_blank">here</a> to download it.<br><br>Regards,<br>Robodokas Team.'

    # path = os.path.join('..',
    #                     filepath)

    # with app.open_resource(path) as fh:
    #     msg.attach(os.path.basename(fh.name),
    #                "application/docx",
    #                fh.read())

    with app.app_context():
        mail.send(msg)
