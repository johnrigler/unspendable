pipeline {
  agent any
  stages {
  stage('Test') {
      steps {
        script {
          sh './test/test.bash'
        }
      }
    }
  stage('Report to Jira') {
      steps {
          jiraSendBuildInfo site: 'secretbeach.atlassian.net'
      }
    }
  }
}
