import logging

from django.core.management.base import BaseCommand
from django_mailbox.models import Mailbox
from django.conf import settings
import django

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            '-n',
            '--name',
            action='store',
            dest='name',
            help='name of mailbox',
        )

    def handle(self, *args, **options):
        mailboxes = Mailbox.active_mailboxes.all()

        if options['name']:
            print('arg_test_name, %s' % options['name'])
            mailboxes = mailboxes.filter(
                name = options['name']
            )
        for mailbox in mailboxes:
            logger.info(
                'Gathering messages for %s',
                mailbox.name
            )
            messages = mailbox.get_new_mail()
            for message in messages:
                logger.info(
                    'Received %s (from %s)',
                    message.subject,
                    message.from_address
                )




