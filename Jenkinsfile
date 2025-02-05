pipeline {
    agent any
    environment {
        GIT_CREDENTIALS_ID = 'github-credentials'  // The credential ID from Jenkins
        REPO_URL = 'https://github.com/sagar-harry/Testing_Jenkins_2'
        BRANCH = 'main'  // Change if pushing to a different branch
        DIR_TO_PUSH = 'C:/Users/RH0957/Desktop/rough/jenkins/workspace/testing1'  // Change to the directory you want to push
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
                    sh 'ls'
                    sh 'cp -r ${DIR_TO_PUSH} repo/'
                }
            }
        }
        stage('Commit and Push') {
            steps {
                script {
                    dir('repo') {
                        sh '''
                        git config --global user.email "10vidyasagarkonni@gmail.com"
                        git config --global user.name "sagar-harry"
                        git add .
                        git commit -m "Added ${DIR_TO_PUSH} from Jenkins"
                        git push https://${GIT_CREDENTIALS_ID}@github.com/sagar-harry/Testing_Jenkins_3.git ${BRANCH}
                        '''
                    }
                }
            }
        }
    }
}
