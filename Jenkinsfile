pipeline {
  agent any
  stages{
    stages("build"){
      steps{
        echo "BUILDING NOW"
      }
    }
    stages("test"){
      keepRunning{
        sh 'python3 app.py'
      }
    }
    stages("deploy"){
      steps{
        echo "DEPLOYING NOW"
      }
    }
  }
}
