pipeline {
    agent {
		any
    }

    stages {
        stage('Build') {
            steps {
                docker build .
            }
        }
        stage('Start Up') {
        	steps { 
        		sh 'docker run -d -p 9001:9001 -p 50001:50001 ProjectEuler/ProjectEuler:latest'
        	}
        }
        stage('Test') {
            steps {
                sh ''
            }
        }
    }
}