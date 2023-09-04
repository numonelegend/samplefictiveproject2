node {
    stage('Checkout') {
        checkout scm
    }
    docker.withRegistry('//https://hub.docker.com/repository/docker/sachy6/ubuntu_public', 'DockerHub') {
	    def dockerImageName = "hub.docker.com/repository/docker/sachy6/ubuntu_public:pythonlatest2"

	    docker.image("${dockerImageName}").inside("-u 0:0"){
            try{
                stage('CompileTest') {
                    sh '/bin/bash compile_test.sh ${VERSION} ${BUILD_NUMBER}'
                }

                stage('Archive'){
                    archiveArtifacts("pytest.log")
                }

                stage('Report'){
                    try{
                        junit 'testreport.xml'
                    }
                    catch(ex){
                        emailext body: 'Sample fictive project failed', subject: '[jenkins] sample fictive project build failed', to: 'sachinhassankumar@gmail.com'
                        echo "Sample fictive project failed"
                        error ex.message
                    }
                }
            }
            finally {
                sh 'chmod -R a+rwx ./'
            }
        }
    }
}
