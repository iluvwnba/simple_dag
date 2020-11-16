from dagger.web import app

from dagger import pipeline


@app.route('/dag')
def dags():
    dag, topological = pipeline.run()
    return "DAG Contents: {}   -----    Is cicular: {}".format(dag.topological_order(), topological)