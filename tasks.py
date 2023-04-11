from invoke import task

@task
def build(ctx):
    ctx.run("python src/intialize_database.py")

@task
def start(ctx):
    ctx.run("python3 src/index.py", pty=True)

@task
def test(ctx):
    ctx.run("pytest src", pty=True)

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest src", pty=True)

@task(coverage) # Miksi on erilainen?? Katsoin vain mallia.
def coverage_report(ctx):
    ctx.run("coverage html", pty=True)