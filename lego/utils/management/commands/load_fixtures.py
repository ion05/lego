import os

from django.conf import settings
from django.core import serializers
from django.core.management import BaseCommand

from lego.app.articles.models import Article
from lego.app.comments.models import Comment
from lego.app.events.models import Event
from lego.users.models import AbakusGroup, Membership, User


def create_if_missing(obj, model):
    if not model.objects.filter(pk=obj.object.pk).exists():
        obj.save()


class Command(BaseCommand):
    help = 'Loads initial data from fixtures.'

    def load_from_fixture(self, fixture_path, model):
        self.stdout.write('Loading fixture %s' % fixture_path)

        fixture_file = os.path.join(settings.BASE_DIR, fixture_path)

        with open(fixture_file) as fixture:
            for obj in serializers.deserialize('yaml', fixture):
                create_if_missing(obj, model)

    def handle(self, *args, **options):
        self.stdout.write('Loading regular fixtures:')
        self.load_from_fixture('users/fixtures/initial_abakus_groups.yaml', AbakusGroup)
        self.load_from_fixture('users/fixtures/initial_users.yaml', User)
        self.load_from_fixture('users/fixtures/initial_memberships.yaml', Membership)

        if settings.DEVELOPMENT:
            self.stdout.write('Loading development fixtures:')
            self.load_from_fixture('users/fixtures/development_users.yaml', User)
            self.load_from_fixture('app/events/fixtures/development_events.yaml', Event)
            self.load_from_fixture('app/articles/fixtures/development_articles.yaml', Article)
            self.load_from_fixture('app/comments/fixtures/development_comments.yaml', Comment)

        self.stdout.write('Done!')
