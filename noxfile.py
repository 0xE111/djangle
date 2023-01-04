# type: ignore
import nox


nox.options.reuse_existing_virtualenvs = True
nox.options.sessions = ['test']


@nox.session
def test(session):
    session.install('pytest', 'pytest-django', '-r', 'requirements.txt')
    session.run('pytest', success_codes=[0, 5], *session.posargs)
