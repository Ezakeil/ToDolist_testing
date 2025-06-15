pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/Ezakeil/ToDolist_testing'
            }
        }

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
            echo 'Pipeline completed.'
        }
    }
}
