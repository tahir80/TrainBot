from app import create_app, db
from sqlalchemy import exc,asc, desc, and_, or_
import datetime
from app.training import training as tr
from flask import session
import requests
# from app.auth import authentication as at
from flask_login import login_required
from flask_login import login_user, logout_user, login_required, current_user
from flask import render_template, request, redirect, url_for, flash, jsonify # for flash messaging
from app.training.models import PROLIFIC_TASK, PROLIFIC_WORKER, TRAINING, TEST_TASK, \
                                BONUS, TRAINING_BONUS, TEST_TASK_BONUS, SELF_EFFICACY, ENJOYMENT

from app.training.forms import CreateNewProlificProject

@tr.route('/')
def home():
    return render_template("index.html")

@tr.route('/training')
def training():
    return render_template("training.html")

@tr.route('/test_task', methods=['GET', 'POST'])
def test_task():
    bonus = request.args.get("bonus")
    bonus = float(bonus)
    bonus = round(bonus, 2)

    return render_template("test_task.html", bonus=bonus)

@tr.route('/prolific_admin',  methods=['GET', 'POST'])
def prolific_admin():

    form = CreateNewProlificProject()
    #if data is validate, hten create a new project
    if form.validate_on_submit():
        p_task = PROLIFIC_TASK(form.title.data, form.Description.data, form.no_of_workers.data, \
                               form.Fix_reward.data, form.completion_code.data, "ACTIVE")

        db.session.add(p_task)
        db.session.commit()
        flash('task was created Successfully!')
        return redirect(url_for('training.prolific_admin'))
    return render_template("prolific_admin.html", form = form)



@tr.route('/self_efficacy')
def self_efficacy():
    return render_template("self-efficacy.html")

@tr.route('/post_self_efficacy')
def post_self_efficacy():
    return render_template("post-self-efficacy.html")

@tr.route('/scale_data', methods=['GET', 'POST'])
def scale_data():
    if request.method == 'POST':
        data = request.get_json()

    if not PROLIFIC_WORKER.query.filter_by(prolific_id = data['workerId']).first():
        worker = PROLIFIC_WORKER(data['workerId'])
        db.session.add(worker)
        db.session.flush()
        print('i added')
    else:
        worker = PROLIFIC_WORKER.query.filter_by(prolific_id = data['workerId']).first()
        print(worker.prolific_id)

    # session['workerId'] = data['workerId']
    task = PROLIFIC_TASK.query.filter_by(status="ACTIVE").first()


    se = SELF_EFFICACY(worker.id, task.id, data['understand'], data['say_next'], data['Help_client_to_talk'], data['conceptualization'], \
    data['explore'], data['helping_skill'], data['realistic_counseling_goals'], data['focused'], data['intentions'], \
    data['planning'], data['status'])

    db.session.add(se)

    bonus = BONUS(task.id, worker.id)
    db.session.add(bonus)

    db.session.commit()

    return jsonify(data)


@tr.route('/setTime', methods=['GET', 'POST'])
def setTime():
    session['start_time'] = datetime.datetime.utcnow()
    return jsonify(123)

@tr.route('/addshortAnswer' , methods=['GET', 'POST'])
def addshortAnswer():
    if request.method == 'POST':
        data = request.get_json()
    task = PROLIFIC_TASK.query.filter_by(status="ACTIVE").first()
    worker = PROLIFIC_WORKER.query.filter_by(prolific_id = data['workerId']).first()

    training_data = TRAINING(worker.id, data['q'], data['ans'], task.id, datetime.datetime.utcnow())

    db.session.add(training_data)
    db.session.flush()

    training_data.start_time = datetime.datetime.min

    if data['rewardable'] == 'yes':
        bonus = BONUS.query.filter(BONUS.w_id==worker.id).order_by(desc(BONUS.id)).first()
        t_bonus = TRAINING_BONUS(bonus.id, training_data.id, 0.1)
        db.session.add(t_bonus)

    db.session.commit()
    return jsonify(123)


@tr.route('/addLongAnswer', methods=['GET', 'POST'])
def addLongAnswer():
    if request.method == 'POST':
        data = request.get_json()
    task = PROLIFIC_TASK.query.filter_by(status="ACTIVE").first()
    worker = PROLIFIC_WORKER.query.filter_by(prolific_id = data['workerId']).first()

    training_data = TRAINING(worker.id, data['q'], data['ans'], task.id, datetime.datetime.utcnow())

    db.session.add(training_data)
    db.session.flush()

    if 'start_time' in session:
        training_data.start_time = session['start_time']

    session.pop('start_time', None)

    if data['rewardable'] == 'yes':
        bonus = BONUS.query.filter(BONUS.w_id==worker.id).order_by(desc(BONUS.id)).first()
        t_bonus = TRAINING_BONUS(bonus.id, training_data.id, 0.1)
        db.session.add(t_bonus)

    db.session.commit()

    print('done adding long answer')
    return jsonify(123)

@tr.route('/addTestingResponses', methods=['GET', 'POST'])
def addTestingResponses():
    if request.method == 'POST':
        data = request.get_json()
    task = PROLIFIC_TASK.query.filter_by(status="ACTIVE").first()
    worker = PROLIFIC_WORKER.query.filter_by(prolific_id = data['workerId']).first()

    test_data = TEST_TASK(worker.id, data['qs'], data['ans'], task.id, datetime.datetime.utcnow())

    db.session.add(test_data)
    db.session.flush()

    if 'start_time' in session:
        test_data.start_time = session['start_time']

    session.pop('start_time', None)

    # if data['rewardable'] == 'yes':
    bonus = BONUS.query.filter(BONUS.w_id==worker.id).order_by(desc(BONUS.id)).first()
    test_bonus = TEST_TASK_BONUS(bonus.id, test_data.id, 0.1)
    db.session.add(test_bonus)

    db.session.commit()
    return jsonify(123)

@tr.route('/enjoyment', methods=['GET', 'POST'])
def enjoyment():
    if request.method == "GET":
        return render_template("enjoyment.html")

    if request.method == 'POST':
        data = request.get_json()
        task = PROLIFIC_TASK.query.filter_by(status="ACTIVE").first()
        worker = PROLIFIC_WORKER.query.filter_by(prolific_id = data['workerId']).first()

        enjoyment = ENJOYMENT(worker.id, task.id, data['enjoy'], data['fun'], data['boring'], data['attention'], data['enjoyable'], data['thinking_enjoyed'], \
        data['nervous'], data['tense'], data['relaxed'], data['anxious'], data['pressured'])

        db.session.add(enjoyment)

        db.session.commit()
        return jsonify(123)
