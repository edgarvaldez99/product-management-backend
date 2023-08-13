import nox


@nox.session
def lint(session):
    session.install("poetry")
    session.run("poetry", "install")
    session.run("poetry", "run", "black", "--check", ".")
    session.run("poetry", "run", "isort", "--check-only", ".")
    session.run("poetry", "run", "flake8", ".")
    session.run("poetry", "run", "mypy", ".")
