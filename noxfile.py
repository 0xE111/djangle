# type: ignore
import nox


nox.options.reuse_existing_virtualenvs = True
nox.options.sessions = ['lint', 'test']


@nox.session
def lint(session):
    session.install('flake8')
    session.run('flake8', *session.posargs, 'src')


@nox.session
def test(session):
    session.install('-r', 'requirements.txt')
    session.run('pytest', success_codes=[0, 5], *session.posargs)
