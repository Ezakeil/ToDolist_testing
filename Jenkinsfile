pipeline {
    agent any

    stages {
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t selenium-test .'
            }
        }
        stage('Run Tests') {
            steps {
                sh 'docker run --rm selenium-test'
            }
        }
    }
    post {
        always {
            echo 'Pipeline finished (Email notification intentionally removed as per requirement)'
        }
    }
}
