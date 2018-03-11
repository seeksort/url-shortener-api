from app import db

class UrlMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(), index=True, unique=True)
    url_no_protocol = db.Column(db.String(), index=True, unique=True)
    short_url_id = db.Column(db.Integer, unique=True)

    def __repr__(self):
        return '<UrlMap {}>'.format(self.original_url)
