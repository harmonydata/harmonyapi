az login
az acr login --name twharmonyacr
az acr update -n twharmonyacr --admin-enabled true.
git submodule update --remote 
export COMMIT_ID=`git show -s --format=%ci_%h | sed s/[^_a-z0-9]//g | sed s/0[012]00_/_/g` && docker build -t harmonyapi -t harmonyapi:$COMMIT_ID -t twharmonyacr.azurecr.io/harmonyapi -t twharmonyacr.azurecr.io/harmonyapi:$COMMIT_ID --build-arg COMMIT_ID=$COMMIT_ID . && docker push twharmonyacr.azurecr.io/harmonyapi:$COMMIT_ID && echo "The container version is $COMMIT_ID"
