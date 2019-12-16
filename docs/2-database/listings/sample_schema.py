class Projects(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    location_id = db.Column(db.Integer, db.ForeignKey('locations.id'))
    source_db = db.Column(db.String(64))
    source_id = db.Column(db.SmallInteger)
    description = db.Column(db.Text)
    warning = db.Column(db.String(255))
    site_name = db.Column(db.String(128))
    source_ref = db.Column(db.Text)
    dqf = db.Column(db.SmallInteger)
    contractor = db.Column(db.String(255))
    number = db.Column(db.String(128))
    title = db.Column(db.String(255))
    date_added = db.Column(db.Date)
    date_modified = db.Column(db.DateTime, default=datetime.utcnow)
    cloned = db.relationship(
        'Projects', secondary=clones,
        primaryjoin=(clones.c.org_id == id),
        secondaryjoin=(clones.c.new_id == id),
        backref=db.backref('clones', lazy='dynamic'), lazy='dynamic'
    )
    in_analyses = db.relationship(
        'Analyses', secondary=projects_analyzed, lazy='dynamic')
    misc = db.relationship('Misc', backref='project', lazy='dynamic')
    attachments = db.relationship('Attachments', backref='project', lazy='dynamic')
    borings = db.relationship('Borings', backref='project', lazy='dynamic')
    piles = db.relationship('Piles', backref='project', lazy='dynamic')

    def __repr__(self):
        return '<Project ID: {}>'.format(self.id)

    def clone(self, project):
        if not self.is_cloned():
            self.cloned.append(project)

    def is_cloned(self):
        return self.cloned.count() > 0

    def make_qs_plot(self):
        if self.piles.first().load_tests.first():
            data = self.piles.first().load_tests.first().static_tests.all()
        else:
            data = None
        return slt_plot_thumb(data)

clones = db.Table(
    'clones',
    db.Column('org_id', db.Integer, db.ForeignKey('projects.id'),
              primary_key=True),
    db.Column('new_id', db.Integer, db.ForeignKey('projects.id'),
              primary_key=True),
)
