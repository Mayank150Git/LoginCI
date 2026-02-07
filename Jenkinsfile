pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/Mayank150Git/LoginCI.git'
            }
        }

        stage('Setup Python Environment') {
            steps {
                // Create virtual environment
                bat 'python -m venv venv'
                // Activate venv and install dependencies
                bat 'call venv\\Scripts\\activate && pip install -r requirements.txt'
                // Install Playwright browsers
                bat 'call venv\\Scripts\\activate && playwright install'
            }
        }

        stage('Run Playwright Tests') {
            steps {
                bat 'call venv\\Scripts\\activate && pytest -v -s test_login.py --headed'
            }
        }

        stage('Publish Test Results') {
            steps {
                junit 'results.xml'
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'results.xml', fingerprint: true
        }
    }
}