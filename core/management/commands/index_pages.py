from django.core.management.base import BaseCommand
    
from core.management.commands import configure_logging
from core.solr_index import index_pages

configure_logging("index_pages_logging.config", "index_pages.log")

class Command(BaseCommand):

    def handle(self, **options):
        index_pages()
