from dagger.web import app
from flask import jsonify, abort, make_response
from dagger import pipeline


@app.route('/dagger/api/v1.0/dags', methods=['GET'])
def get_dags():
    dag_run = pipeline.run()
    dag = dag_run.topological_order()
    return jsonify({'dag': str(dag)})


@app.route('/dagger/api/v1.0/dags/<int:dag_id>', methods=['GET'])
def get_dag(dag_id):
    dag = [dag for dag in [] if dag['id'] == dag_id]
    if len(dag) == 0:
        abort(404)
    return jsonify({'task': dag[0]})


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


