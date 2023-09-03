node {
    stage('Checkout') {
        checkout scm
    }

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