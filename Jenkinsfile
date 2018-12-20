pipeline {
    agent any

    stages {
        stage('Setup') {
            steps {
                sh '''
                    if ! [ -d env ]; then
                        virtualenv -p python3 env
                    fi
                    source env/bin/activate
                    pip install -r requirements.txt
                    '''
            }
        }

        stage('Test features') {
            steps {
                sh "export PATH=env/bin:$PATH"
                sh '''source env/bin/activate; behave'''
            }
        }
    }
}
