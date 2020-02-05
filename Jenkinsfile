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
          jiraComment 'This is a comment from the Pipeline'
          jiraSendBuildInfo site: 'secretbeach.atlassian.net'
      }
    }
  }
}
