pipeline {
    agent any

    stages {
        stage('Setup') {
            steps {
                sh '''
                    set -x
                    set -e
                    if ! [ -d env ]; then
                        virtualenv -p python3 env
                    fi
                    source env/bin/activate
                    pip install -r requirements.txt
                    '''
            }
        }
    }
}
