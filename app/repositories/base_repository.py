from app.models.models import Base


class BaseRepository:
    def __init__(self, session, model):
        self.session = session
        self.model = model

    def get_all(self):
        return self.session.query(self.model).all()

    def create(self, model: Base):
        self.session.add(model)
        self.session.commit()

    def update(self, id: int, attributes: dict):
        self.session.query(self.model).filter_by(id=id).update(attributes)
        self.session.commit()

    def get_by_id(self, id: int):
        return self.session.query(self.model).filter_by(id=id).first()
