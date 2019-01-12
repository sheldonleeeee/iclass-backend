#!/usr/bin/env python

from flask_migrate import MigrateCommand, Migrate
from flask_script import Manager, Shell

from iclass import create_app, db
from iclass.models import ApplicationInfo, ClassRoom, User

app = create_app()
manager = Manager(app)


def make_shell_context():
    return dict(app=app, db=db, ApplicationInfo=ApplicationInfo, ClassRoom=ClassRoom, User=User)


manager.add_command("shell", Shell(make_context=make_shell_context))
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)


@manager.command
def deploy():
    db.create_all()
    # upgrade()
    # User.generate_fake(100)
    # Post.generate_fake(100)


@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


if __name__ == "__main__":
    app.run()
