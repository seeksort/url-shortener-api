from app import urlapp, db
from app.models import UrlMap


@urlapp.shell_context_processor
def make_shell_context():
    return {'db': db, 'UrlMap': UrlMap}