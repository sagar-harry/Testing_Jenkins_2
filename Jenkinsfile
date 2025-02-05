pipeline {
    agent any
    stages {
        stage(''){
            steps {
                deleteDir()
            }
        }
        stage('Stage-1: Clone repository') {
            steps {
                bat 'git clone https://github.com/sagar-harry/Testing_Jenkins'
            }
        }
        
        stage("Stage-3: Activate environment") {
            steps {
                script {
                    bat """
                        echo 'hello world'
                    """
                    echo "Completed Stage-3"
                }
            }
        }
    }
}
