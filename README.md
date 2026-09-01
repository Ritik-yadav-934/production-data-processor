# production-data-processor

# Step-1
git clone <your-github-repository>
cd production-data-processor

# Step -2 
docker build -t production-data-processor .

# step -3
docker run --name production-data-processor-app production-data-processor
