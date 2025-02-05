pipeline {
    agent any
    environment {
        GIT_CREDENTIALS_ID = 'github-credentials'  // The credential ID from Jenkins
        REPO_URL = 'https://github.com/sagar-harry/Testing_Jenkins_2'
        BRANCH = 'main'  // Change if pushing to a different branch
        DIR_TO_PUSH = '/var/jenkins_home/workspace/testing1'  // Change to the directory you want to push
    }
    stages {
        stage('Clone Repository') {
            steps {
                script {
                    sh 'rm -rf repo && git clone ${REPO_URL} repo'
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
                    gitUsernamePassword(credentialsId: 'mygitid', gitToolName: 'Default')
                ]) {
                    sh '''
                    cd repo
                    git config --global user.email "your-email@example.com"
                    git config --global user.name "Jenkins"
                    git add .
                    git commit -m "register work"
                    git push origin ${BRANCH}
                    '''
                }
            }
        }
    }
}
