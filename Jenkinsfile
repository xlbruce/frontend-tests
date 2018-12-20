pipeline {
    agent any

    stages {
        stage('Setup') {
            steps {
                sh "requirements path: ${env.WORKSPACE}/requirements.txt"
                withPythonEnv('python3') {
                    sh "pip install -r ${env.WORKSPACE}/requirements.txt"
                }
            }
        }
    }
}
