
pipeline {
    agent any

    environment {
        IMAGE_NAME = 'jenkins-flask-lab'
        CONTAINER_NAME = 'jenkins-flask-app'
        APP_PORT = '8081'
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
                echo 'Source code downloaded from GitHub.'
            }
        }

        stage('Build') {
            steps {
                bat 'docker build -t %IMAGE_NAME%:%BUILD_NUMBER% .'
            }
        }

        stage('Test') {
            steps {
                bat 'docker run --rm %IMAGE_NAME%:%BUILD_NUMBER% python -m pytest -v'
            }
        }

        stage('Deploy') {
            steps {
                bat '''
                    docker rm -f %CONTAINER_NAME% 2>NUL
                    docker run -d --name %CONTAINER_NAME% -p %APP_PORT%:8000 -e APP_VERSION=%BUILD_NUMBER% %IMAGE_NAME%:%BUILD_NUMBER%
                '''
            }
        }

        stage('Verify') {
            steps {
                bat 'curl.exe --fail --retry 10 --retry-delay 2 http://localhost:%APP_PORT%/health'
                bat 'curl.exe --fail http://localhost:%APP_PORT%/'
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully.'
        }

        failure {
            echo 'Pipeline failed. Check the failed stage.'
        }
    }
}
