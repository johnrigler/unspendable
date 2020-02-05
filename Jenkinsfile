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
          comment_issues()
        }
    }
  }
}

void comment_issues() {
    def issue_pattern = "TEST-\\d+"

    // Find all relevant commit ids
    currentBuild.changeSets.each {changeSet ->
        changeSet.each { commit ->
            String msg = commit.getMsg()
            msg.findAll(issue_pattern).each {
                // Actually post a comment
                id -> jiraAddComment idOrKey: id, comment: 'Hi there!'
            }
        }
    }
}

