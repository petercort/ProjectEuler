def projectname = "ProjectEuler"

pipeline {
    agent any
    stages {
    	stage('Build') {
    		steps{ 
    			script {
    				sh ('ls -l')
					def customImage = docker.build("$projectname:${env.BUILD_ID}")
				}
			}
    	}
        stage('Test') {
        	steps {
        		script {
        			customImage.inside {
	        			sh 'curl localhost'
	    			}
        		}
        	}	
        }
    }
}