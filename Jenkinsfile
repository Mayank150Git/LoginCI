pipeline {
    agent any   // Run on any available Jenkins agent

    stages {
        stage('Checkout Code') {
            steps {
                // Pull latest code from GitHub
                git branch: 'main', url: 'https://github.com/Mayank150Git/LoginCI.git'
            }
        }

        stage('Setup Python Environment') {
            steps {
                // Create virtual environment and install dependencies
                bat 'python -m venv venv'
                bat '. venv/bin/activate && pip install -r requirements.txt'
                // Install Playwright browsers
                bat 'playwright install'
            }
        }

        stage('Run Playwright Tests') {
            steps {
                // Run pytest with Playwright tests
                bat '. venv/bin/activate && pytest --junitxml=results.xml'
            }
        }

        stage('Publish Test Results') {
            steps {
                // Publish results in Jenkins dashboard
                junit 'results.xml'
            }
        }
    }

    post {
        always {
            // Archive test results for future reference
            archiveArtifacts artifacts: 'results.xml', fingerprint: true
        }
//         failure {
//             // Notify team if build fails
//             mail to: 'mayanktripathi150@gmail.com',
//                  subject: "Build Failed: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
//                  body: "Check Jenkins for details."
//         }
    }
}