pipeline {
  agent any
  stages{
    stages("build"){
      steps{
        sh 'pip install flask'
      }
    }
    stages("test"){
      keepRunning{
        sh 'python app.py'
      }
    }
    stages("deploy"){
      steps{
        echo "DEPLOYING NOW"
      }
    }
  }
}
