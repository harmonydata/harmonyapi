docker login -u harmonydata
export COMMIT_ID=`git show -s --format=%ci_%h | sed s/[^_a-z0-9]//g | sed s/0[012]00_/_/g` && docker build -f Dockerfile_local_api -t harmonyapilocal --build-arg COMMIT_ID=$COMMIT_ID . && docker tag harmonyapilocal harmonydata/harmonyapilocal:latest && docker push harmonydata/harmonyapilocal:latest
