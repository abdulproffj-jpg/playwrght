pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/abdulproffj-jpg/playwrght.git'
            }
        }

        stage('Run Pytest') {
            steps {
                // Run Python tests with JUnit XML output
                sh 'pytest tests --maxfail=1 --disable-warnings -q --junitxml=test-results/results.xml'
            }
        }

        stage('Archive Reports') {
            steps {
                archiveArtifacts artifacts: 'test-results/*.xml', fingerprint: true
                junit 'test-results/*.xml'
            }
        }
    }
}
