pipeline {
  agent any
  stages {
  stage('Stage 1') {
      steps {
        script {
          sh 'pwd' 
        }
      }
    }
  stage('Stage 2') {
      steps {
        script {
          sh 'python -v' 
          }
          jiraSendBuildInfo site: 'secretbeach.atlassian.net'
      }
    }
  }
}
