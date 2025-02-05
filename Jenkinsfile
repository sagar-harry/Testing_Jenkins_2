pipeline {
    agent any
    environment {
        GIT_CREDENTIALS_ID = 'github-credentials'  // The credential ID from Jenkins
        REPO_URL = 'https://github.com/sagar-harry/Testing_Jenkins_3'
        BRANCH = 'main'  // Change if pushing to a different branch
        DIR_TO_PUSH = '/var/jenkins_home/workspace/testing1'  // Change to the directory you want to push
    }
    stages {
        stage('Clone Repository') {
            steps {
                script {
                    sh 'rm -rf repo && git clone https://github.com/sagar-harry/Testing_Jenkins_3 repo'
                }
            }
        }
        stage('Copy Directory') {
            steps {
                script {
                    sh 'pwd'
                    sh 'cp -r ${DIR_TO_PUSH} repo/'
                }
            }
        }
        stage('Commit and Push') {
            steps {
                withCredentials([
                    gitUsernamePassword(credentialsId: 'github-credentials', gitToolName: 'Default')
                ]) {
                    sh '''
                    cd repo
                    git config --global user.email "10vidyasagarkonni@gmail.com"
                    git config --global user.name "sagar-harry"
                    git add .
                    git commit -m "register work"
                    git push origin ${BRANCH}
                    '''
                }
            }
        }
    }
}
