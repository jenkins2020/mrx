#!/bin/groovy
pipeline {
  agent { dockerfile true }
  stages {
    stage('Prepare source & specs') {
      steps {
          sh 'wget -c --directory-prefix=/home/build/rpmbuild/SOURCES http://ftp.gnu.org/gnu/hello/hello-2.10.tar.gz'
          sh 'pwd'
          sh 'cp "${WORKSPACE}"/*.spec /home/build/rpmbuild/SPECS/'
          sh 'ls -lah /home/build/rpmbuild/SPECS/'
      }
    }
    stage('Build RPM') {
      steps {
          sh 'cd /home/build/rpmbuild/SPECS/ && rpmbuild -ba hello.spec'
          sh 'cp /home/build/rpmbuild/SRPMS/hello* .'
          sh 'cp /home/build/rpmbuild/RPMS/*/hello* .'

      }
    }
    // stage('Lint RPM') {
    //   steps {
    //     sh 'cd /home/build/rpmbuild/SPECS/ && rpmlint hello.spec ../SRPMS/hello* ../RPMS/*/hello*'
    //   }
    // }
    stage('Archive RPMs') {
      steps {
        archiveArtifacts artifacts: '*.rpm'
      }
    }
  }
  post { 
    success {
      build job: 'mrx_rpm_test_hello_world'
    }
  }
}
