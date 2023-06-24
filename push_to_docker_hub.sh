docker login -u fastdatascience
export COMMIT_ID=`git show -s --format=%ci_%h | sed s/[^_a-z0-9]//g | sed s/0[012]00_/_/g`
docker build -t harmonyapi --build-arg COMMIT_ID=$COMMIT_ID .
docker tag harmonyapi fastdatascience/harmonyapi:$COMMIT_ID
docker push fastdatascience/harmonyapi:$COMMIT_ID

