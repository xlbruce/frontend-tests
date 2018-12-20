pipeline {
    agent any

    environment {
        PATH = "env/bin/:$PATH"
    }

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
                    sh "which python"
                    sh "which chromedriver"
                    sh "behave"
                }
            }
        }
    }
}
