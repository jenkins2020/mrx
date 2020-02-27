#!/bin/groovy
pipeline {
  agent { dockerfile true }
  stages {
    stage('Hello World') {
      steps {
        dir('/home/build/rpmbuild/SOURCES') {
          sh 'pwd'
        }
        echo('Hello World!')
        sh 'whoami'
        sh 'echo "${HOME}"'
      }
    }
  }
}
