import psycogreen.gevent


def post_fork(server, worker):
    psycogreen.gevent.patch_psycopg()
