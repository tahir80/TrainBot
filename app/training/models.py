from app import db # we already defined db instance inside app/__init__.py file
import datetime
# from app.auth.models import User

class PROLIFIC_TASK(db.Model):
    __tablename__ = 'PROLIFIC_TASK'
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable = False)
    desc = db.Column(db.String(500), nullable = False)
    no_of_workers = db.Column(db.Integer, default=10)
    fix_price = db.Column(db.Float)
    completion_code = db.Column(db.String(500), nullable = False)
    s_start_time = db.Column(db.DateTime, default = datetime.datetime.utcnow())
    s_end_time = db.Column(db.DateTime, nullable = True)
    status = db.Column(db.String(100))

    def __init__(self, title, desc, no_of_workers, fix_price, completion_code, status):
        self.title = title
        self.desc = desc
        self.no_of_workers = no_of_workers
        self.fix_price = fix_price
        self.completion_code = completion_code
        self.status = status

class PROLIFIC_WORKER(db.Model):
    __tablename__ = 'PROLIFIC_WORKER'
    id = db.Column(db.Integer, primary_key = True)
    prolific_id = db.Column(db.String(100))
    time_stamp = db.Column(db.DateTime, default = datetime.datetime.utcnow())

    def __init__(self, prolific_id):
        self.prolific_id = prolific_id

class TRAINING(db.Model):
    __tablename__ = 'TRAINING'
    id = db.Column(db.Integer, primary_key = True)
    w_id = db.Column(db.Integer, db.ForeignKey('PROLIFIC_WORKER.id'))
    qs = db.Column(db.String(500), nullable = False)
    ans = db.Column(db.String(500), nullable = False)
    start_time = db.Column(db.DateTime, default = datetime.datetime.utcnow())
    end_time =db.Column(db.DateTime)
    t_id = db.Column(db.Integer, db.ForeignKey('PROLIFIC_TASK.id'))

    def __init__(self, w_id, qs, ans, t_id, end_time):
        self.w_id = w_id
        self.qs = qs
        self.ans = ans
        self.t_id = t_id
        # self.start_time = start_time
        self.end_time = end_time

class TEST_TASK(db.Model):
    __tablename__ = 'TEST_TASK'
    id = db.Column(db.Integer, primary_key = True)
    w_id = db.Column(db.Integer, db.ForeignKey('PROLIFIC_WORKER.id'))
    qs = db.Column(db.String(500), nullable = False)
    ans = db.Column(db.String(500), nullable = False)
    start_time = db.Column(db.DateTime, default = datetime.datetime.utcnow())
    end_time = db.Column(db.DateTime)
    t_id = db.Column(db.Integer, db.ForeignKey('PROLIFIC_TASK.id'))
    def __init__(self, w_id, qs, ans, t_id, end_time):
        self.w_id = w_id
        self.qs = qs
        self.ans = ans
        self.t_id = t_id
        self.end_time = end_time

class BONUS(db.Model):
    __tablename__ = 'BONUS'
    id = db.Column(db.Integer, primary_key = True)
    t_id = db.Column(db.Integer, db.ForeignKey('PROLIFIC_TASK.id'))
    w_id = db.Column(db.Integer, db.ForeignKey('PROLIFIC_WORKER.id'))
    timestamp = db.Column(db.DateTime, default = datetime.datetime.utcnow())
    def __init__(self, t_id,w_id):
        self.t_id = t_id
        self.w_id = w_id

class TRAINING_BONUS(db.Model):
    __tablename__ = 'TRAINING_BONUS'
    id = db.Column(db.Integer, primary_key = True)
    b_id = db.Column(db.Integer, db.ForeignKey('BONUS.id'))
    train_id = db.Column(db.Integer, db.ForeignKey('TRAINING.id'))
    bonus = db.Column(db.Float)
    timestamp = db.Column(db.DateTime, default = datetime.datetime.utcnow())
    def __init__(self, b_id, train_id,bonus):
        self.b_id = b_id
        self.train_id = train_id
        self.bonus = bonus

class TEST_TASK_BONUS(db.Model):
    __tablename__ = 'TEST_TASK_BONUS'
    id = db.Column(db.Integer, primary_key = True)
    b_id = db.Column(db.Integer, db.ForeignKey('BONUS.id'))
    tt_id = db.Column(db.Integer, db.ForeignKey('TEST_TASK.id'))
    bonus = db.Column(db.Float)
    timestamp = db.Column(db.DateTime, default = datetime.datetime.utcnow())
    def __init__(self, b_id, tt_id, bonus):
        self.b_id = b_id
        self.tt_id = tt_id
        self.bonus = bonus

class SELF_EFFICACY(db.Model):

    __tablename__ = 'SELF_EFFICACY'
    id = db.Column(db.Integer, primary_key = True)
    w_id = db.Column(db.Integer, db.ForeignKey('PROLIFIC_WORKER.id'))
    t_id = db.Column(db.Integer, db.ForeignKey('PROLIFIC_TASK.id'))
    #survey items
    understand = db.Column(db.String(500), nullable = False)
    say_next = db.Column(db.String(500), nullable = False)
    Help_client_to_talk = db.Column(db.String(500), nullable = False)
    conceptualization = db.Column(db.String(500), nullable = False)
    explore = db.Column(db.String(500), nullable = False)
    helping_skill = db.Column(db.String(500), nullable = False)
    realistic_counseling_goals = db.Column(db.String(500), nullable = False)
    focused = db.Column(db.String(500), nullable = False)
    intentions = db.Column(db.String(500), nullable = False)
    planning = db.Column(db.String(500), nullable = False)
    beforeafter = db.Column(db.String(500), nullable = False)
    timestamp = db.Column(db.DateTime, default = datetime.datetime.utcnow())

    def __init__(self, w_id, t_id, understand, say_next, Help_client_to_talk, conceptualization, \
    explore, helping_skill, realistic_counseling_goals, focused, intentions, planning, beforeafter):
        self.w_id = w_id
        self.t_id = t_id
        self.understand = understand
        self.say_next = say_next
        self.Help_client_to_talk = Help_client_to_talk
        self.conceptualization = conceptualization
        self.explore = explore
        self.helping_skill = helping_skill
        self.realistic_counseling_goals = realistic_counseling_goals
        self.focused = focused
        self.intentions = intentions
        self.planning = planning
        self.beforeafter = beforeafter

class ENJOYMENT(db.Model):
    __tablename__ = 'ENJOYMENT'
    id = db.Column(db.Integer, primary_key = True)
    w_id = db.Column(db.Integer, db.ForeignKey('PROLIFIC_WORKER.id'))
    t_id = db.Column(db.Integer, db.ForeignKey('PROLIFIC_TASK.id'))
    #survey items
    enjoy = db.Column(db.String(500), nullable = False)
    fun = db.Column(db.String(500), nullable = False)
    boring = db.Column(db.String(500), nullable = False)
    attention = db.Column(db.String(500), nullable = False)
    enjoyable = db.Column(db.String(500), nullable = False)
    thinking_enjoyed = db.Column(db.String(500), nullable = False)
    nervous = db.Column(db.String(500), nullable = False)
    tense = db.Column(db.String(500), nullable = False)
    relaxed = db.Column(db.String(500), nullable = False)
    anxious = db.Column(db.String(500), nullable = False)
    pressured = db.Column(db.String(500), nullable = False)
    timestamp = db.Column(db.DateTime, default = datetime.datetime.utcnow())

    def __init__(self, w_id, t_id, enjoy, fun, boring, attention, \
    enjoyable, thinking_enjoyed, nervous, tense, relaxed, anxious, pressured):
        self.w_id = w_id
        self.t_id = t_id
        self.enjoy = enjoy
        self.fun = fun
        self.boring = boring
        self.attention = attention
        self.enjoyable = enjoyable
        self.thinking_enjoyed = thinking_enjoyed
        self.nervous = nervous
        self.tense = tense
        self.relaxed = relaxed
        self.anxious = anxious
        self.pressured = pressured
