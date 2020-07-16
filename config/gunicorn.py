from psycogreen.gevent import patch_psycopg
#from gevent import monkey


def post_fork(server, worker):
    #monkey.patch_all()
    patch_psycopg()
    worker.log.info("Enabled async Psycopg2")
