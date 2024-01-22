# docker login -u harmonydata
export COMMIT_ID=`git show -s --format=%ci_%h | sed s/[^_a-z0-9]//g | sed s/0[012]00_/_/g` && docker build -t harmonyapi -t harmonyapi:latest -t harmonyapi:$COMMIT_ID -t harmonydata/harmonyapi:latest -t harmonydata/harmonyapi:$COMMIT_ID --build-arg COMMIT_ID=$COMMIT_ID . && docker push harmonydata/harmonyapi --all-tags && echo "The container version is $COMMIT_ID"
