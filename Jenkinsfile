pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/abdulproffj-jpg/playwrght.git'
            }
        }

        stage('Run Playwright Tests') {
            steps {
                // Run Playwright directly if installed globally
                sh 'playwright test'
            }
        }

        stage('Archive Reports') {
            steps {
                // Archive Playwright HTML report if generated
                archiveArtifacts artifacts: 'playwright-report/**', fingerprint: true
            }
        }
    }

    post {
        always {
            // If Playwright exports JUnit XML results, publish them
            junit 'test-results/*.xml'
        }
    }
}
