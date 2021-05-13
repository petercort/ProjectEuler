def projectname = ProjectEuler

pipeline {
    agent {
		any
    }
    stages {
    	stage('Build') {
    		steps{ 
    			script {
					def customImage = docker.build("{$projectname}:${env.BUILD_ID}")
				}
			}
    	}
        stage('Test') {
        	steps {
        		customImage.inside {
	        		sh 'curl localhost'
	    		}
        	}	
        }
    }
}