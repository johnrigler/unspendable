pipeline {
  agent any
  stages {
  stage('Test') {
      steps {
        script {
          sh './test/jenkins-test.bash'
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
