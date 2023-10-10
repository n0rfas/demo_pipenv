from invoke import task

@task
def runserver(cmd):
    cmd.run("python ld.py")
    cmd.run("uvicorn main:app --reload")
