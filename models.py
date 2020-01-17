
class PlacementStatus(ma.Schema):
  table = __tablename__ = 'placements'
  id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
  name = db.Column(db.Float, nullable=False)
  placed = db.Column(db.Boolean, nullable=False)
