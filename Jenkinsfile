pipeline {
  agent { docker { image 'python:3.10.0' } }
  stages{
    stages("build"){
      steps{
        sh 'pip install flask'
      }
    }
    stages("test"){
      steps{
        sh 'python test.py'
      }
      post{
        always {junit 'test-reports/*.xml'}
      }
    }
    stages("deploy"){
      steps{
        echo "DEPLOYING NOW"
        echo 'BOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOM'
      }
    }
  }
}
