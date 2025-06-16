pipeline {
    agent any

    environment {
        // Extract email of the person who pushed (from Git log)
        COMMIT_AUTHOR_EMAIL = sh(
            script: "git --no-pager log -1 --pretty=format:'%ae'",
            returnStdout: true
        ).trim()
    }

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/Ezakeil/ToDolist_testing.git' // replace this with your repo URL
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
            echo "Sending result email to: ${COMMIT_AUTHOR_EMAIL}"

            mail to: "${COMMIT_AUTHOR_EMAIL}",
                 subject: "Assignment 3 - Jenkins Selenium Test Result",
                 body: """\
Hello ${COMMIT_AUTHOR_EMAIL},

The Jenkins pipeline for Selenium tests has completed.

Please check the Jenkins console output for detailed test results.

Regards,
Jenkins Automated Pipeline
"""
        }
    }
}
