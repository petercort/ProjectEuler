projectname = ProjectEuler

pipeline {
    agent {
		checkout scm

	    def customImage = docker.build("{$projectname}:${env.BUILD_ID}")

	    customImage.inside {
	        sh 'curl localhost'
	    }
    }

    stages {
        stage('Test') {
            steps {
                sh 'echo "hi"'
            }
        }
    }
}