pipeline {
    agent any

    stages {
        stage('Setup') {
            steps {
                withPythonEnv('python3') {
                    sh "pip install -r requirements.txt"
                }
            }
        }
    }
}
