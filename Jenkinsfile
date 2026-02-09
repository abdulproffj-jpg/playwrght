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
                // Use npx to ensure correct binary is called
                sh 'npx playwright test'
            }
        }

        stage('Archive Reports') {
            steps {
                // Archive Playwright HTML report
                archiveArtifacts artifacts: 'playwright-report/**', fingerprint: true
            }
        }
    }

    post {
        always {
            // Publish JUnit XML results if Playwright is configured to generate them
            junit 'test-results/*.xml'
        }
    }
}
