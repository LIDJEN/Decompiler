pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                script {
                    when {
                        branch 'release' 
                    }
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    // Выполнить определенные действия в зависимости от ветки
                    when {
                      branch 'develop'
                    }
                }
            }
        }
    }
}