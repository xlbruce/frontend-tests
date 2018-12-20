pipeline {
    agent any

    stages {
        stage('Setup') {
            steps {
                withPythonEnv('python3') {
                    sh "pip install -r ${env.WORKSPACE}/requirements.txt"
                }
            }
        }

        stage('Test features') {
            steps {
                withPythonEnv('python3') {
                    sh "behave"
                }
            }
        }
    }
}
