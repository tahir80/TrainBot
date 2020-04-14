from app import create_app, db
from app.auth.models import User
from app.training.models import PROLIFIC_TASK, PROLIFIC_WORKER, TRAINING, TEST_TASK, \
                                BONUS, TRAINING_BONUS, TEST_TASK_BONUS
from sqlalchemy import exc
from flask import session



# --------local testing----------------
# flask_app = None
# if __name__ == "__main__":
#     flask_app = create_app('dev')
#     with flask_app.app_context():
#         db.create_all()
#     flask_app.run()
# ------------------------------------------

#-----------------PRODUCTION---------------------
flask_app = create_app('dev')

with flask_app.app_context():
    db.create_all()
    try:
        if not User.query.filter_by(user_name='harry').first():
            User.create_user(user='harry', email='harry@potters.com', password='secret')
    except exc.IntegrityError:
        pass
