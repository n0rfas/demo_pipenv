from invoke import task

@task
def runserver(cmd):
    cmd.run("python ld.py")
    cmd.run("uvicorn main:app --reload")
    
    # for examples

    # 1
    # cmd.run("python ./app/manage.py makemessages -l en")
    # cmd.run("python ./app/manage.py makemessages -l ru")
    # cmd.run("python ./app/manage.py compilemessages")

    # 2
    # psql_env = {
    #     "PGHOST": os.getenv("DATABASE_HOST"),
    #     "PGPORT": os.getenv("DATABASE_PORT"),
    #     "PGDATABASE": os.getenv("DATABASE_NAME"),
    #     "PGUSER": os.getenv("DATABASE_USER"),
    #     "PGPASSWORD": os.getenv("DATABASE_PASSWORD"),
    # }
    # cmd.run("psql -c 'DROP SCHEMA IF EXISTS public CASCADE'", env=psql_env)
    # cmd.run("psql -c 'CREATE SCHEMA public'", env=psql_env)
    # cmd.run("python ./app/manage.py makemigrations")
    # cmd.run("python ./app/manage.py migrate")

    # 3
    # cmd.run(
    #     """
    #     docker build \
    #     --build-arg VERSION={0} \
    #     --build-arg BUILD_DATE="$(date -Iseconds)" \
    #     --build-arg PYPI_MIRROR=${{PIPENV_PYPI_MIRROR:-https://pypi.org/simple}} \
    #     --tag docker.my-comp.ru/pro/backend/application:{0} \
    #     --file Dockerfile \
    #     .
    #     """.format(
    #         tag
    #     )
    # )
